from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.server.connection_manager import ConnectionManager


router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You said: {data}", websocket)
            await manager.broadcast(f"{data}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast("A user disconnected")