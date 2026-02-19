import requests

req = requests.get('https://api.fda.gov/food/event.json?search=reactions.exact:"Death"&count=products.industry_name.exact')
req_text = req.content.decode('utf-8')
print(req_text)