# DataSherpa AI

**Your AI data analyst — with answers you can trust.**
*Navigate data. Discover answers. Make better decisions.*

Upload a sales file (CSV or Excel), ask a business question in plain English — *"Why did sales
drop last month?"* — and get a formal report: key numbers, charts, possible reasons and next
steps. Every number is calculated from your data, **checked a second way**, and nothing is final
until **you approve** it.

![DataSherpa AI infographic](infographic.png)

## 🎥 Demo

[▶ Watch the demo video](demo/DataSherpa-AI-demo.mp4) — about 4 minutes, from sign-in to the
approved report, narrated in English.

## What makes it different

- **The AI never does the maths** — numbers come only from executed calculations.
- **Checked twice** — key numbers are recomputed independently; a mismatch blocks the answer.
- **Data Quality Guardian** — duplicates, wrong dates and odd values are found and explained first.
- **Facts vs. possible reasons** — guesses are clearly labelled "not proven".
- **Human in control** — the AI reviewer and the person's approval are separate; only a click approves.
- **Formal report** with KPI cards and charts, downloadable as **PDF** or a styled **Excel** report.

## How it's built

- **Smart router** — cached answers (0 AI tokens), a verified Python engine for standard questions,
  and a full AI agent loop only for custom questions.
- **AI agent team** — Planner → Coder → Sandbox → Verifier → Reviewer → Advisor → human approval,
  built with **Microsoft Agent Framework + OpenAI**.
- **Safe execution** — AI-written code runs in a locked-down **Docker** sandbox: no internet,
  non-root, memory/CPU/time limits.
- **Hard limits in code** — max 3 attempts, 12 agent messages, time and token budgets.
- **Security** — bcrypt passwords, rotating httpOnly refresh tokens, one-time password-reset links,
  rate limiting, per-user data isolation.

**Stack:** Python 3.11 · FastAPI · pandas · PostgreSQL + SQLAlchemy · React + TypeScript ·
Chakra UI · Docker · Microsoft Agent Framework · OpenAI

## Results (demo data)

| Measure | Result |
|---------|--------|
| Known answers correct | 24 / 24 |
| Verification checks passed | 84 / 84 |
| Reproducible runs | 6 / 6 |
| Automated tests | 260+ |

## More

- 📄 [Technical guide (PDF)](docs/TECHNICAL_GUIDE.pdf) — how it works, guardrails, error handling.
- Source code is private; a walkthrough is available on request.

*All data shown is demo data.*
