#!/usr/bin/python

from flask import Flask, render_template, request
app = Flask(__name__)

@app.template_filter('orderBets')
def order_bets(bets):
	return sorted(bets, key = lambda (name, (t,f)): (t + f, name != 'total'))[::-1]

@app.template_filter('orderWealth')
def order_wealth(wealths):
	return sorted(wealths, key = lambda (name, wealth): wealth)[::-1]

@app.route("/")
def index():
	from state import State
	return render_template('index.html', state=State.load())

@app.route("/history")
def history():
	from state import State
	return render_template('history.html', state=State.load())

@app.route("/test", methods=['GET', 'POST'])
def test():
	if request.method == 'GET':
		return render_template('test.html')

	else:
		name = request.form['name']
		code = request.form['code']

		from main import run, loadBettingFunctions
		bfs = loadBettingFunctions()

		error = None
		def catchErrors(bf):
			def bf2(*args):
				try:
					return bf(*args)
				except Exception as ex:
					error = ex
					raise ex
			return bf2

		try:
			from random import randint
			filename = 'temp_test_%d.py' % randint(0,1000000)
			with open(filename, 'w') as f:
				f.write(code)
				f.close()
			bfs[name] = __import__(filename[:-3]).bet

			from state import State
			state = State.load()

			bets, converged = run(state, bfs, max_iterations = 50)

			if error:
				raise error

			return render_template('test.html', run=True, bets=bets, converged=converged)

		except int as ex:
			print repr(ex)
			return render_template('test.html', error=repr(ex))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)

