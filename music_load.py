import requests

REQUEST_STATUS_CODE = 200

url = 'ЗДЕСЬ ПИШЕМ АДРЕС MP3 ФАЙЛА'

if __name__ == '__main__':
	r = requests.get(url, stream=True)
	if r.status_code == REQUEST_STATUS_CODE:
		with open('	НАЗВАНИЕ ПЕСНИ С РАСШИРЕНИЕМ MP3', 'wb') as file:
			file.write(r.content)