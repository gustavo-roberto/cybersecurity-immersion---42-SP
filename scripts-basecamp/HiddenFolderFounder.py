import requests

file  = open("list.txt", mode='r')
file_w = open("saida.txt", mode="w")

list = file.readlines()
url = "http://10.51.1.198:7631/images/"
i = 0

for word in list:
    i = i + 1
    full_url = url + word
        
    full_url.strip()
    print(str(i) + " | " + full_url + " | " + str(len(full_url)))
    try:
       

        #full_url.replace(r'\n','').replace(r'\r', '')
        # .replace('\r\n', '').replace('\r', '').replace(' ','')
        #full_url.rstrip('\r\n')

        

        response = requests.get(full_url, timeout=1)

        if response.status_code == 200:
            print("OK: " + full_url)
            file_w.write(full_url)
    except:
        i = 1

file.close()