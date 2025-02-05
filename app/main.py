"""
This module defines the main entry point for the application.
"""

from fastapi import FastAPI
from app.api.endpoints import petit_lenormand

app = FastAPI(title="Tarot API", version="1.0.0")

app.include_router(petit_lenormand.router, prefix="/api/v1")
