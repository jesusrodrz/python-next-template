import uvicorn
from fastapi import FastAPI
from shared.environment import Environment
app = FastAPI()


@app.get("/")
async def main():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level= 'debug' if Environment.DEBUG else None)