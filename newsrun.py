#!/usr/bin/python3
import subprocess, os
from time import sleep

def runnews():
    cmd = "cd"
    #os.system(cmd)
    
    commands = '''
        pwd
        cd /home/matias/Documentos/firebase/public/elpais/files
        pwd
        python3 elpais.py
        pwd
        cd /home/matias/Documentos/firebase/public/elobservador/files
        python3 elobservador.py
        pwd
    '''

    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print(out.decode('utf-8'))

    #subprocess.call('cd', shell=True, cwd='/home/matias/Documentos/firebase/public/elpais/files')
    #print(os.getcwd())
    #result = subprocess.call("python3 elpais.py", shell=True)
    #print(str(result))
    #result = subprocess.call(["python3","elpais.py"], capture_output=True)
    #out = subprocess.call('ps -ef | grep "python3 elpais.py"', shell=True)
    #print(out)

    #result = subprocess.call('cd /home/matias/Documentos/firebase/public/elpais/files', shell=True)
    #print(result)

    #result = subprocess.run(["python3","elpais.py"], capture_output=True, check=True)
    #print(result.returncode)

    #result = subprocess.call('cd /home/matias/Documentos/firebase/public/elobservador/files', shell=True)

    #result = subprocess.run(["python3","elobservador.py"], capture_output=True)
    #print(result.returncode)

    

if __name__ == "__main__":  
    runnews()
else:
    runnews()


