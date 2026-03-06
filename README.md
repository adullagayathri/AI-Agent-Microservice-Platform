# AI-Agent-Microservice-Platform

**Cloud-Native Distributed Runtime for Autonomous AI Agents**

---

## Overview
The **AI Agent Microservice Platform** is a containerized, distributed system designed to orchestrate autonomous AI agents at scale.  
Built with **FastAPI, Docker, and Redis**, this platform simulates concurrent agent execution, incorporates health monitoring, retry logic, and structured logging, and enables reproducible multi-agent experiments.

This project demonstrates **cloud-native architecture, distributed orchestration, and scalable AI agent management**, aligned with modern Core AI engineering practices.

---

## Features

- Runtime orchestration of multiple autonomous AI agents  
- Simulates **50+ concurrent agents**  
- Centralized **health checks and retry logic**  
- Structured logging for reproducible evaluation  
- Containerized microservices for **scalable deployment**  
- Modular design supporting **multi-agent pipelines**

---
## Project Structure
```
AI-Agent-Microservice-Platform/
├── orchestrator/
│   ├── main.py          # Orchestrator entrypoint
│   ├── scheduler.py     # Task scheduling logic
│   ├── health_monitor.py# Agent health checks
│   └── logger.py        # Structured logging
├── agents/
│   ├── agent_worker.py  # Agent microservice logic
│   └── tasks.py         # Example AI tasks agents can perform
├── simulation.py        # Script to simulate 50+ agents concurrently
├── docker-compose.yml   # Multi-container orchestration
├── Dockerfile           # Base Dockerfile for services
└── README.md            # Your Markdown
```
## Architecture

```
+----------------------+       +----------------------+
|     Orchestrator     |<----->|      Redis Queue     |
|  - Scheduler         |       +----------------------+
|  - Health Monitor    |                 ^
|  - Logger            |                 |
+----------------------+                 |
             |                            |
             v                            |
+----------------------+       +----------------------+
|    Agent Service 1   |       |    Agent Service N   |
|    - Task Handler    |       |    - Task Handler    |
+----------------------+       +----------------------+
```

**Orchestrator**: Coordinates agent execution, scheduling, health checks, and logging  
**Agents**: Independent microservices simulating AI tasks  
**Redis**: Message queue for communication and task dispatch 

---

## Tech Stack

- **Backend / Orchestrator:** FastAPI, Python  
- **Microservices & Concurrency:** asyncio, threading  
- **Queue / Messaging:** Redis  
- **Containerization:** Docker, Docker Compose  
- **Logging / Monitoring:** JSON structured logging  
- **Simulation:** Concurrent execution of multiple agents  

---
## Requirements

- Python 3.10+
- Docker
- Docker Compose
- Redis

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/<gayathriadulla>/AI-Agent-Microservice-Platform.git
cd AI-Agent-Microservice-Platform
```

2. Start the platform using Docker Compose:
```bash
docker compose up --build
```
3. Access orchestrator API:
```bash
http://localhost:8000/status
```
## Usage

Start orchestrator: orchestrator/main.py

Run agent workers: agents/agent_worker.py

Monitor logs in logs/ or via API endpoints

Simulate 50+ agents concurrently using the included simulation.py script

## Example Output

Running the simulation script generates concurrent agent tasks:

```
python simulation.py
```

Output:

```
Task sent
Task sent
Task sent
Task sent
Task sent
```

Agent worker logs:

```
Agent received task
Processing task...
Task completed
```

API health check:

```
GET /status

{
  "system": "running",
  "redis": "connected",
  "agents": "active"
}
```

## Demo

Simulates 50+ concurrent agents performing tasks

Health monitoring reports real-time agent status

Centralized structured logs stored for reproducible experiments

## Contributing

This project is intended as a demonstration of cloud-native distributed AI agent systems. Contributions for improved scalability, additional agent types, and advanced orchestration are welcome.
## Future Improvements

- Distributed agent scaling using Kubernetes
- Agent priority scheduling
- Prometheus + Grafana monitoring
- Integration with real AI models (LLMs, computer vision pipelines)
- Multi-agent collaboration workflows


