from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.app.api.health import router as health_router
from backend.app.api.profile import router as profile_router
from backend.app.api.skills import router as skills_router
from backend.app.api.experience import router as experience_router
from backend.app.api.projects import router as projects_router
from backend.app.api.education import router as education_router
from backend.app.api.ask import router as ask_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Ask Abhinav API",
    description="Backend API for Abhinav's AI-powered developer portfolio",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "frontend"

app.add_middleware(
    CORSMiddleware,
#    allow_origins=[
#       "http://127.0.0.1:5500",
#       "http://localhost:5500",
#   ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/css",
    StaticFiles(directory=FRONTEND_DIR / "css"),
    name="css",
)

app.mount(
    "/js",
    StaticFiles(directory=FRONTEND_DIR / "js"),
    name="js",
)

app.mount(
    "/assets",
    StaticFiles(directory=FRONTEND_DIR / "assets"),
    name="assets",
)

@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse(FRONTEND_DIR / "index.html")


app.include_router(
    health_router,
    prefix="/api",
)

app.include_router(
    profile_router,
    prefix="/api",
)

app.include_router(
    skills_router,
    prefix="/api",
)

app.include_router(
    experience_router,
    prefix="/api",
)

app.include_router(
    projects_router,
    prefix="/api",
)

app.include_router(
    education_router,
    prefix="/api",
)

app.include_router(
    ask_router, 
    prefix="/api"
)