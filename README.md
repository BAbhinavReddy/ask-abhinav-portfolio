# Ask Abhinav — AI Developer Portfolio

An AI-powered developer portfolio built with Python, FastAPI, PostgreSQL, LangChain, Google Gemini, and Pinecone.

The application combines a recruiter-focused portfolio website with an AI assistant that can answer questions about my professional experience, technical skills, education, and projects using Retrieval-Augmented Generation (RAG).

## Live Application

**Portfolio:** https://abhinavreddyb.com

---

## Overview

Ask Abhinav is a full-stack AI-powered developer portfolio designed to make it easy for recruiters and hiring managers to learn about my technical background.

Instead of navigating through multiple pages or documents, visitors can explore my experience, skills, education, and projects through a single-page interface and interact directly with an AI assistant.

The AI assistant uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from a curated portfolio knowledge base before generating an answer with Google Gemini.

The application is deployed on AWS EC2 using Docker and Nginx, with HTTPS enabled through Cloudflare. GitHub Actions automates testing, Docker builds, and production deployment.

---

## Key Features

- Single-page recruiter-focused portfolio
- AI-powered "Ask Abhinav" assistant
- Retrieval-Augmented Generation (RAG)
- Semantic search using vector embeddings
- Pinecone vector database
- Google Gemini LLM integration
- LangChain-based AI pipeline
- PostgreSQL-backed portfolio content
- FastAPI REST API
- SQLAlchemy database layer
- Pydantic request and response validation
- Responsive frontend
- Interactive experience, education, skills, and project sections
- Automated testing with pytest
- Dockerized application
- AWS EC2 deployment
- Nginx reverse proxy
- HTTPS
- Cloudflare integration
- GitHub Actions CI/CD
- Automatic deployment after pushes to `main`

---

# Architecture

```text
                         ┌─────────────────────┐
                         │      Recruiter      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   HTML / CSS / JS   │
                         │      Frontend       │
                         └──────────┬──────────┘
                                    │
                              REST / JSON
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │       Backend       │
                         └──────┬─────────┬────┘
                                │         │
                       Portfolio │         │ Ask Abhinav
                                │         │
                                ▼         ▼
                         ┌──────────┐  ┌──────────────┐
                         │PostgreSQL│  │   LangChain  │
                         └──────────┘  └──────┬───────┘
                                              │
                                              ▼
                                      ┌──────────────┐
                                      │   Pinecone   │
                                      │ Vector Search│
                                      └──────┬───────┘
                                             │
                                      Relevant Context
                                             │
                                             ▼
                                      ┌──────────────┐
                                      │Google Gemini │
                                      │     LLM      │
                                      └──────┬───────┘
                                             │
                                             ▼
                                      Generated Answer
                                             │
                                             ▼
                                      Frontend Chat UI
```

---

# AI / RAG Architecture

The Ask Abhinav assistant follows a Retrieval-Augmented Generation workflow.

```text
User Question
      │
      ▼
POST /api/ask
      │
      ▼
FastAPI
      │
      ▼
LangChain
      │
      ▼
Generate Query Embedding
      │
      ▼
Pinecone Vector Search
      │
      ▼
Retrieve Relevant Documents
      │
      ▼
Construct Prompt with Context
      │
      ▼
Google Gemini
      │
      ▼
AI Response
      │
      ▼
Frontend Chat Interface
```

The RAG pipeline allows the assistant to answer questions using information from a controlled portfolio knowledge base rather than relying only on the LLM's general knowledge.

## Knowledge Base

The AI assistant uses curated knowledge files covering:

- Professional profile
- Technical skills
- Work experience
- Education
- Projects
- CareerFlow AI API
- Gemini Coding Agent
- Ask Abhinav portfolio

The knowledge documents are split into smaller chunks before being converted into vector embeddings and stored in Pinecone.

## Embedding Pipeline

```text
Knowledge Files
      │
      ▼
Text Extraction
      │
      ▼
Recursive Character Text Splitter
      │
      ▼
Text Chunks
      │
      ▼
Gemini Embeddings
      │
      ▼
Pinecone
```

The application uses Google's `gemini-embedding-001` embedding model for generating vector representations of the portfolio knowledge.

---

# Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Responsive UI
- REST API integration

## Backend

- Python 3.11
- FastAPI
- Pydantic
- SQLAlchemy
- REST APIs
- Swagger / OpenAPI

## Database

- PostgreSQL
- SQLAlchemy ORM
- SQL

## AI / LLM

- Google Gemini API
- LangChain
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Pinecone
- Prompt Engineering
- Structured LLM workflows

## DevOps / Cloud

- AWS EC2
- Docker
- Nginx
- GitHub Actions
- Git
- GitHub
- Linux
- HTTPS
- Cloudflare

## Testing

- pytest
- FastAPI TestClient
- Postman

---

# Project Structure

