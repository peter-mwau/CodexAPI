import requests
import gradio as gr

# def codex(value):
#     url = 'https://api.codex.jaagrav.in/execute'
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     data = {
#         'code': f"predefined_number = 5\nresult = predefined_number + {value}\nprint(result)",
#         'language': 'python',
#         'input': ''
#     }

#     response = requests.post(url, headers=headers, json=data)
#     if response.ok:
#         result = response.json()['stdout']
#         return result
#     else:
#         return "Error: Failed to execute the code."

# demo = gradio.Interface(fn=codex, inputs='number', outputs='text', title="Codex API: Add Predefined Number")
# demo.launch()



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
    else:
        result = response.text
    
    return result

input_text = gr.inputs.Number(label="Enter a value")
output_text = gr.outputs.Textbox(label="Result")

gr.Interface(fn=CodexAPI, inputs=input_text, outputs=output_text, title="CodexAPI with Gradio").launch(share=True)


