import os, paramiko, time, getpass
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = getpass.getpass('Password: ')

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        stdin, stdout, stderr = client.exec_command('calc.exe')
        time.sleep(1)

        result = stdout.read().decode()
        print(result)
        client.close()
    except Exception as e:
        print(e)
        client.close()
        exit(1)