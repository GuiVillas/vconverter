from flask import Flask

app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))