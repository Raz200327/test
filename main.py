from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1, 1000)
    return render_template('index.html', random_num=random_num)

if __name__ == "__main__":
    app.run(debug=True)


