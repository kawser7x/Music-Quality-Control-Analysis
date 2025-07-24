from fastapi import FastAPI
from app.routes import upload

app = FastAPI(title="TrackVerify - Music QC")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def read_root():
    return {"msg": "Welcome to TrackVerify – Music Quality Control Automation"}
