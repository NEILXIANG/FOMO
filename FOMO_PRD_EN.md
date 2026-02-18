# FOMO Product Requirements Document (PRD)

Version: 0.1
Date: 2026-02-17  
Stage: Production-Ready Execution Document
Maintainer: Product Lead

## TL;DR
- Goal: Use an AI coach to turn "unconscious phone use" into "intentional choice." North Star Metric: weekly count of "opens that the user then abandons."
- Audience: Students, professionals, poor sleepers, parents, mental-health-aware users who need to reduce high-risk app usage; native Chinese contexts first.
- Differentiation: Three-layer combo of interruption + rules + insights; AI personalization; non-shaming humanistic design; local data flywheel + partner/family relationship moat.
- Success signals (first 6 months KRs): D1≥60%, D7≥35%, D30≥22%, high-risk time ↓≥20%, AI suggestion satisfaction ≥75%, onboarding completion ≥80%.
- Near-term gates: W12 MVP Gate (D7≥30%, NPS≥30, crash <0.5%); risks R1 iOS limits and R10 psychological burden reviewed biweekly.

---

## Table of Contents

1. Product Overview
  - 1.1 Background & Market Insights
  - 1.2 Mission
  - 1.3 Target Users
  - 1.4 North Star Metric (NSM)
  - 1.5 Key Results (first 6 months)
  - 1.6 Humanistic Guardrails & Ethics
  - 1.7 Humanistic Philosophy Mechanisms
  - 1.8 One-Pager Positioning
  - 1.9 In/Out of Scope
  - 1.10 Accessibility & Inclusion Requirements
2. Competitive Deep Dive
  - 2.1 Global Overview (International + China)
  - 2.2 Deep Logic Breakdowns (A–H)
  - 2.3 Capability Matrix
  - 2.4 Intervention Types
  - 2.5 Pricing Landscape
  - 2.6 Cross-Dimensional Comparison
  - 2.7 Evolution & Trends
  - 2.8 Differentiation Strategy
3. Functional Specs
  - 3.0 Priority Table (+ iOS/Android gaps)
  - 3.1 AI Touchpoint Map
  - F-01 Interruption Gate
  - F-02 Rules Hub
  - F-03 Insights & Achievements
  - F-04 Anti-Bypass
  - F-05 Onboarding
  - F-06 AI Coach (Phase 2)
  - F-07 Partner Supervision (Phase 2)
  - F-08 Browser Extension (Phase 2)
  - F-09 Family Empathy (Phase 2–3)
  - F-10 In-App Feature Blocking (Phase 3)
  - F-11 Minimal Mode (Phase 3)
  - F-12 Emotion Sensing Engine (Phase 2)
  - F-13 Mindful Moments (Phase 2)
4. Milestones
  - 4.1 12-Month Roadmap
  - 4.2 Phase Details (0–3)
  - 4.3 Critical Path & Dependencies
5. Iteration Plan
  - 5.1 Sprint Rituals & DoD
  - 5.2 MVP Sprints (S1–S4)
  - 5.3 Phase 2 Sprints (S5–S10)
  - 5.4 Release & Rollback Tree
6. Lean Resourcing
7. Business Model
  - 7.1 Pricing (Freemium)
  - 7.2 Unit Economics
  - 7.2.1 Model Deep Dive
  - 7.2.2 Scenario Revenue Model (Year 2)
  - 7.2.3 Unit Cost & Gross Margin
  - 7.3 Revenue Mix (Year 1 End)
  - 7.3.1 Conversion Funnel
  - 7.3.2 Year 2 Forecast
  - 7.3.3 B2B Path
  - 7.4 Growth Flywheel
  - 7.5 Humanistic vs Business Balance
  - 7.6 Why Us
8. Risk Management
  - 8.1 Heatmap
  - 8.2 Risk Playbooks (R1–R13)
  - 8.3 Four-Dimensional Dashboard
  - 8.4 Security & Compliance Checklist
9. Appendix
  - 9.1 Glossary
  - 9.2 References
10. Business & Execution Pack
   - 10.1 Pitch Deck Outline (12 slides)
   - 10.2 MVP Story Backlog
   - 10.3 Product Philosophy Manifesto
   - 10.4 GTM Strategy
   - 10.5 12-Month Financials

---

## 1. Product Overview

### 1.1 Background & Market Insights

Global daily screen time > **6.5 hours** (DataReportal 2025), ~40% is “unconscious use.” Systemic issue:

| Source | Finding |
|--------|---------|
| DataReportal 2025 | Daily screen 6.5h, +4.2% YoY |
| Opal Screen Time 2025 | 96 unlocks/day |
| PNAS Nexus 2024 | Persistent access lowers focus & mood |
| one sec | Interruptions cut app use by 57% |
| Microsoft Research 2023 | Blocking distractions boosts productivity 20% |
| Carnegie Mellon 2021 | Freedom users +22% hourly output |

