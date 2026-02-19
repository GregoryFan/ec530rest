import requests

req = requests.get('https://api.fda.gov/food/event.json?search=products.industry_code:23&count=reactions.exact')
print(req.status_code)
req_in_text = req.content.decode('utf8')
print(req_in_text)