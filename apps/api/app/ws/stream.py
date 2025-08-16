"""WebSocket endpoint for streaming messages."""

from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    """Accept a connection and send a single greeting."""
    await ws.accept()
    await ws.send_text("hello")
    await ws.close()
