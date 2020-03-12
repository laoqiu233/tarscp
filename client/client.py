from paramiko import SSHClient
from scp import SCPClient
import tarfile
import os

folder = 'SmartMirror'

path = '~/Desktop/'

host = '192.168.0.199'
username = 'pi'
password = ''

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(host, username=username, password=password)
scp = SCPClient(ssh.get_transport())

# Compress folder

print('Compression starting...')

if not os.path.exists('tmp'):
    os.mkdir('tmp')

tar = tarfile.open(os.path.join('tmp', '{}.tar.gz'.format(folder)), 'w:gz')

for root, dirs, files in os.walk(folder):
    for name in files:
        print(os.path.join(root, name))
        tar.add(os.path.join(root, name))

tar.close()

print('Finished compressing.')

# Send folder

print('SCP starting...')
scp.put('tmp/{}.tar.gz'.format(folder), path)
print('File sent.')
ssh.close()

# Clean up

print('Clean-up starting...')

os.remove(os.path.join('tmp', '{}.tar.gz'.format(folder)))
os.rmdir('tmp')

print('Clean-up finished.')