from tradingview_ta import TA_Handler, Interval, Exchange

def analysisForm(symbol, screener, exchange, interval):

    graph = TA_Handler(
        symbol = symbol,
        screener = screener,
        exchange = exchange,
        interval = interval)

    return graph.get_analysis().summary

