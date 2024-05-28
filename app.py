from time import sleep

from flask import Flask, Response

app = Flask(__name__)

frames = []
for i in range(0, 200):
    with open(f'frames/{i}.txt', 'r') as file:
        frames.append(file.read())

@app.route('/')
def stream():
    def generate():
        while True:
            for frame in frames:
                yield frame + "\n"
                sleep(0.05)
                yield "\033[2J\033[H"

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)