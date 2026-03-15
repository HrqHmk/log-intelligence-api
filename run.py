import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.server.server:app",
        host="0.0.0.0",
        port=3001,
        log_level="info",
        reload=True,
    )
