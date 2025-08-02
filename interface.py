import gradio as gr
from ai_engine import generate_response
from presets import get_prompt
from utils import export_chat

def create_interface():
    with gr.Blocks(css="assets/style.css", title="AI Chat Application") as demo:

        with gr.Column(elem_id="header-section"):
            gr.Markdown("## <center>⚡ AI Chat Application</center>", elem_id="title")

        chatbot = gr.Chatbot(elem_id="chat-window")

        with gr.Row(elem_id="chat-controls"):
            with gr.Column(scale=8):
                msg = gr.Textbox(placeholder="Ask anything...", show_label=False, elem_id="input-field")
            with gr.Column(scale=2):
                send_btn = gr.Button("➤", elem_id="send-btn")

        with gr.Accordion("⚙️ Advanced Settings", open=False):
            model = gr.Dropdown(choices=["gpt-3.5-turbo", "gpt-4"], label="Model", value="gpt-3.5-turbo")
            sys_prompt = gr.Textbox(label="System Prompt", value="You are a helpful assistant.")
            temp = gr.Slider(minimum=0, maximum=1.5, step=0.1, label="Temperature", value=0.7)

        def respond(user_message, history, model, sys_prompt, temp):
            reply, updated = generate_response(user_message, model, sys_prompt, history)
            return updated, ""

        send_btn.click(fn=respond, inputs=[msg, chatbot, model, sys_prompt, temp], outputs=[chatbot, msg])

    return demo
