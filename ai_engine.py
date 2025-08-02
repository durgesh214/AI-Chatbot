import gradio as gr
import openai

openai.api_key = "your_api_key"

def generate_response(message, model, system_prompt, chat_history):
    print(f"Received message: {message}")  # Debug print
    if not message or not message.strip():
        return "Please enter a message.", chat_history

    # Add user message to chat history immediately
    chat_history = chat_history + [[message, None]]

    messages = [{"role": "system", "content": system_prompt}]
    for user_msg, ai_msg in chat_history:
        if user_msg: messages.append({"role": "user", "content": user_msg})
        if ai_msg: messages.append({"role": "assistant", "content": ai_msg})

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=2000,
            temperature=0.7,
            top_p=0.9
        )
        content = response.choices[0].message.content
        return content, chat_history[:-1] + [[message, content]]  # Update with AI response
    except Exception as e:
        return f"Error: {e}", chat_history

def create_interface():
    with gr.Blocks(css="assets/style.css", title="AI Chat Application") as demo:

        with gr.Column(elem_id="header-section"):
            gr.Markdown("## <center>⚡ AI Chat Application</center>", elem_id="title")

        chatbot = gr.Chatbot(elem_id="chat-window")

        with gr.Row(elem_id="chat-controls"):
            with gr.Column(scale=8):
                msg = gr.Textbox(placeholder="Ask anything...", show_label=False, elem_id="input-field", lines=1)
            with gr.Column(scale=2):
                send_btn = gr.Button("➤", elem_id="send-btn")

        with gr.Accordion("⚙️ Advanced Settings", open=False):
            model = gr.Dropdown(choices=["gpt-3.5-turbo", "gpt-4"], label="Model", value="gpt-3.5-turbo")
            sys_prompt = gr.Textbox(label="System Prompt", value="You are a helpful assistant.")
            temp = gr.Slider(minimum=0, maximum=1.5, step=0.1, label="Temperature", value=0.7)

        msg.submit(fn=generate_response, inputs=[msg, model, sys_prompt, chatbot], outputs=[chatbot, msg], _js="() => { document.getElementById('input-field').value = ''; return true; }")  # Clear input and submit
        send_btn.click(fn=generate_response, inputs=[msg, model, sys_prompt, chatbot], outputs=[chatbot, msg])  # Click button

    return demo