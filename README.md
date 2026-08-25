# Python → Django → AI Agent Engineer

A personal learning journey from frontend development to
full-stack Python/Django and AI agent engineering.

This repository contains my practical study notes, exercises,
experiments, and projects as I work toward deeply understanding
the Python/Django/AI codebase I work with.

---

## 🎯 Goal

The goal is not simply to learn Python syntax or complete
tutorials.

I want to be able to:

- Read unfamiliar Python code confidently
- Understand why the code works
- Explain the code without relying on AI
- Debug problems independently
- Understand Django request and database flows
- Understand the architecture of the application
- Build and modify backend features confidently
- Understand the LLM layer underneath AI frameworks
- Eventually contribute to LangChain, LangGraph, and PydanticAI
  work in a meaningful way

> **Understanding is the goal, not just getting working code.**

---

# 🧠 Learning Habits

These are ongoing habits throughout the entire roadmap.
They are not a stage to complete.

### Understand Before Shipping

Don't ship code that I cannot explain.

If AI gives me a solution, I should understand why every
important part exists before using it.

### Close-the-Tab Test

After AI helps me write something important:

1. Close the AI conversation
2. Try to retype the code from memory
3. Identify what I don't understand
4. Learn those concepts
5. Recreate the solution

### Find the Precedent

Before accepting a new pattern suggested by AI:

- Find an existing example in the project
- Understand how the project already solves the problem
- Prefer consistency with the existing architecture

### Confusion Log

Keep track of code and concepts that I used without fully
understanding.

The confusion log becomes a personal curriculum.

📄 [`notes/confusion-log.md`](notes/confusion-log.md)

### Use the Debugger

Learn to understand what the application is actually doing.

Practice:

- `breakpoint()`
- Django Debug Toolbar
- Django Extensions
- Inspecting variables
- Inspecting QuerySets
- Stepping through requests

### Scratchpad Practice

Use disposable `scratchpad.py` files for experiments.

The goal is to:

- Try things
- Break things
- Inspect the result
- Fix them
- Run them again

---

# 🗺️ Learning Roadmap

## 🐍 Stage 1 — Python for Real

**Status:** 🟢 In Progress

Build the Python fundamentals required to understand the
existing Django codebase.

### Core Topics

- [ ] Data Model
- [ ] Functions
- [ ] Classes & Object-Oriented Python
- [ ] Exceptions & Error Handling
- [ ] Modules & Imports
- [ ] Type Hints
- [ ] Decorators
- [ ] Generators & `yield`
- [ ] Context Managers
- [ ] `async` / `await`
- [ ] Virtual Environments & Poetry

### Practice

- Rewrite a small utility from the real codebase
- Build a service-style Python class
- Create a custom exception
- Write a generator that yields chunks
- Apply Python concepts to real project code

### Exit Test

> Explain `intelligence/ai_models/services/model_factory.py`
> line by line without skipping anything.

📂 [`stage-1-python/`](stage-1-python/)

---

# 🌐 Stage 2 — Django

**Status:** ⚪ Not Started

Understand how Django works and how the application is
structured.

### Core Topics

- [ ] Request lifecycle
- [ ] URL routing
- [ ] Views
- [ ] Django ORM
- [ ] QuerySets
- [ ] Lazy QuerySets
- [ ] `filter()` / `exclude()` / `get()`
- [ ] `first()` / `exists()`
- [ ] `select_related`
- [ ] `prefetch_related`
- [ ] N+1 queries
- [ ] `annotate()` / `aggregate()`
- [ ] `F()` / `Q()`
- [ ] Models
- [ ] Model managers
- [ ] Migrations
- [ ] Forms
- [ ] Templates
- [ ] Settings & environments
- [ ] Admin
- [ ] Signals
- [ ] Project's DDD structure

### Practice

- Trace a request end-to-end
- Add a model field
- Generate and inspect a migration
- Add an admin entry
- Build a small view
- Build an HTMX-powered template
- Find and reduce unnecessary database queries

### Exit Test

