from tradingview_ta import TA_Handler, Interval, Exchange

def analysisForm(symbol, screener, exchange, interval, analysisType):

    graph = TA_Handler(
        symbol = symbol,
        screener = screener,
        exchange = exchange,
        interval = interval)

    if analysisType == 'Summary':
        return graph.get_analysis().summary
    elif analysisType == 'Open':
        return graph.get_analysis().indicators['open']
    elif analysisType == 'Close':
        return graph.get_analysis().indicators['close']
    elif analysisType == 'Momentum':
        return graph.get_analysis().indicators['Mom']
    elif analysisType == 'RSI':
        return graph.get_analysis().indicators['RSI']
    elif analysisType == 'MACD':
        return graph.get_analysis().indicators['MACD.macd']
