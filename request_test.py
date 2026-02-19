import requests

# Get's the number of deaths by industry type.
req = requests.get('https://api.fda.gov/food/event.json?search=reactions.exact:"Death"&count=products.industry_name.exact')

#Prints the response text in the form of JSON.
req_text = req.content.decode('utf-8')
print(req_text)

