from flask import Flask, render_template, request
from finwatch.scrape import get_basic_financials

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        single_metrics, periodic_metrics = get_basic_financials(ticker=ticker)
        return render_template('result.html', single_metrics=single_metrics, periodic_metrics=periodic_metrics, ticker=ticker)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')