from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fResult = "safe"
    tResult = "no_safe"
    uResult = "error"
    return render_template('index.html', fResult=fResult, tResult=tResult, uResult=uResult)
    # x_results = ["% of precision", "status (safe or no_safe)", "result text"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)