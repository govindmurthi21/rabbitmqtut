from src.consumers.consumer import run as run_consumers
from fastapi import FastAPI
from src.apis import web_api
import uvicorn

app = FastAPI()

app.include_router(web_api.router)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    run_consumers()

if __name__ == "__main__":
    main()
