from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        return render_template('result.html', entered_text=ticker)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')