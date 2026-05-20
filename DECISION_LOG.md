# StoreSignal — Decision Log

> Every significant decision made during the build of StoreSignal.
> Format: We considered X, chose Y, because Z.
> This log was maintained throughout the build process, not written at the end.

---

## Day 1 — Planning & Problem Deep Dive

**Decision: Track Selection**
We considered all 5 tracks. Chose Track 5 (AI Representation Optimizer) because it is the closest to a real product problem — not a demo exercise. Every Shopify merchant will eventually face the problem of AI agent visibility. Building the diagnostic layer felt like the most original and commercially relevant contribution.

**Decision: Project Name**
We considered names including "ShopLens", "RepresentAI", and "AuraCheck". Chose "StoreSignal" because it is short, memorable, immediately communicates the idea of broadcasting information to AI agents, and works cleanly as a GitHub repo name and product brand.

**Decision: Input Method — URL vs Manual Paste**
We considered two approaches: (1) merchant pastes their product description manually, (2) we connect directly to their Shopify store via API. Chose Shopify Admin API integration as the primary method because manual paste creates friction and limits analysis depth. Manual input is kept as a fallback only.

---

## Day 2 — Foundation Setup

**Decision: Backend Framework — Flask vs Django**
We considered both Flask and Django. Chose Flask because of its lightweight architecture, fast development cycle, and simple AI service integration. Django's ORM and admin overhead were unnecessary for this project scope. Flask allowed each AI module to be plugged in independently.

**Decision: Database — PostgreSQL vs SQLite**
We considered SQLite for simplicity. Chose PostgreSQL because it is production-ready, supports concurrent analysis requests, and is compatible with our Render deployment. SQLite would have been a bottleneck for multi-merchant data storage.

**Decision: Frontend Framework — React vs Flask Templates**
We considered using Flask Jinja templates for the entire frontend. Chose React + Tailwind CSS because the dashboard requires dynamic state management — score animations, before/after toggling, copy-to-clipboard — which is painful in pure Jinja. React makes these interactions clean and maintainable.

---

## Day 3 — Shopify Integration

**Decision: Shopify API — Admin API vs Storefront API**
We considered the Shopify Storefront API (public, no auth needed). Chose the Admin API because it gives access to policies, metadata, and detailed product attributes that the Storefront API does not expose. Policies and metadata are critical for AI readiness analysis.

**Decision: Data Fetching Scope**
We considered fetching only product descriptions. Chose to fetch: product titles, descriptions, variants, policies, FAQ content, metadata, and review data. Reasoning: AI agents read all of this when forming a store perception. Analyzing only descriptions would miss 60% of the problem.

---

## Day 4 — Deterministic Audit Engine

**Decision: Scoring Dimensions**
We considered a single overall score. Chose 6 separate dimension scores (product descriptions, policy clarity, FAQ coverage, trust signals, structured data, review quality) because a single score hides where the problem is. Merchants need to know which specific area to fix first.

**Decision: FAQ Scoring — Binary vs Nuanced**
We considered scoring FAQ presence as binary (yes = 1, no = 0). Chose nuanced scoring (no FAQ = 5, basic FAQ = 45, detailed FAQ = 85) because a store with one FAQ question is almost as helpless as a store with none. Granular scoring produces more actionable results.

**Decision: What Counts as a "Weak" Description**
We defined weak descriptions as: under 30 words, no material/dimension mentions, no technical specifications, only generic adjectives (beautiful, great, amazing). This threshold was set after testing 10 real Shopify store descriptions and identifying the common failure patterns.

---

## Day 5 — OpenAI Integration

**Decision: AI Model Selection — GPT-4 vs GPT-3.5 vs Claude**
We considered Claude API (already accessible), GPT-3.5 (cheaper), and GPT-4. Chose OpenAI GPT-4 because it produces more structured JSON outputs reliably, handles long product descriptions without degradation, and has better performance on semantic ambiguity detection tasks in our tests.

**Decision: Prompt Architecture — Single Prompt vs Chained Prompts**
We considered one large prompt that does everything. Chose separate chained prompts for: (1) ambiguity detection, (2) AI perception simulation, (3) rewrite generation, (4) FAQ generation. Reasoning: smaller focused prompts produce better quality outputs than one giant prompt. Also easier to debug when one step fails.

**Decision: JSON Output Enforcement**
We considered parsing free-text AI outputs. Chose to enforce strict JSON output from all prompts because free-text parsing is fragile. All prompts specify exact JSON schema. Responses are validated before use. If JSON parsing fails, fallback handler activates.

