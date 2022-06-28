from datetime import datetime


class _Color:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class _Recom:
    strongBuy = 'STRONG_BUY'
    buy = 'BUY'
    neutral = 'NEUTRAL'
    sell = 'SELL'
    strongSell = 'STRONG_SELL'


def _getIndicator(recom):
    if recom == _Recom.strongBuy:
        return f'{_Color.green}▲{_Color.end}'
    elif recom == _Recom.buy:
        return f'{_Color.green}△{_Color.end}'
    elif recom == _Recom.neutral:
        return f'⁃'
    elif recom == _Recom.sell:
        return f'{_Color.fail}▽{_Color.end}'
    elif recom == _Recom.strongSell:
        return f'{_Color.fail}▼{_Color.end}'
    else:
        return recom


def _getSummayRecomString(h4, h1, m15):
    buy = [_Recom.strongBuy, _Recom.buy]
    sell = [_Recom.strongSell, _Recom.sell]
    if (h4 in buy) and (h1 in buy) and (m15 in buy):
        return _Recom.buy
    if (h4 in sell) and (h1 in sell) and (m15 in sell):
        return _Recom.sell


def _getSummayRecom(h4, h1, m15, finviz):
    if _getSummayRecomString(h4, h1, m15) == _Recom.buy and finviz:
        return f'{_Color.bold}{_Color.green} {_Recom.buy} {_Color.end}{_Color.end}'
    if _getSummayRecomString(h4, h1, m15) == _Recom.sell and finviz:
        return f'{_Color.bold}{_Color.fail} {_Recom.sell} {_Color.end}{_Color.end}'

    return f' NONE '


def getTimeFrameRecom(symbol, dataSource, finvizes):
    kRecom = 'RECOMMENDATION'
    # d1 = list(filter(lambda x: x.symbol == symbol, dataSource.d1))[0].summary[kRecom]
    h4 = list(filter(lambda x: x.symbol == symbol, dataSource.h4))[0].summary[kRecom]
    h1 = list(filter(lambda x: x.symbol == symbol, dataSource.h1))[0].summary[kRecom]
    #    m30 = list(filter(lambda x: x.symbol == symbol, dataSource.m30))[0].summary[kRecom]
    m15 = list(filter(lambda x: x.symbol == symbol, dataSource.m15))[0].summary[kRecom]

    recom = _getSummayRecomString(h4, h1, m15)

    forex = list(filter(lambda x: x.name == symbol, finvizes))
    change = 0

    if len(forex) > 0:  # forex from finviz
        change = abs(float(forex[0].change))
        finviz_result = (recom == _Recom.buy and float(forex[0].change) > 0) \
                        or (recom == _Recom.sell and float(forex[0].change) < 0)
    else:  # future from finviz
        first_change = float(list(filter(lambda x: x.name == symbol[0:3], finvizes))[0].change)
        last_change = float(list(filter(lambda x: x.name == symbol[3:6], finvizes))[0].change)
        # print(symbol, first_change, last_change)
        change = abs(first_change - last_change)
        finviz_result = (recom == _Recom.buy and float(first_change) > float(last_change)) \
                        or (recom == _Recom.sell and float(first_change) < float(last_change))

    # correct = "✓" if finviz_result else "✗"
    change_string = f'{"[{:4.2f}".format(change)}]'

    if change > 1.0:
        change_string = f'{_Color.blue}{change_string}{_Color.end}'

    return f'{_getIndicator(h4)} {_getIndicator(h1)} {_getIndicator(m15)} {change_string} {_getSummayRecom(h4, h1, m15, finviz_result)} '

    # return f'{_getIndicator(h4)} {_getIndicator(h1)} {_getIndicator(m30)} {_getIndicator(m15)} {corect} {_getSummayRecom(h4, h1, m30, m15, finviz_result)}'
    # return f'{_getIndicator(d1)} {_getIndicator(h4)} {_getIndica.tor(h1)} {_getIndicator(m15)}  {_getSummayRecom(h4, h1, m15)}'


def getDaytradeRecom(symbol, dataSource):
    kRecom = 'RECOMMENDATION'
    mn = list(filter(lambda x: x.symbol == symbol, dataSource.mn))[0].summary[kRecom]
    w1 = list(filter(lambda x: x.symbol == symbol, dataSource.w1))[0].summary[kRecom]
    d1 = list(filter(lambda x: x.symbol == symbol, dataSource.d1))[0].summary[kRecom]
    h4 = list(filter(lambda x: x.symbol == symbol, dataSource.h4))[0].summary[kRecom]
    buy = [_Recom.strongBuy, _Recom.buy]
    sell = [_Recom.strongSell, _Recom.sell]
    if (mn in buy) and (w1 in buy) and (d1 in buy) and (h4 in buy):
        return _Recom.buy
    if (mn in sell) and (w1 in sell) and (d1 in sell) and (h4 in sell):
        return _Recom.sell


def getTimeStamp():
    return f'{_Color.bold}{_Color.warning}{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}{_Color.end}{_Color.end}'
