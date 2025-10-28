import json
import gradio as gr
import requests

url = "http://localhost:11434/api/generate"
headers = {"Content-Type":"application/json"}

history = []
def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model" : "codegun",
        "prompt" : final_prompt,
        "stream" : False
    }

    response = requests.post(url,headers=headers,data = json.dumps(data))

    if response.status_code==200:
        response = response.text
        data = json.loads(response)
        actualResponse = data['response']
        return actualResponse
    
    else:
        print("error:",response.text)

interface = gr.Interface(
    fn = generate_response,
    inputs = gr.Textbox(lines=4,placeholder="enter your Prompt"),
    outputs = gr.Textbox(lines=10)
)

interface.launch()