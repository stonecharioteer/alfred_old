import requests
import oauth2
import rauth
import goodreads

def getKeyAndSecret():
    return (
            "SvIF7l1OTPwaZZv5QMw",
            "Jouf5FtKxBOMcPNwX4lgGBDmWOUdM82YK1lOw0lXpE"
        )

def getBookFromGoodreads(isbn):
    from random import randint
    from goodreads import client
    key, secret = getKeyAndSecret()
    gc = client.GoodreadsClient(key, secret)
    number = randint(0,10**6)
    print number
    book = gc.book(number)
    return book

