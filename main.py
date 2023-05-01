from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1, 1000)
    names = ["Ryan", "James", "Greg", "Jan", "June"]
    chosen_name = random.choice(names)
    return render_template('index.html', random_num=random_num, name=chosen_name)

if __name__ == "__main__":
    app.run(debug=True)


