from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

counts = {}


@app.route('/')
def index():
    global counts
    return str(counts)


@app.route('/request-counter', methods=['POST', 'GET', 'PUT', 'DELETE'])
def request_counter():
    global counts
    if request.method in counts:
        counts[request.method] += 1
    else:
        counts[request.method] = 0
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