**Decision: Where AI Starts and Code Ends**
Deliberate boundary: if a check can be expressed as a rule, it is deterministic. If it requires understanding meaning, context, or intent — it goes to the AI layer. This keeps scoring consistent while making semantic analysis intelligent. Mixed responsibility would make debugging impossible.

---

## Day 6 — Dashboard & Visualization

**Decision: Chart Generation — Matplotlib vs Recharts**
We considered Recharts (React-based, interactive). Chose Matplotlib for backend chart generation because server-side rendering is more stable, consistent across browsers, and charts can be exported for PDF reports. Recharts would have required significant state management for the analytics we needed.

**Decision: Before vs After UI Layout**
We considered showing before/after as separate pages. Chose side-by-side comparison on the same screen because merchants need to see the contrast immediately — the gap between current and optimized content is the core insight. Separate pages reduce the impact of that contrast.

**Decision: Action Plan Ranking**
We considered alphabetical ordering of recommendations. Chose impact-based ranking (highest business impact first) because merchants have limited time. The first thing they see should be the highest-value fix. Impact scores are calculated from: how often this issue causes AI agents to skip merchants, and effort required to fix.

---

## Day 7 — Failure Handling

**Decision: Fallback Strategy When OpenAI Fails**
We considered showing an error screen when OpenAI API fails. Chose graceful degradation: deterministic scoring continues, default rule-based recommendations are shown, dashboard remains functional. A partial result is always better than a crashed screen. Retry logic with 3 attempts and exponential backoff before fallback activates.

**Decision: Invalid Input Handling**
We considered rejecting invalid inputs with generic error messages. Chose specific, actionable error messages: "Description too short: 12 words. Minimum recommended: 50 words." This keeps the experience educational even when the merchant submits incomplete data.

---

## Day 8 — Scoring Engine

**Decision: Weighting Formula**
We considered equal weights across all 6 dimensions. Chose weighted scoring after researching which factors most affect AI recommendation rates:
- Product descriptions: 25% (most read by AI agents)
- Policy clarity: 20% (second biggest trust factor)
- FAQ coverage: 18% (directly answers buyer queries AI agents relay)
- Trust signals: 15% (credibility indicator)
- Structured data: 12% (machine-readable attributes)
- Review quality: 10% (supporting signal)

**Decision: Score Thresholds**
- 0–34: Needs Work (red)
- 35–59: Developing (amber)
- 60–79: Good (green)
- 80–100: Excellent (dark green)

Thresholds were set to be honest — most real stores score in the 30–50 range. Inflating scores would reduce merchant trust in the tool.

---

## Day 9 — Documentation

**Decision: What NOT to Build**
We considered adding: user authentication, multi-store comparison, real-time monitoring, mobile app, browser extension. Chose to scope tightly to the core diagnostic + fix loop. Reasoning: a focused tool that does one thing excellently beats a broad tool that does many things poorly. All excluded features are documented as future improvements.

**Decision: Explainability Over Black-Box Scoring**
We deliberately chose to explain every score rather than just showing numbers. Merchants need to understand WHY they scored 34 — not just that they did. Explainability increases trust, reduces confusion, and makes recommendations actionable. This added development time but is core to the product value.

---

## Day 10 — Final Polish & Submission

**Decision: Deployment Platform — Render vs Railway vs Vercel**
We considered Vercel (frontend-focused) and Railway. Chose Render because it supports both Flask backend and PostgreSQL database in one platform, has a free tier suitable for hackathon demos, and has straightforward environment variable management.

**Decision: Demo Video Structure**
We considered a feature walkthrough format. Chose problem-first structure: 30 seconds on the problem (why merchants are invisible to AI), then live demo, then outcome. Reasoning: judges need to feel the problem before they can appreciate the solution. Starting with features assumes they already care.

---

## Summary of Key Tradeoffs

| Decision | What We Gave Up | What We Gained |
|---|---|---|
| Shopify API over manual input | Simpler setup | Real data, deeper analysis |
| Chained prompts over single prompt | Speed (more API calls) | Output quality and debuggability |
| Matplotlib over Recharts | Interactivity | Stability and PDF export capability |
| Weighted scoring over equal weights | Simplicity | Accuracy and merchant relevance |
| Focused scope over broad features | Feature count | Depth and polish on core flow |
| Explainability over speed | Processing time | Merchant trust and actionability |
