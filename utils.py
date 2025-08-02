from datetime import datetime

def export_chat(history):
    if not history:
        return "No chat history to export."
    export = f"# Chat Export - {datetime.now()}\n\n"
    for i, (user, ai) in enumerate(history, 1):
        export += f"## Message {i}\n**User:** {user}\n\n**AI:** {ai}\n\n---\n"
    return export

def interpret_error(e, model):
    msg = str(e).lower()
    if "api_key" in msg or "authentication" in msg:
        return "🔑 API key issue. Please verify credentials."
    if "quota" in msg:
        return "💳 Quota exceeded. Check billing."
    if "rate_limit" in msg:
        return "⏱️ Rate limited. Try again shortly."
    if "model" in msg:
        return f"🤖 Model Error: {model} might be invalid."
    return f"⚠️ Error: {str(e)}"
