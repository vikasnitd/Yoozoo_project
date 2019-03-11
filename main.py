from flask import Flask,render_template,request
import subprocess
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/teen_patti")
def teen_patti():
	return render_template('teen_patti_home.html')

@app.route("/patti_answer" , methods = ['GET','POST'])
def patti_answer():

	num_player = request.args.get('count')
	return render_template('patti_input.html' , player_count = int(num_player))

@app.route("/patti_output" , methods = ['GET' , 'POST'])
def patti_output():
	import yoozo
	data1 = request.args.getlist('card_num')
	print(data1)
	indx_of_winner = yoozo.run_in(data1)
	# indx_of_winner = 1

	return render_template('patti_output.html' , indx = indx_of_winner)






@app.route("/hungarian")
def hungarian():
	return render_template('hung_home.html')

@app.route("/output")
def output():
	data = request.args.getlist('company')
	mat_size = request.args.get('matrix_size')
	file = open("input.txt" , "w")
	# print(mat_size)
	file.write(str(mat_size)+"\n")

	for i in data:
		file.write( str(i) + " ")

	# call('g++ ass.cpp && ./a.out', shell = True)
	p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", "ass", 'ass.cpp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.communicate()
	p = subprocess.Popen(["./ass"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	return render_template('output.html')

@app.route("/answer" , methods=['GET','POST'])
def answer():

	cost = request.args.get('cost')

	return render_template('input.html', mat_size = int(cost))


if __name__ == "__main__":
	app.run(debug=True)
