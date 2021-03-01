import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = ""
my_pass = ""
url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-512GB/dp/B08N5WRWNW/ref=sr_1_8?crid=1ZZO8QM6G7Z3G&dchild=1" \
      "&keywords=apple+macbook&qid=1614498392&sprefix=apple+macbo%2Caps%2C317&sr=8-8 "
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4427.4 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price_tag = soup.select_one(selector=".priceBlockBuyingPriceString")
price = price_tag.getText()[2:]
# print(price)
if price <= "1,40,000.00":
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Amazon Price Alert!\n\n{price}\nLink: {url}",
    )