```text
ask-abhinav/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   │   ├── profile.py
│   │   │   ├── skills.py
│   │   │   ├── experience.py
│   │   │   ├── projects.py
│   │   │   ├── education.py
│   │   │   └── ask.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── profile.py
│   │   │   ├── skill.py
│   │   │   ├── experience.py
│   │   │   ├── project.py
│   │   │   └── education.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── profile.py
│   │   │   ├── skills.py
│   │   │   ├── experience.py
│   │   │   ├── projects.py
│   │   │   ├── education.py
│   │   │   └── ask.py
│   │   │
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   ├── rag_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── pinecone_service.py
│   │   │
│   │   ├── db/
│   │   │   ├── database.py
│   │   │   ├── session.py
│   │   │   └── seed_*.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_health.py
│   │   ├── test_profile.py
│   │   ├── test_skills.py
│   │   ├── test_experience.py
│   │   ├── test_projects.py
│   │   ├── test_education.py
│   │   └── test_ask.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   │
│   ├── index.html
│   │
│   ├── css/
│   │   ├── main.css
│   │   ├── sections.css
│   │   └── chat.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── portfolio.js
│   │   └── chat.js
│   │
│   └── assets/
│
├── knowledge/
│   ├── profile.txt
│   ├── skills.txt
│   ├── experience.txt
│   ├── education.txt
│   ├── careerflow.txt
│   ├── coding_agent.txt
│   └── ask_abhinav.txt
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── .gitignore
└── README.md
```

---

# API Endpoints

## Health Check

```http
GET /api/health
```

Used for application health checks and deployment verification.

## Profile

```http
GET /api/profile
```

Returns professional profile information.

## Skills

```http
GET /api/skills
```

Returns technical skills.

## Experience

```http
GET /api/experience
```

Returns professional experience.

## Projects

```http
GET /api/projects
```

Returns portfolio projects.

## Education

```http
GET /api/education
```

Returns educational background.

## Ask Abhinav

```http
POST /api/ask
```

Accepts a natural-language question and returns an AI-generated response using the RAG pipeline.

Example request:

```json
{
  "question": "What experience does Abhinav have with Python?"
}
```

---

# Database Design

Portfolio information is stored in PostgreSQL rather than being hardcoded directly into the frontend.

The primary entities are:

```text
Profile
   │
   ├── Skills
   ├── Experience
   ├── Projects
   └── Education
```

SQLAlchemy provides the ORM layer between FastAPI and PostgreSQL.

Pydantic schemas provide validation and structured API responses.

Seed scripts are used to initialize portfolio data in development and CI environments.

---

# Deployment Architecture

The application is deployed on AWS EC2 using Docker.

```text
                        Internet
                           │
                           ▼
                       Cloudflare
                           │
                           ▼
                     Nginx :443
                           │
                           ▼
                  Docker Container
                           │
                           ▼
                    FastAPI :8000
                       /        \
                      /          \
                     ▼            ▼
              PostgreSQL      AI Services
                              /          \
                             ▼            ▼
                         Pinecone      Gemini
```

FastAPI runs inside a Docker container and is bound to:

```text
127.0.0.1:8000
```

This keeps the FastAPI port from being directly exposed to the public internet.

Nginx acts as the public reverse proxy and forwards incoming web requests to the FastAPI container.

HTTPS is enabled for the public application.

---

# CI/CD Pipeline

Every push to the `main` branch triggers GitHub Actions.

```text
                         git push
                            │
                            ▼
                     GitHub Actions
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       │
          Install Python                │
                │                       │
                ▼                       │
        Start PostgreSQL                │
                │                       │
                ▼                       │
       Initialize database              │
                │                       │
                ▼                       │
          Seed test data                │
                │                       │
                ▼                       │
           Run pytest                   │
                │                       │
                ▼                       │
         Build Docker image             │
                │                       │
                └───────────┬───────────┘
                            │
                          Success
                            │
                            ▼
                     SSH into EC2
                            │
                            ▼
                       git pull
                            │
                            ▼
                     docker build
                            │
                            ▼
                 Replace old container
                            │
                            ▼
                      Health check
                            │
                            ▼
                      Production
```

The deployment pipeline is designed so that production deployment occurs only after the automated test stage succeeds.

---

# Local Development

## 1. Clone the Repository

```bash
git clone git@github.com:BAbhinavReddy/ask-abhinav-portfolio.git

cd ask-abhinav-portfolio
```

## 2. Create a Virtual Environment

```bash
python3.11 -m venv backend/venv
```

Activate it:

### macOS / Linux

```bash
source backend/venv/bin/activate
```

### Windows

```powershell
backend\venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

## 4. Configure Environment Variables

Create:

```text
backend/.env
```

with:

```env
DATABASE_URL=your_postgresql_connection_string
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

Never commit API keys, database passwords, or production environment files to Git.

## 5. Run the Application

From the project root:

