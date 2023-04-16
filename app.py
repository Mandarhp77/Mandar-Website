from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/edu/")
def edu():
    return render_template('edu.html')

@app.route("/proj/")
def proj():
    return render_template('proj.html')


if __name__=="__main__":
    app.run(debug=True)