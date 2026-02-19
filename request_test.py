import requests

req = requests.get('https://api.fda.gov/food/event.json?search=products.name_brand:"nuts"&count=reactions.exact')
req_text = req.content.decode('utf-8')
print(req_text)