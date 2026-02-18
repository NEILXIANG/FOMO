import re
import time
import json
import concurrent.futures
from pathlib import Path
from deep_translator import GoogleTranslator
import random

# Configuration
src = Path('FOMO_PRD.md')
dst = Path('FOMO_PRD_EN.md')
cache_file = Path('.chat/translate_cache.json')
MAX_WORKERS = 10  # Concurrency level
SAVE_INTERVAL = 20 # Save cache every N segments

# Load resources
lines = src.read_text(encoding='utf-8').splitlines()
translator = GoogleTranslator(source='zh-CN', target='en')
cache: dict[str, str] = {}

if cache_file.exists():
    try:
        cache = json.loads(cache_file.read_text(encoding='utf-8'))
    except Exception:
        cache = {}

zh_re = re.compile(r'[\u4e00-\u9fff]')

def has_zh(s: str) -> bool:
    return bool(zh_re.search(s))

def tr_single_with_retry(text: str) -> tuple[str, str, bool]:
    """
    Returns (original_text, translated_text, success_bool)
    """
    if text in cache:
        return text, cache[text], True
    
    # Retry loop
    for i in range(3):
        try:
            # Jitter to avoid exact synchronized hits if rate limiting is strict
            if i > 0:
                time.sleep(random.uniform(0.5, 1.5) * i)
            
            # Use a fresh instance if needed
            local_translator = GoogleTranslator(source='zh-CN', target='en')
            res = local_translator.translate(text)
            
            if res:
                return text, res, True
        except Exception as e:
            # Print error only on last attempt to reduce noise
            if i == 2:
                # print(f"Failed to translate '{text[:10]}...': {e}")
                pass
            pass
            
    return text, text, False

def collect_unique_segments(lines: list[str]) -> list[str]:
    """
    Extracts all unique Chinese segments from the markdown file 
    that need translation, skipping code blocks and metadata.
    """
    segs: set[str] = set()
    in_code_block = False
    
    for line in lines:
        stripped = line.strip()
        
        # Handle code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        if not has_zh(line):
            continue

        # Table separators
        if re.fullmatch(r'\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*', line):
            continue

        # Tables
        if '|' in line and not line.lstrip().startswith('>'):
            for p in line.split('|'):
                t = p.strip()
                if t and has_zh(t):
                    segs.add(t)
            continue

        # Headings
        hm = re.match(r'^(\s*#{1,6}\s+)(.*)$', line)
        if hm and has_zh(hm.group(2)):
            segs.add(hm.group(2).strip())
            continue

        # Lists
        lm = re.match(r'^(\s*[-*+]\s+)(.*)$', line)
        if lm and has_zh(lm.group(2)):
            segs.add(lm.group(2).strip())
            continue

        # Blockquotes
        if line.lstrip().startswith('>'):
            content = line.lstrip()[1:].strip()
            if content and has_zh(content):
                segs.add(content)
            continue

        # Normal text
        segs.add(stripped)
        
    return list(segs)

def warmup_cache_concurrent(segments: list[str]) -> None:
    pending = [s for s in segments if s not in cache]
    total = len(pending)
    if total == 0:
        print("All segments already cached.")
        return
    
    print(f'Starting translation of {total} new segments with {MAX_WORKERS} threads...')
    
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Map future to original text
        future_to_text = {
            executor.submit(tr_single_with_retry, text): text 
            for text in pending
        }
        
        for future in concurrent.futures.as_completed(future_to_text):
            original, translated, success = future.result()
            if success and translated != original:
                cache[original] = translated
            
            completed += 1
            if completed % SAVE_INTERVAL == 0 or completed == total:
                # Save progress
                try:
                    cache_file.parent.mkdir(parents=True, exist_ok=True)
                    cache_file.write_text(
                        json.dumps(cache, ensure_ascii=False, indent=2), 
                        encoding='utf-8'
                    )
                    percent = (completed / total) * 100
                    print(f'Progress: {completed}/{total} ({percent:.1f}%)')
                except Exception as e:
                    print(f"Error saving cache: {e}")

def tr_lookup(text: str) -> str:
    """Look up translation from cache, return original if validation fails"""
    t = text.strip()
    if not t or not has_zh(t):
        return text
    
    if t in cache:
        trans = cache[t]
        
        # Preserve leading/trailing whitespace of the original line
        lead = text[:len(text) - len(text.lstrip())]
        tail = text[len(text.rstrip()):]
        return lead + trans + tail
        
    return text

def generate_output():
    out: list[str] = []
    in_code_block = False
    
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        
        # Maintain code block state
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            out.append(line)
            continue
            
        if in_code_block:
            out.append(line)
            continue

        if not has_zh(line):
            out.append(line)
            continue

        # Table separators
        if re.fullmatch(r'\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*', line):
            out.append(line)
            continue

        # Tables
        if '|' in line and not line.lstrip().startswith('>'):
            parts = line.split('|')
            new_parts = []
            for p in parts:
                p_stripped = p.strip()
                if has_zh(p_stripped):
                    if p_stripped in cache:
                        # Replace only the content part, keeping spaces if any inside the cell
                        # Actually splitting by | preserves some structure but stripping removes spaces.
                        # Simple replace might be risky if multiple same words.
                        # Let's reconstruct cautiously.
                        trans = cache[p_stripped]
                        # Try to replace loosely
                        new_parts.append(p.replace(p_stripped, trans))
                    else:
                        new_parts.append(p)
                else:
                    new_parts.append(p)
            out.append('|'.join(new_parts))
            continue

        # Headings
        hm = re.match(r'^(\s*#{1,6}\s+)(.*)$', line)
        if hm and has_zh(hm.group(2)):
            content = hm.group(2).strip()
            trans = cache.get(content, content)
            out.append(hm.group(1) + trans)
            continue

        # Lists
        lm = re.match(r'^(\s*[-*+]\s+)(.*)$', line)
        if lm and has_zh(lm.group(2)):
            content = lm.group(2).strip()
            trans = cache.get(content, content)
            out.append(lm.group(1) + trans)
            continue

        # Blockquotes
        if line.lstrip().startswith('>'):
            prefix_len = len(line) - len(line.lstrip())
            content_part = line.lstrip() # starts with >
            content = content_part[1:].strip()
            trans = cache.get(content, content)
            out.append(' ' * prefix_len + '>' + trans)
            continue

        # Regular lines
        # Check if the whole line strip matches a segment
        if stripped in cache:
             out.append(tr_lookup(line))
        else:
             # Fallback: if it wasn't caught in collection but has zh?
             # Just keep it or try tr_lookup which does look up stripped.
             out.append(tr_lookup(line))

    text = '\n'.join(out) + '\n'

    # Post-processing fixes
    subs = [
        ('North Star Index', 'North Star Metric'),
        ('North Star indicators', 'North Star Metric'),
        ('Humane care', 'Human-Centered Care'),
        ('humanistic', 'human-centered'),
        ('interruption page', 'pause screen'),
        ('Interruption Page', 'Pause Screen'),
        ('（', ' ('),
        ('）', ') '),
    ]
    for a, b in subs:
        text = text.replace(a, b)

    dst.write_text(text, encoding='utf-8')
    print(f'Done! Wrote {len(out)} lines to {dst}')

if __name__ == '__main__':
    segs = collect_unique_segments(lines)
    warmup_cache_concurrent(segs)
    generate_output()
