from fastapi import FastAPI
from app.main.routes.request_log_routes import request_log_routes

app = FastAPI()
app.include_router(request_log_routes)
@app.get("/")
async def root():
    return {"message": "API is running!"}
