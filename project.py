#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import smtplib
import time

while(True):
  URL = "https://www.rte.ie/news/"

  page = requests.get(URL, "lxml")

  soup = BeautifulSoup(page.content, "html.parser")
  News = ""
  for article in soup.find_all("div", class_="article-meta"):
    headline = article.find("h3").text.strip()
    News = News + headline + "\n \n"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  
  sender = "123@gmail.com"
  sender-password = "123"
  server.login(sender, sender-password)

  subject = "Latest News"
  body = News

  message = 'Subject: {}\n\n{}'.format(subject, body)
  recipients = ["456@gmail.com"]
  server.sendmail(
    sender,
    recipients,
    message.encode("utf8")
  )
  print("Email sent")

  server.quit()

  time.sleep(86400)
