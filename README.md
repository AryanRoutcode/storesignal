# StoreSignal 🔍
### Understand how AI shopping agents see your Shopify store. Fix gaps. Get recommended.

> **Kasparro Agentic Commerce Hackathon 2026 — Track 5: AI Representation Optimizer**

---

## The Problem

AI shopping agents (ChatGPT, Google AI, Perplexity) now recommend products directly inside conversations — without sending users to websites. These agents read store data: product descriptions, policies, reviews, and metadata. If that data is vague, incomplete, or contradictory, the AI either skips the merchant or misrepresents them.

**Merchants have zero visibility into how AI agents perceive them. StoreSignal fixes that.**

---

## What StoreSignal Does

StoreSignal is a merchant intelligence platform that:

1. **Diagnoses** — Connects to a Shopify store and analyzes how AI agents currently perceive it
2. **Scores** — Generates an AI Readiness Score (0–100) across 6 dimensions
3. **Detects** — Identifies ambiguity, missing information, and weak trust signals
4. **Fixes** — AI rewrites vague descriptions, unclear policies, and generates store-specific FAQs
5. **Shows** — Before vs. After comparison showing exactly how AI perception improves

---

## Demo Video

▶️ [Watch the demo](https://drive.google.com/file/d/1oy3CgAnZLMQnR6nHkUV4JEl2OgvNSNld/view?usp=drivesdk)

---

## Screenshots

### AI Readiness Dashboard
![Dashboard](screenshots/dashboard.png)

### AI Perception Gap
![Perception Gap](screenshots/perception_gap.png)

### Before vs After Optimization
![Before After](screenshots/before_after.png)

### Ranked Action Plan
![Action Plan](screenshots/action_plan.png)

---

## How It Works

```
Merchant connects Shopify store (OAuth)
        ↓
System fetches products, policies, FAQs, reviews, metadata
        ↓
Deterministic Audit Engine
(missing fields, policy completeness, schema validation)
        ↓
OpenAI Semantic Analysis
(ambiguity detection, AI perception simulation, rewrite generation)
        ↓
Hybrid Scoring Engine
(AI Readiness Score, Trust Score, Recommendation Confidence)
        ↓
Merchant Dashboard
(score, perception gap, before/after, ranked action plan)
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend | Python + Flask |
| AI Layer | OpenAI API |
| Database | PostgreSQL + SQLAlchemy |
| Store Data | Shopify Admin API |
| Charts | Matplotlib |
| Deployment | Render |

---

## AI vs Deterministic Logic

| Deterministic (Code Rules) | AI (OpenAI API) |
|---|---|
| Missing field detection | Ambiguity analysis |
| Policy completeness checks | AI perception simulation |
| Schema/metadata validation | Rewrite suggestions |
| Scoring calculations | Recommendation confidence |
| KPI aggregation | Contextual reasoning |

---

## Project Structure

```
storesignal/
│
├── README.md
├── DECISION_LOG.md
├── CONTRIBUTION.md
│
├── docs/
│   ├── product_document.pdf
│   └── technical_document.pdf
│
├── backend/
│   ├── app.py
│   ├── routes/
│   └── services/
│       ├── shopify_service.py
│       ├── scoring_engine.py
│       ├── openai_service.py
│       ├── audit_engine.py
│       ├── fallback_handler.py
│       └── analytics_engine.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── screenshots/
```

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL
- Shopify Partner account
- OpenAI API key

### Backend Setup

```bash
# Clone the repo
git clone https://github.com/AryanRoutcode/storesignal.git
cd storesignal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Set environment variables
cp .env.example .env
# Fill in: OPENAI_API_KEY, SHOPIFY_API_KEY, DATABASE_URL

# Run database migrations
flask db upgrade

# Start backend
cd backend
flask run
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

### Environment Variables

```
OPENAI_API_KEY=your_openai_key
SHOPIFY_API_KEY=your_shopify_key
SHOPIFY_API_SECRET=your_shopify_secret
DATABASE_URL=postgresql://localhost/storesignal
FLASK_SECRET_KEY=your_secret_key
```

---

## What the Judges Will See

- **AI Readiness Score** — overall score out of 100
- **Trust Score** — how credible the store appears to AI agents
- **Recommendation Confidence** — likelihood of AI recommending this store
- **AI Perception Simulation** — exactly how an AI agent would describe the store
- **Ambiguity Detection** — specific vague phrases flagged with reasoning
- **Before vs. After** — rewritten descriptions, policies, and generated FAQ
- **Ranked Action Plan** — top fixes sorted by business impact

---

## Team

| Name | Role |
|---|---|
| Aryan Rout | Product Thinking, AI Layer, Documentation, Demo |
| Sambhav Sahoo | Backend Architecture, Shopify Integration, Audit Engine, Database, Deployment |

---

## Submission

- **Hackathon:** Kasparro Agentic Commerce Hackathon 2026
- **Track:** Track 5 — AI Representation Optimizer
- **Deadline:** 20th May 2026, 11:59 PM IST
- **Demo Video:** [Link](YOUR_YOUTUBE_LINK_HERE)
