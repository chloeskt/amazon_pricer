import os
import smtplib
from typing import Dict

import requests
from bs4 import BeautifulSoup
import unidecode


class AmazonPricer:
    def __init__(self, url: str, headers: Dict[str, str], current_price: float):
        self.URL = url
        self.HEADERS = headers
        self.CURRENT_PRICE = current_price

    def send_mail(self, title: str):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("PASSWORD"))
        subject = f"Price of {title} has gone DOWN!"
        body = f"The price of the wanted article has done down, check the following link {self.URL}"
        msg = f"Subject: {subject} \n\n {body}"

        server.sendmail(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_RECEIVER"), msg)
        server.quit()

    def check_price(self):
        page = requests.get(self.URL, headers=self.HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find(id="productTitle").get_text().strip()
        price = float(
            soup.find(id="priceblock_ourprice")
            .get_text()
            .split("€")[0]
            .replace(",", ".")
            .replace("\xa0", "")
        )
        if price < self.CURRENT_PRICE:
            unaccented_title = unidecode.unidecode(title)
            self.send_mail(unaccented_title)
