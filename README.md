# 🧠 WebSockets with FastAPI — Server & Client Separation

This project demonstrates how to implement **WebSocket-based real-time communication** using **FastAPI**. It showcases a clear separation between backend (server logic) and frontend (client logic) — ideal for learners and developers exploring modern WebSocket APIs in Python.

---

## 🚀 Features

- ✅ FastAPI-powered WebSocket backend
- ✅ JavaScript+HTML frontend with dynamic client ID
- ✅ Clean separation of `server/` and `client/` logic
- ✅ Broadcast messaging between multiple clients
- ✅ Unique client identifiers per session
- ✅ Easy to extend into real-time chat apps or dashboards

---


---

## 💡 How It Works

1. A client opens the app at `http://localhost:8000/`
2. A unique `client_id` is generated in the browser
3. The browser connects to `ws://localhost:8000/ws/{client_id}`
4. Messages are:
   - Shown back to the sender: `You said: ...`
   - Broadcast to all others: `Client #1234 says: ...`
5. On disconnect, others are notified: `Client #1234 has left the chat`

---

## 📦 Installation & Setup

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/your-username/WebSockets_With_FastAPI.git
cd WebSockets_With_FastAPI


🐍 2. Create and Activate a Virtual Environment

python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


📦 3. Install Dependencies
pip install -r requirements.txt


▶️ Run the App

🖥️ 1. Start the FastAPI Server
uvicorn app.main:app --reload


🌐 2. Open the Frontend in a Browser
http://localhost:8000/
