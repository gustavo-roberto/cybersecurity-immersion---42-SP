import requests

ip = "http://10.51.1.198:"



for port in range(0, 50000):
    url = ip + str(port)
    try:
        resp = requests.get(url, timeout=1)
        
        if resp.status_code == 200:
            print("Porta: " + url)
    except Exception:
        i = 1
    

