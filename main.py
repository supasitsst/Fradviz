from os import system, name
import time as t
from datetime import datetime
import source_finviz
import source_tradingview
from model import DataSource, SoupResponse
from helper import getTimeFrameRecom, getTimeStamp
from source_tradingview import symbols, dataSource
from source_finviz import finvizes


def displayData():
    _ = system('clear')
    print(f'Last update : {getTimeStamp()}')
    # print(' # symbol           Sum')
    mql4 = 'string datas[] = {'
    for idx, symbol in enumerate(symbols):
        no = '0'+str(idx+1) if idx < 9 else str(idx+1)
        rec = getTimeFrameRecom(symbol, dataSource, finvizes)

        if "BUY" in rec:
            mql4 += f'"{symbol}#0",'
            print(f'{symbol}  {rec}')
        if "SELL" in rec:
            mql4 += f'"{symbol}#1",'
            print(f'{symbol}  {rec}')

        # print(f'{no} {symbol}  {rec}')

    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n\n\n", mql4[: len(mql4)-1] + '};', "\n\n\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")


def startProgram():
    source_tradingview.fetchAPI()
    source_finviz.fetchAPI()
    displayData()

    if input("Type `Enter` to reload data: ") == "":
        startProgram()


startProgram()