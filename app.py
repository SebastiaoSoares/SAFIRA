from flask import Flask, render_template, request
import values

app = Flask(__name__)

@app.route('/')
def index():

    fumaca = request.form.get('fumaca')
    return render_template('index.html', fumaca=fumaca, fResult=values.fResult, tResult=values.tResult, uResult=values.uResult, r=values.r)
    # x_results = ["% of precision", "status (safe or no_safe)", "result text"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
