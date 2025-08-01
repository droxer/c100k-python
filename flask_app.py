from flask import Flask, request, jsonify
import time
import requests # This will be monkey-patched by gevent

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "OK"

@app.route('/')
def hello():
    # This sleep will be cooperative if gevent is patching time.sleep
    time.sleep(0.1) # Simulate some I/O bound delay
    return "Hello, Gevent Flask!"

@app.route('/external')
def call_external():
    # This requests.get will be cooperative if gevent is patching socket
    try:
        response = requests.get("http://localhost:8000/slow_api_endpoint", timeout=5)
        return jsonify({"message": f"Called external API: {response.text}"})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# (Optional) A slow API endpoint for demonstration if you want to run one
@app.route('/slow_api_endpoint')
def slow_api():
    time.sleep(2) # Simulate a slow external API
    return "This was a slow external call!"