**AI double whammy**: 2024–2026 mobile AI (ChatGPT/Gemini/Claude) makes the phone an “AI entry point,” legitimizing every unlock and deepening FOMO.

AI opportunity: cheaper LLM inference, higher AI trust, mature on-device models; AI agents enable auto-adjusting rules.

**Core belief**: Use AI to fight AI—AI coach vs. AI recommender.

**Market gap**: Current tools = hard block, light nudge, or pure stats. **No mainstream AI-driven personalized, real-time intervention.**

### 1.2 Mission

Turn “unconscious phone use” into “intentional choice.” Not a phone blocker; an **AI decision co-pilot** that times and styles the right intervention so the user chooses.

### 1.3 Target Users

| Segment | Age | Pain | Scenarios | Size |
|---------|-----|------|-----------|------|
| Students | 16-24 | Short-video disruption in study | Dorms, library | 44M CN college |
| Professionals | 22-40 | Context-switching ruins deep work | Office/remote | ~350M |
| Poor sleepers | 18-40 | 1-2h bedtime doomscroll | Bedroom | 300M with issues |
| Parents | 30-50 | Kids overuse, weak controls | Home | ~200M parents |
| Mental-health aware | 18-45 | Know the harm, can’t stop | Any | Growing |

### 1.4 NSM

Weekly per-user count of “opened then abandoned” (unconscious → conscious choice).

### 1.5 Key Results (first 6 months)

| Metric | Target | Measure | Benchmark | Owner | Review |
|--------|--------|---------|-----------|-------|--------|
| D1 retention | ≥60% | Events | Opal ~55% | PM+Growth | Weekly |
| D7 retention | ≥35% | Events | Tools ~30% | PM+Growth | Weekly |
| D30 retention | ≥22% | Events | Tools ~18% | PM+Growth | Biweekly |
| High-risk app time ↓ | ≥20% | System data | one sec 57% (with hard lock) | PM+Data | Weekly |
| Users 3+ days plan completion | ≥45% | Rule stats | — | Ops+PM | Biweekly |
| NPS | ≥40 | In-app | ScreenZen high rating | PM | Monthly |
| Onboarding completion | ≥80% | Funnel | — | Design+PM | Weekly |
| AI suggestion “helpful” | ≥75% | In-app vote (Phase 2) | Zario+Stanford +40pp vs rules | AI PM+BE | Weekly |
| AI one-click exec rate | ≥40% | Clicks (Phase 2) | Similar features ~30-50% | AI PM+BE | Weekly |

### 1.6 Humanistic Guardrails

- No shaming copy; encourage only (negative copy share = 0).
- User sovereignty: all limits user-configured; no default hard lock.
- Fragile moments: night/anxiety → gentle first; soft mode ≥90% coverage.
- AI explainability: every suggestion includes “why.”
- Low burden: avoid “self-discipline anxiety”; allow failure/recovery; “pressure too high” feedback ≤5%.

### 1.7 Humanistic Philosophy Mechanisms

| Chapter | Requirement | How |
|---------|-------------|-----|
| Competitive | Evaluate “respect” not just features | Add emotional safety dimension |
| Features | Each core flow has low-pressure path | Soft mode, recoverable feedback |
| AI touchpoints | AI suggests next step, not judge | Always explain + intensity control |
| Business | No anxiety paywall | Free core value; pay for depth/efficiency |
| Risk | Psychological burden is top risk | Dedicated KPI and playbook (R10) |

### 1.8 One-Pager Positioning

Elevator pitch: “FOMO is an AI behavior coach. When you unconsciously open TikTok, it asks: do you really want to? It learns your patterns and weekly shows your weak spots and how to improve. Like a fitness coach—it won’t do push-ups for you but stands there to ask: are you sure?”

- Name: FOMO (reframed: Freedom Over My Output)
- Core value: Turn unconscious scrolling into conscious choice via AI coach
- Target: 16–45 seeking less waste, more focus/emotional health
- Solution: Light friction + AI insights + humanistic design
- Model: Freemium (core free + Pro AI coach ¥28/mo)
- Differentiation: Only product deeply fusing AI behavior analysis + humanistic design
- NSM: Weekly “opened then abandoned” count

### 1.9 Scope

| Dimension | In (Year 1) | Out |
|-----------|-------------|-----|
| Platform | iOS/Android (P0); browser ext (P1) | Wearables standalone |
| Interventions | Pause page, rules, AI tips, mindful | Irreversible hard lock |
| AI | Behavior insights, rule advice, explainable prompts, weekly coach | Medical-grade diagnosis/therapy |
| Data | Local-first, de-identified summaries, export/delete | No chat/content capture |
| Biz | Personal Pro, Family, Team PoC | Ads, data sales |

