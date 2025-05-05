from fastapi import WebSocket
from typing import List


class ConnectionManager:
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def send_personal_message(self, msg: str, websocket: WebSocket):
        await websocket.send_text(f"Personal: {msg}")
    
    async def broadcast(self, msg: str):
        for connection in self.active_connections:
            await connection.send_text(f"Broadcast: {msg}")

