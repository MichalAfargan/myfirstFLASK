from flask import Flask , json, request, jsonify, render_template

app = Flask(__name__)
@app.route('/yossef')
def get_about():
    return render_template('test.html')


@app.route('/eli')
def eli():
    with open("x.json", "r") as read_file:
        books = json.load(read_file)
    # books=['alice','wonders','sherlook']
    shirli = "i love horses"
    return render_template('index.html',ar=books)

def calc(x,y): return x+y
@app.route('/stam')
def aaaa():
    return render_template('anyname.html')


# http://127.0.0.1:5000/
@app.route("/")
def hello_world():
    return render_template('xyz.html')


# http://127.0.0.1:5000/
@app.route("/about")
def about():
    return "<a href='/'>Home</a> <img src='https://picsum.photos/20/21'><img src='https://picsum.photos/21/20'><img src='https://picsum.photos/20/20'>"


if __name__ == '__main__':
    app.run(debug=True)