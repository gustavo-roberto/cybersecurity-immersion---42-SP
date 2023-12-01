import subprocess
 
# From Python3.7 you can add 
# keyword argument capture_output
for i in range(860,870):
    if i%1000 == 0:
        print("RODANDO")
    command = f"gpg --batch --yes --passphrase {str(i).zfill(4)} -o saidaSenha.txt --decrypt secret.txt.gpg"
    print(command)
    r = subprocess.run(command, 
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, 
                       text=True)

    if r.returncode == 0:
        file = open("saidaSenha.txt", mode="a")
        file.write("passphrase: " + str(i))
        file.close()
        print("SUCESSO")