> Add a small feature to the project involving a model,
> migration, admin, view, and HTMX template.

📂 [`stage-2-django/`](stage-2-django/)

---

# ⚙️ Stage 3 — Backend Around Django

**Status:** ⚪ Not Started

Understand the infrastructure surrounding the Django application.

### Core Topics

- [ ] PostgreSQL
- [ ] Joins
- [ ] Indexes
- [ ] `EXPLAIN ANALYZE`
- [ ] Transactions
- [ ] Connection pooling
- [ ] pgvector
- [ ] Celery
- [ ] Celery tasks
- [ ] Workers
- [ ] Brokers
- [ ] Retries
- [ ] Idempotency
- [ ] Redis
- [ ] Channels
- [ ] WebSockets
- [ ] ASGI vs WSGI
- [ ] HTMX
- [ ] Testing
- [ ] Mocking external APIs
- [ ] Git workflow

### Practice

- Move a slow operation into Celery
- Add proper task retries
- Monitor the task in Flower
- Find and fix an N+1 query
- Mock an external API in a test

### Exit Tests

- Move a slow operation to Celery and verify it runs
- Find and fix a real N+1 query
- Write a test that mocks an external API

📂 [`stage-3-backend/`](stage-3-backend/)

---

# 🤖 Stage 4 — LLM Fundamentals

**Status:** ⚪ Not Started

Understand LLMs at the SDK and API level before depending
on AI frameworks.

### Core Topics

- [ ] Raw OpenAI SDK
- [ ] Messages and roles
- [ ] Model parameters
- [ ] Tokens
- [ ] Token usage
- [ ] Context windows
- [ ] LLM cost
- [ ] Streaming
- [ ] Structured output
- [ ] JSON output
- [ ] Tool/function calling
- [ ] Embeddings
- [ ] Cosine similarity
- [ ] Vector search
- [ ] pgvector
- [ ] RAG
- [ ] Chunking
- [ ] Retrieval quality
- [ ] Prompt engineering
- [ ] Rate limits
- [ ] Timeouts
- [ ] Retries
- [ ] Backoff
- [ ] Hallucination
- [ ] Prompt injection
- [ ] Multi-provider LLMs

### Practice

Build a `scratchpad.py` that:

1. Calls an LLM directly
2. Streams the response
3. Produces structured JSON
4. Parses the result
5. Creates embeddings
6. Compares similarity between two strings

### Exit Test

> Explain why the project uses model routing and what would
> happen without it.

📂 [`stage-4-llm/`](stage-4-llm/)

---

# 🧱 Stage 5 — Pydantic

**Status:** ⚪ Not Started

Understand typed data validation and structured LLM output.

### Core Topics

- [ ] `BaseModel`
- [ ] `Field()`
- [ ] Field constraints
- [ ] Field descriptions
- [ ] Aliases
- [ ] `field_validator`
- [ ] `model_validator`
- [ ] `model_validate()`
- [ ] `model_dump()`
- [ ] `model_dump_json()`
- [ ] Nested models
- [ ] `Optional`
- [ ] `Union`
- [ ] `Literal`
- [ ] Enums
- [ ] `ValidationError`
- [ ] Pydantic v2

### Key Concept

> Structured LLM output = an expected schema + model output
> validated against that schema.

### Exit Test

> Define a Pydantic model for a candidate assessment result,
> get an LLM to produce the data, validate it, and handle
> validation failures.

📂 [`stage-5-pydantic/`](stage-5-pydantic/)

---

# 🧠 Stage 6 — AI Agent Frameworks

**Status:** ⚪ Not Started

Learn the frameworks only after understanding the layers
underneath them.

---

## LangChain

- [ ] Chat models
- [ ] Prompt templates
- [ ] Output parsers
- [ ] LCEL
- [ ] Retrievers
- [ ] Document loaders
- [ ] Text splitters
- [ ] Vector stores
- [ ] Message history
- [ ] Existing LangChain POC

