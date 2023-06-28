import requests
import gradio as gr

def CodexAPI(value):
    data = {
        'code': f'val = {value} + 5\nprint(val)',
        'language': 'py',
        'input': ''
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://api.codex.jaagrav.in', headers=headers, data=data)

    if response.ok:
        result = response.json()
        output = result['output'].strip()  # Extract the output value and remove leading/trailing whitespace
    else:
        output = "Error: Failed to execute the code."
    
    return output

input_text = gr.inputs.Number(label="Enter a value(add 5 to the input value)")
output_text = gr.outputs.Textbox(label="Result")

gr.Interface(fn=CodexAPI, inputs=input_text, outputs=output_text, title="CodexAPI with Gradio").launch() 
# To create a public link, set `share=True` in `launch()`.