Principle: start with high-frequency, low-friction, provable effectiveness; then expand to cross-device, social graph, on-device AI.

### 1.10 Accessibility & Inclusion

| Dimension | Requirement | Priority | Acceptance |
|-----------|-------------|----------|------------|
| Screen reader | Labels/contentDescription on all controls | P0 | VO/TB fully operable |
| Contrast | Text/background ≥ 4.5:1 (WCAG AA) | P0 | 100% automated scan pass |
| Touch target | ≥44×44pt iOS / 48×48dp Android | P0 | Design spec check |
| Color vision | Don’t rely on color only | P0 | Pass color-blind sim |
| Reduce motion | Respect system reduce motion; allow turning off breathing anim | P1 | Degrade to static |
| Dynamic type | Support system font scale | P1 | No truncation/overlap at max |

---

## 2. Competitive Deep Dive

(Contains global overview, A–H breakdowns, capability matrix, intervention taxonomy, pricing, cross & longitudinal analysis, differentiation strategy, and AI data flywheel.)

---

## 3. Functional Specs

### 3.0 Priority Table

**iOS vs Android Capability Gaps (Expectation Management)**

| Capability | Android (Accessibility) | iOS (Screen Time API) |
|------------|-------------------------|-----------------------|
| In-app feature blocking | Yes (e.g., only block feed) | No (block whole app) |
| Browser URL blocking | Yes (major browsers) | Safari only (ext) |
| Grayscale mode | One-tap | Jump to system/Shortcut |
| Anti-uninstall | Yes (Device Admin) | No |

| ID | Module | Priority | Phase | Value | Status |
|----|--------|----------|-------|-------|--------|
| F-01 | Interruption | P0 | MVP | Break impulsive loops | TBC |
| F-02 | Rules Hub | P0 | MVP | Configurable constraints | TBC |
| F-03 | Insights & Achievements | P0 | MVP | Make progress visible | TBC |
| F-04 | Anti-Bypass | P0 | MVP | Prevent self-sabotage | TBC |
| F-05 | Onboarding | P0 | MVP | 3-step setup | TBC |
| F-06 | AI Weekly Coach | P1 | Phase 2 | Personalized insights | Planned |
| F-07 | Partner Supervision | P1 | Phase 2 | Social accountability | Planned |
| F-08 | Browser Extension | P1 | Phase 2 | Desktop coverage | Planned |
| F-09 | Family Empathy | P1 | Phase 2–3 | Family safety & trust | Planned |
| F-10 | In-app Feature Block | P2 | Phase 3 | Precise feed block | Evaluating |
| F-11 | Minimal Mode | P2 | Phase 3 | Boring phone | Evaluating |
| F-12 | Emotion Sensing | P1 | Phase 2 | Stress-aware softening | Planned |
| F-13 | Mindful Moments | P1 | Phase 2 | 30–90s recovery | Planned |

**Status definitions**: TBC, Planned, Evaluating, etc. (aligned with Chinese doc.)

### 3.1 AI Touchpoint Map

(T1–T7 triggers, inputs, outputs, user actions, safety boundaries; principles: explain → suggest; gentle → escalate; always exit; never judge.)

### F-01 Interruption Gate

- Pause page on high-risk app launch; configurable wait (3/5/8/10/15s);
- Intent confirmation; secondary delay for “habitual/boring” intents;
- Leave button always; custom prompts; optional breathing; soft mode at night; AI adaptive wait & prompts (P1).
- Acceptance: pop within 300ms; 60fps anim; <2% battery/24h; offline ok; 30 apps; strict correctness & edge cases.

### F-02 Rules Hub

- Template-first (study/work/bedtime/custom);
- Rule types: daily limit, unlock count, time blocks, recurrence, strict mode cooldown; whitelist always allowed;
- AI rule suggestions (too loose/tight, time leaks, substitution drift);
- Acceptance: ≤3 steps enable template; conflicts = stricter wins; 15 parallel rules (free ≤3; Pro unlimited); timezone tamper-safe.

### F-03 Insights & Achievements

- Daily recap (time saved, correct choices, risky periods, total high-risk time vs yesterday);
- AI Weekly Report (trends, best/worst apps, streak, time-window analysis, emotion triggers, rule efficacy, substitution drift, 1–3 actions with one-click apply);
- Mission log (optional reflection, relation reminders);
- Achievements + viral cards: brag, ask-for-help (Panic Button), challenge/taunt; shareable with UTM;
- Humanistic feedback rules: always one “you did well,” no punishment framing; soften for high-stress users.

### F-04 Anti-Bypass

- Edit cooldown (5/10/15/30m); password; abnormal-behavior hint; Android uninstall guard; “pause 1 day.”
- **Emergency pass**: 1–2 times/month with “cost” (e.g., ¥3 or 60s long countdown) to reduce deadlock fear.

