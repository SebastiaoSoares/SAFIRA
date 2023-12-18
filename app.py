from flask import Flask, render_template, request
import values

app = Flask(__name__)

@app.route('/')
def index():

    fumaca = request.form.get('fumaca')
    return render_template('index.html', fumaca=fumaca, r=values.r)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)