# Hint: Those modules aren't going to import themselves

def main():
    hypothetical_gain = kind_of_lame_module.get_50_percent_increase(4)
    print('Hypothetical gain: %s' % hypothetical_gain)

    multiplied_gain = kind_of_lame_module.multiply_by_12(hypothetical_gain)
    print('multiplied gain: %s' % multiplied_gain)

    for _ in range(4):
        my_list = kind_of_lame_module.get_list_with_one_item()
        print('this list only has one item: %s' % my_list)

    price = funky_module.get_bitcoin_prices()

    mid_market_price = funky_module.get_mid_market_price(
        bitcoin_prices=price
    )

    trade_imbalance = funky_module.get_trade_imbalance()


if __name__ == '__main__':
    main()
