import json

from flask import Flask, request, Response

app = Flask(__name__)

stats = {
	'attemps': 0,
	'success': 0
}

@app.route('/') #декоратор, программирует, что происходит на странице браузера
def hello():
	return f'Hello, user. stats = {stats}'

@app.route('/auth', methods = ['POST'])
def auth():
	stats['attemps'] += 1

	data = request.json
	login = data['login']
	password = data['password']

	with open('users.json') as users_file: #чтобы не забыть закрыть
		users = json.load(users_file)

	# users_file = open('users.json')
	# users = json.load(users_file)
	# users_file.close()

	if login in users and users[login] == password:
		status_code = 200
		stats['success'] += 1
	else:
		status_code = 401

	return Response(status=status_code)

if __name__ == '__main__':
	app.run()