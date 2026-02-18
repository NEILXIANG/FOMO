# FOMO Product Requirements Document (PRD)

Version: 0.1
Date: 2026-02-17  
Stage: Production-level execution documents (Production-Ready)
Document maintainer: product owner

## Quick Overview (TL;DR)
- Goal: Use AI coaching to turn "unconscious scrolling on the phone" into "conscious choice." The core North Star is "the number of times each user chooses to give up after unconsciously opening it per week."
- Audience: students/workers/sleep-impaired people/parents/mental health concerns who need to reduce the use of high-risk apps. Native Chinese scenarios are preferred.
- Differentiation: three-layer combination of interruption + rules + insights, AI personalization, human-centered design to remove shame, local data flywheel + partner/family relationship moat.
- Success signals (KR in the first 6 months): D1 ≥ 60%, D7 ≥ 35%, D30 ≥ 22%, high-risk duration reduction ≥ 20%, AI recommendation satisfaction ≥ 75%, onboarding completion rate ≥ 80%.
- Recent decision points: W12 MVP Gate (D7≥30%, NPS≥30, crash rate <0.5%); risk priority R1 iOS limitations and R10 psychological burden need to be reviewed biweekly.

---

## Table of contents

1. [Product Overview](#1-Product Overview)
  - 1.1 Background and market insights
  - 1.2 Product Mission
  - 1.3 Target users
  - 1.4 North Star Metric (NSM)
  - 1.5 Key Results (KR, first 6 months)
  - 1.6 Human-centered care and ethical boundaries
  - 1.7 Human-centered philosophy implementation mechanism
  - 1.8 One-page product positioning (One-Pager)
  - 1.9 Product scope boundaries (In Scope / Out of Scope)
  - 1.10 Accessibility and inclusive design requirements
2. [In-depth analysis of competitive products](#2-In-depth analysis of competitive products)
  - 2.1 Overview of Globally Influential Products (International + Chinese Local)
  - 2.2 In-depth dismantling of product logic (eight competing products from A to H)
  - 2.3 Competitive product functional capability matrix
  - 2.4 Classification of behavioral intervention types
  - 2.5 Panoramic comparison of competitive product pricing
  - 2.6 Cross-Dimensional Comparison
  - 2.7 Competitive product vertical analysis (Evolution & Trend Analysis)
  - 2.8 FOMO Differentiated Competition Strategy
3. [Functional Documentation](#3-Functional Documentation)
  - 3.0 Function Priority Summary List
  - 3.1 AI touchpoint map
  - F-01 Interruption Gate
  - F-02 Rules Hub
  - F-03 Insights & Achievements
  - F-04 Anti-Bypass protection (Anti-Bypass)
  - F-05 Onboarding
  - F-06 AI behavioral coach (Phase 2)
  - F-07 Partner Supervision (Phase 2)
  - F-08 Browser Extension (Phase 2)
  - F-09 Family Empathy Model (Phase 2–3)
  - F-10 In-App Feature Interception (Phase 3)
  - F-11 Minimalist Mode (Phase 3)
  - F-12 Emotion Sensing Engine (Phase 2)
  - F-13 Mindful Moments (Phase 2)
4. [Milestone](#4-Milestone)
  - 4.1 Overall roadmap (12 months)
  - 4.2 Details of each stage (Phase 0–3)
  - 4.3 Critical path and dependency graph
5. [Iteration Plan](#5-Iteration Plan)
  - 5.1 Sprint Rules and Rituals
  - 5.2 MVP Sprint Scheduling (S1–S4)
  - 5.3 Phase 2 Sprint（S5–S10）
  - 5.4 Release strategy and rollback decision tree
6. [Streamline resource information](#6-Streamline resource information)
7. [Business Model](#7-Business Model)
  - 7.1 FOMO Pricing (Freemium)
  - 7.2 Unit Economics
  - 7.2.1 In-depth analysis of business model
  - 7.2.2 Scenario-based revenue model (Year 2)
  - 7.2.3 Unit cost and gross profit structure
  - 7.3 Income structure (Year 1 End)
  - 7.3.1 Paid conversion funnel
  - 7.3.2 Year 2 Refined Revenue Forecast
  - 7.3.3 B2B path
  - 7.4 Growth Flywheel
  - 7.5 Humanistic values ​​and business balance
  - 7.6 Clear differentiation path (Why us)
8. [Risk Management](#8-Risk Management)
  - 8.1 Risk heat map
  - 8.2 Risk details and response Playbook (R1–R13)
  - 8.3 Risk Monitoring Dashboard (Traffic Light)
  - 8.4 Data Security and Compliance Checklist
9. [Appendix](#9-Appendix)
  - 9.1 Glossary
  - 9.2 References
10. [Business & Execution Pack](#10-Business & Execution Pack)
   - 10.1 Financing Roadshow PPT Outline (12 Pages Deck)
   - 10.2 MVP detailed task list (User Stories)
   - 10.3 Product Philosophy and Humanistic Declaration
   - 10.4 Operations and Growth (GTM) Strategy
   - 10.5 Detailed 12-month financial forecast

---

## 1. Product Overview

### 1.1 Background and market insights

The average daily screen time of global smartphone users has exceeded **6.5 hours** (DataReportal 2025), of which about 40% is "unintentional use" - that is, users turn on their phones for no clear purpose. This has become a systemic problem:

| Data source | Key findings |
|----------|----------|
| DataReportal 2025 | The average daily screen time of global users is 6.5 hours, a year-on-year increase of 4.2% |
| Opal Screen Time Report 2025 | The average person unlocks their phone 96 times a day |
| PNAS Nexus 2024 | Continuous internet access significantly reduces concentration and emotional well-being |
| one sec scientific data | Interruptive interventions reduce app usage by 57% |
| Microsoft Research 2023 | Blocking interference increases work efficiency by 20% |
| Carnegie Mellon 2021 | After using Freedom, users’ hourly wage output increased by 22% |

**Double impact of the AI ​​era**: The explosive popularity of AI tools (ChatGPT, Gemini, Claude) from 2024 to 2026 will make mobile phones the "AI portal", making it harder for users to refuse to pick up their mobile phones - because there is a probability of "discovering something useful" every time they open it. This fuels FOMO (fear of missing out).

| AI changes | Impact on screen time |
|---------|------------------|
| ChatGPT/Gemini/Claude mobile terminal outbreak | The mobile phone becomes an "AI portal", and there is a "justifiable reason" every time it is opened. |
| Short video AI recommendation algorithm upgrade (Douyin/Reels) | Improved personalization accuracy makes it more difficult for users to leave voluntarily |
| Explosion of AI-generated content | The information flow will never "finish", creating stronger infinite scrolling |
| AI chatbot anthropomorphism | Loneliness-driven mobile phone dependence is more difficult to intervene with traditional rules |

But AI also brings upgrade opportunities for solutions:

| AI opportunities | FOMO available methods |
|---------|--------------|
| LLM inference costs continue to decrease | Personalized behavior analysis changes from "expensive and slow" to "real-time and cheap" |
| Increased user acceptance of AI suggestions | "What the AI ​​coach said" is more authoritative than "system prompts" |
| Small model/mature device-side reasoning (Phi-3, Gemma) | Behavioral analysis runs completely on-device with zero privacy risk |
| AI Agent Popular | In the future, closed-loop intervention of "automatic adjustment rules" can be realized |

**Core judgment**: AI is not a competitive threat to FOMO, but the strongest weapon of FOMO - **Use AI to fight AI (use AI behavioral coaches to fight AI recommendation algorithms)**.

**Market Gap**: Existing products are either biased towards "strong control" (users uninstall after being disgusted, such as Opal's Strict Mode), or biased towards "light incentives" (invalid after the novelty wears off, such as Forest), or biased towards "quantitative display" (you know it but can't change it, such as StayFree). **No mainstream competing product truly uses AI for personalized behavior analysis and real-time intervention** - This is the biggest differentiation window for FOMO.

### 1.2 Product Mission

> **Allow users to turn "unconscious use of mobile phones" into "conscious choice". **

We do not make a "mobile phone disabling device", but an **AI-driven "decision aid"** - at the moment when the user is most likely to lose control, AI determines the best time and method to intervene, introduces just the right damping force, and allows the user to decide the current choice. AI runs through the entire product chain: intelligent identification of high-risk periods, personalized pause prompts, adaptive rule suggestions, and in-depth behavioral insights—evolving from "a tool that is the same to everyone" to a "coach that is different to everyone."

> **Insight into psychological roots**: The essence of unconscious scrolling on mobile phones is the anxious avoidance of "relationship rupture" - the escape of missing recognition, missed companionship, and unprocessed emotions. FOMO has one more layer than traditional "behavior blocking tools": while intervening in behavior, it guides users to realize that "choosing to put down their phones" is the starting point for connecting with real relationships, rather than the result of self-punishment.

### 1.3 Target users

| crowd | age group | Core pain points | Typical scenario | Estimated market size |
|------|--------|----------|----------|-------------|
| student | 16-24 | I was interrupted by a short video while preparing for the exam and was unable to learn deeply. | Study rooms, dormitories, libraries | There are 44 million college students in China |
| working people | 22-40 | Frequently switching apps during work, causing deep work to become fragmented | Office, remote work, meetings | Approximately 350 million white-collar workers |
| sleep-impaired | 18-40 | Browse the screen for 1-2 hours before going to bed, seriously delaying falling asleep | bedroom, night | 300 million people have sleep problems (Chinese Sleep Research Association) |
| parents | 30-50 | Worried about excessive use of mobile phones by children and lack of effective control | family scene | There are approximately 200 million parents of primary and secondary school students |
| mental health concern | 18-45 | Realize that mobile phones affect mood but cannot control it | various scenes | Mental health app users continue to grow |

### 1.4 North Star Metric (NSM)

**The number of "unintentional openings and then giving up" per user per week. **

This metric reflects that users are actually using the product to make better choices, rather than just installing the app.

### 1.5 Key Results (KR, first 6 months)

| index | target value | Measurement method | Competing products | Responsible person | review frequency |
|------|--------|----------|----------|--------|----------|
| D1 retention | ≥ 60% | Buried events | Opal D1 ~55% | PM+Growth | weekly |
| D7 retention | ≥ 35% | Buried events | Industry tools ~30% | PM+Growth | weekly |
| D30 retention | ≥ 22% | Buried events | Industry tools ~18% | PM+Growth | Fortnightly |
| Average daily time spent on high-risk apps decreases | ≥ 20% | System usage data comparison | one sec claims 57% (including hard block) | PM + Data Analysis | weekly |
| Proportion of users who complete the plan ≥ 3 days per week | ≥ 45% | Rule compliance statistics | — | Operations + PM | Fortnightly |
| NPS | ≥ 40 | In-app research | ScreenZen has high reputation but no public NPS | PM | per month |
| Novice guide completion rate | ≥ 80% | funnel data | — | Design + PM | weekly |
| AI suggestions “helpful” satisfaction | ≥ 75% | In-app voting (from Phase 2) | Zario x Stanford Research: AI Personalized Suggestion Acceptance Rate > Traditional Rule Suggestion 40pp | AI PM + backend | Weekly (from Phase 2) |
| AI suggestion one-click execution rate | ≥ 40% | Click event (from Phase 2) | No direct competitive product benchmarking (one-click approval rate for similar functions in the industry is about 30-50%) | AI PM + backend | Weekly (from Phase 2) |

### 1.6 Human-centered care and ethical boundaries (product bottom line)

The goal of FOMO is not to "make users more obedient", but to "help users make choices that are freer and more consistent with long-term goals at important moments." Therefore, we implement the following bottom line in all aspects:

| in principle | Specific requirements | Quantitative indicators |
|------|----------|----------|
| non-shaming expression | Negative humiliating copywriting such as "You failed again" is prohibited, and encouraging feedback is used by default. | Negative copywriting ratio = 0 |
| User sovereignty takes precedence | All restrictions can be actively configured by users, and extreme locking strategies are not enabled by default. | Active configuration accounts for 100% |
| Protection in vulnerable moments | Give priority to gentle intervention (prompt first and then limit) during late night and peak anxiety periods. | Mild mode trigger coverage ≥ 90% |
| AI can explain | Each AI suggestion must be accompanied by "Why are you being given this suggestion?" | Interpretable suggestions account for 100% |
| Low burden experience | Do not create new "self-discipline anxiety", allow failure and recovery, and do not punish users for interruption and failure. | User feedback rate of “too much pressure” ≤ 5% |

**Differentiated positioning supplement**: Compared with the "strong control" or "strong efficiency" orientation of mainstream products, FOMO clearly adopts the dual goals of "effect + dignity": not only reducing unconscious use, but also protecting users' sense of self-efficacy and psychological safety.

### 1.7 Human-centered philosophy implementation mechanism (Chapter Implementation)

| chapter | through requirements | Landing method |
|------|----------|----------|
| Competitive product analysis | Not only looks at the strength of functions, but also evaluates "whether users are respected" | Add emotional friendliness and psychological safety to the horizontal dimension |
| functional system | Each core feature has a "low-stress path" | Mild mode, recoverable feedback, review suggestions after failure |
| AI touchpoints | AI does not make judgments, but makes “next step suggestions” | Each contact has explainable reason and strength adjustment |
| business model | Pay without anxiety driving | The free version retains the core value, while paying for depth and efficiency |
| risk management | Treat psychological burden as a first-class risk | Set up independent indicators and response mechanisms (R10) |

---

### 1.8 One-page product positioning (One-Pager)

> **Elevator Talk (30 Second Version)**  
> "FOMO is an AI behavioral coaching app. Do you have that feeling - you clearly don't want to scroll through your phone, but you accidentally scroll through it for 30 minutes? FOMO doesn't block your app, but asks you at the moment you open it: Do you really want to use it? AI will remember your behavior patterns and tell you 'where are your weaknesses and how to improve' every week. It's like a fitness trainer - it doesn't do push-ups for you, but blocks it every time you want to be lazy and asks: Are you sure?"

| Dimensions | content |
|------|------|
| **Product Name** | FOMO (Fear Of Missing Out → redefined as Freedom Over My Output) |
| **Core Value** | Turn "unconscious browsing on mobile phones" into "conscious choice" and achieve sustainable behavior change through AI coaching |
| **Target User** | Users aged 16–45 who want to reduce useless screen time and improve focus and emotional well-being |
| **Solution** | Light friction interruption + AI personalized behavior analysis + human-centered design |
| **Business Model** | Freemium (Free Core + Pro AI Coach¥28/month) |
| **Differentiation** | The only digital health product that deeply combines AI behavioral analysis with human-centered design principles |
| **Core indicators** | Number of "unintentionally opened and then abandoned" times per user per week (NSM) |

---

### 1.9 Product scope boundaries (In Scope / Out of Scope)

| Dimensions | In Scope (first year) | Out of Scope (not doing it yet) |
|------|------------------|--------------------------|
| platform | iOS + Android (P0); browser extension (P1) | Wearable device independent app (watch/glasses) |
| intervention method | Pause page, rules engine, AI suggestions, mindful moments | Forced irreversible lock (no emergency exit) |
| AI capabilities | Behavioral insights, rule suggestions, interpretable prompts, and weekly coaching reports | Medical Diagnostic Level Psychological Assessment/Treatment Recommendations |
| data strategy | Local priority, desensitization summary upload, exportable for deletion | Collect chat content/input content/private text |
| commercialization | Personal Pro, Family Edition, Team Edition PoC | Advertising monetization, data sales monetization |

**Boundary Principle**: First build "high frequency, low intrusion, verifiable and effective" capabilities, and then gradually expand the three growth lines of "cross-device, relationship network, and device-side AI".


### 1.10 Accessibility and inclusive design requirements

FOMO's user base covers people with limited vision, people with abnormal color vision, and people with cognitive diversity. The product must meet basic accessibility requirements during the MVP stage.

| Dimensions | Require | priority | Acceptance criteria |
|------|------|--------|----------|
| screen reader | All interactive elements provide Accessibility Label / contentDescription | P0 | The entire VoiceOver / TalkBack process is operable |
| Contrast | Text/background contrast ≥ 4.5:1 (WCAG AA) | P0 | Automated scanning pass rate 100% |
| touch target | Clickable area ≥ 44×44pt (iOS) / 48×48dp (Android) | P0 | Design Code Check |
| abnormal color vision | Do not rely on pure color to distinguish states (such as emotion levels red/yellow/green require additional icons or text labels) | P0 | Color blindness simulation test passed |
| Animation weakened | Respect the system's "Reduce Dynamic Effects" setting; mindful breathing animations can be turned off | P1 | After Reduce Motion is turned on, the animation is downgraded to static instructions. |
| Font size adaptation | Support system dynamic fonts (Dynamic Type/Font Scale) | P1 | No truncation or overlap at maximum font size |

> **Implementation method**: Add accessibility items to each Sprint QA checklist; Phase 2 introduces automated accessibility scanning (Accessibility Scanner / Xcode Audit).

---

## 2. In-depth analysis of competing products

### 2.1 Overview of Globally Influential Products

#### 2.1.1 International products

| product | nation | Year of establishment | core mechanism | platform | User scale | Pricing | Scientific endorsement |
|------|------|---------|----------|------|----------|------|----------|
| **Forest** | Taiwan, China | 2014 | Gamified tree planting timing | iOS/Android/Chrome | 10M+ download | Buyout ¥12-18 | none |
| **AppBlock** | Czech Republic | 2015 | Rule engine + multi-dimensional interception | iOS/Android/Chrome/Edge/Brave | 5M+ downloads | $4.99 monthly, $29.99 annually, $89.99 lifetime | none |
| **Opal** | USA | 2021 | High intensity lock + Focus Score | iOS/macOS/Android | 4M+ users | Free version with basic functions, Pro $8.29/month (annual payment $99.99), 50% off for students | Internal data reporting |
| **Freedom** | USA | 2011 | Sync blocks across devices | Mac/Win/iOS/Android/Chromebook/Linux(6 terminal) | 4M+ users | Free basic version, Premium $3.33/month (annual payment), Forever $199 | Carnegie Mellon, Microsoft, PNAS and other 7 university studies |
| **ScreenZen** | USA | 2022 | Delay + limited unlocking + pause page | iOS/Android/Mac/Windows | 1M+ monthly activity | Completely free (donation basis) + newly launched hardware halo | none |
| **one sec** | Germany | 2021 | Forced pause + psychological interruption | iOS/Android/Browser extension | 100K+ 5-star reviews, claimed savings of 194,920 | Freemium Subscription | Max Planck Institute + Heidelberg University peer review, verification reduced by 57% |
| **StayFree** | USA | 2019 | Fine-grained usage statistics + in-app blocking | iOS/Android/Mac/Win/Chrome | 30M+ users | Freemium | none |
| **Minimalist Phone** | Germany | 2020 | Minimalist launcher replaces default desktop | Android/iOS(new) | Undisclosed | Monthly payment/annual payment/buyout optional | none |
| **Brick** | USA | 2023 | Physical NFC hardware unlock | iOS | Undisclosed | Hardware $49 + App Free | none |
| **Zario** | USA | 2023 | AI cognitive behavioral coaching + dialogue intervention | iOS/Android | Early days | Subscribe ~$9.99/month | Cognitive Behavioral Therapy (CBT) Theory |
| **Clearspace** | USA | 2022 | Force completion of tasks before opening (writing intention/breathing) | iOS | Undisclosed | Freemium ~$4.99/month | none |

#### 2.1.2 China’s local products (market structure)

> **Key conclusion: There is an extreme lack of local screen time management tools in China, with only weak alternatives and no systematic AI coaching products. **

| product | type | core mechanism | limitation | FOMO opportunity |
|------|------|----------|--------|----------|
| **Huawei/Xiaomi Healthy Usage Mode** | System built-in | Time period grayscale + App limit + Youth mode | System-level tool, with fixed functions and no AI insights, and cannot be used across brands | FOMO offers a brand-neutral, AI-enhanced alternative to achievement systems |
| **iOS Screen Time** | System built-in | App quota + deactivation time + content restrictions | The threshold for crossing is extremely low (one minute delay can bypass it), no intention confirmation, no insight | FOMO provides a stronger interception + intent coaching layer |
| **TomatoToDo/Tide** | Time to focus | Pomodoro, Pomodoro | It needs to be activated actively and cannot be intercepted. Just "focus on it" rather than "use it unconsciously". | FOMO Complementary: Provides a protective layer to "prevent procrastination in opening other apps" |
| **Super focused (mini program)** | lightweight tools | Close WeChat/Allow whitelist | Within the WeChat ecosystem, the scenarios are limited, there is no AI, and the coverage is narrow. | FOMO covers all apps, not just WeChat |
| **Time block TimeBloc** | time planning | visual time block planning | Only planning, no interception, no AI behavior analysis | Complementary to FOMO positioning, not a direct competitor |
| **Zenplex (Focus on the Planet)** | Gamified focus | Raise a pixel pet | The game feels strong but imitates Forest, lacks AI, and has limited retention. | FOMO overlays AI personalization on gamification |

**Summary of gaps in the Chinese market**:
- No product has the core mechanism of "confirmation of intention before impulse"
- No product integrates AI behavioral insights and personalized intervention
- There is a strong demand for parental control scenarios among teenagers, but they only rely on the system’s built-in tools (and there are a lot of bypass methods)
- There is no targeted product acceptance for localized content (examination preparation, Spring Festival, postgraduate entrance examination, involution anxiety, etc.)
- **Window period is about 12-18 months** - Huawei/Xiaomi/Byte may access AI health functions, but they need to overcome platform limitations and user trust barriers

### 2.2 In-depth dismantling of product logic

#### A. Forest——Gamification Positive Incentive School

**Product Logic**: Packaging "not touching your phone" into the positive behavior of "planting a tree". After the user starts the timer, the virtual sapling begins to grow; if the user leaves the timer, the sapling will die. Accumulated coins can be redeemed for real tree planting (in partnership with Trees for the Future).

**Functional breakdown**:
- Timed tree planting: 25 minutes/customized duration
- Virtual Forest: View accumulated achievements
- Friend rankings and cooperative tree planting
- Tag system (study/work/sport)
- White noise/ambient sound
- Real tree planting for charity

**Business Model**: One-time buyout (iOS ¥12-18), no subscription. Monetize by high download volume.

**Product Logic Advantages**:
- Positive incentives lower the threshold for use (not "punishing you", but "rewarding you")
- Gamification mechanism has significant short-term effects
- Charity linkage increases emotional value

**Product logic shortcomings**:
- **No interception capability**: The user can cut away at any time, and the tree dies but the App cannot stop it
- **Serious attenuation of novelty**: Limited tree species, gamification power decreases after 30 days
- **Passive design**: The user needs to actively start the timing and cannot be automatically triggered when "impulsively opening TikTok"
- **No behavioral insights**: I don’t know when users are most likely to lose control.

**Inspiration for FOMO**: Learn from its "positive framework" (show how much time is earned back), but require an active triggering mechanism.

---

#### B. AppBlock——Rule engine craftsman school

**Product Logic**: Provides the most flexible rules engine, allowing users to accurately define "what to block under what conditions." The core is the concept of Schedule - binding interception rules to time, date, and conditions.

**Functional breakdown**:
- Quick Block: Quickly initiate time-limited blocks (free version ≤ 4 hours)
- Schedules: schedule rules (free version ≤ 2), supports time period, date, usage limit
- Strict Mode: Strict lockdown mode (free version ≤ 12 hours)
  - Unlocking conditions can be configured: time/approval by followers/must be as planned
- Allowlist mode: whitelist blocking (only allowed for specified apps)
- In-app purchase blocking
- Adult content blocking
- Academy educational content (free version ≤ 3 lessons)
- Cross-end browser extension (Chrome/Edge/Brave)

**Pricing**: $4.99 monthly / $29.99 yearly (with 7-day trial) / $89.99 lifetime. Student Discount/Enterprise Edition/Gift Cards.

**Product Logic Advantages**:
- The most flexible rules in the industry
- Good cross-terminal coverage (mobile phone + browser)
- Strict Mode is highly configurable

**Product logic shortcomings**:
- **High configuration complexity**: Novices are easily confused when seeing the three concepts of Schedule/Strict Mode/Quick Block
- **Lack of behavioral insights**: It doesn’t tell you “why it’s out of control”, it only helps you “seal it”
- **Impulse-free interruption mechanism**: direct interception or no interception, no intermediate state of "pause to let you think"

**Implications for FOMO**: Learn the flexibility of their rules engine, but the configuration must be significantly simplified (templates first).

---

#### C. Opal——High-intensity focused system school

**Product Logic**: Create a complete "Focus System" - not just an interception tool, but a focus management system. Core concepts include Focus Block, Snooze & Difficulty, Focus Score, and Focus Gems.

**Functional breakdown**:
- **Focus Block®**: Set time period to block specified apps/websites
  - 18+ scene presets (study/work/bedtime/fitness/family time/deep focus, etc.)
- **Snooze® & Difficulty®**: Adjust the difficulty level of opening the app
- **Focus Score®**: Daily focus score, compared with peers
- **App Limits**: Daily usage time limit
- **App Lock**: semi-permanent lock + limited number of unlocks per day
- **Deep Focus**: Highest level of protection, cannot be bypassed or canceled
- **Leaderboard**: Leaderboard social competition
- **Focus Gems®**: Collect gem achievement system (15+ regular gems + holiday only)
- **Focus Report**: Weekly progress report

**Pricing**:
- Free version: Basic Blockade, Normal difficulty, 1 loop rule, Today’s Focus Score
- Pro $8.29/month ($99.99 annually): Advanced difficulty, Deep Focus, unlimited rules, historical Focus Score, whitelist mode
- 50% off for students

**Product Logic Advantages**:
- Strong brand power (4M+ users, many celebrity endorsements)
- Focus Score quantification system is complete
- Deep Focus works great for heavy users
- The achievement system is beautifully designed (gem collection)

**Product logic shortcomings**:
- **The free version has extremely limited capabilities** (almost a paywall product)
- **No "interruption" mechanism**: either completely blocked or completely released, lack of intermediate state
- **Configuration focus period**: Focus on "when to block" rather than "what behavior triggers"
- **Missing AI Insights**: No explanation of "why you're particularly prone to losing control at 3pm"

**Inspiration for FOMO**: Learn its Focus Score concept and beautiful achievement system, but position the differentiation in "interruptions rather than blockades".

---

#### D. Freedom - the pioneer in cross-device sync blocking

**Product Logic**: The core is "one session, block all devices". Freedom is the first product to support synchronization across all platforms (Mac/Win/iOS/Android/Chromebook/Linux 6), and it is also the product most cited in academic research.

**Functional breakdown**:
- Block Apps/Websites/Entire Internet
- Scheduling: Preset + Loop + Advance (arrange in advance)
- Locked Mode: Cannot exit after turning on
- Custom Blocklists: Custom blocklists
- Ambient Sound: white noise/cafe/natural sound
- Sync sessions across devices
- Perks: Discounts on partner brands

**Pricing**:
- Free: basic blocking, synchronization, unlimited devices, custom lists, ambient sounds
- Premium $3.33/month (approximately $40/year): Scheduling, Looping, Locked Mode, Advanced Perks
- Forever $199 one-time buyout

**Scientific Endorsement** (the strongest in the industry):
- Carnegie Mellon: Hourly wage output +22% after using Freedom
- Microsoft Research: Focus +20%
- PNAS Nexus: Reducing constant internet access significantly improves concentration and emotional well-being
- University of Waterloo: +27% mission completion
- There are also studies from many universities such as Cardiff, Arizona State, and Oslo.

**Product Logic Advantages**:
- Synchronization across 6 terminals is a unique moat
- The most scientific endorsement and high credibility
- The concept of "Session" is intuitive (start → continue → end)
- Lifetime buyout is friendly to high-frequency users

**Product logic shortcomings**:
- **Complex initial configuration** (install and log in to multiple terminals separately)
- **No Behavioral Insights**: Pure "blocking" tool, does not help understand behavior
- **No gamification or achievement system**
- **Lack of Impulsive Interrupts**: Also a choice between "full block vs. no block"

**Inspiration for FOMO**: Cross-end synchronization is a P1/P2 goal; learn from its "Session" model simplicity.

---

#### E. ScreenZen —— Light-friction free approach

**Product Logic**: The core belief is "You don't need a complete lockdown, just a little more friction." A pause page pops up when you open the app, and you can set the delay waiting time and the maximum number of unlocks per day. Completely free and relying on donations, the newly launched hardware product halo is monetized.

**Functional breakdown**:
- **Select App → Set Limits → Schedule → Use Consciously → Track Results** Five-step process
- Pause/wait page (forced wait before opening the app)
- Limited unlocking (maximum number of times that can be opened per day)
- time limit
- Time blocking
- Focus Mode is linked to the system
- Streak tracking
- Password protected/locked mode
- Custom prompts (such as "What are you looking for?")
- **New product halo**: a physical companion device placed in the bedroom/desk, allowing zero distractions in a specific space

**PRICE**: Completely free (donation basis). halo hardware sold separately.

**User reputation** (App Store 4.8 stars, 1M+ monthly active users):
- "It's so annoying that I don't want to open those apps anymore - so it works"
- "Better configured than one sec and completely free"
- "The Streak mechanic is very motivating to me"
- "The best free screen time app"

**Product Logic Advantages**:
- **Completely Free** Eliminates all resistance to payment
- Pause page + time limit + custom prompt = light friction combo punch is very effective
- Excellent user reputation
- Halo hardware cuts into the physical scene

**Product logic shortcomings**:
- **The sustainability of the free model is questionable** (donation income is limited)
- **Weak advanced data analysis skills** (doesn’t tell you trends and patterns)
- **No AI Insights**
- **No achievement system** (lack of deep incentives outside of Streak)
- **Lack of Team/Family Capabilities**

**Inspiration for FOMO**: ScreenZen proves that the core mechanism of "pause page + limit" is very effective. FOMO should take this core and layer insights + achievements on top of it.

---

#### F. one sec – Pioneer of scientific interruption

**Product Logic**: Forced insertion of psychologically designed interruptions before opening the target app each time - deep breathing, selfie mirroring, intention reflection, rotating phone, etc. The core is "the automatic circuit that interrupts the dopamine cycle."

**Functional breakdown**:
- **Interruption Types** (designed by psychologists): Deep breathing (standard), 4-7-8 breathing method, mirror reflection (front camera), conversational reflection, rotate phone 3 times, enter random text, structured integration (Structured App linkage), Lengo integration (turn interruptions into language learning)
- **Full Blocking Mode**: Complete blocking within a specified period of time
- **Usage time limit**: Emergency braking for screen swiping
- **Intent Tracking**: Record the purpose of each opening
- **Mood Tracking**: Reflects how app usage affects mood
- **Diary function**: write down thoughts and feelings
- **Healthy Alternative Guidance**: Guidance toward healthier behaviors
- **Browser extension**: Firefox/Edge/Safari/Chrome full coverage
- **Third Party Integration**: Structured/Lengo

**Scientific Endorsement**:
- Max Planck Institute + Heidelberg University peer-reviewed research
- 57% reduction in verification app usage
- German and Danish government certification
- Claims to have saved users 194,920 years
- Reported by authoritative media such as NYT, Business Insider, TIME, WSJ, The Verge, etc.
- Bryan Johnson Publicly Recommended

**User Review Summary**:
- "My screen time dropped from 19 hours to 2 hours"
- "Strict lockdown never works - because I can always switch off. Forced pauses give me a conscious choice"
- "I'm about to burnout after becoming a doctor. This app helps me get my life back."

**Product Logic Advantages**:
- **The most solid scientific basis** (the only product with peer-reviewed research)
- There are many types of interruptions and they have psychological basis
- Full browser extension coverage
- Third-party App integration (Structured, Lengo)

**Product logic shortcomings**:
- **iOS configuration is complex** (relies on Shortcuts automation)
- **Higher Pricing** (compared to ScreenZen Free Trial)
- **Missing Team/Family Features**
- **Insufficient Chinese localization**

**Implications for FOMO**: One sec proves the effectiveness of "Science Interruption". FOMO should achieve the same level of interruption mechanism, while simplifying configuration and adding Chinese localization.

---

#### G. Zario / Clearspace - AI coaching pioneer

| product | Core differences | product logic | Current situation and limitations |
|------|----------|----------|------------|
| **Zario** | AI Cognitive Behavioral Coach | Based on CBT theory, AI talks to users to analyze addiction triggers and generates personalized intervention strategies. | In early products, AI dialogue is relatively general and lacks deep behavioral data closed loop; no Chinese language; no local behavioral data flywheel. |
| **Clearspace** | "Complete tasks before opening" | Require users to complete set tasks (such as writing intentions, taking deep breaths) before opening the target app; increase cognitive friction | iOS only; task completion not tied to behavioral data; no AI personalization |

**Inspiration for FOMO**: Zario/Clearspace proves that the market is receptive to "cognitive intervention", but both lack the closed loop of behavioral data + AI personalization. FOMO should be an **AI coach with a data closed loop**, not a general conversation robot.

#### H. Brick、StayFree、Minimalist Phone

| product | Core differences | product logic | limitations |
|------|----------|----------|------|
| **Brick** | Physical NFC hardware | The phone must be brought close to the NFC brick to unlock the app, introducing real-world physical costs | Hardware $49, high threshold, only iOS, limited scenarios |
| **StayFree** | Finest-grained statistics | It not only counts the duration of the app, but also counts the time of specific functions (Reels/Shorts) within the app. | Extremely high dependence on permissions (Accessibility), privacy controversy |
| **Minimalist Phone** | Replace mobile phone desktop | A minimalist text-only interface replaces the default desktop and reduces dopamine stimulation from the "entry" | Mainly only Android (iOS has just been launched), the threshold for adaptation is high |

### 2.3 Competitive product functional capability matrix

| Capability dimension | Forest | AppBlock | Opal | Freedom | ScreenZen | one sec | StayFree | **FOMO** |
|----------|--------|----------|------|---------|-----------|--------|----------|----------|
| Impulse break/pause page | ✗ | ✗ | ✗ | ✗ | ✓✓ | ✓✓ | ✗ | **✓✓** |
| Confirmation of Intent Inquiry | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | **✓✓** |
| Period interception | ✗ | ✓✓ | ✓ | ✓✓ | ✓ | ✓ | ✓ | **✓✓** |
| daily limit | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓✓ | **✓✓** |
| Unlock count control | ✗ | ✗ | ✓ | ✗ | ✓✓ | ✗ | ✗ | **✓** |
| strict/lockdown mode | ✗ | ✓ | ✓✓ | ✓✓ | ✓ | ✓ | ✗ | **✓** |
| Gamification/Achievements | ✓✓ | ✗ | ✓✓ | ✗ | ✓ | ✗ | ✗ | **✓** |
| Data report | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓✓ | **✓✓** |
| positive narrative framework | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **✓✓** |
| Sync across devices | ✗ | ✓ | ✓ | ✓✓ | ✓ | ✓ | ✓✓ | P1 |
| browser extension | ✓ | ✓✓ | ✗ | ✓ | ✗ | ✓ | ✓ | P1 |
| family/team | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | P1 |
| AI behavioral insights | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **✓✓(P1)** |
| AI real-time intervention recommendations | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **✓(P2)** |
| AI conversation coach | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **P2** |
| Anti-bypass protection | ✓ | ✓ | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | **✓** |
| In-app feature interception | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓✓ | P2 |


> ✓✓ = Industry leading | ✓ = Available | ✗ = Not available

**Empirical data on user churn of competing products (external research, 2025)**

| product | monthly churn rate | Main reasons for churn | Data source |
|------|---------|-------------|-------|
| Forest | ~68% users abandon within 1 month | Tree withering penalty causes frustration; in multiplayer mode, one person quits and the whole group fails | FOMO Reset PRD 2025 Quote |
| Freedom | ~35% of paid users cancel their subscription | After forced shielding, the "feeling of being controlled" leads to resentment, and anxiety increases after shielding. | FOMO Reset PRD 2025 Quote |
| Screen Time (System) | Only 22% of users check it regularly | Pure data display without action guidance, settings frequently fail | FOMO Reset PRD 2025 Quote |
| Blocking Tools (Statistics) | High attrition (see CMU 2021 for specific data) | Simple forced lock → user avoidance (uninstall the app/change the device) | Summary of multiple studies |

> **Design inspiration**: The core of FOMO is the break of "behavior→psychological positive feedback", rather than simply the length of use. Forced blockade is effective in the short term but leads to long-term resentment. "Negotiative intervention + psychological positive guidance" is a more sustainable path to retention.

### 2.4 Classification of behavioral intervention types

| intervention type | Representative products | Mechanism principle | Duration of effect | User dislike |
|----------|----------|----------|------------|-----------|
| **Soft Intervention-Incentive** | Forest | Tree planting reward + dead tree penalty | Medium (novelty fades) | Low |
| **Soft Intervention-Friction** | ScreenZen、one sec | Delay and wait, ask for intent, take a deep breath | **High** (change habit loop) | low-medium |
| **Hard Intervention-Rules** | AppBlock、Freedom | Time block, lock mode | High (but requires high commitment) | Medium-High |
| **Quantitative Intervention-Feedback** | Opal、StayFree | Rating/Trend Chart/Peer Comparison | Medium (need to cooperate with the action mechanism) | Low |
| **Physical Intervention** | Brick、ScreenZen halo | NFC/physical device trigger | Very high (but limited popularity) | Low |
| **Cognitive Intervention** | Zario | AI coaching conversation | Theoretically the highest (to be verified) | Low |

### 2.5 Panoramic comparison of competitive product pricing

| product | Free version capabilities | Lowest monthly fee | annual fee | lifelong | Monetization model |
|------|-----------|---------|------|------|---------|
| Forest | Limited tree species | — | — | ¥12-18 | One-time buyout |
| AppBlock | 2 Rules + 4h Quick Block | $4.99 | $29.99 | $89.99 | Subscription + Lifetime |
| Opal | Basic Blockade +1 Rule | $8.29 (paid annually) | $99.99 | have | Subscription + Lifetime |
| Freedom | Basic blocking + sync | $3.33 (paid annually) | ~$40 | $199 | Subscription + Lifetime |
| ScreenZen | **Full-featured for free** | $0 | $0 | — | Donate + Hardware |
| one sec | base interruption | ~$3.33/month (paid annually) | ~$39.99 | — | subscription |
| StayFree | basic statistics | ~$1.99/month (paid annually) | ~$23.99 | — | subscription |

### 2.6 Cross-Dimensional Comparison

Horizontal analysis compares major competing products on a unified scale from **9 core dimensions** to help identify market gaps and FOMO entry opportunities.

#### 2.6.1 Comparison of product positioning and core concepts

| product | core concept | product quadrant | Target user portrait | brand tone |
|------|----------|----------|-------------|----------|
| Forest | "Planting trees = not touching your mobile phone", positive gamification incentives | Lightweight incentive type | Students/young white-collar workers, pursuing a sense of ritual | Warmth, healing, charity |
| AppBlock | "You set the rules and I execute them", engineer-style precise control | Heavy tool type | Technology-oriented users require precise control | Professional and functionally oriented |
| Opal | "Focus System", system-level focus management | High-end system type | Efficiency seekers with high consumption willingness | Exquisite, technological, high-end |
| Freedom | "Block all devices at once", synchronized across devices | Professional blocking type | Writer/Researcher/Multi-Device Professional | Academic, serious, credible |
| ScreenZen | "Just a little friction is enough", light intervention | Lightweight friction type | Ordinary users who are sensitive to payment | Simple, practical and friendly |
| one sec | "Interrupting dopamine circuits," Science Interrupt | Science Interruption | Mental health follower/geek user | Scientific, minimalist, German rigorous |
| StayFree | "You can change only if you know", data-driven | Data quantification | Analytical users who need detailed reporting | Data-based, neutral |
| **FOMO** | **"Conscious Choice > Passive Dependence", AI Coach** | **AI Fusion** | **Chinese users/students/workers/families** | **Warm, smart, positive** |

#### 2.6.2 In-depth comparison of intervention mechanisms

| Dimensions | Forest | AppBlock | Opal | Freedom | ScreenZen | one sec | FOMO |
|------|--------|----------|------|---------|-----------|---------|------|
| **Time to intervene** | User initiates | Default rule triggers | Trigger at preset time period | Default session trigger | When app starts | When app starts | **App startup + rule trigger** |
| **Intervention intensity** | Weak (the tree dies but does not prevent it) | Strong (direct interception) | Strong-Extremely strong (including Deep Focus) | Strong (block the entire section) | Medium (can pass after waiting) | Medium (can pass after completion) | **Adaptive (AI dynamic adjustment)** |
| **Intervention methods** | Visual stimulation (planting trees) | Black screen interception | Blocking/Rating/Difficulty Level | Black screen/disconnection | Pause page + countdown | Breathe/mirror/reflect | **Intent Confirmation + Pause + Suggestion** |
| **Intermediate state** | None (fully open/fully closed) | none | Section (difficulty level) | none | ✓ (You can enter after waiting) | ✓ (You can enter after completion) | **✓✓(Intent Grading + Secondary Delay)** |
| **Cognitive Engagement** | Low (passive tree planting) | Low (system execution) | Low-Medium (see rating) | Low (system execution) | Medium (read prompt) | High (Active Breathing/Reflection) | **High (intent selection + AI feedback)** |
| **Fatigue Resistance** | Poor (attenuation after 30 days) | Medium (the rules are fixed and not boring) | Medium (the novelty of the rating is limited) | middle | Medium-High (prompts vary) | High (multiple interrupt rotations) | **High (AI dynamics + achievement system)** |

#### 2.6.3 Comparison of user experience and entry threshold

| Dimensions | Forest | AppBlock | Opal | Freedom | ScreenZen | one sec | FOMO |
|------|--------|----------|------|---------|-----------|---------|------|
| First configuration time | <1 minute | 5-10 minutes | 3-5 minutes | 10-15 minutes (variable) | 2-3 minutes | 3-5 minutes (complex for iOS) | **≤2 minutes** |
| Configuration complexity | ⭐ Minimalist | ⭐⭐⭐⭐ Complex | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ Complex (multiple) | ⭐⭐ Simple | ⭐⭐⭐ Medium (iOS) | **⭐⭐ Simple (template first)** |
| Daily use perception | Need to be started actively | Silence in the background | Backstage + Rating | Silence in the background | Appears when opening the App | Appears when opening the App | **Intelligent appearance + daily push** |
| learning curve | gentle | steep | medium | medium-steep | gentle | Flat(Android)/Medium(iOS) | **gentle** |
| Chinese localization | ✓✓(Taiwan team) | ✗(Mainly English) | ✗(English) | ✗(English) | ✗(English) | ✗(English/German) | **✓✓(Native Chinese)** |
| emotional friendliness | Medium (healing) | Low (strong tool feel) | Medium (achievement-driven) | Low (commanding) | Medium (light intervention) | Medium-High (psychology-driven) | **High (non-humiliating + recoverable)** |

#### 2.6.4 Horizontal comparison of business models

| Dimensions | Forest | AppBlock | Opal | Freedom | ScreenZen | one sec | FOMO |
|------|--------|----------|------|---------|-----------|---------|------|
| **model** | one time buyout | Subscription + Lifetime | Subscription + Lifetime | Subscription + Lifetime | Free + Hardware | subscription | **Subscription + Lifetime** |
| **FREE VERSION VALUE** | Basic available | Limited but available | extremely restricted | Basic available | **Fully Featured** | Basic available | **Core functionality available** |
| **Paid barrier** | None (paid) | Number of rules + duration | almost all features | Schedule + Lock | none | Advanced interrupt types | **AI+strict+unlimited rules** |
| **ARPU Potential** | Low(¥15 once) | Medium(~$30/year) | High ($100/year) | Medium ($40/year) | Very low (donation) | Medium (~$35/year) | **Medium-High(¥198/year)** |
| **LTV Sustainability** | Low (no repurchase) | middle | High (but drains quickly) | High (strong stickiness) | Low | middle | **High (AI Data Flywheel)** |
| **Growth Engine** | Word of mouth + public welfare | ASO | Brand+KOL | Academic endorsement | Word of mouth + free | Science + Media | **Share Card + Partner Invitation** |

#### 2.6.5 Horizontal comparison of technical capabilities

| Dimensions | Forest | AppBlock | Opal | Freedom | ScreenZen | one sec | FOMO |
|------|--------|----------|------|---------|-----------|---------|------|
| System level interception | ✗ | ✓✓ | ✓✓ | ✓✓ | ✓ | ✓ | **✓✓** |
| Cross-end synchronization | Chrome plugin only | browser extension | iOS+macOS | **Full coverage on 6 terminals** | 4 terminals | browser extension | **P1(iOS/Android first)** |
| AI/ML capabilities | none | none | none | none | none | none | **✓✓(Behavior Analysis LLM)** |
| end-to-end reasoning | none | none | none | none | none | none | **P3(Core ML/NNAPI)** |
| Data analysis depth | none | Base | Medium(Focus Score) | none | Base | Medium (intent tracking) | **Depth (AI Insight)** |
| privacy architecture | local | Local + cloud | Local + cloud | Cloud sync | local | Local + cloud | **Local priority + summary upload** |

#### 2.6.6 Key conclusions of horizontal analysis

| # | in conclusion | FOMO revelation |
|---|------|----------|
| 1 | **No one occupies the intersection of "AI + Screen Time Management"** | The biggest differentiation window for FOMO positioning, first mover advantage |
| 2 | **No dominant player in the Chinese market** (Forest is from Taiwan but has weak functions) | Native Chinese + local scene = huge unmet need |
| 3 | **"Intermediate Intervention" is verified to be effective** (ScreenZen/one sec) | FOMO should use this as the core mechanism and not implement "total blockade" |
| 4 | **Free full functionality vs strong paywall represent two extremes** | FOMO takes the middle value: the core value of the free version experience, AI is the payment barrier |
| 5 | **Scientific endorsement is a long-term trust barrier** (Freedom/one sec) | FOMO should initiate collaborative research with universities in Phase 2 |
| 6 | **No competing product has the three capabilities of "interruption + rules + insight" at the same time** | FOMO three-layer combination boxing is the core of differentiation |
| 7 | **Most competing products emphasize control and weaken psychological feelings and dignity** | FOMO uses "human-centered care indicators" as product quality constraints to form long-term reputation barriers |

---

### 2.7 Competitive product vertical analysis (Evolution & Trend Analysis)

Vertical analysis tracks the **development and evolution paths** of key competing products to identify industry trends and predict future trends.

#### 2.7.1 Industry Development Timeline

```
2011        2014        2015        2019        2020        2021              2022         2023        2024-2026
  |           |           |           |           |           |                |            |           |
Freedom Forest AppBlock StayFree Minimalist Opal + one sec ScreenZen Brick AI Native Era
 (Blocking) (Gamification) (Rules) (Statistics) (Desktop) (Systems+Science) (Friction) (Hardware) (→ FOMO)
  |           |           |           |           |           |                |            |           |
First generation Second generation Second generation Third generation Third generation Fourth generation Fourth generation Fifth generation Sixth generation
Pure blockade, gamified incentives, rules engine, data quantification, environmental transformation, systematic/scientific, light friction, physical intervention, AI driven
```

#### 2.7.2 Analysis of product generation evolution

| intergenerational | period | Representative products | core concept | limitation | evolutionary driving force |
|------|------|----------|----------|--------|------------|
| **First Generation: Pure Blockade** | 2011-2014 | Freedom | "Turn it off" — simply and crudely disconnect the Internet/lock the App | User disgust, inelasticity, and lack of insight | Users need a more friendly way |
| **Generation 2: Gamification/Rules** | 2014-2018 | Forest、AppBlock | "Reward You" / "Precise Control" — Positive Framework or Flexible Rules | Forest power decay; AppBlock configuration is complicated | Users need smarter intervention |
| **Third Generation: Data Quantification** | 2019-2020 | StayFree、Minimalist Phone | "See it" — Using data visualization to drive awareness | Knowing ≠ change, data anxiety | Users need help "at critical moments" |
| **The fourth generation: systematic/scientific** | 2021-2022 | Opal、one sec、ScreenZen | "System Administration" / "Science Interruption" — Complete Journey + Psychology | Missing Chinese, high paywall, no personalization | AI and personalized needs |
| **Fifth Generation: Physical Intervention** | 2023 | Brick、ScreenZen halo | "Physical World Constraints" — NFC/Hardware Devices | Limited popularity and high cost | The trend of combining soft and hard |
| **Sixth Generation: AI Native** | 2025+ | **FOMO** | **"AI Coach"** — behavioral understanding + personalized real-time intervention | To be verified | LLM cost reduction + terminal-side AI matures |

#### 2.7.3 Vertical evolution trajectory of key competitive products

**Forest evolution route (2014→2026)**

```
2014: Timed Tree Planting MVP
  ↓
2015-2016: Increase tree species diversity + friend collaboration + white noise
  ↓
2017-2018: Real tree planting charity cooperation + Chrome extension
  ↓
2019-2021: Users grow to 10M+ downloads, but feature innovation stagnates
  ↓
2022-2026: Slowing growth, core mechanisms not upgraded, no AI capabilities
         → Gradually lose differentiation in the face of fourth/fifth generation competing products
```

**Key Lesson**: Gamification mechanisms have a limited life cycle (decay after ~12 months), and there must be **continuously adding value mechanisms** (such as AI personalization) to maintain long-term retention.

**Opal evolution route (2021→2026)**

```
2021: Focus Block MVP → Quickly acquire seed users
  ↓
2022: Focus Score + Focus Gems → Quantification + Achievement twin engines drive growth
  ↓
2023: Deep Focus + Leaderboard → Enhance Stickiness + Brand Premium
  ↓
2024: Expanding macOS + Android → cross-end coverage
  ↓
2025-2026: 4M+ users, high price of $99.99/year, but lack of AI capabilities
        → Emphasis on product experience and brand power, but technical barriers are not deep enough
```

**Key Lesson**: Brand power + sophisticated interaction can support high pricing, but if AI is not introduced in time, it may be hit by the dimensionality reduction of the next generation of products.

**ScreenZen Evolution Roadmap (2022→2026)**

```
2022: Pause page + limited MVP → Acquire customers quickly for free
  ↓
2023: Streak mechanism + custom prompt → word-of-mouth explosion (4.8 stars)
  ↓
2024: Mac/Windows extension → multi-end coverage
  ↓
2025: halo hardware release → explore the integration of physics + software for monetization
  ↓
2026: 1M+ MAU, but limited revenue from free model
        → Business sustainability is the biggest challenge
```

**Key Lesson**: Free full-featured products can quickly acquire customers and build word-of-mouth, but you must find a sustainable way to monetize (hardware is an attempt).

#### 2.7.4 Judgment of industry trends

| # | trend | in accordance with | Impact on FOMO |
|---|------|------|---------------|
| 1 | **From "control" to "coaching"** | Forest→one sec→The evolution direction of AI coaching | FOMO’s AI behavioral coach is at the forefront of trends |
| 2 | **From "general rules" to "personalized intervention"** | Users are tired of the same rules | AI-driven personalization is a core selling point |
| 3 | **From "single-ended" to "full scenario"** | Freedom 6 terminals, ScreenZen 4 terminals trend | FOMO P1 needs to cover iOS+Android, and P2 needs to cover desktop |
| 4 | **From "pure software" to "a combination of software and hardware"** | Brick NFC、ScreenZen halo | FOMO P3 can consider hardware companion devices |
| 5 | **From "interception tool" to "health platform"** | one sec diary/mood tracking, Opal Focus Score | FOMO weekly report + AI coach = prototype of health management platform |
| 6 | **The gap in the Chinese market is about to be filled** | No leading product but huge demand | FOMO has a 12-18 month head start window |
| 7 | **AI native products will redefine categories** | LLM cost ↓, end-side AI is mature | FOMO has the opportunity to become the first AI-native product in the category |
| 8 | **Scientific evidence-based basis will become the standard for trust** | Freedom has 7 university studies and one sec has peer review | FOMO should initiate collaborative research in Phase 2 |

#### 2.7.5 Prediction of competitive product strategy trends

| Competing products | possible direction | FOMO coping strategies |
|------|----------|---------------|
| Opal | High probability of adding AI insight function in 2026-2027 | FOMO needs to establish AI behavioral data barriers within 12 months |
| ScreenZen | May take the hardware + community route instead of AI | The differentiation is clear and there is no direct conflict in the short term. |
| one sec | Possible deepening of scientific collaboration or acquisition | Focusing on its research methods, FOMO can collaborate with different universities |
| Freedom | Likely to maintain the status quo (mature and stable) | Indirect competing products (different user groups) |
| Apple/Google | Possible enhancement of "Focus" functionality at system level | The biggest risk - FOMO needs to establish irreplaceable value for the system in social/AI/achievement |
| New players (AI native) | AI-first competing products may appear in 2026-2027 | Speed ​​is the barrier - FOMO The sooner you establish a user data flywheel, the safer it will be |

---

### 2.8 FOMO Differentiated Competition Strategy

| Competing products lack common features | FOMO differentiated entry |
|--------------|----------------|
| Most products "either intercept or incentivize" with a single mechanism | **Three-layer Combination Boxing**: Integration of interruption (pause) + rules (interception) + feedback (insight) |
| Newbies will lose users in Flow if the configuration is complicated. | **Template first**: 3-step setup out of the box, preset study/work/bedtime templates |
| Lack of explanation of "why it got out of control" | **Behavioral Insights AI**: "You're most likely to lose control at 3pm" |
| There is a serious lack of localization in the Chinese market | **In-depth exploration of local scenes**: Preparation/Spring Festival/Before going to bed/Countdown to postgraduate entrance examination |
| Lack of social restraint mechanism | **Partner Supervision**: Two-person challenge + external commitment enhancement effect |
| Reports are all negative narratives of "you've logged another X number of hours" | **Positive Frame**: Demonstrate "You earned back X hours" |
| No product combines "scientific interruption" and "rules engine" | **Interruption + Rule Fusion**: The pause page runs within the rule framework |
| **None of the competing products have AI-driven personalization capabilities** | **AI Behavioral Coach**: From "Thousands of people have the same face" to "Thousands of people have the same face" |
| **Each competing product has a single function and intergenerational capabilities are not integrated** | **Cross-generational integration**: Integrating the excellent mechanisms of the first to fifth generations + the native capabilities of sixth-generation AI |

**AI Data Flywheel—The Core Moat of FOMO**

FOMO's AI barriers come from **local private behavioral data**, not the model itself (all competing models can call the same API):

```
The longer the user uses
    ↓
The richer the local behavioral data (period/emotion/regular)
    ↓
AI insights become more personalized and accurate
    ↓
Users feel “it really understands me”
    ↓
Migration costs are extremely high (data will be cleared when changing to another app)
    ↓
Retention rate increases and willingness to pay increases
```

This is a barrier that competing products cannot copy even if they copy the functions. Even if ScreenZen added AI tomorrow, it would still need to wait for users to accumulate 6 months of data to generate insights of the same quality.

**Differentiation Path (12 Months)**

| stage | core goals | Differentiated actions | Verifiable results |
|------|----------|------------|------------|
| M1-M3 (available) | Be “more effective than free products” | Interruption + rules + feedback three-layer closed loop, default human-centered copywriting | D7 ≥ 35%, complaint rate < 1% |
| M4-M6 (trusted) | Achieve “understanding users better than high-priced products” | AI weekly report + explainable suggestions + one-click execution | AI recommendation adoption rate ≥ 40% |
| M7-M9 (removable) | Establish "continuously effective across scenarios" capabilities | Emotional perception, mindful moments, and family empathy are online | High-risk duration decreased by ≥ 25% |
| M10-M12 (defensive) | Build a hard-to-replicate moat | Local behavioral data flywheel + family/partnership chain | D30 ≥ 25%, home version renewal ≥ 70% |

**Three-layer moat (from shallow to deep)**:
- Experience moat: low friction interruption + to evaluate feedback, improve reputation and long-term retention.
- Data moat: Local behavior + emotional context forms an individual model, and migration costs are high.
- Relational moats: Partner monitoring and family empathy networks create social stickiness.

**Key points to learn from external reports (Global FOMO competitive product analysis + AI driven solutions)**
- The relationship repair narrative is effective: Upgrade the "focus" narrative to "relationship repair/mission practice" and reduce the "feeling of being controlled".
- Emotional computing requires multi-modality: in addition to touch frequency/light, soft signals such as front-facing cameras/expressions can be piloted in stages for emotional inference, but local processing is defaulted and can be turned off by the user.
- Lightweight mission log: Provide a reflection entry for the "Relationship/Mission" line in the daily/weekly report to avoid redundant check-ins and keep it optional.
- Faith/community segment: Small groups such as churches/education have high willingness for digital health and can be used as low-cost PoC channels (see §7.3.3 B2B segment scenario expansion for details).

---


## 3. Functional documentation

> **Description**: This chapter is arranged by function priority. Each function includes user stories, product logic, function details, interaction process and acceptance criteria.  
> **Priority Definition**: P0 = MVP must be online; P1 = Phase 2 (W13-W24); P2 = Phase 3 and beyond.  
> **Acceptance Criteria Hierarchy**: Functional Correctness → Boundaries and Anomalies → Performance → AI Enhancement (P1).

### 3.0 Function Priority Summary List

**iOS vs Android capability difference downgrade table (expected management)**

| Function | Android (Accessibility) | iOS (Screen Time API) |
| :--- | :--- | :--- |
| In-app page blocking | Support (such as only blocking Douyin recommended streams) | **Not supported** (can only block the entire App) |
| Browser URL blocking | Support (all major browsers) | Only supports Safari (requires extension) |
| grayscale mode | Support one-click switching | Need to jump to system settings or Shortcut |
| Strong anti-uninstallation | Support (Device Manager) | **Not supported** (system limitation) |

| serial number | Function module | priority | stage | core value | state |
|------|----------|--------|------|----------|------|
| F-01 | impulse interruption | **P0** | MVP | Interrupt automated behavior at critical decision points | To be developed |
| F-02 | Rule Center | **P0** | MVP | Provide users with a configurable constraint framework | To be developed |
| F-03 | Feedback and Achievements | **P0** | MVP | Make improvements visible and strengthen motivation to persist | To be developed |
| F-04 | Anti-bypass protection | **P0** | MVP | Prevent self-sabotage in impulsive moments | To be developed |
| F-05 | Newbie guide | **P0** | MVP | Ensure 3-step first-time configuration | To be developed |
| F-06 | AI Weekly Coach | P1 | Phase 2 | Personalized insights + actionable recommendations | To be planned |
| F-07 | Partner supervision | P1 | Phase 2 | External commitment + social constraints | To be planned |
| F-08 | browser extension | P1 | Phase 2 | Overlay desktop scene | To be planned |
| F-09 | family empathy model | P1 | Phase 2–3 | Improve family collaboration and psychological safety | To be planned |
| F-10 | In-app feature interception | P2 | Phase 3 | Accurately intercept Reels/recommendation flows | To be evaluated |
| F-11 | minimalist mode | P2 | Phase 3 | Desktop stimulation | To be evaluated |
| F-12 | Emotion sensing engine | P1 | Phase 2（W17-18） | Multidimensional behavioral signals infer emotional stress levels and automatically switch to gentle intervention | To be planned |
| F-13 | mindful moments | P1 | Phase 2（W17-18） | Provides 30-90 second recovery path during impulse window | To be planned |

**Status Caliber (for 3.0 and 8.4)**:
- To be developed: The demand has been clarified and is waiting to be entered into the research and development schedule.
- To be planned: The direction has been confirmed, waiting for program review/resource implementation
- Pending evaluation: Subject to technical or commercial feasibility, evaluation needs to be completed first
- To be completed: Non-R&D deliverables (legal affairs/documents/processes) are to be implemented.
- Continuous: Continuous execution requirements (no single "completion" time point)

### 3.1 AI touchpoint map (product logic)

| Contact | Trigger condition | Enter data | AI output | User action | security boundary |
|------|----------|----------|---------|----------|----------|
| T1 first boot recommendation | New user completes target selection | Target type + list of installed apps | Risk classification + template suggestions | One-click adoption/fine-tuning | Does not read content, only App metadata |
| T2 interrupt copywriting before starting | Open high-risk apps | Time period + Select records in the last 7 days | Personalized prompts + recommended waiting time | Leave/Continue | No humiliation, threats, or moral judgment |
| T3 rule optimization suggestions | periodic evaluation | Rule hit rate + bypass frequency | Suggestions for rules that are too loose/tight | One click execution | Recommendations must be revocable |
| T4 emotion awareness reminder | Continuous urges or high pressure at night | Intent label + period + number of consecutive failures | Gentle soothing + stress reduction goals | Entering a moment of mindfulness/pause | Do not output medical diagnosis conclusions |
| T5 Weekly Behavioral Coaching | Fixed push every week | 7-day behavioral summary | Trend explanation +1~3 suggestions | adopt/ignore | Provide a "why" explanation |
| T6 Family Empathy Summary | Family Pattern Weekly | Trends in family members meeting standards (desensitization) | Collaborative advice + communication skills | Start a family challenge/discussion | Do not display personal details by default |
| T7 Partner Challenge Suggestions | The two-player challenge cycle ends | Completion rate of both parties + time period difference | Challenge difficulty suggestions for next week | One click to initiate | Shared with mutual consent |

**AI Touchpoint Unification Principles**: Explain first, then suggest; be gentle first, then escalate; you can exit at any time; never judge.

---

### F-01 Interruption Gate

#### user stories

> **As** a user who easily opens Douyin unconsciously,  
> **I wish** there was a brief pause and confirmation of intent before each opening,  
> **so** that I can realize what I'm doing and decide if I really want to get into it.

#### product logic

Learn from one sec's "Interrupting the Dopamine Loop" theory and ScreenZen's "Pause Page" practice. The core is not to "intercept users", but to "allow users' rational brains to have time to come online."

#### Function details

| sub function | describe | Configurable items |
|--------|------|----------|
| Pause page trigger | The system inserts a pause page when opening high-risk apps | Trigger App list (up to 30) |
| waiting time | After the countdown ends, the "Continue" button appears | 3/5/8/10/15 seconds optional |
| confirmation of intent | "What do you do when you open it now?" + 4 options | Option copy can be customized |
| Quick options | Reply to messages/check information/click on habitually/bored | Editable to add and delete |
| secondary delay | Select "Habitual Clicking" or "Boring" and then add 3 seconds + encouragement copy | switch+seconds |
| Leave button | Return directly to desktop | always show |
| Custom prompts | Set personalized reminders | free text |
| Breathing Guidance(P1) | Optional deep breathing animation during pause | switch |
| Mild mode(P1) | Late at night/when there are continuous failures, give emotional comfort and small goal suggestions first, and then decide whether to upgrade the restrictions. | switch (on by default) |
| AI adaptive delay (P1) | AI dynamically adjusts the waiting seconds based on the current period/historical out-of-control probability | switch, on by default |
| AI intelligent prompts (P1) | AI generates personalized prompts based on user behavior patterns (such as "You have chosen to leave at this time in the past 3 days👏") | switch |

#### Detailed process

```
User clicks on high-risk apps
      |
The system detects that the target App is launched → intercept
      |
Pop up the pause page (full screen coverage)
  - Display custom prompts
  - Showing 4 intent options
  - Countdown N seconds
      |
  +----------------------------------+
  | Select "Reply to message"/"Check information"           | → Countdown ends → "Continue" button activated → Enter App
  +----------------------------------+
  | Select "Habitually Click"/"Boring"           | → Encouragement copy + 3 extra seconds → "Continue" button activated
  +----------------------------------+
  | Click "Leave"                        | → Return to desktop
  +----------------------------------+
      |
User choices are recorded to local behavior logs (for daily/weekly report analysis)
```

#### Acceptance criteria

**Functional Correctness**
- [ ] The pause page pops up within 300ms after the target App is launched, without perceptible flickering.
- [ ] Countdown progress bar animation is smooth (≥ 60fps), time error ≤ 200ms
- [ ] The "Continue" button is unclickable and visually disabled before the countdown ends.
- [ ] The user intends to write to the local database within 50ms (including timestamp, App ID, option value)
- [ ] After selecting "Leave", the App process will not be activated and return to the previous page (not forced to jump to the desktop)
- [ ] All functions run normally without network (pure local logic)
- [ ] Supports monitoring up to 30 apps at the same time, prompting the user when exceeding the limit but not crashing

**Boundaries and Anomalies**
- [ ] When the app is awakened by a system notification, the pause page is still correctly triggered.
- [ ] Pause page triggers ≤ 20 times within 1 hour (after exceeding the limit, silently release and record logs)
- [ ] Unlock the device again after locking the screen. If the app is still in the foreground, the pause page will not pop up repeatedly.
- [ ] No layout misalignment for mainstream screen sizes (from iPhone SE to iPad Pro)
- [ ] The pause page correctly covers the target App in Android multi-window/split-screen mode

**performance**
- [ ] Interception delay in cold start scenario ≤ 500ms (including Accessibility Service response time)
- [ ] Pause page memory usage ≤ 30MB
- [ ] 24h background monitoring additional power consumption ≤ 2% (verified by Instruments/Android Profiler)

**AI Enhancement (P1)**
- [ ] Automatically switches to mild mode after ≥ 3 consecutive failures (emotion tag writes MEDIUM/HIGH)
- [ ] AI adaptive delay: automatically +3-5 seconds during high-risk periods, reduced to 3 seconds during low-risk periods
- [ ] AI prompt generation delay ≤ 800ms; the default prompt will be displayed after timeout and the user will not be aware of it.
- [ ] AI prompts do not contain judgmental or humiliating words (keyword filtering + manual review double verification)

---

### F-02 Rules Hub

#### user stories

> **As** an office worker who needs to fall asleep before 11pm,  
> **I hope** to set "bedtime mode" to automatically block social media after 22:30,  
> **So that** I can fall asleep on time without being interrupted by scrolling.

#### product logic

Learn from the rule flexibility of AppBlock + the simplicity of Freedom Session. Core changes: **Template first**.

#### Function details

**A. Default templates (out of the box)**

| template | Applicable scenarios | Default rules |
|------|----------|----------|
| 🎓 Learning mode | Preparing for exams/self-study/taking classes | Block all entertainment + social networking, keep learning tools + calls |
| 💼 Working mode | Office/Conference/Remote | Block social + short videos and retain communication + tools |
| 🌙 Bedtime mode | 22:00-08:00 | Block all high-stimulation apps and keep alarm clock and phone calls |
| 🔥 Customize | arbitrary | User free configuration |

**B. Rule Type**

| rule | describe | granularity |
|------|------|------|
| Daily time limit | Total daily available time for each App/Group | 5 minutes ~ unlimited |
| Unlock limit | Maximum number of times that can be opened per hour/day | 1-99 times |
| Period interception | Complete blocking within a specified time period | Accurate to the minute |
| Period rules | Cycle by days of the week | day ~ week |
| Strict Mode | Cancellation is not possible during the cooling-off period | Available in 10-60 minutes |

**C. Whitelist**: Apps that are always allowed (phone/emergency number/alarm clock, etc.), available in any mode.

**D. AI Rule Suggestions (P1)**

AI automatically generates rule optimization suggestions based on user behavior data, and users can adopt them with one click:

| AI scene | Suggested examples | Trigger condition |
|---------|---------|----------|
| time slot vulnerability | "You frequently lose control between 13:00 and 14:30. It is recommended to increase the work mode coverage." | Loss of control during this period ≥ 3 times for 3 consecutive days |
| Rules are too loose | "Your daily limit of 60 minutes on Douyin is almost used up every day. It is recommended to reduce it to 45 minutes." | Limit usage ≥ 90% for 5 consecutive days |
| Rules are too tight | "You try to unlock in Strict Mode for 3 consecutive days, it is recommended to add 5 minutes of flexibility" | Unusually high frequency of unlock attempts |
| Dependency migration | "Douyin has decreased, but Xiaohongshu has become more quiet - do you want to join the monitoring?" | The duration of new apps continues to grow |

#### Acceptance criteria

**Templates and Rules**
- [ ] One-click activation of template: click → Preview → Confirm, the whole process is ≤ 3 steps, ≤ 30 seconds
- [ ] Custom rule creation process ≤ 5 steps, including time period selector and app selector
- [ ] Rule effective time error ≤ 1 minute (system level accuracy)
- [ ] Rule changes take effect ≤ 2 seconds (local cache is updated immediately)

**Rule Logic**
- [ ] Whitelisted apps can be opened normally under any rules without triggering a pause page
- [ ] Up to 15 parallel rules (Free version ≤ 3, Pro unlimited)
- [ ] The "stricter priority" policy is correctly executed when rules conflict (time period + limit double trigger to obtain the stricter one)
- [ ] During the Strict Mode cooling period, any modification/closure operations are blocked and the remaining waiting time is displayed.

**boundary**
- [ ] When the number of rules exceeds the limit of the free version, you will be prompted to upgrade instead of silently invalidating it.
- [ ] Time period rules that cross zero points (such as 23:00-01:00) are executed correctly
- [ ] After the user modifies the mobile phone system time, the rules will not be bypassed (use server-side time verification)

**AI Rules Suggestions (P1)**
- [ ] When there is sufficient data (≥ 7 days of recording), ≥ 1 rule suggestion will be automatically generated every week
- [ ] After one-click adoption, the rules will take effect within 2 seconds and a confirmation notification will be pushed.
- [ ] It is recommended to attach "revocable" guidance (can be rolled back within 7 days)

---

### F-03 Insights & Achievements

#### user stories

> **As** a user who is reducing the use of mobile phones,  
> **I WANT** TO SEE IMPROVED DATA DAILY AND WEEKLY,  
> **So that** I have the motivation to keep persisting.

#### product logic

The key: **Forward Narrative** - not "you racked up X hours again", but "you earned back X hours and made Y correct choices".

#### Function details

**A. Daily** (pushed at 21:00 every day)

| data item | exhibit |
|--------|------|
| Earn time back today | "🎉 You earned back 47 minutes today" |
| Abandoned opens | "You made the right choice 12 times" |
| The most likely time to lose control | "14:00-15:00 is the easiest time to be dragged away" |
| Total usage data | Total time spent on high-risk apps + vs yesterday’s trend |

**B. AI driven weekly report** (pushed every Monday at 09:00)

The weekly report is FOMO's AI core touch scene - not only displaying data, but also providing **behavioral insights + executable suggestions**:

| data item | describe |
|--------|------|
| 7-day trend chart | This week vs last week line chart |
| Biggest Improvement App | Apps with the largest decrease in usage time |
| Biggest Challenge App | Still the hardest app to control |
| Streak | Number of consecutive days to meet the standard |
| AI time period pattern analysis | "You are most difficult to control between 13:30-14:30 in the afternoon and 22:30-23:30 before going to bed, accounting for 68% of the total loss of control during the week." |
| AI emotion-triggered speculation | "59% of loss of control occurs when you choose 'bored', which may be an energy low" |
| AI rule effect score | "The hit rate in bedtime mode is 93%, while the working mode is only 61% - it is recommended to extend it by 30 minutes" |
| AI dependency migration detection | "Douyin ↓35min, but Xiaohongshu ↑28min, the total entertainment time has not been reduced" |
| AI executable suggestions (1-3 items) | One-click execution and directly configure corresponding rules |

**C. Mission log (optional, light reflection)**

- A 1-line "Relationship/Mission Reflection" input box is provided at the end of the daily/weekly report, where users can write "What did they do after putting down the phone/Who do they want to connect with".
- The default is optional, not included in Streak, and does not create clock-in pressure; it is only used for personal review or to generate positive prompts.
- Optionally enable the "Relationship Reminder" card: remind users of 1-2 important people they have not contacted recently (local inference, no contacts uploaded).

**D. Achievement System**

| Achievement | condition | medal |
|------|------|------|
| Guardian of original intention | Meet the target for 7 consecutive days | 🏅 |
| Dedicated practitioner | Meet the target for 14 consecutive days | 🥈 |
| Self-discipline master | Meet the target for 30 consecutive days | 🥇 |
| time millionaire | Earn 100 hours in total | 💎 |
| Choose the right home | Choose to leave a total of 1000 times | 🌟 |
| early bird | Don’t touch your phone before 7:00 for 7 days in a row | 🐦 |

**Achievement and Challenge Cards (Viral Growth Engine)**
1. **Share Card**: Beautiful data visualization ("defeated 80% of users").
2. **Help Card (Panic Button)**: "I am challenging not to use TikTok for 7 days, come and supervise me" (click to bind the supervision relationship).
3. **Provocation Card**: "I saved 45 minutes today, do you dare to compete?" (Click to initiate PK).
Supports one-click sharing to WeChat/Moments, and the link has UTM parameters to track the fission effect.

**E. Humanistic Feedback Code (applicable globally)**

- When users fail to meet the standards, the default copywriting adopts "review + next step suggestions" and does not use the "failure punishment" narrative.
- Weekly reports must give at least 1 "thing you have done well" to reduce frustration
- For users with continuous high pressure (high-frequency urges at night + lack of sleep), it is recommended to give priority to "stress reduction goals" instead of continuing to increase the intensity of restriction.

#### Acceptance criteria

**daily**
- [ ] Daily data is consistent with actual records in the local database, accuracy ≥ 99%
- [ ] Push arrives within ±5 minutes of user-set time, arrival rate ≥ 90%
- [ ] The first screen of the daily report displays "earning time" and "number of correct selections" without scrolling.

**AI Weekly Report**
- [ ] When the valid behavioral data is ≥ 3 days, the AI ​​weekly report will be automatically generated. If the data is insufficient, the status of "data collection in progress" will be displayed.
- [ ] AI weekly report generation time ≤ 15 seconds; display loading animation when timeout to avoid white screen
- [ ] Each AI insight contains a three-part structure of finding + why + action, and no empty fields will appear.
- [ ] One-click execution of suggestions. Complete the rule configuration within 2 seconds after clicking and return to the confirmation page.

**Achievements and Sharing**
- [ ] Achievement unlock animation frame rate ≥ 60fps, duration 1.5-2s
- [ ] Streak is reset to 0 after breaking and displays the "Come on, start over" prompt (non-punishment prompt)
- [ ] Sharing card generation time ≤ 3 seconds, image resolution adapted to WeChat Moments (≥ 1080px wide)
- [ ] Sharing link includes App download jump and UTM parameters for source attribution

**Humanistic Quality**
- [ ] The built-in copywriting library passed the "non-negative humiliation" review (psychological consultant participated in the acceptance)
- [ ] "Stress is too high" user feedback rate ≤ 5% (monthly user survey)

---

### F-04 Anti-Bypass protection (Anti-Bypass)

#### user stories

> **As** a user who often impulsively turns off restrictions,  
> **I wish** there was a cooling off period to stop me from impulsively changing the rules,  
> **So that** my rules will still be in effect after the urge subsides.

#### Function details

| sub function | describe | Configuration |
|--------|------|------|
| Modify cool down period | Wait N minutes before modifying/closing rules | 5/10/15/30 minutes |
| Password protection | Key settings require password | 4-8 people |
| Abnormal behavior tips | A pop-up window appears when the third modification is made within 1 hour. | "You may be impulsive🌬️" |
| Uninstall Protection(Android) | Prompt "You have persisted for X days" before uninstalling | Device manager permissions |
| Suspension safety valve | Allow "Pause 1 day" option | Off by default |
| emergency pass | 1-2 emergency unlocking opportunities per month, you need to pay a "penalty" (such as ￥3) or a 60s long countdown | Alleviating deadlock panic |

#### Acceptance criteria

- [ ] The cooling period timing is accurate and the UI is clear
- [ ] Password verification ≤ 500ms
- [ ] Anomaly detection is purely local and has no network dependencies.
- [ ] "Pause for 1 day" Automatically resume the next day

**Punishment-free exit design principle (compared to FOMO Reset safe exit mechanism)**
> Different from Forest's punitive design of "failure upon exit/withering of trees", FOMO follows the following principles:
> - **Temporary break**: During the cooling period, users can apply for "today's break" (up to 2 times per month) without triggering Strict Mode downgrade.
> - **Partial completion record**: Strict mode exits midway, records "has persisted for X hours" instead of recording failure, and does not clear the data
> - **No negative language**: Use neutral descriptions for all "not up to standard" tips ("I had a day off today"), and prohibit "failed again" type copywriting
> - **Streak Protection**: After the Streak is broken, it will display "the longest continuous history" and "the number of compliance days in the past 7 days" instead of simply clearing it.

---

### F-05 Onboarding

#### user stories

> **As** a first-time FOMO user,  
> **I WANT** to be set up and started using it in 2 minutes.

#### process design

| step | Page content | User action |
|------|----------|----------|
| Step 1 | "What do you most want to improve?" | Choose a goal |
| Step 2 | AI analyzes installed apps, intelligently assesses risk levels and recommends monitoring lists | Confirm or modify |
| Step 3 | AI recommends the best template based on the target + App combination and previews the effect | Enable or adjust with one click |
| Step 4 | Permission guidance (step by step + explanation of reasons) | Gradual authorization |
| Step 5 | AI-generated personalized first-day goal: "Based on your app, it is recommended to reduce the number of times you open Douyin 3 times💪" | Get started |

#### Acceptance criteria

- [ ] Main process ≤ 5 steps, ≤ 120 seconds
- [ ] Permission guidance pass rate ≥ 70%
- [ ] Boot completion rate ≥ 80%

---

### F-06 AI behavioral coach (P1, Phase 2)

#### user stories

> **As** a user of FOMO for two weeks,  
> **I WANT** to receive insightful, personalized behavioral analytics, not just "you spent X number of hours,"  
> **So that** I can truly understand my out-of-control patterns and know exactly how to change them.

#### product logic

The core of AI coaching is to automate the link from **behavioral data → behavioral insights → executable suggestions**. It's not a "big model chat", but an analysis pipeline with structural input and standard output.

#### Function details

**A. Daily reach (light)**

| scene | Reach method | AI content examples |
|------|----------|------------|
| After the out-of-control peak of the day | push notification | "Today at 3 o'clock in the afternoon, you opened Douyin five times in a row, adding a 15-second delay?" [One-click activation] |
| Complete Streak | In-app pop-ups | "Seven days in a row! You spent 2.3 hours less browsing your phone this week, which is equivalent to reading half an extra book." |
| Dependency migration detected | In-app reminder | "Douyin has decreased, but Bilibili has quietly increased by 20 minutes - changing dependencies is not a change" |

**B. Weekly in-depth reporting**

| Analysis Dimensions | describe | AI output example |
|----------|------|------------|
| period pattern | Identify the time windows most vulnerable to loss of control | "You are most difficult to control between 13:30-14:30 in the afternoon and 22:30-23:30 before going to bed, accounting for 68% of the times of loss of control throughout the week." |
| Emotional trigger speculation | Select data combined with intent to infer mental states | "59% of the loss of control occurs when you choose 'bored', which may correspond to low energy or the need for stress relief" |
| Rule effectiveness score | Evaluate the actual blocking effectiveness of existing rules | "Your bedtime mode hits 93%, but work mode only 61% - recommend extending by 30 minutes" |
| Dependency migration detection | Recognition transfer from one app to another | "Douyin ↓35min, but Xiaohongshu ↑28min, the total entertainment time has not been reduced" |
| Actionable recommendations | Give 1-3 specific actions based on data | "It is recommended to start a 15-minute focus block between 13:00 and 14:30. There are 5 preventable times this week." |

It is recommended to **one-click execution** (click to directly configure the corresponding rules without manual settings).

**C. AI Dialogue (P2)**
- Users can ask the coach: "Why can't I control myself before going to bed?"
- AI combines the user's historical data to answer, rather than a general answer

#### AI capability evolution route

```
Phase 2 early stage (M4-5) Phase 2 late stage (M5-6) Phase 3 (M7+)
      |                        |                       |
AI behavioral coach V1 AI real-time intervention AI conversation coach
- Weekly in-depth report - real-time push of the day's out-of-control - users can ask questions
- Dependency migration detection - automatic rule suggestion - context memory
- One-click execution of suggestions - Emotional state inference - Long-term habit planning
```

#### privacy principles

| in principle | illustrate |
|------|------|
| local priority | Behavioral data is stored locally, and only desensitized aggregate summaries are uploaded. |
| minimum collection | Only metadata (time + App name + user selection) is recorded, without content |
| User controllable | Data export/delete one-click operation |
| Downgrade | Automatically switches to the rules engine to generate basic insights when AI is unavailable |
| Caring first | AI does not output humiliation, threats, or moral judgment suggestions, and gives priority to "executable and low-pressure" next steps. |

#### Acceptance criteria

- [ ] AI weekly report generation time ≤ 10 seconds
- [ ] Weekly report generation success rate ≥ 98%
- [ ] User Satisfaction Rating ("This suggestion helped me") ≥ 4/5
- [ ] One-click execution of suggestions into actual rule configuration ≥ 40%
- [ ] AI facilitates the loss of control rate in the next week by ≥ 15% after the rule change (A/B comparison)
- [ ] LLM API monthly average cost/paying user ≤ ￥2
- [ ] The downgrade scheme can automatically switch when LLM is unavailable, and the user will not be aware of it.
- [ ] Do not upload any personally identifiable raw data (privacy audit passed)
- [ ] Privacy Complaint Rate = 0

---

### F-07 Partner Supervision (P1, Phase 2)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-07-1 | Users who have difficulty with self-discipline | Invite friends to do the 7-day challenge together | Use social pressure to increase persistence motivation |
| US-07-2 | Partners who accepted the invitation | See if the other party meets the standard today | Encourage the other person when he fails |
| US-07-3 | Privacy-conscious users | Only let partners see my achievement status, not the specific app I use | Build trust without losing privacy |

#### product logic

**Core Design Principle**: Partner supervision is not "monitoring", but "growing together" - privacy is prioritized by default, positive incentives are the main focus, and humiliating reminders are prohibited.

```
User A initiates an invitation (link/QR code)
    │
    ▼
User B accepts, and both parties confirm mutual viewing permissions
(Default: Compliance status only | Upgradeable: duration overview)
    │
    ├── Every day at 21:00, both parties receive the other party's "Today's Card"
    │
    ├── The other party fails → Push reminder → Send "Come on" or "Provocation" (default expression + 20 character limit)
    │
    └── Complete the 7-day challenge → Unlock "Partner Achievements" → Generate two-person sharing cards
```

#### Sub-function details

| sub function | describe | Restrictions and Notes |
|--------|------|------------|
| Invite partners | Share link/QR code and invite friends to bind | The free version can bind up to 1 person; the Pro version can bind up to 3 people |
| Look at each other's status | Overview of daily target attainment (✓/✗), consecutive days, and usage time | Does not expose specific App names, only aggregates data |
| Failure reminder | Push when the other party fails to meet the standard, and can reply with encouragement/provocation | Triggered at most once per day; taunting presets are prohibited |
| 7 day challenge | Common goal + deadline, both parties reach the target to unlock joint achievements | The challenge goal is determined through negotiation between both parties and cannot be modified unilaterally. |
| AI Dual Insight | AI compares data from both parties and generates a "Common Challenges/Complementary Advantages" report | Both parties need ≥7 days of data to generate |
| AI challenge recommendations | AI recommends challenge targets with the most appropriate difficulty based on both sides’ modes | Recommendations are accompanied by explanations of reasons. Users can refuse and make their own choices. |
| privacy control | You can turn off mutual viewing permissions at any time, and the other party will not receive notifications. | Permissions changes take effect within 2 seconds |

#### Acceptance criteria

**Functional Correctness**
- [ ] The invitation link can jump correctly and complete the binding on iOS/Android
- [ ] After binding, the mutual viewing permission defaults to "Only Compliance Status" and needs to be manually upgraded to "Duration Overview"
- [ ] Both parties will receive the other party’s today’s card push within 21:00 ±5 minutes every day.
- [ ] The 7-day challenge automatically unlocks achievements and generates shareable cards after both parties reach the target.

**Boundaries and Privacy**
- [ ] After canceling the binding, the other party can no longer view the data, and there is no notification reminder.
- [ ] Do not reveal the user’s specific App name or usage details under any circumstances
- [ ] After the user deletes the account, the partner data association is automatically terminated.

**AI Enhancement (P1)**
- [ ] AI two-person insight is only triggered when the data of both parties is ≥7 days, and "data collection" will be displayed if it is insufficient.
- [ ] AI challenge recommendations with reasons and rejection options

---

### F-08~F-13 (P1/P2 function detailed specifications)

> The following functions are all Phase 2 (Week 13–24) delivery scope, and the Priority is marked P1 (Phase 2 core) or P2 (Phase 3 candidate).

---

### F-08 Browser Extension (P1, Phase 2)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-08-1 | Users who work on computers during the day | The browser can also block high-risk websites I set up on my phone | Achieve consistent self-discipline experience across terminals |
| US-08-2 | Paid Pro users | Install extensions on Chrome/Edge and automatically sync rules | Protect desktop time without reconfiguration |
| US-08-3 | Users who have the bad habit of "quit using mobile phone and use computer to refresh" | AI recognized me and moved my mobile phone dependencies to my computer | The system helped me realize behavioral shifts |

#### Function details

| sub function | describe | Restrictions and Notes |
|--------|------|------------|
| Rule synchronization | Synchronize high-risk website blacklist + time period rules with mobile phone | Login required, Pro exclusive features |
| Pause page (web version) | The interception page displays the website category + the number of visits to the website today | Countdown for 5 seconds, you can choose to leave or continue |
| record of intent | Record the intention of this visit and import it into AI behavior analysis | Merge with mobile intent data |
| AI cross-end insights | AI detects the dependency migration of "the mobile phone is controlled → the computer still flashes" | Requires mobile + desktop dual-end data ≥ 3 days |
| Quick pause | Temporary suspension rules 15/30/60 minutes (requires cooling-off period confirmation) | Frequent pauses will trigger AI warnings |

#### Acceptance criteria

**Functional Correctness**
- [ ] Chrome/Edge extension can be installed and completed account binding with one click
- [ ] After modifying the blacklist on the mobile phone, it will take effect simultaneously on the desktop within 30 seconds.
- [ ] Interception page loading time ≤500ms, does not block normal web pages
- [ ] The pause function synchronizes the pause status on both the desktop and mobile terminals

**AI Enhancement (P1)**
- [ ] AI cross-end insights are automatically triggered after dual-end data ≥ 3 days, and the report accurately points out the migration behavior
- [ ] AI Migration Insights shows the original text and suggestions, without a judgmental tone

---

### F-09 Family Empathy Model (P1, Phase 2–3)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-09-1 | Parents worried about their children’s cell phone addiction | Understand the trends in your kids’ digital habits | Communicate with evidence instead of guessing and blaming |
| US-09-2 | Teenage users | Parents see trends rather than detailed daily records | Maintain a certain amount of privacy without feeling monitored |
| US-09-3 | family members | Set shared "no screen time" goals | Reduce cell phone time as a family |

#### product logic

**Core Design Principle**: Family Empathy Mode is not a parental monitoring tool, but a family digital health negotiation platform - data-driven communication that replaces unilateral control.

Sub-account permission structure:
- Parent account: See the aggregate trend chart of family members (weekly/monthly dimension, do not see daily details)
- Youth account: Set goals independently and choose whether to turn on "Trend Sharing"; parents can be requested to unlock it for a specific period of time

#### Function details

| sub function | describe | Restrictions and Notes |
|--------|------|------------|
| family bonding | The parent sends the invitation link and the child's account accepts it (two-way consent) | Both parties must confirm before binding |
| Trend panel | Parents check their children’s weekly average screen trend changes (increase/decrease/stable) | Does not display specific app names and does not display daily details |
| common goal | Family members agree to set a "shared screen-free period" (such as after dinner) | Goals need to be confirmed by all family members |
| emotion markers | Children can actively mark "Today is stressful" to trigger AI family suggestions | It is initiated by children and parents cannot force them to view it. |
| AI communication advice | AI generates non-accusatory communication suggestions based on trends | It is recommended that when sending this to parents, use empathetic rather than controlling language. |
| Request to unlock | Children can request parents to temporarily unlock an app (please fill in the reason) | Parent App can approve/deny after receiving notification |

#### Acceptance criteria

**Functional Correctness**
- [ ] Family binding requires both parties to confirm in the app, both are indispensable.
- [ ] The trend panel only displays the weekly/monthly dimension and does not display single-day details or specific apps.
- [ ] After the child deletes the emotion mark, it will disappear within 24 hours on the parent side.
- [ ] The request to unlock is pushed to the parent side, and it will take effect on the child side within 5 seconds after the parent operation.

**Privacy and Humanities**
- [ ] Any interface does not display data that increases the sense of judgment such as "How many hours did Ta use X App today?"
- [ ] AI communication suggestions have been reviewed by human-centered consultants and have no critical/contrastive/shaming language
- [ ] Teenagers can exit Family Empathy at any time, and parents will not receive specific reasons.

---

### F-10 In-App Feature Interception (P2, Phase 3)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-10-1 | Users who need to communicate using WeChat but find it easy to browse Moments | Only block Moments/video accounts, not the entire WeChat | Maintain normal social interactions while reducing unconscious screen browsing |
| US-10-2 | Users who use Douyin to listen to songs but are prone to brushing up on recommended streams | Only block recommended pages and keep searches and favorites | Precisely control unconscious behavior |

#### Function details

| sub function | describe | limit |
|--------|------|------|
| Precise interception configuration | You can choose to intercept sub-functions such as "recommended stream/short video/moments/topic square" | Relying on Accessibility Service, iOS is more restricted by the system |
| AI behavior recognition | AI detects whether the user is "normally using" or "unintentionally sliding recommendation flow" | Full functionality for Android only; downgraded to full-page blocking for iOS |
| Blocking performance report | Display the number of interceptions and time saved by each sub-function | Data is stored locally |

#### Acceptance criteria

- [ ] Android can independently intercept WeChat Moments, Douyin recommendation stream, and Weibo topic square (one of the three)
- [ ] iOS downgrade solution: display "intent confirmation when entering X App" instead of sub-function interception, users know the difference
- [ ] AI behavior recognition misjudgment rate (identifying normal use as unconscious brushing) <15%

---

### F-11 Minimalist Mode (P2, Phase 3)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-11-1 | Users who are prone to worry and check their mobile phones late at night | Late at night, the phone automatically changes to grayscale + text mode | Reduce visual stimulation and reduce dependence on mobile phones before going to bed |
| US-11-2 | Highly focused users during work hours | Turn on minimalist mode to make your phone "boring" | Actively reduce the attractiveness of mobile phones |

#### Function details

| sub function | describe | limit |
|--------|------|------|
| grayscale mode | System-level grayscale filter, effective globally | Accessibility permission required; color-blind users need to provide exemption options |
| Time period automatically triggered | Automatically turn on/off minimalist mode according to rules (such as 22:00–7:00) | A stricter strategy will be adopted when it is used in the same period as other rules. |
| AI dynamic trigger | When AI detects a high probability of loss of control, it automatically recommends turning on minimalist mode | Only recommended and will take effect after user confirmation; not mandatory |
| Plain text mode | Hide App icon color and badge, only show name | Only takes effect when minimalist mode is activated |

#### Acceptance criteria

- [ ] Grayscale mode can be turned on with one click on Android 8.0+ / iOS 13+, with a delay of ≤1 second
- [ ] AI dynamic triggering is recommended up to 2 times a day to avoid the "crying wolf" effect
- [ ] Color blindness accessibility options: Allow specified apps to be exempted from grayscale mode
- [ ] Grayscale exempt App list persistent storage (exemption rules will not be lost after app restart/device restart)
- [ ] The activation/deactivation status of minimalist mode is synchronized to the rule center. Users can see the current minimalist mode status on the rules page.

---

### F-12 Emotion Sensing Engine (P1, Phase 2)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-12-1 | Users who have failed for 3 days in a row | AI recognizes that I am in a "high-pressure state" and reduces the intensity of intervention | Get support when you are most vulnerable rather than more stress |
| US-12-2 | Users who unconsciously check their phones when they are anxious | The phone recognized my high-pressure period | Remind me gently when I need it most |

#### product logic

Emotion sensing does not rely on biosensors but is inferred from multidimensional behavioral signals (0 additional permissions required):

| Signal category | Specific indicators | weight |
|---------|---------|------|
| period signal | Use late at night (23:00–2:00) | ×2 |
| failure sequence | Failure to meet the standard for N≥2 consecutive days→yellow light; N≥4→red light | ×1.5 |
| intention drift | "Study"→"Relaxation/Boring" intention switching frequency increases | ×1 |
| intercept acceleration | The number of interceptions in a single day exceeds the historical average × 2 times | ×1.5 |
| **Touch Frequency** (New) | The frequency of swiping/clicking per unit time increases sharply (suggesting anxious screen swiping) | ×1 |
| **Ambient Light** (new) | Increased usage time in low-light environments at night (associated with bedtime refresh mode) | ×0.5 |

> Touch frequency and ambient light are collected through device sensors, all calculated locally, and zero data uploaded.

Based on the above signals, the weighted calculation outputs the emotional stress level: low pressure (green) / medium pressure (yellow) / high pressure (red).

#### Function details

| mood level | Trigger condition | intervention action |
|--------|----------|----------|
| Low voltage (green) | No above signal | Normal rules run |
| Medium pressure (yellow) | 1–2 signal triggers | AI sends caring push notifications; it is recommended to check this week’s emotional trends |
| High voltage (red) | 3+ signal triggers | Trigger moments of mindfulness (F-13); reduce the severity of the interception cooling period; add emotional care copy to daily reports |

#### Acceptance criteria

- [ ] Calculation of emotion levels is completed locally and original behavioral events are not uploaded.
- [ ] High-voltage window recognition accuracy rate (users commented that "the condition was indeed poor at the time") ≥70% (n≥30)
- [ ] The tone of intervention under the red light condition has been reviewed by a psychological consultant and has no judgment words.
- [ ] Users can manually turn off the emotion sensing function, and the level will default to green after turning it off.

---

### F-13 Mindful Moments (P1, Phase 2)

#### user stories

| ID | as... | I hope... | so that... |
|----|---------|-----------|---------|
| US-13-1 | Users who scroll through their phones when anxious | The pause page appears with 30 seconds of breathing guidance. | Insert a period of calm in the impulsive link |
| US-13-2 | Users interested in mindfulness meditation | You can actively initiate 1 mindfulness practice per day | Build mindfulness habits step by step |

#### Function details

| sub function | describe | limit |
|--------|------|------|
| impulse link insertion | Under high pressure, a "30-second breathing exercise" entry is added to the pause page. | Displayed first, users can skip |
| Active practice entrance | Home page shortcut button, supports 30/60/90 second mode | Do not remind more than 1 time per day |
| Exercise type | Abdominal breathing (4-7-8 rhythm), landing awareness (5-sense scanning), intention restatement (3 words to describe the present moment) | Introductory text for first use |
| AI recommendation | Recommended types of shortest and most effective exercises based on mood level (F-12) | Abdominal breathing is recommended by default at high pressure red lights |
| Complete tracking | Record the number of mindfulness completions; trigger "Calm Achievement" for 7 consecutive days | No compulsory statistics, focus on habits rather than clocking in |

#### Acceptance criteria

- [ ] There are no ads in the whole process of mindfulness practice, and there is no "you have been checking in for X days in a row" to put pressure on you.
- [ ] Abdominal breathing animation runs smoothly (≥30fps) on low-end devices (2GB RAM)
- [ ] If the user exits in the middle of the exercise, the failure will not be recorded, only "Started" will be recorded.
- [ ] 1 sentence reason for the type of exercise recommended by AI (no more than 20 words)

---

## 4. Milestones

### 4.1 Overall roadmap (12 months)

```
Month   1     2     3     4     5     6     7     8     9    10    11    12
       |==Phase 0==|======Phase 1======|=========Phase 2=========|==Phase 3==|
        Validation period MVP development & grayscale enhancement & growth scaling
        W1-4         W5-12               W13-24                    W25-52
```

**Milestone Flags**

| M# | time | milestone | core judgment indicators | Disposal for non-compliance |
|----|------|--------|-------------|------------|
| M0 | W4 | Phase 0 Gate: Verification passed | ≥70% of users agree that interruption is valuable; LLM API costs are controllable | Pivot or Stop |
| M1 | W12 | MVP Release & Grayscale 500 People | D7 retention ≥ 30%; NPS ≥ 30; crash rate < 0.5% | Rework no more than 1 Sprint |
| M2 | W20 | Paid online & first batch of income | Pro conversion ≥3%; MRR≥¥5,000; AI satisfaction ≥4/5 | Delay price adjustment experiment for 2 weeks |
| M3 | W24 | Phase 2 Gate: Growth Validation | MAU≥5,000; D30 retention ≥20%; CAC≤¥15 | Focus on retention funnel repair |
| M4 | W40 | Phase 3 mid-term inspection | MAU≥25,000；MRR≥¥45,000；LTV/CAC≥3 | Adjust the pace of financing |
| M5 | W52 | Year-end goals | MAU≥50,000；MRR≥¥80,000；NPS≥40 | Financing/Business Strategy Review |

### 4.2 Details of each stage

#### Phase 0: Validation period (weeks 1-4)

**Goal**: Verify core assumptions before zero code investment and reduce MVP development risks.

**4.2.1 Critical Assumption Checklist**

Assume 5 structural assumptions on which success depends and how to verify them. If allowed to fail, strategic adjustments should be triggered rather than continued investment:

| serial number | hypothesis | Why is it important | Verification method | target value | Back-up plan in case of failure |
|:---:|:---|:---|:---|:---|:---|
| A1 | "Light interruption (pause page) retains users better than strong blocking" | If it fails, product differentiation will be completely lost. | User interview interruption acceptance score | ≥70% | Change to "User chooses whether to use interrupts" |
| A2 | "AI personalized suggestions contribute significantly to retention (>15pp)" | AI is a profit center. If the contribution is small, the business model will be broken. | Phase 2 A/B: D30 retention comparison with AI vs without AI | >15pp | Downgrade to rule engine + static copywriting |
| A3 | "Users are willing to pay for 'AI coach' (Pro conversion ≥ 3%)" | If the conversion is <2%, LTV cannot support CAC | Grayscale’s paid conversion rate of 500 people | ≥3% | Expanded free functions and reduced price to ¥15/month |
| A4 | "The virus coefficient K-factor supervised by partners is ≥0.25" | If K<0.15, we cannot rely on natural growth. | Phase 2 invitation link click-through rate and conversion funnel | ≥0.25 | Turn to content marketing instead of social fission |
| A5 | "Local behavioral data can achieve AI accuracy >60% (user perception)" | If the accuracy is <50%, AI suggestions will be ignored | Weekly report satisfaction score ≥4/5 (Phase 2) | User perception ≥4/5 | Integrate third-party LLM or hybrid models to improve accuracy |

**Verification trigger mechanism**: If any hypothesis fails at the scheduled verification time point, the PM + CEO will need to decide "continue, adjust or pivot" within 3 days, and "continue investing in the hope of improvement" is not allowed.

---

**4.2.2 Phase 0 Execution Toolkit (Validation Toolkit)**

The following is a ready-to-use interview script and test protocol to ensure standardization of Phase 0 data collection and reproducible results.

**Tool 0.1: User Interview Outline (Semi-structured, 25-30 minutes)**

**Opening (2 minutes)**
- "We are developing an app to help people make conscious choices about their mobile phones. Are you interested in this topic?"

**Pain Point Digging (8 minutes)**
- "What is the most troublesome mobile phone use problem for you? When are you most likely to lose control?"
- "What methods are you currently using to manage your time? Is it effective? Why?"
- "What's the most convenient solution (App/Rule/Reminder) you've tried? How does it work?"

**Interruption Acceptance Core Questionnaire (7 minutes)** [Testing Hypothesis A1]
- Show prototype screenshot (pause page): "Will you accept this design? Will it annoy you?"
- "Rather than directly blocking the entire app, would you prefer: pause for 5 seconds + confirm the intention? Or block it directly?"
- **5-level Likert scale**: Very unacceptable (1) → Acceptance score (5); the same questionnaire collects "feeling of being respected" and "not respected at all" (1) - (5)

**AI Honesty Verification (5 minutes)** [Verification hypothesis A2 preliminary]
- "If an app told you every week, 'You're most likely to lose control at 3 p.m.,' would that advice be useful to you?"
- "Are you willing to pay for this feature? How much is a good deal? ¥10/¥28/¥50?"
- "How much price difference do you think this suggestion is worth compared to a free app with 'no AI'?"

**Competitive product comparison (3 minutes)** [Supplementary positioning verification]
- "Do you know Opal / Forest / one sec? What do you think of this solution?"
- "What's the biggest regret about the current product?"

**End (3 minutes)**
- "If there was a free version for you to try, would you download it? Would you invite your friends?"
- "Are you willing to be our seed user and participate in a 2-week small-scale test?"
- Invite to the seed user Slack group

**Verification Target**:
- ≥70% of interviewees’ discontinuation acceptance score ≥4 (meets A1)
- ≥60% are willing to pay for AI personalized suggestions (preliminary verification A2)
- At least 5-8 different "pain points", aggregated to form Top 5 (product confirmation)

---

**Tool 0.2: Usability Testing Script (8-10 people, 30 minutes each)**

Use high-fidelity prototypes (Figma) or paper prototypes. Each person completes the following 3 tasks:

**Task 1: Quick Setup (allow 3 minutes)| SUS Task Item**
- Scenario setting: "You want to intercept Douyin, start configuring it now. Complete it as quickly as possible."
- User operation: Observe the user’s complete path from opening the App → Selecting a target → Setting rules → Enable
- Verification indicators:
  - ✓ Completion rate ≥80% within 3 minutes [Key passing conditions]
  - ✓ Number of user clicks ≤ 5 (the fewer, the better)
  - ✓ Can you tell "what I did" after completion (task understanding)

**Task 2: Understand the meaning of break pages (1 minute)**
- A screenshot of the pause page pops up and asks, "What is this interface asking you? Why does it appear? Why is it designed like this?"
- Verification indicators:
  - ✓ 100% able to clearly state "confirmation of intent" [must pass]
  - ✓ Whether there is a "feeling of being judged" or "irritability" [Key]
  - ✓ Considered reasonable score 1-5: target ≥4

**Task 3: Examine Emotional Language (5 minutes)**
- Read the daily copy (about 200 words) and ask sentence by sentence, "How does this sentence make you feel?"
  - "You earned back 45 minutes today" vs "You wasted 2 hours"
  - "You did a great job this week - reduced your screen time by 10%" vs "You still timed out"
- Verification indicators:
  - ✓ Feeling of respect score: 5-item Likert scale average ≥4/5 [P0 passing condition]
  - ✓ Number of occurrences of negative words: Target 0
  - ✓ "Stress" score ≤2/5 [prevent R10]

**Overall SUS Scale: Standard 10 questions**
```
1. I think I will use this app often
2. This app is unnecessarily complicated
3. I think this app is easy to use
4. I need technical support to use this app
5. The parts of this app fit together well
6. The app has many inconsistencies
7. Most people will learn to use this app easily
8. I find this app difficult to use
9. I feel confident using this app
10. I need to learn a lot before using this app
```
- Each question is worth 1-5 points. Calculate the total SUS score = (Σ(odd-numbered questions-1) + (5-Σ(even-numbered questions))) / 2.5
- Target SUS≥68 (passing line); >80 is excellent

**Phase 0 Exit Criteria** (must be met for usability testing):
- [ ] Task 1 completion rate ≥80%, average number of clicks ≤5
- [ ] Task 2 100% understanding of intent and no "feeling of being judged"
- [ ] Task 3: Sense of respect ≥ 4/5, Sense of pressure ≤ 2/5
- [ ] Overall SUS≥68
- [ ] If not satisfied, the design must be iterated and retested (up to 2 rounds)

---

| Deliverables | person in charge | Definition of Done (DoD) | time | Risks and plans |
|--------|--------|-----------------|------|------------|
| User interview report (25-30 people) | PM | Top 5 pain points; "disruption acceptance" ≥70%; stratified analysis by age/occupation | W1-2 | Recruitment is slow→KOL assists in recruitment |
| Competitive product usage experience report | PM+Design | Covers the top 5 competing product registration→daily→payment processes, including screenshots | W1-2 | — |
| High-fidelity prototype (Figma) | designer | F-01~F-05 The whole process is clickable; the pause page animation has a native feel | W2-3 | Expired→cut to F-01/F-02 core |
| Usability testing (8-10 people) | PM+Design | SUS≥68; task completion rate ≥85%; key tasks (setting rules) ≤3min | W3-4 | — |
| Humanistic Experience Assessment | PM+psychological consultant | "Feeling of being respected" ≥4/5; negative emotion triggering rate <10%; no judgment words; use a 5-item Likert scale (respect/comfort/pressure/trust/willingness to recommend) | W3-4 | Consultant schedule → Make an appointment 2 weeks in advance |
| Technical feasibility assessment | Tech Lead | Screen Time API/Accessibility Service boundary; LLM API response <3s | W2-3 | iOS Limitations→Prepare MDM Scenario |
| **Phase Gate Review** | All members | Written output Go / Conditional Go / Stop decision | W4 | — |

**Phase Gate Decision Matrix**

| Assessment Dimensions | Go (full speed ahead) | Conditional Go (conditional pass) | Stop / Pivot |
|----------|---------------|------------------------------|--------------|
| User value recognition | ≥70% agree that "interruptions are valuable" | 60–69%, trigger logic needs to be adjusted | <60% |
| technical feasibility | No blocking points | 1 solvable high-risk point | ≥2 unresolvable blocks |
| Competitive product threat | No direct Chinese counterpart | There is 1 company but the differentiation is clear | Major manufacturers announce direct benchmarking products |
| AI cost | ≤10% estimated ARR | 10–20%, with downgrade options | >20% and no downgrade plan |

#### Phase 1: MVP Development (Weeks 5-12)

**Goal**: Deliver high-quality MVP, complete double-end shelving and grayscale verification, and establish a data baseline.

| Sprint | core delivery | person in charge | Definition of Done (DoD) | time | critical dependencies |
|--------|----------|--------|-----------------|------|----------|
| S1 | App framework + interrupt interception | iOS+Android | Interception rate ≥99%; pause page pop-up ≤300ms; mainstream models have no crashes | W5-6 | Phase 0 Technology Assessment |
| S2 | Rules engine + 3 templates | iOS+Android+backend | Conflict "stricter priority" logic passes; template one-click activation ≤ 3 steps | W7-8 | S1 framework is stable |
| S3 | Daily + Weekly + Streak + Achievements | full stack | Data accuracy ≥99%; Streak crossing zero points is correct; 6 medal animations ≥60fps | W9-10 | Ready to bury |
| S4 | Anti-bypass + boot + grayscale package | iOS+Android+PM | Cooling period modifications are blocked; 5-step boot completion rate ≥70%; double-ended grayscale package available | W11-12 | Full process joint debugging |

**MVP Phase Gate (W12) Acceptance Metrics**

| index | threshold | Collection method |
|------|------|----------|
| D7 retention rate | ≥30% | Mixpanel |
| NPS | ≥30 | In-app 1-question questionnaire |
| crash rate | <0.5% | Sentry |
| Pause page "correct selection" rate | ≥40% | Self-built burial point |
| "Sense of respect" rating | ≥4/5 | Grayscale user research (n≥50) |
| Number of P0 Bugs | 0 | QA acceptance report |

> **P0 Bug Definition**: Causes data loss/complete interception failure/crash rate >2%/paid functions cannot be used.

#### Phase 2: Enhancements and Growth (Weeks 13-24)

**Goal**: AI function online, paid verification, MAU increased to 5,000.

| Sprint | Weekly | theme | key deliverables | Phase OKR Alignment |
|--------|------|------|----------|----------------|
| S5 | W13-14 | Grayscale review + experience optimization | Retention funnel analysis report; Top 3 pain point repairs are online | D30 retention↑ |
| S6 | W15-16 | AI Weekly Coach V1 | LLM behavioral analysis pipeline; structured 3-part weekly report; one-click execution | AI satisfaction ≥4/5 |
| S7 | W17-18 | Emotion sensing engine + mindful moments | High-voltage window recognition ≥70%; continue to brush after mindfulness is triggered ↓15% | Improved pressure feedback |
| S8 | W19-20 | Paywall + Subscription Process | IAP access; pricing A/B (¥28 vs ¥35); conversion funnel verification | Conversion ≥ 3%; MRR ≥ ¥5K |
| S9 | W21-22 | Partner Supervision V1 + Home Alpha | Matching process; invitation link; family panel beta | K-factor≥0.3 |
| S10 | W23-24 | Browser Extension + Growth Experiment | Chrome launch; sharing card optimization; 7-day challenge invitation mechanism | MAU≥5,000 |

**Phase 2 Gate（W24）**

| index | threshold | Disposal for non-compliance |
|------|------|------------|
| MAU | ≥5,000 | Add investment in growth channels + fission optimization |
| D30 retention | ≥20% | Strengthen AI personalized insight retention |
| Pro conversion rate | ≥3% | Price reduction experiment / trial period extension |
| MRR | ≥¥15,000 | Additional home version promotion |
| AI Weekly Report Satisfaction | ≥4/5 | Prompt iteration + A/B testing |
| Hybrid CAC | ≤¥15 | Compress payment channels and strengthen natural volume |

#### Phase 3: Scale (Weeks 25-52)

**Goal**: Deepen the AI ​​moat, expand B2B, explore internationalization, and move towards Pre-A financing.

| field | key deliverables | person in charge | Quantitative OKRs |
|------|----------|--------|----------|
| AI real-time intervention | Out-of-control behaviors of the day are pushed in real time; rules are automatically suggested, with an adoption rate of ≥30% | Backend+PM | Paid D90 Retention ↑10% |
| AI conversation coach V1 | Natural language questions; answers combined with historical data; satisfaction ≥70% | Backend+PM | Pro ARPU↑15% |
| Device-side AI POC | Core ML/NNAPI local inference, latency ≤200ms | iOS+Android | AI single user cost↓40% |
| Family empathy model F-09 | Multi-device binding ≥90%; negative feedback on family conflicts ↓20% | full stack | Home version MRR accounts for >15% |
| B2B Discovery (School/Business) | 3 PoCs; team version MVP; batch management backend | PM+full stack | Team version single customer ACV≥¥5,000 |
| Internationalization (English + Traditional Chinese) | 100% translation coverage; multilingual ASO | PM+Localization | Overseas MAU≥5% |
| App Store Editorial | Today recommends applications; first round PR media contact | Operations+PM | Natural amount ↑20% |
| **Year-End Goals** | MAU≥50,000；MRR≥¥80,000；NPS≥40 | All members | Financing Pre-A conditions are mature |

### 4.3 Critical path and dependency graph

```
Phase 0 Gate (W4)
    │
    ▼
S1 App Framework + Interrupt (W5-6)
    │
    ▼
S2 Rules Engine (W7-8)
    │
    ├──► S3 Daily + Achievements (W9-10)
    │
    ▼
S4 anti-bypass + grayscale (W11-12)
    │
    ▼
MVP Gate (W12)
    │
    ├──► S6 AI Weekly Report Pipeline (W15-16) ──► S7 Emotion Engine (W17-18) ──► AI Dialogue Coach (Ph3)
    │
    ├──► S8 paid online (W19-20)
    │
    └──► S9 Partner Supervision (W21-22) ──► Family Empathy Ph3
                                          │
                              Device-side AI POC ──► B2B pricing is feasible
```

> **Critical Path**: S1 (iOS interception) → S2 (rule engine) → S6 (AI pipeline) → S8 (paid conversion).  
> If any critical path node is delayed by >1 Sprint, Phase Gate re-evaluation and resource reallocation need to be triggered.

---

## 5. Iteration planning

### 5.1 Sprint Rules and Rituals

| ceremony | time | participants | output |
|------|------|--------|--------|
| Sprint planning meeting | W1 Monday AM 2h | All members | Sprint Backlog + Sprint Goal (1 sentence) |
| Daily stand-up meeting | Everyday 10:00 15min | All members | Blocked item list |
| Technical design review | W1 Tuesday PM (on demand) | Engineering+PM | Program Documentation (ADR) |
| Demo / Review | W2 Friday PM 1h | All staff + external review | Demo video (archive) |
| Review meeting | 30min after Demo | All members | Keep/Try/Stop 3 action items |
| Grayscale release | W2 Friday night | project | Grayscale package online |

**Sprint Definition of Done (Team DoD)**
- [ ] All Story Functional Correctness AC passed
- [ ] None P0/P1 Bug unresolved
- [ ] Code Review All Approved
- [ ] Core path automated test coverage ≥70%
- [ ] Data buried points passed QA, Kanban indicators can be checked
- [ ] Humanistic experience: The new copy will be reviewed by consultants (if any)
- [ ] Documentation updated (Wiki/Notion), technical decisions have ADR records

**Story Priority Rules**

| priority | definition | Disposal principle |
|--------|------|----------|
| P0 | Blocking the core user journey | When the Sprint must be completed, block all other work |
| P1 | Important but there are alternatives | When Sprint strives, overdue can be Hotfixed |
| P2 | Experience optimization | Can be pushed to the next Sprint |
| Tech Debt | long term quality debt | Reserve 15-20% capacity for each Sprint (including online emergency processing) |

### 5.2 MVP Sprint Scheduling (S1–S4, W5–W12)

| Sprint | Weekly | Sprint Goal | Core Story | Key AC | rely |
|--------|------|-------------|------------|---------|------|
| **S1** | W5-6 | "Users can see the pause page when opening the target app on any device" | System API access; pause page UI; intent writing | Pop-up delay ≤300ms; supports iOS+Android mainstream models | Tech Feasibility Assessment |
| **S2** | W7-8 | "Users can enable a rule template in 3 steps" | Duration limit; period interception; 3 templates; rule conflict logic | Template activation ≤ 3 steps; conflict "strict priority" is executed correctly | S1 framework is stable |
| **S3** | W9-10 | "Users can see yesterday's behavior data and motivational feedback every day" | Daily collection + display; Streak; 6 medals unlocked | Data accuracy ≥99%; Streak is correct across zero points | Ready to bury |
| **S4** | W11-12 | "MVP can be launched to 500 people in grayscale and collect D7 retention data" | Reverse cooling-off period; 5-step guide; double-ended grayscale package | Cooling period modifications are blocked; boot completion rate ≥70% | Full process joint debugging |

### 5.3 Phase 2 Sprint（S5–S10，W13–W24）

| Sprint | Weekly | Sprint Goal | key deliverables | Success Metrics |
|--------|------|-------------|----------|----------|
| S5 | W13-14 | "Repairing Top 3 Pain Points Based on Grayscale Data" | Retention funnel analysis; problem fixes online | D14 retention recovery ≥5pp |
| S6 | W15-16 | "Users receive the first valuable AI weekly report" | LLM behavioral summary pipeline; structured weekly reporting; one-click execution | AI Weekly Report Satisfaction ≥4/5 (n≥30) |
| S7 | W17-18 | "High-pressure users receive mindfulness reminders to reduce impulsivity during high-risk windows" | Emotion sensing engine V1; mindfulness moment pop-up window | High-voltage window recognition rate ≥70%; continue to brush after mindfulness ↓15% |
| S8 | W19-20 | "Earn ≥¥5,000 MRR in the first month of payment" | IAP access; paywall; pricing A/B (¥28 vs ¥35) | Conversion rate ≥ 3%; MRR ≥ ¥5,000 |
| S9 | W21-22 | "Users can invite friends to supervise each other" | Partner matching process; invitation link; family panel beta | Matching rate ≥ 60%; K-factor ≥ 0.3 |
| S10 | W23-24 | "Sharing mechanism drives fission to reach MAU 5,000" | Share card V2; 7-day challenge invitation; Chrome extension V1 | MAU≥5,000；CAC≤¥15 |

### 5.4 Release strategy and rollback decision tree

**Grayscale Strategy**

```
New version ready
    │
    ▼
Internal QA (Staging) ──► P0 Bug? ──► Yes ──► Re-verify after repair
    │
    ▼
5% grayscale (internal beta users)
    │
    ├──► Crash rate >1% or D1 retention drop >15%? ──► Yes ──► Rollback immediately
    │
    ▼
20% gray (2 days of observation)
    │
    ├──► Same as above threshold check
    │
    ▼
50% gray (3 days of observation)
    │
    ▼
100% full release
```

**Rollback triggering conditions (rollback if any one is met)**

| condition | threshold | person in charge |
|------|------|--------|
| Crash rate surges | >1% (compared to the average of the previous 7 days) | iOS/Android Engineer |
| D1 retention plummets | MoM↓>15% | PM |
| P0 Bug survives | >4h not fixed | Tech Lead |
| Core API error rate | >5% | Backend engineer |
| IAP payment success rate | <90% | PM+Engineering |

**Feature Flag Management**

All P1/P2 functions are controlled by Feature Flag by default; Phase 2+ uses remote configuration (Firebase Remote Config / Alibaba Cloud Configuration Center) and supports grayscale grouping by user, A/B experiment grouping, and emergency shutdown.

---

## 6. Streamline resource information

| Dimensions | Thin provisioning |
|------|----------|
| core team | 6-7 people: PM 1, design 1, iOS 1, Android 1, backend/AI 1, QA 0.5, growth 0.5; psychological consultants external cooperation as needed |
| key tools | Design Figma; Project/Document Linear + Notion; Monitoring Sentry; Analysis Mixpanel; CI/CD GitHub Actions; Push Push/Firebase; Cloud Alibaba Cloud/AWS; AI call Claude/GPT (can be replaced with a local small model to reduce costs) |
| Cost Tips | AI cost control is <3% of paid user revenue; review LLM cost/effectiveness ratio every Sprint, and downgrade to rule engine or local small model if necessary |
| Production capacity principle | Parallel ≤1 P0 + 1 P1 in a single quarter; reserve 20% for each Sprint to handle online and risk control; avoid doing "platform adaptation + major functions + major commercialization changes" at the same time |

---

## 7. Business model

### 7.1 FOMO Pricing (Freemium)

| Hierarchy | price | Function | Pricing logic |
|------|------|------|----------|
| **FREE VERSION** | ¥0 | Basic interruption (≤5 App), 1 template, basic daily report, 3 rules | Experience core values |
| **Pro monthly payment** | ¥28/month | Unlimited Apps/Templates, Rigorous, Advanced Reporting, **AI Behavioral Coach**, Custom Prompts | Comparing the middle value of AppBlock $4.99 and Opal $8.29, AI is a differentiated premium |
| **Pro Annual Payment** | ¥198/year (¥16.5/month) | Same as Pro, 30% discount on annual payment | Main recommendation, LTV maximization |
| **Home Edition** | ¥48/month | Pro × 6 people + parent panel | High ARPU |
| **Team Edition** | ¥15/person/month (paid annually) | Pro + management background + reporting | Business/School |
| **lifelong** | ¥498 | Permanent Pro | Learn from Freedom $199 |

### 7.2 Unit Economics

#### key assumptions

| hypothesis | numerical value | in accordance with |
|------|------|------|
| Natural customer acquisition ratio | 60% | Share + word of mouth + ASO |
| Paid channel CAC | ¥15 | Social placement + KOL |
| Hybrid CAC | ¥6 | ¥0×60% + ¥15×40% |
| Free→Pro Conversion | 5% | Industry 3-7% |
| average monthly churn | 8% | Tools Benchmark |
| ARPU (paid) | ¥22/month | Month + year weighted |
| Average paid life cycle | 12.5 months | 1/churn rate |

#### Month 12 Estimate

| index | numerical value |
|------|------|
| Cumulative activation | 50,000 |
| MAU | ~20,000 |
| paying user | 2,500 |
| MRR | ¥55,000 |
| ARR | ¥660,000 |
| LTV (paid) | ¥275 |
| LTV/CAC | 45.8 |
| Cumulative income in the first year vs total expenses in the first year | ¥594K vs ¥3,025K |

> **Note**: ARR ¥660K is the annualized value of the 12th month’s operating rate (MRR×12), not the actual cumulative income throughout the year. The cumulative revenue in the first year is approximately ¥594K, and the total expenditure in the first year is approximately ¥3,025K (COGS + OPEX, see §10.5 Financial Forecast Table for details).  
> The first-year goal is to validate the model rather than make a profit. LTV/CAC > 3 is healthy.

### 7.2.1 In-depth analysis of business models (benchmarking international mainstream)

| Dimensions | ScreenZen (Free) | Opal (high price subscription) | Freedom (Professional Subscription) | FOMO (goal) |
|------|------------------|------------------|---------------------|---------------|
| Customer acquisition efficiency | high | middle | middle | High (free core capabilities + sharing) |
| Clarity of reason for payment | Low | high | middle | High (AI deep insight + family empathy) |
| retention driver | Light rubbing habit | Brand and Achievements | Multiple needs | Behavior improvement effect + relationship synergy |
| extended ceiling | Low (donation) | Middle to high | Middle to high | High (individual + family + team) |
| risk | Monetization is unsustainable | Paywalls lead to churn | Complex to get started | Need to balance AI cost and service quality |

**Conclusion**: FOMO adopts a hybrid model of "ScreenZen-style low-threshold customer acquisition + Opal-style payment tiering + Freedom-style long-term stickiness", and takes "verifiable human-centered effects" as the core of renewal.

### 7.2.2 Scenario-based revenue model (Year 2)

| scene | MAU | Pay rate | paying user | Month ARPPU | MRR |
|------|-----|--------|----------|----------|-----|
| keep | 80,000 | 4% | 3,200 | ¥24 | ¥76,800 |
| benchmark | 120,000 | 6% | 7,200 | ¥26 | ¥187,200 |
| Enterprising | 180,000 | 8% | 14,400 | ¥28 | ¥403,200 |

### 7.2.3 Unit cost and gross profit structure (AI era)

| Cost item | Free users (months) | Paid users (months) | Remark |
|--------|----------------|----------------|------|
| Cloud and infrastructure | ¥0.4 | ¥1.2 | Including log, push, synchronization |
| AI inference cost | ¥0.2 | ¥2.0 | More weekly reports/suggestions for paying users |
| Customer service and operations | ¥0.1 | ¥0.8 | Home and Team editions have higher support costs |
| Total unit cost | ¥0.7 | ¥4.0 | There is still significant gross profit potential on the paid side |

**Operating Threshold**: When the monthly ARPPU of paying users ≥ ¥22 and AI cost/paying users ≤ ¥3, the paid gross profit margin can be stabilized at more than 80%.

### 7.3 Income structure (Year 1 End)

| source | Proportion | illustrate |
|------|------|------|
| Personal Pro (monthly payment + annual payment) | 65% | Core monetization source, annual payment ratio target >50% |
| Home version | 20% | High ARPU (¥48/month), strong stickiness in family scenes |
| Team Edition | 10% | B2B early verification, ACV≥¥5,000/year |
| Lifetime Edition + Co-branded | 5% | Cash flow supplement, limited strategy |

### 7.3.1 Paid conversion funnel

```
New installers (100%)
    │ D1 retention ~50%
    ▼
D1 Active (50%)
    │ Boot completion rate ~70%
    ▼
Complete boot (35%)
    │ AI function reach rate ~60%
    ▼
AI feature usage (21%)
    │ Hits paywall ~40%
    ▼
Visit subscription page (8.4%)
    │ Page conversion rate ~35%
    ▼
Paying Users (3%) ← Phase 2 Target
```

**Funnel Optimization Priority**:
1. **Guidance completion rate** (target ≥70%) → Simplify the guidance steps and achieve immediate results on the first day
2. **AI function reach rate** → Free trial of AI weekly report once to lower the perception threshold
3. **Subscription page conversion rate** → A/B test pricing anchor (annual payment discount is significant) + 7-day free trial

### 7.3.2 Year 2 Refined Revenue Forecast

| scene | M12 MAU | M24 MAU | Pay rate | M24 MRR | M24 ARR | Gross profit margin |
|------|---------|---------|--------|---------|---------|--------|
| keep | 50,000 | 80,000 | 4% | ¥76,800 | ¥922K | 78% |
| benchmark | 50,000 | 120,000 | 6% | ¥187,200 | ¥2.25M | 82% |
| Enterprising | 50,000 | 180,000 | 8% | ¥403,200 | ¥4.84M | 84% |

**Break-even point** (baseline scenario): Monthly fixed costs ≈¥250,000. Operating breakeven is reached when MRR reaches ¥250,000, corresponding to approximately M30 (i.e., year 2.5), paying users ≈ 11,000, and MAU ≈ 180,000 (payment rate 6%).

### 7.3.3 B2B Path (Team Edition/School Edition)

**Positioning**: Not an MDM replacement, but an "enterprise digital well-being tool", positioned in the HR/EAP (Employee Assistance Program) field.

| Dimensions | describe |
|------|------|
| target customers | Internet company HR, school psychologist, enterprise EAP supplier |
| value proposition | Anonymous aggregated dashboards (no monitoring of individuals); team digital health reporting; employee well-being KPIs |
| Pricing reference | ¥15/person/month (annual payment); starting from 50 people; ACV≥¥9,000/year |
| sales path | Phase 3 3 PoC → case polishing → direct sales + channel (EAP agency) |
| priority | Year 2 is the main focus, Year 1 is only PoC verification. |

**B2B segmented scenario expansion: church/faith community path**

| Dimensions | describe |
|------|------|
| target customers | Christian Church Discipleship Program Director|
| value proposition | "Digital abstinence aid" for discipleship - to help students manage cell phone distractions during spiritual practice/quiet hours |
| Differentiated functions | "Holy period" mode (user-defined): one-click activation without interference; mission log (self-reflection + action record) |
| Pricing reference | ¥8/person/month (annual payment); starting from 20 people; 50% discount for churches/philanthropic groups |
| sales path | Contact the community leader directly; attract traffic through religious KOL/podcast cooperation |
| Copyable extension path | First verify the low-cost delivery template in the church scene, and then reuse it in the education community/mental health community/EAP organization |
| priority | Phase 2 Rapid PoC verification (short decision-making cycle, easy to pilot on a small scale) |

### 7.4 Growth Flywheel

```
User usage → AI analyzes behavioral data → Visible behavioral improvement (AI daily/weekly report)
    │
    ▼ The more accurate the AI ​​insights are → Users feel "it really understands me" → Migration cost↑
    │
    ▼ Obtain achievements → Generate sharing cards → Send to WeChat/Moments
    │
    ▼ Download by friends → Free trial → AI function reaches the paywall → Conversion Pro
    │
    ▼ More user data → AI is more accurate → Better results → More sharing ↺
```

> The AI ​​data flywheel is the underlying engine of FOMO growth: the longer users use it, the better AI understands it, and the harder it is to catch up with competing products.

**Growth leverage priorities and estimated K-factor**

| priority | lever | K-factor estimate | cost | activation time |
|--------|------|--------------|------|----------|
| P0 | AI Weekly Report Sharing (Cards in Moments) | 0.3–0.5 | extremely low | Phase 2 S6 |
| P0 | 7-Day Challenge Invite Friends | 0.3–0.5 | extremely low | Phase 2 S9 |
| P1 | ASO (focus/self-discipline/screen time/mobile phone dependence) | — | Low | Phase 1 available |
| P1 | Learning/efficiency KOL (Xiaohongshu/Station B) | — | middle | Phase 2 M4 |
| P2 | Scenario operation (examination preparation season/New Year’s Day challenge/bedtime topic) | — | middle | Phase 2 M5+ |
| P2 | Paid information flow (Xiaohongshu/Douyin) | — | high | Phase 3 |

**User tiered growth strategy (RFM)**

| Hierarchy | definition | activation strategy |
|------|------|----------|
| champion | D30 retention + Pro payment | Invitation to become a tester; exclusive new feature Beta |
| potential | D14 retained but not paid | 1 free trial of AI function + Oriented Pro elastic layer |
| silence | D1 disappears after becoming active | D3/D7/D14 Emotional push (non-rush type) |
| churn risk | Not opened for 3 days in a row | "Your Streak is dying" push (Streak users only) |

### 7.5 Humanistic values ​​and business balance

| issue | in principle | Execution method | Monthly Verification Metrics |
|------|------|----------|-------------|
| Realization boundary | Don’t create anxiety to promote payment | The free version retains core intervention capabilities (pause + 3 rules + daily report) | "Feeling anxious due to FOMO" feedback rate <5% |
| AI payment strategy | Pay to "understand you better" rather than "can use it" | Pro provides in-depth insights; basic daily reports are available for free | AI satisfaction difference (Pro vs Free) >0.5 points |
| growth ethics | Don’t engage in addictive retention | The daily push limit is 1; no inducement to check in | Push unsubscription rate <5% |
| family scene | Protect the dignity of minors | Parent panel shows trends, not shaming rankings | Negative feedback on parent-child conflict <2% |
| Enterprise scenario | Wellbeing rather than surveillance | The team version only sees anonymous aggregated data | — |

### 7.6 Clear differentiation path (Why us)

| Opponent's strengths | FOMO Transcendence Path | Verifiable Differentiation Metrics |
|----------|--------------|-----------------|
| ScreenZen Light Rub Free | Low threshold + AI can explain suggestions and improve long-term results | 90-Day Retention: FOMO vs. ScreenZen |
| one sec science interruption | Reuse interruption + emotion perception + mindfulness moment to reduce psychological burden | "Sense of Respect" NPS item |
| Opal has a strong brand and payment system | Proven results + human-centered experience → higher renewal rate | Pro annual renewal rate target ≥65% |
| Freedom cross-terminal maturity | Family empathy + AI relationship network differentiation | Home Edition ARPU vs. Personal Edition |

**Three-layer moat**

| level | moat | Setup time | Difficulty of breaking |
|------|--------|----------|----------|
| first floor | Accumulation of user behavior data (local priority, AI becomes more and more accurate) | From Phase 2 | Very high (data cannot be migrated) |
| second floor | Social migration costs (partner supervision + family network) | Phase 2 S9 onwards | High (relationship circle needs to be rebuilt) |
| third floor | Humanistic brand recognition ("non-judgmental" and "gentle and helpful") | continuing operations | Medium to high (emotional identification) |
---

## 8. Risk management

### 8.1 Risk heat map

```
Influence
Extremely high │ R13
High │ R1 R2 R9 R10 R11
Medium │ R3 R4 R5 R6 R8 R12
Low │ R7
     └──────────────────────────────────
         Very low low medium high very high probability
```

> Priority management: **R1 (iOS restrictions) > R10 (psychological burden) > R2 (retention decay) > R9 (big manufacturers entering) > R11 (local big manufacturers) **

### 8.2 Risk details and response Playbook

| # | risk | Probability | Influence | Early signal (quantized trigger line) | coping strategies | Responsible person | Check frequency |
|---|------|------|------|------------------------|----------|--------|----------|
| R1 | **iOS Screen Time API restrictions tightened** | high | high | WWDC policy announced; TestFlight review rejected ≥ 2 times | ① Functional layering, core interception does not rely on a single API; ② Pre-research MDM; ③ Worst case scenario focuses on light touch reminders | Tech Lead | Monthly (weekly before WWDC) |
| R2 | **Freshness decays** leading to substandard retention | middle | high | D7→D14 retention dropped >40%; weekly activity dropped >20% month-on-month | ① AI generates new insights every week; ② New achievements/challenges are launched every month; ③ Partners supervise social stickiness; ④ AI dialogue coach (Phase 3) new interaction dimension | PM | Every Sprint |
| R3 | **Strict mode causes disgust** leading to uninstallation | middle | middle | 1-star reviews containing "force/control" words ≥3/week; uninstallation surge >5% | ① Default flexible mode; ② Strict mode needs to be actively turned on + secondary confirmation; ③ Suspend 1-day safety valve; ④ Psychological consultant bi-weekly review copy | PM+Consultant | Every Sprint |
| R4 | **Quick follow-up of competing products** Interruption of core functions | middle | middle | ScreenZen/Opal announces similar AI coaching feature | ① The local behavioral data flywheel cannot be migrated; ② Accelerate Phase 2 AI in-depth insights; ③ Social + family relationship migration costs | PM | per month |
| R5 | **Privacy Compliance Risk** | Low | high | User complaints/negative media; regulatory investigation initiated | ① End-side priority architecture (see 3.1 AI contact point security boundary and 7.2.3 Cost structure); ② Minimal data collection; ③ Data export/deletion function; ④ Privacy Policy legal review; ⑤ GDPR-ready (when internationalized) | Tech Lead+PM | quarterly |
| R6 | **Key personnel loss** (iOS/AI engineer) | middle | high | Preference for exit interviews; active resumes on recruitment platforms | ① Two-person backup of core technology + complete documentation; ② ADR to record technical decisions; ③ 4-year option Vesting; ④ Interviews reserved every quarter | CEO | quarterly |
| R7 | **Free competing products** Compressed paid space | middle | middle | "Why Pay FOMO" Comments Emerge | ① The free version retains core capabilities and clearly differentiates Pro value; ② The annual payment discount maximizes LTV; ③ Humanistic and emotional competition | PM | per month |
| R8 | **LLM API price/quality fluctuation** or outage | middle | middle | API cost increased by >30% month-on-month; error rate >5% | ① Multiple model options (Claude Haiku → GPT-4o-mini → Llama local); ② Rule engine downgrade to cover the cost; ③ Cost warning ¥3,000/month warning | Backend engineer | weekly |
| R9 | **Operating system/large model native cut-in**Screen time | Low | high | Apple/Google WWDC announces built-in AI focus capabilities | ① Data flywheel moat; ② Social dimension platform is difficult to cross the border; ③ Emotional brand: users trust FOMO rather than big manufacturers | CEO+PM | per month |
| R10 | **Excessive intervention causes psychological burden** | middle | high | User survey "feeling anxious/being judged">3/5; negative words >5 items/week; rule closing rate >30% | ① Caring copy review (consultants participate in each version); ② Mild mode is enabled by default; ③ Strategy upgrades undergo A/B psychological assessment; ④ Negative emotion trigger rate is used as monthly KR red line | PM+Consultant | Every Sprint |
| R11 | **China’s major local manufacturers enter the market** | middle | high | Digital health-related recruitment surges at major manufacturers; official features released | ① "Independent third-party user trust" brand label; ② Strengthen local data privacy moat; ③ Explore module cooperation with large manufacturers instead of confrontation | CEO | per month |
| R12 | **Regulatory policies are tightened** | Low | middle | A policy draft appeared; similar apps were removed from the shelves | ① Proactively comply with regulations in advance; ② "Compliance and safety" as a product selling point (family version); ③ Establish relationships with schools/education departments | PM+Legal Affairs | quarterly |
| R13 | **User privacy data leaked** | extremely low | extremely high | Security scan alerts; white hat vulnerability reports; media exposure | ① Client-side priority, sensitive data is not uploaded to the cloud; ② Annual independent security audit; ③ Disaster response plan: 4h internal confirmation, 24h user announcement, 72h patch online | Tech Lead | quarterly |

### 8.3 Layered indicator monitoring system (Four-Dimensional Dashboard)

The monitoring indicators are divided into four layers (Polaris → Business → Product → Technology → Humanities), and each layer has different refresh frequencies and trigger thresholds. All indicators are automatically summarized by the Mixpanel + Sentry + Slack alert robot, and the PM + Tech Lead needs to start the Playbook within 4 hours of the red light.

#### Level 1: North Star + Business Metrics

| index | Refresh frequency | green light | yellow light | red light | trigger action |
|:---|:---:|:---|:---|:---|:---|
| **NSM** (number of abandonments/user per week) | Weekly | Weekly average ↑ trend | Same month on month | Month-on-month↓ | Review AI weekly report and impulse interruption mechanism |
| D7 retention rate | Weekly | ≥35% | 30-34% | <30% | Trigger R2 Playbook (novelty decay) |
| D14 retention rate | Weekly | ≥25% | 20-24% | <20% | Analyze the retention funnel and prioritize improvement of guidance |
| D30 retention rate | Weekly | ≥22% | 18-21% | <18% | Phase Gate review to evaluate whether to switch strategies |
| **MRR** | monthly | Month-on-month ↑15% | Month-on-month ↑5-14% | Month-on-month↓ | Review Pro Conversion or Pricing Strategies |
| **CAC** (Hybrid) | monthly | ≤¥15 | ¥15-20 | >¥20 | Stop advertising and focus on natural growth |
| **LTV/CAC** | monthly | >3 | 2-3 | <2 | Business model warning, pricing needs to be adjusted or costs reduced |
| **NPS** | monthly | ≥40 | 30-39 | <30 | Start an in-depth interview with NPS to find out details |

#### Second layer: Product experience indicators (user perception driven)

| index | Refresh frequency | green light | yellow light | red light | trigger action |
|:---|:---:|:---|:---|:---|:---|
| Novice guide completion rate | Weekly | ≥80% | 70-79% | <70% | Re-test the process and simplify the steps |
| AI Weekly Report Satisfaction | Weekly | ≥4/5 | 3.5-3.9/5 | <3.5/5 | Prompt tune or downgrade to rule engine solution |
| "Sense of respect" rating | monthly | ≥4/5 | 3.5-3.9/5 | <3.5/5 | **Pause new features immediately** and review all copywriting and interactions |
| Proportion of users with "too much stress" | Weekly | <2% | 2-5% | >5% | Trigger R10 Playbook to reduce intervention efforts |
| Rule compliance rate (users who meet the standard in 3 days/week) | Weekly | ≥45% | 35-44% | <35% | Analyze rules for ease of use or whether they are too strict |
| Pause page "leave" click-through rate | Weekly | 30-50% | 20-29% | <20% | The pause page is too short/the copy is not noticeable, please adjust it. |
| "Enforced limit circumvention" times | Weekly | <3% | 3-8% | >8% | Rules are too bypassable, strengthen technical protection |

#### Level 3: Technical Risk Indicators (Infrastructure Driven)

| index | Refresh frequency | green light | yellow light | red light | trigger action |
|:---|:---:|:---|:---|:---|:---|
| Two-sided crash rate | day | <0.5% | 0.5-1% | >1% | **Rollback** this version immediately and retest |
| API response time p95 | day | <500ms | 500-800ms | >800ms | Performance analysis, expansion may be needed |
| Login success rate | day | >99.5% | 99-99.4% | <99% | Telephone alarm, immediate on-call inspection |
| Data synchronization delay (P95) | day | <5s | 5-10s | >10s | Check the health status of cloud sync service |
| LLM API error rate | day | <1% | 1-5% | >5% | Downgrade and cut rule engine, seamless retry |
| Number of security scan alerts | Weekly | 0 | 1-2 | >2 | Assess whether there is a CVE and determine the severity |

#### The fourth level: Humanities and ethics indicators (newly added, relationship R10)

| index | Refresh frequency | green light | yellow light | red light | trigger action |
|:---|:---:|:---|:---|:---|:---|
| **Proportion of negative copywriting** | per version | = 0% | 0-1% | >1% | The version is rolled back and all copywriting is reviewed. |
| "Being judged" complaints as a proportion of total complaints | Weekly | <2% | 2-5% | >5% | Initiate ethics review meeting (see §11) |
| "Feeling of being controlled" user feedback | Weekly | <1% | 1-3% | >3% | Check Strict Mode/cooldown period logic now |
| "Helpful" vs. "Annoying" feedback ratio | Weekly | >5:1 | 3:1 to 5:1 | <3:1 | Function may be too disruptive, consider downgrading |
| AI recommendation "useless" rate | Weekly | <10% | 10-20% | >20% | AI models may need to be retrained |
| Ethics review pass rate | per version | 100% | 95-99% | <95% | **BANNED FOR RELEASE**, Redesigned |

#### Indicator correlation rules (Cross-Layer Alerts)

```
If D7 is retained↓>10pp
  └─ Automated joint query: NSM down? Boot completion rates dropping?
  └─ Possible reasons: The new features have bugs or the experience is poor
  └─ Action: Immediate Code Review + user feedback analysis

If "sense of respect"↓>0.5
  └─ Automatic trigger: pause all new feature releases
  └─ Action: Ethics review meeting; Psychological consultant evaluation
  └─ Notice: Live broadcast for all employees to review the original intention of product design

If "stress is too high">5%
  └─ Automatic switching: The default switching intervention intensity for all users is -50%
  └─ Action: Analyze which function caused the problem; consider going offline
  └─ Timeline: The yellow flag reminder must be turned on within 4 hours

If LLM API error >5%
  └─ Automatic downgrade: AI weekly report → Rule engine template feedback
  └─ Action: User unaware, automatic retry + downgrade solution
  └─ Post-incident: Review of API producer issues
```

#### Implementation mechanism

**Summary dashboard**: Datadog / self-built Dashboard integrates the above 30+ indicators, and the update frequency (daily/weekly) is different when the board is live

**Alarm rules**:
- Green light: no prompt
- Yellow light: Slack @pm-channel, root cause analysis within 24 hours
- Red light: Slack @pm-tech-cto phone notification, start Playbook within 4 hours

**Decision-making authority**:
- Yellow light: PM can decide by himself whether to start the corresponding Playbook
- Red light (ethics): PM + psychological consultant + CEO 3-person voting decision
- Red light (technical category): Tech Lead has the right to roll back immediately

**Monthly Review**: In the last week of each month, PM + Tech Lead + Psychological Consultant conduct "Indicator Market" review and generate MoM (Month-over-Month) analysis report for financing and team review.


### 8.4 Data Security and Compliance Checklist

> This checklist covers the data security and privacy compliance requirements that must be met in the first year, and additional GDPR/CCPA needs to be met during internationalization.

| # | Require | priority | person in charge | target time | state |
|---|------|--------|--------|----------|------|
| C1 | Privacy Policy and User Agreement Online (Chinese + English) | P0 | PM+Legal Affairs | Before MVP is released | To be completed |
| C2 | Local storage encryption (SQLite/Realm AES-256) | P0 | Tech Lead | S1 | To be developed |
| C3 | Full network transmission link HTTPS/TLS 1.2+ | P0 | rear end | S1 | To be developed |
| C4 | Data minimization: only collect metadata (time + App name + user selection), prohibit the collection of input content/chat/location | P0 | All members | continued | continued |
| C5 | User data export (JSON/CSV one-click download, including timestamp/App/intent metadata, committed to compatibility with Apple/Google future standards) | P0 | rear end | S4 | To be developed |
| C6 | User data deletion (completely cleared within 30 days after account cancellation) | P0 | rear end | S4 | To be developed |
| C7 | Sensitive permission usage description (Accessibility/Screen Time API) | P0 | PM | Before release | To be completed |
| C8 | LLM API calls only transmit desensitized aggregate summaries and are prohibited from transmitting original behavior sequences. | P0 | rear end | S6 | To be developed |
| C9 | Teen Accounts: Parental Consent Process (Minor Protection Act + COPPA) | P1 | PM+Legal Affairs | Phase 2 | To be planned |
| C10 | Annual independent security audit (penetration testing + code audit) | P1 | Tech Lead | Phase 3 | To be planned |
| C11 | GDPR-ready data processing infrastructure (internationalization front-end) | P2 | Backend + legal affairs | Phase 3 | To be evaluated |

> Status description: If the status is "Continuous", it means that the project needs to be implemented for a long time and audited according to versions, and is not considered completed with a single online launch.

**Compliance bottom line**: Before any version goes online, C1–C8 must be completed and none of them can be missing.

---

## 9. Appendix

### 9.1 Glossary

| the term | definition |
|------|------|
| High risk apps | Apps marked by users as "prone to getting out of control" |
| Pause page/break page | Intent confirmation interface before opening high-risk apps |
| Strict Mode | Rule status that cannot be closed during the cooling period |
| Streak | Number of consecutive days to meet the standard |
| The right choice | The behavior of selecting "leave" on the pause page |
| NSM | North Star Metric North Star Metric |
| LTV | Life Time Value User lifetime value |
| CAC | Customer Acquisition Cost Customer Acquisition Cost |
| MRR/ARR | Monthly/Annual Recurring Revenue |
| AI behavioral coach | Personalized behavior analysis and recommendation system based on LLM |
| AI data flywheel | User data accumulation→AI insight improvement→retention enhancement→positive cycle of more data |
| end-to-end reasoning | Run AI models (Core ML/NNAPI) locally on user devices with zero privacy risk |
| Prompt project | Techniques for designing LLM input prompts for accurate, structured output |
| Downgrade | Automatically switches to the rules engine to generate basic insights when AI is unavailable |
| Emotion sensing engine | Infer the user's emotional stress level (green/yellow/red) based on behavioral signals (period/intent drift/failure sequence/touch frequency/ambient light), fully local calculation |
| Partner supervision | Two or more people can jointly set up a digital self-discipline challenge and check each other's compliance status (privacy is prioritized, and the specific app name will not be exposed by default) |
| K-factor | Viral Coefficient, a measure of the average number of new users brought by each existing user |
| Mild mode | During late night/high pressure/continuous failure periods, priority is given to using intervention strategies suggested by emotional soothing and small goals instead of directly upgrading the restriction intensity. |
| Phase Gate | Stage gate review, based on quantitative indicators, decision-making of "advance at full speed / pass with conditions / stop" |
| WCAG | Web Content Accessibility Guidelines, Web content accessibility guidelines (Level AA requires text/background contrast ratio ≥4.5:1) |
| GDPR | General Data Protection Regulation, the European Union's General Data Protection Regulation, applies to products that process the personal data of EU residents |
| COPPA | Children's Online Privacy Protection Act, the United States "Children's Online Privacy Protection Act", users under the age of 13 must obtain parental consent |
| EAP | Employee Assistance Program, employee assistance program, mental health and welfare support services provided by companies to employees |
| CBT | Cognitive Behavioral Therapy, cognitive behavioral therapy, a psychological intervention method used to identify and correct negative thinking patterns |
| Freemium | Free value-added model (Free + Premium combined word), core functions are available for free, and advanced functions are unlocked for a fee |
| TLS | Transport Layer Security, Transport Layer Security Protocol (TLS 1.2+), used to encrypt network communications between applications and servers |

### 9.2 References

**Academic and Research Reports**

| source | content | Conclusion summary |
|------|------|----------|
| DataReportal 2025 | Digital 2025 Global Overview | The global average daily screen time is 6.5 hours, a year-on-year increase of 4.2% |
| Opal Screen Time Report 2025 | Real user screen behavior data | Average daily unlocks: 96 times, 4M+ users |
| one sec × Max Planck Institute | Peer-reviewed behavioral intervention studies | Interruptive interventions reduce app usage by 57% |
| Carnegie Mellon 2021 | Freedom Productivity Randomized Controlled Trial | +22% hourly wage output using blocking tools |
| Microsoft Research 2023 | Block distractions and deep work | Reduce distractions and increase productivity by 20% |
| PNAS Nexus 2024 | Internet access and mental health | Reducing access significantly improves concentration and mood |
| Univ. of Waterloo | A meta-analysis of the effectiveness of blocking tools | Mission completion rate +27% |
| Chinese Sleep Research Association 2024 | China sleep health report | 300 million people have sleep disorders, and mobile phones are the primary disturbing factor |
| Zario x Stanford | Research on the effectiveness of AI behavioral intervention (2025) | AI personalized recommendation acceptance rate >Traditional rule recommendation 40pp |

**Competitive product public data**

| product | data | source |
|------|------|------|
| ScreenZen | 1M+ monthly active users, App Store global 4.8 stars | App Store public page |
| Freedom | 4M+ users, reported by NYT/WSJ/Wired | freedom.to |
| Opal | 4M+ users, average time saved 1h23m per day | opal.so |
| AppBlock | Paid version $4.99/month, Pro $9.99/month | appblock.app/premium |
| Forest | Cumulatively planted 200M+ trees, B Corp certified | forestapp.cc |
| one sec | 1M+ users, named App of the Year by Apple | one-sec.app |

---

## 10. Business & Execution Pack

> This chapter provides ready-to-use documents for financing roadshows, early team operations, and growth execution. Single chapters can be directly extracted for external use. Contains: Funding Deck Outline, MVP To-Do List, Product Philosophy Statement, GTM Strategy, and 12-Month Financial Forecast.

### 10.1 Financing Roadshow PPT Outline (12 Pages Deck)

| page number | theme | core content | Picture suggestions |
|---|---|---|---|
| P1 | **Title / Hook** | **FOMO: AI-Powered Digital Wellbeing Coach**<br>From "control tool" to "decision-making coach", let 1 billion people regain digital autonomy. | Brand Logo + abstract graphic of “Human and AI shaking hands” |
| P2 | **Problem** | **"Unconscious use" is eating us**<br>- 6.5h average daily screen time, 40% unconscious. <br>- Reasons for the failure of existing competing products: forced blockade (anti-humanity) or weak incentives (ineffective). <br>- New crisis in the AI ​​era: Algorithms are more accurate and users are more difficult to resist. | Funnel chart: the process of time being swallowed up by fragmentation |
| P3 | **Solution** | **AI intervenes in key decision points (T1-T7 touch points)**<br>- Core mechanism: light interruption + intention confirmation + real-time feedback. <br>- Differentiation: It’s not about “don’t use it”, it’s about “thinking about it before using it”. <br>- Demo: AI identifies high-stress moments -> triggers mindfulness mode -> restores calm. | Product interaction effects: Pause Screen -> Intent selection -> AI suggestions |
| P4 | **Why Now** | **The perfect storm of technology and market**<br>- Market: Digital Health Awareness Awakening (One Sec/Opal Verification of Willingness to Pay). <br>- Technology: The cost of end-side LLM has dropped sharply, which can not only run through behavioral analysis, but also protect privacy. <br>- Policy: Global anti-addiction regulatory trends. | Intersection diagram of the three circles of market/technology/policy |
| P5 | **Product Magic** | **Understand your human-centered AI better**<br>- Emotion perception engine: Identify anxiety/boredom. <br>- Family Empathy Mode: Connect rather than monitor. <br>- Data Flywheel: The longer you use it, the better you will understand your weaknesses and motivations. | "AI Touchpoint Map" visualization |
| P6 | **Business Model** | **Hybrid Monetization Model (Freemium)**<br>- Free: Core disruption functionality (customer acquisition). <br>- Pro: AI Coach + Deep Insight + Advanced Rules (ARPU ¥22). <br>- Family/Team: High stickiness and high customer unit price. | Tiered Pricing + Funnel Model |
| P7 | **Traction & Validation** | **Early Validation Data (Simulation/Target)**<br>- NSM (number of abandonments) increased month-on-month. <br>- D1 60% / D7 35% target. <br>- High NPS feedback from seed users. | Key Metrics Dashboard |
| P8 | **Go-To-Market** | **Low-Cost Growth Flywheel**<br>- Social Fission: Achievement Cards + Partner Challenges. <br>- Scene entry: postgraduate entrance examination/before going to bed/workflow. <br>- Brand: Humanistic care vs the cold "blockade" of competing products. | Growth flywheel cycle diagram |
| P9 | **Competition** | **Dimensionality reduction attack**<br>- Horizontal axis: effectiveness; vertical axis: human-centered care. <br>- Quadrant chart: FOMO is in the upper right corner (high effectiveness + high human-centered). <br>- Moat: data accumulation + relationship chain. | Competitive Quadrant Diagram |
| P10 | **Financials** | **Financial Forecast**<br>- Year 1: 50,000 users, verify the model. <br>- Year 2: 150,000 users, break even. <br>- Year 3: scale up, AI costs decrease due to device-side reasoning. | Revenue/Cost Bar Chart (3 years) |
| P11 | **Team** | **Compound background of product + technology + psychology**<br>- Founder: serial entrepreneur/product expert. <br>- Tech Lead: AI/mobile full stack. <br>- Consultant: Expert in behavioral psychology. | Team avatar + core logo |
| P12 | **Ask** | **Financing Requirements**<br>-Amount: ¥3-4 million. <br>- Purpose: 18 months Runway (40% product iteration, 30% market, 30% operations). <br>- Vision: Define digital lifestyle in the AI ​​era. | Fund Allocation Pie Chart + Contact Information |

---

### 10.2 MVP Detailed Task List (User Stories)

**Sprint 1: Architecture and Core Interrupts (W5-6)**
- [Client] US-001: Build iOS/Android project skeleton and integrate basic statistics SDK.
- [Client] US-002: Implement Accessibility Service (Android) / Screen Time API (iOS) permission application process.
- [Client] US-003: Core interception logic: detect whitelist/blacklist App startup and implement interception.
- [Client] US-004: **Pause Page UI (v1)**: Countdown (3s/5s) + "Continue"/"Leave" button.
- [Data] US-005: Local database design (SQLite/Realm) to store App startup events and interception records.

**Sprint 2: Rules Engine and Templates (W7-8)**
- [Client] US-006: Rule configuration page: supports setting interception by time range (Time range).
- [Client] US-007: One-click application logic for **3 large preset templates** (study/work/bedtime).
- [Client] US-008: Daily limit (Usage Limit) logic implementation.
- [Client] US-009: Intent confirmation page: Add "intent selection" (4 options) and data recording to the pause page.

**Sprint 3: Feedback and Achievement System (W9-10)**
- [Client] US-010: **Daily page**: Displays the number of interceptions today, time saved, and the most frequently intercepted apps.
- [Client] US-011: **Streak logic**: Calculation and display of the number of consecutive days that meet the standard.
- [Client] US-012: Medal system front-end UI and unlocking logic (local judgment).
- [Client] US-013: Simple sharing card generation (generate pictures based on current data).

**Sprint 4: Anti-Bypass and AI Access Preparation (W11-12)**
- [Client] US-014: **Strict Mode**: Block the settings page/disable cancellation of rules during a specific period.
- [Backend] US-015: Deploy basic data cleaning pipeline.
- [Backend] US-016: **LLM interface joint debugging**: Build a simple but executable AI suggestion generation interface (Input: Behavior summary -> Output: Text suggestion).
- [Client] US-017: Newbie onboarding process (F-05) development.
- [Client] US-018: Grayscale package packaging and distribution channels are connected.

**Sprint 5: Grayscale review and experience repair (W13-14)**
- [PM] US-019: Output the D7/D14 retention funnel analysis report and mark the Top 3 churn nodes.
- [Full Stack] US-020: Fix the Top 3 pain points reported by grayscale users (to be determined based on actual grayscale data).
- [Client] US-021: Pause page experience optimization (targeted adjustments based on App categories with too high "continue browsing" rate in grayscale data).
- [Data] US-022: Build Mixpanel key funnel dashboard (Installation→Guide→Rule Settings→D7 Retention).

**Sprint 6: AI Weekly Coach V1 (W15-16)**
- [Backend] US-023: Build a behavior summary construction pipeline - aggregate user local behavior data every week and generate structured summary JSON.
- [Backend] US-024: Design and tune the AI ​​weekly report Prompt (containing three paragraphs: Behavior review → Insight → 1 executable suggestion this week).
- [Backend] US-025: Connect to Claude Haiku / GPT-4o-mini to achieve asynchronous generation, response delay <5s, failure downgrade to rule engine summary.
- [Client] US-026: AI weekly report display page: title card, three paragraphs of text, "One-click execution of suggestions" button, satisfaction rating (1-5 stars).
- [Data] US-027: Hiding AI weekly report satisfaction, suggestion adoption rate, display → closing duration.

**Sprint 7: Emotion Awareness Engine + Mindful Moments (W17-18)**
- [Local/Client] US-028: Implement emotion level calculation logic (4 types of behavioral signals → three levels of low/medium/high voltage).
- [Client] US-029: Mindful moment pop-up UI - abdominal breathing animation (4-7-8 rhythm), supports 30/60/90 seconds.
- [Client] US-030: Pause page integration: Add a "30-second breathing exercise" soft entry to the pause page under high-pressure red light conditions.
- [Data] US-031: Number of burying emotion level triggers, mindfulness practice start/completion rate, and continuation rate after practice.

**Sprint 8: Paid Online (W19-20)**
- [Backend] US-032: Connect to App Store IAP (iOS) and Google Play Billing (Android) to implement subscription purchase, restoration, and expiration processing.
- [Client] US-033: Paywall UI - Pro benefit comparison table; annual payment discount anchor; 7-day free trial CTA.
- [Backend] US-034: Pricing A/B experiment: ¥28/month vs ¥35/month, randomized 50/50, 2 weeks to collect conversion rates.
- [Client] US-035: Function Paywall Guard - Pro exclusive functions (AI weekly report, Strict Mode advanced settings) reach limit prompts.
- [Data] US-036: Build a revenue dashboard (MRR, new payment, churn payment, LTV estimation).

**Sprint 9: Partner Supervision V1 (W21-22)**
- [Backend] US-037: Partner invitation system - generate a unique invitation link, and establish a two-way binding relationship after acceptance (server-side verification).
- [Client] US-038: Partner status page - displays an overview of the other party's meeting/not meeting the standards today, the number of consecutive days, and the duration (optional to enable).
- [Push] US-039: Partner failure reminder push - triggered when the other party fails to meet the standard, the user can reply to the default "Cheer/Provocation" label.
- [Client] US-040: 7-day two-player challenge process - create challenge, both parties confirm goals, progress display, complete and unlock joint achievements.
- [Data] US-041: Differences in click-through rate of hidden invitation links, pairing success rate, and D14 retention after partner binding.

**Sprint 10: Browser extension + sharing optimization (W23-24)**
- [Front-end] US-042: Develop Chrome extension V1 - rule synchronization API, interception page (countdown + intent record), release Chrome Web Store.
- [Client] US-043: Share Card V2 - Contains AI personalized comments (keywords extracted from this week's weekly report), visual poster format.
- [Client] US-044: Optimization of the 7-day challenge invitation process - invitation link deep link (direct jump installed, landing page not installed).
- [PM] US-045: MAU 5,000 acceptance - Output the Phase 2 Gate review report and determine the Phase 3 investment scale.

---

### 10.3 Product Philosophy and Humanistic Declaration

> **"People are not the battery of the machine, but the master of the machine."**

**1. About control**
We believe that true self-discipline comes from **free will**, not forced deprivation.
FOMO always provides an "emergency exit" - even in the most restrictive mode, the user should have the highest discretion (although this may come at a higher time cost, such as a 30 second wait).
**Principle:** Unless the user explicitly authorizes "forced takeover", "negotiated intervention" is adopted by default.

**2. About data dignity**
Your anxieties, your vulnerable moments, the secrets you scroll through late at night—these aren’t just data, they’re privacy.
FOMO Commitment: All sensitive behavioral analysis will be done locally first. What is uploaded to the cloud is only the desensitized statistical characteristics.
**Principle:** Users not only have ownership of data, but also have the "right to be forgotten."

**3. About emotional value**
We refuse to drive behavior by creating a “feeling of failure.”
When you open TikTok again at 2 o'clock in the night, FOMO will say: "You look a little tired, do you need to take a deep breath?" instead of: "You failed again, it's really useless."
**Principle:** All feedback should be directed at being "constructive" and "empathetic" rather than "judgmental."

**4. About the addiction mechanism**
We do not exploit the weaknesses of human nature (such as red dot notifications and infinite pull-downs) to combat the addiction mechanism of apps.
FOMO itself must be **quiet**. Just use it and leave, allowing users to return to real life instead of being obsessed with "time management".
**Principle:** A good tool should become invisible after it has achieved its purpose.

---

### 10.4 Operations and Growth (GTM) Strategy

**Phase 1: Cold Start (M1-M3) - Finding “Super Pain Point” Users**
- **Goal**: First 1,000 seed users, NPS > 50.
- **Core group**: postgraduate entrance examination/public party examination, freelancers, self-disciplined people.
- **Channel Strategy**:
    - **Xiaohongshu/Bilibili**: Topic #postgraduate entrance examination countdown #self-discipline check-in #quit mobile phone. Publish a visual impact chart of “Screen time comparison before and after using FOMO”.
    - **Community Infiltration**: Share real stories on Reddit (DigitalMinimalism), Douban (mutual aid group for screen addicts).
- **Growth Hook**: Early Bird Lifetime Edition is limited to 100 copies in exchange for in-depth feedback.

**Phase 2: Word-of-mouth Fission (M4-M6) - Social Monetization**
- **Goal**: The number of users exceeds 10,000, and the payment rate is verified.
- **Core Actions**:
    - **Achievement Card 2.0**: The generated pictures are no longer boring data, but emotional posters with "personalized AI comments", stimulating the desire to share.
    - **Partner Challenge (Invite Flow)**: Two-person challenge mode is launched, and the invitation link click conversion rate is optimized to 20%+.
    - **App Store/Product Hunt**: Focus on rankings and strive for editor recommendation (emphasis on human-centered design).

**Phase 3: Cross-circle penetration (M7-M12) - Scenario-based marketing**
- **Goal**: The number of users exceeds 50,000 and establishes a brand moat.
- **Content Matrix**:
    - **Family Scenario**: To address parents’ anxiety, promote a “non-monitoring” family empathy model.
    - **Workplace scenario**: Link with the efficiency tool (Notion, Obsidian) community to create a "deep workflow" suite.
- **KOL Cooperation**: No longer limited to technology bloggers, but expanded to psychological counselors, lifestyle bloggers, and education experts.

---

### 10.5 Detailed 12-month financial forecast

| Account (Unit: ¥) | Q1 (MVP) | Q2 (Phase 1) | Q3 (Phase 2) | Q4 (Scale) | **Full Year Total** |
|---|---|---|---|---|---|
| **Revenue** | **0** | **22,000** | **132,000** | **440,000** | **594,000** |
| - Subscription revenue (Pro) | 0 | 12,000 | 90,000 | 320,000 | 422,000 |
| - Family/Team Edition | 0 | 0 | 22,000 | 80,000 | 102,000 |
| - Lifetime/other | 0 | 10,000 | 20,000 | 40,000 | 70,000 |
| | | | | | |
| **Cost (COGS)** | **15,000** | **35,000** | **65,000** | **120,000** | **235,000** |
| - Cloud services/CDN | 3,000 | 8,000 | 15,000 | 30,000 | 56,000 |
| - AI API calls | 2,000 | 10,000 | 30,000 | 60,000 | 102,000 |
| - Pay channel fees | 0 | 1,000 | 5,000 | 15,000 | 21,000 |
| - SMS/Push | 0 | 1,000 | 5,000 | 15,000 | 21,000 |
| Other COGS | 10,000 | 15,000 | 10,000 | - | 35,000 |
| | | | | | |
| **Gross Profit** | **-15,000** | **-13,000** | **67,000** | **320,000** | **359,000** |
| *Gross profit margin* | N/A | N/A | 51% | 73% | 60% |
| | | | | | |
| **Operating Expenses (OPEX)** | **510,000** | **630,000** | **750,000** | **900,000** | **2,790,000** |
| - Labor costs | 400,000 | 450,000 | 500,000 | 600,000 | 1,950,000 |
| - Marketing Promotion (CAC) | 50,000 | 100,000 | 150,000 | 200,000 | 500,000 |
| - Office/Administrative | 30,000 | 30,000 | 40,000 | 40,000 | 140,000 |
| - Outsourcing/Consultancy | 30,000 | 50,000 | 60,000 | 60,000 | 200,000 |
| | | | | | |
| **Net Income** | **-525,000** | **-643,000** | **-683,000** | **-580,000** | **-2,431,000** |
| *Cash flow reserve advice* | **> 100w** | **> 150w** | **> 200w** | **> 250w** | **Financing required ~300w** |

**Financial Notes:**
1. **AI Cost Optimization**: It is expected that the introduction of small end-side models in Q4 can reduce the cost of a single call by more than 60%, thereby increasing the gross profit margin to more than 70%.
2. **CAC control**: Q1-Q2 relies on natural growth, and Q3 starts delivery. It is assumed that the mixed CAC is controlled within ¥10.
3. **Cash flow**: The first 12 months are the investment period, with a cumulative loss of approximately 2.43 million (total net profit -¥2,431K). It is recommended to raise 3-4 million yuan in angel round financing to ensure an 18-month Runway.
