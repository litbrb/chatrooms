from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', chatrooms=[file.replace(".txt", "") for file in os.listdir("chatrooms") if file.endswith(".txt")])

@app.route('/chatroom/<name>', methods=["GET", "POST"])
def chatroom(name):
    message = request.form.get("message")

    if request.method == "POST":
        with open(f"chatrooms/{name}.txt", "a") as f:
            f.write(f"\n{message}")

    with open(f"chatrooms/{name}.txt", "r") as f:
        content = f.read()

    return render_template("chatroom.html", name=name, content=content)

app.run(debug=True)