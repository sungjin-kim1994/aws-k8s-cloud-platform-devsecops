from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevSecOps Platform - Book Search API",
        "status": "running"
    })

@app.route('/health')
def health():
    # CI/CD 파이프라인 테스트용 주석 0927_0107
    return jsonify({"status": "healthy"})

@app.route('/books')
def books():
    return jsonify({
        "books": [
            {"id": 1, "title": "클라우드 x 보안 실무 가이드"},
            {"id": 2, "title": "AWS 클라우드 보안 핸드북"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
