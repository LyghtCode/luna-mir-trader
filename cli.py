import requests
import terra_sdk
import sys
import config as config
from terra_sdk.key.mnemonic import MnemonicKey

from terra_sdk.client.lcd import LCDClient
from terra_sdk.core import Coins

from src.trading_core import get_all_mirror_swap_price, get_all_mirror_for_ust_price, get_bluna_for_luna_price, \
    get_luna_for_bluna_price, \
    get_ust_for_mspy_price, get_mspy_for_ust_price, get_maapl_for_ust_price, mirror_sell, mirror_buy, buy, sell, \
    get_mbtc_for_ust_price, get_mko_for_ust_price, get_mtsla_for_ust_price, get_mtwtr_for_ust_price
from src.helpers import create_params, info, create_terra, create_wallet, warn, from_u_unit, get_arg_safe, get_pk
from src import bot, const, mirror_bot


def main():
    with open("files/greeting.txt") as f:
        content = f.read()
        print(content)

    params, terra, wallet = setup()

    while True:
        inp = input(' 👽    >>> ').strip()
        split = inp.split()
        if not len(split):
            continue
        command = split[0]
        args = split[1:]
        if command == 'quit':
            terra.session.close()
            break
        try:
            if command == 'price':
                # return_amount, price = get_bluna_for_luna_price(terra, params)
                # info("returned for {} Luna: {} bLuna, price: {}".format(params.amount_luna, from_u_unit(return_amount),
                #                                                         price))
                # return_amount, price = get_luna_for_bluna_price(terra, params)
                # info("returned for {} bLuna: {} Luna, inv price: {}, price: {}".format(params.amount_bluna,
                #                                                                        from_u_unit(return_amount),
                #                                                                        1 / price, price))
                return_amount, price = get_mspy_for_ust_price(terra, params)
                info("returned for {} mSPY: {} UST, inv price: {}, price: {}".format(1,
                                                                                     from_u_unit(return_amount),
                                                                                     1 / price, price))
                return_amount, price = get_maapl_for_ust_price(terra, params)
                info("returned for {} mAAPL: {} UST, inv price: {}, price: {}".format(1,
                                                                                     from_u_unit(return_amount),
                                                                                     1 / price, price))
                return_amount, price = get_mbtc_for_ust_price(terra, params)
                info("returned for {} mBTC: {} UST, inv price: {}, price: {}".format(1,
                                                                                      from_u_unit(return_amount),
                                                                                      1 / price, price))
                return_amount, price = get_mko_for_ust_price(terra, params)
                info("returned for {} mKO: {} UST, inv price: {}, price: {}".format(1,
                                                                                     from_u_unit(return_amount),
                                                                                     1 / price, price))
                return_amount, price = get_mtsla_for_ust_price(terra, params)
                info("returned for {} mTSLA: {} UST, inv price: {}, price: {}".format(1,
                                                                                     from_u_unit(return_amount),
                                                                                     1 / price, price))
                return_amount, price = get_mtwtr_for_ust_price(terra, params)
                info("returned for {} mTWTR: {} UST, inv price: {}, price: {}".format(1,
                                                                                     from_u_unit(return_amount),
                                                                                     1 / price, price))

            elif command == 'amount-luna':
                amount_luna = get_arg_safe(args)
                if amount_luna:
                    params.amount_luna = float(amount_luna)
                    info("amount for selling Luna set to {}".format(params.amount_luna))
            elif command == 'amount-bluna':
                amount_luna = get_arg_safe(args)
                if amount_luna:
                    params.amount_bluna = float(amount_luna)
                    info("amount for selling bLuna set to {}".format(params.amount_bluna))
            elif command == 'amount-mspy':
                amount_mspy = get_arg_safe(args)
                if amount_mspy:
                    params.amount_mspy = float(amount_mspy)
                    info("amount for selling mSPY set to {}".format(params.amount_mspy))
            elif command == 'inv-sell-price':
                inv_sell_price = get_arg_safe(args)
                if inv_sell_price:
                    params.inv_sell_price = float(inv_sell_price)
                    info("price for selling set to {}".format(params.inv_sell_price))
            elif command == 'buy-price':
                buy_price = get_arg_safe(args)
                if buy_price:
                    params.buy_price = float(buy_price)
                    info("price for buying set to {}".format(params.buy_price))
            elif command == 'spread':
                spread = get_arg_safe(args)
                if spread:
                    params.spread = float(spread)
                    info("max spread set to {}".format(params.spread))
            elif command == 'bot':
                bot.run(params, terra, wallet)
            elif command == 'mirrorbot':
                mirror_bot.run(params, terra, wallet)
            elif command == 'mode-buy':
                params.mode = const.buy
                info("set mode to buy ({})".format(params.mode))
            elif command == 'mode-sell':
                params.mode = const.sell
                info("set mode to sell ({})".format(params.mode))
            elif command == 'buy':
                _, price = get_bluna_for_luna_price(terra, params)
                buy(params, terra, price, wallet)
            elif command == 'sell':
                _, price = get_luna_for_bluna_price(terra, params)
                sell(params, terra, price, wallet)
            elif command == 'mirror_buy':
                _, price = get_mspy_for_ust_price(terra, params)
                mirror_buy(params, terra, price, wallet)
            elif command == 'mirror_sell':
                _, price = get_ust_for_mspy_price(terra, params)
                mirror_sell(params, terra, price, wallet)
            else:
                info('Invalid Command.')
        except terra_sdk.exceptions.LCDResponseError as e:
            warn(str(e))


def setup(is_bot=False):
    params = create_params(is_bot)
    prices = requests.get(const.gas_price_url).json()
    uusd = prices["uusd"]
    coins = Coins(uusd=uusd)
    terra = LCDClient(chain_id=const.chain_id, url=const.lcd_url, gas_prices=coins, gas_adjustment=1.4)
    terrainfo = terra.tendermint.node_info()['default_node_info']['network']
    print(terrainfo)
    info("Connected to " + const.chain_id + " via " + const.lcd_url)
    mk = MnemonicKey(mnemonic=config.mnemonic)
    wallet = terra.wallet(mk)
    account_address = wallet.key.acc_address
    print(wallet)
    print("Welcome to Chigag Mir Bot")
    print("Wallet Address is: " + account_address)
    # info("Creating wallet" + wallet.account_number())
    # terra, wallet = create_terra()
    # wallet = create_wallet(terra)
    return params, terra, wallet


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[1] == 'bot':
        params, terra, wallet = setup(True)
        bot.run(params, terra, wallet)
    else:
        main()
