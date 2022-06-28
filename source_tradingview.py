from tradingview_ta import TA_Handler, Interval, Exchange, get_multiple_analysis
from model import DataSource

# symbols = ["AUDUSD", "EURGBP", "CADJPY"]
symbols = []
symbols.extend(["EURUSD", "USDJPY", "GBPUSD", "USDCAD", "USDCHF", "AUDUSD", "NZDUSD"])
symbols.extend(["EURGBP", "EURCHF", "EURCAD", "EURAUD", "EURNZD", "EURJPY", "GBPJPY"])
symbols.extend(["CHFJPY", "CADJPY", "AUDJPY", "NZDJPY", "GBPCHF", "GBPAUD", "GBPCAD"])
symbols.sort()

dataSource = DataSource()


def extend_list(lists):
    result = list(filter(lambda x: x is not None, lists))
    if result[0].interval == Interval.INTERVAL_1_MONTH:
        dataSource.mn.extend(result)
    elif result[0].interval == Interval.INTERVAL_1_WEEK:
        dataSource.w1.extend(result)
    elif result[0].interval == Interval.INTERVAL_1_DAY:
        dataSource.d1.extend(result)
    elif result[0].interval == Interval.INTERVAL_4_HOURS:
        dataSource.h4.extend(result)
    elif result[0].interval == Interval.INTERVAL_1_HOUR:
        dataSource.h1.extend(result)
    elif result[0].interval == Interval.INTERVAL_30_MINUTES:
        dataSource.m30.extend(result)
    elif result[0].interval == Interval.INTERVAL_15_MINUTES:
        dataSource.m15.extend(result)
    elif result[0].interval == Interval.INTERVAL_5_MINUTES:
        dataSource.m5.extend(result)


def fetchAPI():
    forexes = list(map(lambda x: "FX_IDC:" + x, symbols))
    intervals = [Interval.INTERVAL_1_DAY, Interval.INTERVAL_4_HOURS,
                 Interval.INTERVAL_1_HOUR, Interval.INTERVAL_15_MINUTES]
    for item in [forexes]:
        for interval in intervals:
            analysis = get_multiple_analysis(screener="forex", interval=interval, symbols=item)
            extend_list(list(analysis.values()))


def fetchDayTradeAPI():
    forexes = list(map(lambda x: "FX_IDC:" + x, symbols))
    intervals = [Interval.INTERVAL_1_MONTH, Interval.INTERVAL_1_WEEK,
                 Interval.INTERVAL_1_DAY, Interval.INTERVAL_4_HOURS]

    for item in [forexes]:
        for interval in intervals:
            analysis = get_multiple_analysis(screener="forex", interval=interval, symbols=item)
            extend_list(list(analysis.values()))
