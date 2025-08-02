from datetime import datetime

class ChatManager:
    def __init__(self):
        self.sessions = {}
        self.current_session_id = None

    def create_session(self, name="New Chat", model="gpt-3.5-turbo", system_prompt=""):
        session_id = f"session_{int(datetime.now().timestamp())}"
        self.sessions[session_id] = {
            "name": name,
            "model": model,
            "system_prompt": system_prompt or "You are a helpful assistant.",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": []
        }
        self.current_session_id = session_id
        return session_id

    def get_current(self):
        return self.sessions.get(self.current_session_id)
