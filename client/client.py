import tarfile, requests, os, time

folder = 'SmartMirror'

path = '~/Desktop/'

host = '192.168.0.199'
username = 'pi'

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

start = time.time()

print('Transfer starting...')
os.system('scp {file} {user}@{host}:{path}'.format(
    file=os.path.join('tmp', '{}.tar.gz'.format(folder)),
    user=username,
    host=host,
    path=path
))
print('File sent in {} seconds.'.format(time.time() - start))

# Notify server to unpack file

requests.post('http://{host}:56597/'.format(), {'folder': folder})

# Clean up

print('Clean-up starting...')

os.remove(os.path.join('tmp', '{}.tar.gz'.format(folder)))
os.rmdir('tmp')

print('Clean-up finished.')