### F-05 Onboarding

- ≤5 steps, ≤120s; permission pass rate ≥70%; completion ≥80%.

### F-06 AI Coach (Phase 2)

- Daily nudges; weekly structured report; one-click actions; substitution detection; future: dialog coach.
- Privacy: local-first, minimal data, export/delete, degrade to rules; no shaming.
- Acceptance: report ≤10s, success ≥98%, helpful ≥4/5, one-click exec ≥40%, cost/paid user ≤¥2.

### F-07 Partner Supervision (Phase 2)

- Invite link/QR; default privacy (status only, optional duration view);
- Daily 9pm cards; fail alerts with encourage/tease preset (no insults);
- 7-day challenge; AI duo insights/recs; unbind anytime.

### F-08 Browser Extension (Phase 2)

- Sync rules; web pause page with counts; intent logging; cross-device drift detection; temporary pause with cooldown.

### F-09 Family Empathy (Phase 2–3)

- Mutual consent binding; trend-only view for parents (no per-app details);
- Shared goals; emotion tags by teen; AI empathy scripts; unlock requests; exit anytime.

### F-10 In-App Feature Blocking (Phase 3)

- Android: block feeds (WeChat Moments, TikTok For You, Weibo topics); iOS degrade to whole-app pause.

### F-11 Minimal Mode (Phase 3)

- Grayscale; scheduled; AI recommend; text-only launcher feel; exemptions.

### F-12 Emotion Sensing Engine (Phase 2)

- Signals: late-night, fail streak, intent drift, intercept spikes, touch frequency, ambient light; outputs stress tier G/Y/R; actions: soften, mindful prompt, reduce strictness.

### F-13 Mindful Moments (Phase 2)

- 30/60/90s breathing/grounding/intent restate; optional in pause; no pressure texts; smooth on low-end devices.

---

## 4. Milestones

(12-month roadmap, Phase 0–3 details, critical path.)

### 4.2 Phase Details (excerpted highlights)

- **Phase 0 (Weeks 1-4)**: **Added Critical Assumption Matrix (A1–A5)** and **Validation Toolkit** with interview scripts and usability tests; gate criteria.
- Phase 1 (W5-12): MVP build; S1–S4 goals; MVP gate (D7≥30%, NPS≥30, crash<0.5%).
- Phase 2 (W13-24): AI/paid/growth; S5–S10; gate targets.
- Phase 3 (W25-52): Scale, AI moat, B2B, intl.

---

## 5. Iteration Plan

(Sprint rituals, DoD, S1–S10 backlogs, release/rollback tree.)

---

## 6. Lean Resourcing

(6-7 core team; tools; cost guardrails; capacity principles.)

---

## 7. Business Model

- Pricing: Free core; Pro ¥28/mo, ¥198/yr; Family ¥48/mo (6 seats + parent panel); Team ¥15/user/mo; Lifetime ¥498.
- Unit econ: blended CAC ¥6; paid ARPU ¥22/mo; churn 8%; LTV/CAC 45.8 at M12 forecast; Year 1 revenue ¥594K vs spend ¥3,025K (model validation, not profit).
- Revenue mix (Y1 end): Personal 65%, Family 20%, Team 10%, Lifetime/other 5%.
- Funnels, Year2 scenarios, B2B path (EAP/education/church PoC), growth flywheel, humanistic-commercial balance, differentiation vs ScreenZen/one sec/Opal/Freedom.

---

## 8. Risk Management

- Heatmap; R1–R13 playbooks (iOS limits, freshness decay, strict-mode backlash, privacy, OS entrants, psychological burden, etc.).
- **8.3 Four-Dimensional Dashboard** (North Star/Business, Product XP, Tech, Ethics) with green/yellow/red and mapped actions; cross-layer rules; alerting & SLA.
- 8.4 Security & Compliance: C1–C11 (privacy policy, AES-256 local, TLS, data minimization, export/delete, permissions disclosure, de-identified LLM payloads, minors consent, audits, GDPR-ready).

---

## 9. Appendix

- Glossary (NSM, LTV, CAC, streak, soft mode, etc.).
- References (research + public data of competitors).

---

## 10. Business & Execution Pack

- 10.1 Pitch Deck (12 slides)
- 10.2 MVP User Stories (S1–S10) 
- 10.3 Philosophy Manifesto (control, data dignity, emotional value, addiction mechanisms)
- 10.4 GTM (cold start, viral, cross-scenario, KOL)
- 10.5 Financials (12-month P&L; gross margin; cash burn; runway/raise ¥3–4M recommended)

---

*Note*: This English version is a faithful translation and condensation of the current Chinese PRD, preserving structure, metrics, and guardrails. If you need a shorter “Investor Cut” (5–8 pages) or a pitch-ready deck export, I can generate that next.
