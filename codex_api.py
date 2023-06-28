import requests
import gradio

def codex(name):
    url = 'https://api.codex.jaagrav.in'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'code': "Good morning, {}".format(name),
        'language': 'py',
        'input': ''
    }

    response = requests.post(url, headers=headers, data=data)
    # print(response.status_code)
    # print(response.content)
    result = response.json()['output']
    return result

demo = gradio.Interface(fn=codex, inputs='text', outputs='text', title="Codex API for Python Compiler")
demo.launch()
