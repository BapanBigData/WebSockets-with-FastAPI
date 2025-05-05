import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.server.websocket_server import router as websocket_router


app = FastAPI()


client = os.path.join(os.path.dirname(__file__), "client", "index.html")


@app.get("/")
async def get_index():
    return FileResponse(client)


app.include_router(websocket_router)
