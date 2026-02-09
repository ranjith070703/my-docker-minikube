from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "Backend is working fine!"

@app.route('/health')
def health():
    app.logger.info("Health check OK")
    return {"status": "healthy"}

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)