import requests

def test_get_deaths_by_industry():
    req = requests.get('https://api.fda.gov/food/event.json?search=reactions.exact:"Death"&count=products.industry_name.exact')
    req_text = req.content.decode('utf-8')
    return req_text
