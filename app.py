from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)