📂 [`stage-6-agent-frameworks/01-langchain/`](stage-6-agent-frameworks/01-langchain/)

---

## LangGraph

- [ ] Agent as a state graph
- [ ] State
- [ ] State schema
- [ ] Nodes
- [ ] Edges
- [ ] Conditional edges
- [ ] Cycles
- [ ] Checkpointing
- [ ] Persistence
- [ ] Human-in-the-loop
- [ ] Streaming
- [ ] Django integration

### Architecture Questions

- Where does graph state live?
- How is state persisted?
- Does Django manage the state?
- Does PostgreSQL manage it?
- Does Redis manage it?
- Should the graph run inside a view?
- Should it run as a Celery task?

📂 [`stage-6-agent-frameworks/02-langgraph/`](stage-6-agent-frameworks/02-langgraph/)

---

## PydanticAI

- [ ] `Agent`
- [ ] System prompts
- [ ] Models
- [ ] Result types
- [ ] Dependency injection
- [ ] `deps_type`
- [ ] Tools
- [ ] Streaming
- [ ] Async agents
- [ ] Retries
- [ ] Validation-driven correction

📂 [`stage-6-agent-frameworks/03-pydantic-ai/`](stage-6-agent-frameworks/03-pydantic-ai/)

---

# 🏁 Final Milestones

The roadmap is complete when I can perform these tasks
without depending on AI to write the implementation.

- [ ] Add a model + migration + admin + view + HTMX template
- [ ] Find and fix an N+1 query
- [ ] Move a slow operation into Celery with retries
- [ ] Verify a Celery task in Flower
- [ ] Write a test that mocks an OpenAI call
- [ ] Build a typed LLM feature returning a validated Pydantic object
- [ ] Explain a design decision in `model_factory.py`
- [ ] Disagree with an existing design decision and explain why

> **The real finish line is not being able to recite the
> architecture. It is being able to critique it.**

---

# 📚 Study Method

My target study ratio:

- **60%** — Building and practicing
- **20%** — Reading the existing codebase
- **20%** — Structured learning

### Learning Loop

```text
Learn
  ↓
Practice
  ↓
Apply to real code
  ↓
Explain
  ↓
Document
  ↓
Commit
```

---

# 🤖 Using AI While Learning

### ✅ Good uses

Ask AI:

- "Explain why this code does X."
- "What is happening in this function?"
- "What are the trade-offs between A and B?"
- "Why does Django behave this way?"
- "Review the code I wrote."
- "Give me a hint without writing the solution."

### ❌ Avoid during study

- "Write this feature for me."
- "Implement the whole task."
- "Fix everything in this file."
- Copying generated code without understanding it.

> **AI should accelerate understanding, not replace it.**

---

# 📝 Progress Log

| Date | Stage | What I learned / built | Still confused about |
|---|---|---|---|
| 2026-08-26 | Stage 1 | Started Python Data Model | |

---

# ❓ Confusion Log

Anything I use or ship without fully understanding goes here.

See:

📄 [`notes/confusion-log.md`](notes/confusion-log.md)

---

# 📂 Repository Structure

```text
python-django-learning/
│
├── README.md
│
├── stage-1-python/
├── stage-2-django/
├── stage-3-backend/
├── stage-4-llm/
├── stage-5-pydantic/
├── stage-6-agent-frameworks/
│
├── notes/
│   ├── learning-log.md
│   └── confusion-log.md
│
└── projects/
```

Each stage contains its own detailed README and practical
exercises.

---

# 🚀 Long-Term Goal

Frontend → Full-Stack Python/Django → AI Agent Engineer

The goal is to understand the entire stack:

```text
Frontend
   ↓
HTMX / Templates
   ↓
Django
   ↓
Services
   ↓
ORM
   ↓
PostgreSQL / Redis
   ↓
Celery / Channels
   ↓
LLM APIs
   ↓
Pydantic
   ↓
LangChain / LangGraph / PydanticAI
   ↓
AI Agent Systems
```

> **Learn the foundations. Understand the system. Then build
> on top of it.**
