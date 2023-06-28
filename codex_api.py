import requests
import gradio

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


def CodexAPI():
    value = int(input("Enter value: "))
    data = {
    'code': f'val = {value}  + 5\nprint(val)',
    'language': 'py',
    'input': ''
}

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://api.codex.jaagrav.in', headers=headers, data=data)

    if response.ok:
        print(response.json())
    else:
        print(response.text)

CodexAPI()  

