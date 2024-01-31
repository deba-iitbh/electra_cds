import uvicorn
from src import config

if __name__ == "__main__":
    uvicorn.run(
        "src:app",
        reload=True,
        host=config.HOST,
        port=config.PORT,
        log_level="info",
    )
