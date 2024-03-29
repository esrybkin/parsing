# import requests

url = ""  #ссылка на картинку
# response = requests.get(url)

# with open('owl.jpg', 'wb') as f:
#     f.write(response.content)

import wget
wget.download(url)