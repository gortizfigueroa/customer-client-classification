# Customer Client Classification

Minimal backend implementing a support-ticket classification + suggested-reply pipeline. This repository contains an MVP simulation used for prototyping smart support automation.

## Contents

- [classifier.py](classifier.py) — main demo script implementing the pipeline.
  - Key functions:
    - [`classifier.preprocess`](classifier.py) — text cleaning and language detection
    - [`classifier.classify_ticket`](classifier.py) — mock intent/urgency/product classifier
    - [`classifier.retrieve_knowledge`](classifier.py) — KB retrieval
    - [`classifier.suggest_reply`](classifier.py) — suggestion generation
    - [`classifier.decide_and_dispatch`](classifier.py) — decision to auto-suggest or escalate
    - [`classifier.handle_ticket`](classifier.py) — orchestration for a single ticket
    - [`classifier.main`](classifier.py) — demo entrypoint

## Overview

The pipeline is intentionally simple to serve as a reference implementation for:
- ingest → preprocess → classify → retrieve_context → generate_suggestion → decide_and_dispatch → (auto-send or human)
- Mock KB is held in-memory (`FAQ_KB`) and intents are derived from its keys.

## Quickstart

Run the demo with Python 3:

```bash
python3 classifier.py
```

## Extending this MVP

- Persist labels & metadata: store tickets, classifications, and human corrections in Postgres (or another DB) to enable retraining and audit.
- Replace the in-memory KB with embeddings + a vector store (FAISS / Pinecone / Milvus) for semantic retrieval and better context ranking.
- Integrate an LLM for reply synthesis using retrieval-augmented generation (RAG); keep KB snippets as grounding and add prompt templates.
- Add model training pipelines: dataset versioning, reproducible training scripts, and automated retrain triggers from labeled data.
- Implement a human-in-the-loop UI for quick corrections and feedback collection to improve dataset quality and calibration.
- Enforce safety/compliance checks and redaction before any auto-send (sensitive data detection, PII stripping, policy filters).
- Add telemetry, observability and metrics (confidence calibration, precision/recall by intent, latency) and expose a dashboard.
- Containerize and add infra automation (Docker, CI/CD, IaC) for consistent staging/production deployments.
- Add end-to-end tests, unit tests for pipeline components, and monitoring for data/model drift with scheduled re-evaluations.

