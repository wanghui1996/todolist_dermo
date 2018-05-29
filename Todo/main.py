from flask import  Flask, render_template



app  = Flask(__name__)


@app.route('/')
def index():
    todo = [

        "ceshi",
        "ceshi",
        "ceshi"

    ]

    return  render_template('index.html',data = todo)






if __name__ == '__main__':
    # aap = Flask()
    app.run(debug = True)