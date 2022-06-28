from builtins import sorted

from bs4 import BeautifulSoup
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor
import cfscrape
from model import SoupResponse
from pprint import pprint

finvizes = []
futures = []
forexes = []


def fetchAPI():
    print("start fetch")
    forex_response = cfscrape.create_scraper().get("https://finviz.com/forex.ashx").content
    forex_soup = BeautifulSoup(forex_response, "html.parser")
    forex_tree = Parser().parse(forex_soup.find("script", text=lambda text: text and "var " + "tiles" in text).text)
    for node in nodevisitor.visit(forex_tree):
        if isinstance(node, ast.VarDecl) and node.identifier.value == "tiles":
            for x in getattr(node.initializer, 'properties'):
                dictionary = getattr(dict(vars(x))['right'], 'properties')
                label = str(dictionary[0].right.value).replace('/', '').replace('"', '')
                change = dictionary[3].right.value
                if isinstance(change, ast.Number):
                    change = -float(vars(change)['value'])
                if label in ["AUDUSD", "EURGBP", "EURUSD", "GBPJPY", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]:
                    finvizes.append(SoupResponse(label, float(change)))
                    # forexes.append(SoupResponse(label, float(change)))

    futures_response = cfscrape.create_scraper().get("https://finviz.com/futures.ashx").content
    futures_soup = BeautifulSoup(futures_response, "html.parser")
    futures_tree = Parser().parse(futures_soup.find("script", text=lambda text: text and "var " + 'tiles' in text).text)
    for node in nodevisitor.visit(futures_tree):
        if isinstance(node, ast.VarDecl) and node.identifier.value == 'tiles':
            for x in getattr(node.initializer, 'properties'):
                dictionary = getattr(dict(vars(x))['right'], 'properties')
                label = str(dictionary[0].right.value).replace('"', '')
                change = dictionary[3].right.value
                if isinstance(change, ast.Number):
                    change = -float(vars(change)['value'])
                if label in ["AUD", "GBP", "CAD", "EUR", "JPY", "NZD", "CHF", "USD"]:
                    finvizes.append(SoupResponse(label, float(change)))
                    # futures.append(SoupResponse(label, float(change)))

    # print("complete")
    # for item in finvizes:
    #     print(item.name, item.change)
    #
    # print("_________________________________________________")
    # def sortFutureKey(e):
    #     return e.change

    # list(filter(lambda x: x is not None, lists))
    # list(sorted(futures, key=sortFutureKey))
    # sorted(futures, key=sortFutureKey)
    # print("______")
    # for item in futures:
    #     print(item.name, item.change)
