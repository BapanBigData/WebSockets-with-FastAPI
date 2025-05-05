from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.server.connection_manager import ConnectionManager


router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You said: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} has left the chat")