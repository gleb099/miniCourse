import requests

sites = ['https://google.com/', 'https://ya.ru/', 'https://vk.com/']
n = 300

for site in sites:
	for i in range(100):
		response = requests.get(site)
		print(i, site, response.status_code)
