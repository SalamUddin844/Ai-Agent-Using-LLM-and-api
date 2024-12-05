import os

from mistralai import Mistral, UserMessage
import gradio as gr


#print(chat_response.choices[0].message.content)
def chat_with_mistral(user_input):
    api_key = "UztPcXqSzMQjjWDKAkIi0dwihkym1w56"
    model = "mistral-large-latest"  # Use "Mistral-7B-v0.2" for "mistral-tiny"

    client = Mistral(api_key=api_key)
    messages = [UserMessage(role="user", content=user_input)]

    chat_response = client.chat.complete(model=model, messages=messages)
    return chat_response.choices[0].message.content
custom_css = """
body {
    background-color: #f0f4f8;
    font-family: Arial, sans-serif;
}
.gradio-container {
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 20px;
}
textarea {
    font-size: 16px;
    border-radius: 5px;
}
.markdown {
    font-size: 18px;
    line-height: 1.6;
}
"""
iface = gr.Interface(
    fn=chat_with_mistral,
    inputs=gr.components.Textbox(
        label="Ask the AI expert",
        placeholder="Type your question here (e.g., What's the best workout plan?)",
        lines=3,
        interactive=True
        ),
    outputs=gr.components.Markdown(label="Chatbot Response"),
    title="Chat With AI Expert",
    description="Enter a message and get a response.",
    examples=[["Give me a meal plan for today"]],
     theme="huggingface",
     live=True,
     css=custom_css,
    allow_flagging="never"
)

iface.launch()

        