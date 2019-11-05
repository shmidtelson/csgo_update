import paramiko

from settings import SERVER_LIST
from utils.key import Key


class SendCommands:
    def __init__(self):
        self.main()

    def main(self):
        for item in SERVER_LIST:
            private_key = paramiko.RSAKey.from_private_key_file(Key().get(item['server_name']))

            connection = self.open_ssh_connection(item['user'], item['ip'], port=int(item['port']), key=private_key)

            stdin, stdout, stderr = connection.exec_command('cd / && ls -la')
            for line in stdout:
                print('... ' + line.strip('\n'))
            connection.close()

    def open_ssh_connection(self, username, hostname, port=22, key=None):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname, port=port, timeout=0.3, username=username, pkey=key)

        return client
