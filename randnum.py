# randnum.py
import flask, random, os

app = flask.Flask(__name__)

@app.route('/')  # we will use the default page
def index(): 
    num_one=random.randint(1, 100)
    num_two=random.randint(1, 100)
    return flask.render_template(
        "index.html", 
        random_num_one=num_one,
        random_num_two=num_two
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    )
