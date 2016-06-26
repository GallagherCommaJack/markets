#!/usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.template_filter('orderBets')
def order_bets(bets):
    return sorted(bets, key = lambda (name, (t,f)): (t + f, name != 'total'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/history")
def history():
	from state import State
	return render_template('history.html', state=State.load())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

