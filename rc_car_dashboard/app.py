from flask import Flask, render_template
from api.drive import bp as drive_bp

app = Flask(__name__)
app.register_blueprint(drive_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000)