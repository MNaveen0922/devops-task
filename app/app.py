from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return {"status": "ok"}

@app.route("/count")
def count():
    value = r.incr("counter")
    return {"counter": value}

@app.route("/health")
def health():
    return {"health": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
