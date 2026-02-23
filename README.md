# ATHAR — Digital Twin

> *"built because time is precious and most people are chomu."*

---

Athar is not a chatbot. It's a localized AI mirror — designed to think, talk, and react with a specific psychological edge. It understands the dread of a matchbox college, high-burst engineering logic, and the necessity of a Japan exit plan.

---

## Philosophy

| Vector | Reality |
|---|---|
| **The Dread** | Total disgust for the NIT Srinagar environment |
| **The Exit** | Financial independence. Italy or Japan. No bragging, just autonomy |
| **The Logic** | Show, don't tell. Work in bursts. AI-assisted because manual is prehistoric |
| **The Vibe** | lowercase only. zero emojis. dry humor. zero patience for invertebrate jellyfish |

---

## Tech Stack

```
Intelligence  →  Ollama / llama3.2     (100% local, zero latency, total privacy)
Backend       →  Python + Flask         (the nervous system)
Frontend      →  Neon-green dark UI     (syne + dm mono typography)
Infrastructure→  Docker + Compose       (containerized logic)
```

---

## Setup

**1. Clone**

```bash
git clone https://github.com/atharbilal/athar.git
cd athar
```

**2. Start containers**

```bash
docker-compose up -d --build
```

**3. Pull the model (first time only)**

```bash
docker exec -it athar-ollama-1 ollama pull llama3.2
```

**4. Open**

```
http://localhost:5001
```

---

## Structure

```
athar/
├── app.py              # the brain — logic, personality, flask
├── static/
│   └── index.html      # the interface — neon-on-black ui
├── Dockerfile          # the cage
├── docker-compose.yml  # the orchestrator
├── requirements.txt    # the dependencies
└── README.md
```

---

## Behavioral Protocols

```
LOWERCASE ONLY  →  no exceptions
STAY REAL       →  smile on the outside, internally disgusted by incompetence
PUNCHY          →  if it fits in 5 words, don't use 10
BRUTAL          →  if you're being a chomu, it will tell you
```

---

## Status

localized and responding. more to come, inshallah.

---

*built by athar.*
