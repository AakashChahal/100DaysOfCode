import requests
from twilio.rest import Client

account_sid = 'AC85c6bf4283fa45de568f6424d8fa0fc7'
auth_token = 'twilio auth token'
client = Client(account_sid, auth_token)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api = "news api key"
stocks_api = "alpha vantage api key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_news = {
    'qInTitle': COMPANY_NAME,
    'apiKey': news_api
}

parameters_stocks = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stocks_api
}
up_down = None

response = requests.get(STOCK_ENDPOINT, params=parameters_stocks)
stock_data = list(response.json()["Time Series (Daily)"].values())[:2]
closing_day2 = float(stock_data[0]['4. close'])
# print("day2: ", closing_day2)
closing_day1 = float(stock_data[1]['4. close'])
# print("day1: ", closing_day1)
diff_in_stocks = closing_day2 - closing_day1
if diff_in_stocks > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if round(5/closing_day1*100, 2) >= abs(diff_in_stocks):
    # print('Get News')
    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    articles = response_news.json()['articles'][:3]
    # print(articles)
    for article in articles:
        title = article["title"]
        description = article["description"]
        news_article = f"""\n{COMPANY_NAME}: {up_down}{round(5/closing_day1*100, 2)}
Headline: {title}
Brief: {description}."""
        message = client.messages.create(
            from_='your twilio number',
            body=news_article,
            to='your number'
        )
        # print(news_article)
