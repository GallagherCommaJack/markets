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

		errors = []
		def catchErrors(bf):
			def bf2(*args):
				try:
					result = bf(*args)
					if result is None or not isinstance(result, tuple) or len(result) != 2:
						raise Exception("Bad value returned: %r" % result)
					return result
				except Exception as ex:
					errors.append(ex)
					raise ex
			return bf2

		from random import randint
		filename = 'temp_test_%d.py' % randint(0,1000000)
		with open(filename, 'w') as f:
			f.write(code)
			f.close()

		try:
			bfs[name] = catchErrors(__import__(filename[:-3]).bet)

			from state import State
			state = State.load()

			bets, converged = run(state, bfs, max_iterations = 100)

			if errors:
				raise errors[0]

			return render_template('test.html', name=name, code=code, run=True, bets=bets, converged=converged)

		except Exception as ex:
			print repr(ex)
			return render_template('test.html', name=name, code=code, error=repr(ex))

		finally:
			import os
			os.remove(filename)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
	if request.method == 'GET':
		return render_template('submit.html')

	else:
		name = request.form['name']
		code = request.form['code']

		import os
		import os.path
		if not os.path.exists('new_players'):
			try:
				os.makedirs('new_players')
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise

		with open('new_players/%s.py' % name.lower(), 'w') as f:
			f.write(code)
			f.close()
		return render_template('submit.html', submitted=True)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)

