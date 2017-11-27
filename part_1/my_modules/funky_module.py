# Some cool python integration challenges

#1. Get bitcoin price from luno (https://api.mybitx.com/api/1/ticker?pair=XBTZAR)
def get_bitcoin_prices():
    print('Hello! I\'m busy retrieving bitcoin prices from the Luno API')
    pass


#2. Calculate the mid-market price (bid + [bid-ask]/2)
def get_mid_market_price(bitcoin_prices=None):
    # Some unnecessary safety check
    if not bitcoin_price:
        return None

    # Some magic here
    pass


#3. Now we're getting funky, trade imbalance (buy volume / sell volume)
def get_trade_imbalance():
    # Get the list of trades (https://api.mybitx.com/api/1/trades?pair=XBTZAR)
    trades = {}

    # do the cool magic that gets our trade imbalance
    pass
