import source_tradingview
from helper import getDaytradeRecom
from source_tradingview import symbols, dataSource


def startDayTrading():
    source_tradingview.fetchDayTradeAPI()
    no = 0
    mql4 = 'string datas[] = {'
    for symbol in symbols:
        rec = getDaytradeRecom(symbol, dataSource)
        if rec is not None:
            no += 1

            if "BUY" in rec:
                mql4 += f'"{symbol}#0",'
            if "SELL" in rec:
                mql4 += f'"{symbol}#1",'

            print(f'{"0"+str(no) if no < 10 else str(no)} {symbol}  {rec}')

    # print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n\n\n", mql4[: len(mql4) - 1] + '};', "\n\n\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")

startDayTrading()