```bash
uvicorn backend.app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger/OpenAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# Running Tests

The automated API test suite can be run with:

```bash
PYTHONPATH=. pytest -v backend/tests
```

The test suite covers:

- Health endpoint
- Profile endpoint
- Skills endpoint
- Experience endpoint
- Projects endpoint
- Education endpoint
- Ask Abhinav endpoint

---

# Docker

## Build the Docker Image

Run from the project root:

```bash
docker build -f backend/Dockerfile -t ask-abhinav .
```

## Run the Container

```bash
docker run -d \
  --name ask-abhinav \
  --restart unless-stopped \
  --env-file backend/.env \
  -p 127.0.0.1:8000:8000 \
  ask-abhinav
```

## Check the Container

```bash
docker ps
```

## Check Application Health

```bash
curl http://127.0.0.1:8000/api/health
```

## Stop the Container

```bash
docker stop ask-abhinav
```

## Remove the Container

```bash
docker rm ask-abhinav
```

---

# Environment Variables

The application requires the following environment variables:

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | PostgreSQL database connection |
| `GOOGLE_API_KEY` | Google Gemini API access |
| `PINECONE_API_KEY` | Pinecone vector database access |

Production environment variables are kept on the EC2 server and are not committed to the repository.

GitHub Actions uses GitHub Secrets for CI-related credentials.

---

# Security

The application follows several basic production security practices:

- API credentials are stored in environment variables.
- Production `.env` files are excluded from Git.
- PostgreSQL is not publicly exposed.
- FastAPI port `8000` is bound to localhost.
- Nginx acts as the public reverse proxy.
- AWS Security Groups control inbound network access.
- A dedicated SSH key is used for GitHub Actions deployment.
- Production secrets remain on the EC2 server.
- HTTPS is enabled for public traffic.

---

# Engineering Highlights

## Backend Engineering

- Designed REST APIs using FastAPI.
- Organized the backend into API routers, schemas, models, services, and database layers.
- Implemented PostgreSQL persistence using SQLAlchemy.
- Used Pydantic for request and response validation.
- Exposed interactive API documentation through Swagger/OpenAPI.
- Implemented automated API testing with pytest.

## AI Engineering

- Integrated Google Gemini for LLM-powered responses.
- Built a Retrieval-Augmented Generation pipeline.
- Implemented semantic document retrieval using vector embeddings.
- Used Pinecone as the vector database.
- Used LangChain to structure the AI workflow.
- Built a portfolio-specific knowledge base for grounded responses.
- Designed the assistant to retrieve relevant context before generating responses.

## Cloud & DevOps

- Containerized the application using Docker.
- Deployed the application to AWS EC2.
- Configured Nginx as a reverse proxy.
- Configured HTTPS for production traffic.
- Implemented GitHub Actions CI/CD.
- Automated testing before deployment.
- Automated Docker image builds.
- Automated production container replacement.
- Added deployment health verification.

---

# Projects Featured

The portfolio currently showcases the following projects:

## Ask Abhinav — AI Developer Portfolio

The current project.

An AI-powered portfolio that combines a recruiter-focused website with a RAG-based conversational assistant.

**Technologies:** Python, FastAPI, PostgreSQL, SQLAlchemy, LangChain, Gemini, Pinecone, JavaScript, Docker, AWS EC2, Nginx, GitHub Actions.

## CareerFlow AI API

A backend API for tracking job applications and using AI to analyze job descriptions and evaluate resume-to-job alignment.

**Technologies:** Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, LangChain, Gemini.

## Gemini Coding Agent

An AI coding assistant built in Python using Gemini function calling.

The agent was designed to interact with files and execute Python code in a controlled environment, including file inspection, file modification, and iterative debugging workflows.

**Technologies:** Python, Google Gemini, Gemini Function Calling, LangChain, LangGraph.

---

# Why This Project?

This project was built to demonstrate practical software engineering and AI engineering skills in a single production-oriented application.

Rather than building a portfolio that only displays static information, the application demonstrates how a modern backend system can combine:

```text
REST APIs
    +
PostgreSQL
    +
AI / LLM
    +
RAG
    +
Vector Search
    +
Docker
    +
AWS
    +
CI/CD
```

The project also demonstrates the complete development lifecycle:

```text
Design
  ↓
Implementation
  ↓
Database Integration
  ↓
AI Integration
  ↓
Testing
  ↓
Containerization
  ↓
Cloud Deployment
  ↓
CI/CD
  ↓
Production
```

---

# Future Improvements

Potential future improvements include:

- Conversation history and session management
- Improved RAG evaluation
- More advanced retrieval strategies
- AI response evaluation and monitoring
- Expanded automated test coverage
- Production observability and logging
- Additional portfolio analytics

---

# Author

## Abhinav Reddy Bobba

**Software Engineer | Python Backend | AI/LLM**

I focus on building backend systems and AI-powered applications using Python, FastAPI, PostgreSQL, and modern LLM technologies.

### Links

- Portfolio: https://abhinavreddyb.com
- GitHub: https://github.com/BAbhinavReddy
- LinkedIn: https://www.linkedin.com/in/abhinav-reddyb/
