from typing import Dict
import asyncio
import ast
import base64, json
from terra_sdk.client.lcd import LCDClient, Wallet
from terra_sdk.client.lcd.api.tx import CreateTxOptions
from terra_sdk.core import Coins
# from terra_sdk.core.auth import StdFee, StdTx
from terra_sdk.core.broadcast import BlockTxBroadcastResult
from terra_sdk.core.wasm import MsgExecuteContract
from terra_sdk.exceptions import LCDResponseError

from src import const
from src.helpers import to_u_unit, info, start_halo, stop_halo, get_address
from src.messages import get_sell_dict, get_buy_dict
from src.params import Params

# GET ASSET PRICE
def get_bluna_for_luna_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving bluna for luna price', params)
    sent_amount = to_u_unit(params.amount_luna)
    result = get_swap_price(sent_amount, terra, const.luna_info)
    stop_halo(spinner)
    return result


def get_mspy_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mSPY for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_mspy_swap_price(sent_amount, terra, const.ust_info)
    stop_halo(spinner)
    return result

def get_maapl_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mAAPL for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.maapl_ust)
    stop_halo(spinner)
    return result

def get_mbtc_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mBTC for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.mbtc_ust)
    stop_halo(spinner)
    return result

def get_miau_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mIAU for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.miau_ust)
    stop_halo(spinner)
    return result

def get_mko_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mKO for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.mko_ust)
    stop_halo(spinner)
    return result

def get_mtsla_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mTSLA for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.mtsla_ust)
    stop_halo(spinner)
    return result

def get_mtwtr_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mTWTR for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_masset_swap_price(sent_amount, terra, const.ust_info, const.mtwtr_ust)
    stop_halo(spinner)
    return result

def get_all_mirror_for_ust_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving mASSETs for UST price', params)
    sent_amount = to_u_unit(params.amount_ust)
    result = get_all_mirror_swap_price(sent_amount, terra)
    stop_halo(spinner)
    return result


def get_luna_for_bluna_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving bluna for luna price', params)
    sent_amount = to_u_unit(params.amount_bluna)
    result = get_swap_price(sent_amount, terra, const.bluna_info)
    stop_halo(spinner)
    return result


def get_ust_for_mspy_price(terra: LCDClient, params: Params):
    spinner = start_halo('Retrieving UST for mSPY price', params)
    sent_amount = to_u_unit(params.amount_mspy)
    result = get_mspy_swap_price(sent_amount, terra, const.mspy_info)
    stop_halo(spinner)
    return result

# SIMULATE SWAPS


def get_swap_price(sent_amount: int, terra: LCDClient, info_dict: Dict):
    return_amount = int(terra.wasm.contract_query(const.luna_bluna, {
        "simulation": {
            "offer_asset": {
                "info": info_dict,
                "amount": str(sent_amount)
            }}
    })['return_amount'])
    return return_amount, sent_amount / return_amount


def get_mspy_swap_price(sent_amount: int, terra: LCDClient, info_dict: Dict):
    return_amount = int(terra.wasm.contract_query(const.mspy_ust, {
        "simulation": {
            "offer_asset": {
                "info": info_dict,
                "amount": str(sent_amount)
            }}
    })['return_amount'])
    return return_amount, sent_amount / return_amount

def get_masset_swap_price(sent_amount: int, terra: LCDClient, info_dict: Dict, pair_address: str):
    return_amount = int(terra.wasm.contract_query(pair_address, {
        "simulation": {
            "offer_asset": {
                "info": info_dict,
                "amount": str(sent_amount)
            }}
    })['return_amount'])
    return return_amount, sent_amount / return_amount

def get_all_mirror_swap_price(sent_amount: int, terra: LCDClient):
    assets = const.massets
    for pair in assets:
        return_amount = int(terra.wasm.contract_query(str(pair), {
        "simulation": {
            "offer_asset": {
                "info": {
                    "token": {
                        "contract_addr": str(assets[pair])
                    },
                    "amount": str(sent_amount)
                }}}
    })['return_amount'])
    return return_amount, sent_amount / return_amount

# BUYING/SELLING/SWAPPING
def buy(params: Params, terra: LCDClient, belief_price: float, wallet: Wallet) -> bool:
    msg = MsgExecuteContract(wallet.key.acc_address, const.luna_bluna,
                             get_buy_dict(belief_price, params), Coins(uluna=to_u_unit(params.amount_luna)))
    return execute_contract(msg, terra, wallet, params)


def mirror_buy(params: Params, terra: LCDClient, belief_price: float, wallet: Wallet) -> str:
    # print("Account #is:" + wallet.account_number())
    # print("Account PubKey is:" + wallet.key.acc_pubkey)
    # print(wallet.key)
    acc = get_address().strip()
    print("Buying with wallet: " + acc)
    # acc = ast.literal_eval(wallet.key.val_address)

    # return execute_contract(msg, terra, wallet, params)
    return mAssetSwap(belief_price, params, terra, wallet)


def sell(params: Params, terra: LCDClient, belief_price: float, wallet: Wallet) -> bool:
    msg = MsgExecuteContract(wallet.key.acc_address, const.bluna_contract,
                             get_sell_dict(belief_price, params))
    return execute_contract(msg, terra, wallet, params)


def mirror_sell(params: Params, terra: LCDClient, belief_price: float, wallet: Wallet) -> bool:
    msg = MsgExecuteContract(wallet.key.acc_address, const.mspy_contract,
                             get_sell_dict(belief_price, params))
    return execute_contract(msg, terra, wallet, params)


def execute_contract(msg, terra, wallet, params: Params) -> bool:
    # execute_tx: StdTx = wallet.create_and_sign_tx(msg.execute_msg)
    # execute_tx_result: BlockTxBroadcastResult = terra.tx.broadcast(execute_tx)
    info("transaction hash:", params.should_log())
    # info(str(execute_tx_result.txhash), params.should_log())
    return "this function is deprecated" is None


def mAssetSwap(belief_price: float, params: Params, terra: LCDClient, wallet: Wallet):
        coins = Coins(uusd=to_u_unit(params.amount_ust))

        contract = const.mspy_ust
        amount = str(to_u_unit(params.amount_ust))
        msg = {
        "swap": {
            "belief_price": str(belief_price),
            "max_spread": str(params.spread),
            "offer_asset": {
                "amount": amount,
                "info": {
                    "native_token": {
                        "denom": "uusd"
                    }
                }
            }
        }
        }
        execute_msg = {
            "send": {
                "contract": contract,
                "amount": str(amount),
                'msg': base64.b64encode(bytes(json.dumps(msg), "ascii")).decode(),
            }
        }
        txhash = execute_transaction(contract, execute_msg, coins, terra, wallet)
        return txhash

def execute_transaction( contract: str, execute_msg: list, coins: Coins, terra: LCDClient, wallet: Wallet):
    try:
        account_address = wallet.key.acc_address
        account_number = wallet.account_number()
        message = MsgExecuteContract(
                sender=account_address,
                contract=contract,
                execute_msg=execute_msg,
                coins=coins,
            )

        transaction = wallet.create_and_sign_tx(
                CreateTxOptions(
                account_number=account_number,
                msgs=[message],
                memo='Mir Tradr by Chigag Studio',
                ))

        result = terra.tx.broadcast(transaction)
    except LCDResponseError as err:
        return f'Execution of tx failed with: {err}'

    return result.txhash


