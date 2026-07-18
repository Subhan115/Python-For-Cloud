from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the main dashboard page
    return render_template('index.html')

@app.route('/api/metrics')
def metrics():
    # interval=None tells psutil to give the instant utilization without blocking the thread
    cpu_util = psutil.cpu_percent(interval=None)
    ram_util = psutil.virtual_memory().percent
    
    return jsonify({
        'cpu': cpu_util,
        'ram': ram_util
    })

if __name__ == '__main__':
    # Setting host to '0.0.0.0' allows you to access this from other devices on your local network
    app.run(host='0.0.0.0', port=80, debug=True)
