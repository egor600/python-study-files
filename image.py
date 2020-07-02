import requests

url = 'https://banner2.cleanpng.com/20180425/pke/kisspng-python-computer-icons-font-awesome-technology-circle-dots-floating-material-5ae020c2d20263.6237444615246378908602.jpg'

r = requests.get(url)

with open('image_py.jpg', 'wb') as file:
	file.write(r.content)