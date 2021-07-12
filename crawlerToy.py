import websocket
# import json

baseUri = 'wss://stream.binance.com:9443'
symbol = 'bnbbtc'
interval = '1m'

uri = baseUri + '/ws/' + symbol + '@kline_' + interval


def on_message(wsapp, message):
    print(message)

wsapp = websocket.WebSocketApp(uri, on_message = on_message)
wsapp.run_forever()