from flask import Flask, request, abort
import tarfile, os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    folder = request.form.get('folder', '')

    if not folder:
        abort(400)

    if not os.path.exists('{}.tar.gz'.format(folder)):
        abort(404)

    # Remove existing files
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.remove(os.path.join(root, dir))

    # Extract
    with tarfile.open('{}.tar.gz'.format(folder), 'r:gz') as file:
        file.extractall()

    return 'ok', 200

    # Clean up
    os.remove('{}.tar.gz'.format(folder))

if __name__ == '__main__':
    print('***WARNING*** This script will delete the existing folder when it gets a new file.')
    app.run(host='0.0.0.0', port=56597)