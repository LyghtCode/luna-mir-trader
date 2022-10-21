# -----------     trading     -----------
# PAIR ADDRESSES
from typing import Dict

luna_bluna = "terra1jxazgm67et0ce260kvrpfv50acuushpjsz2y0p"
maapl_ust = "terra1774f8rwx76k7ruy0gqnzq25wh7lmd72eg6eqp5"
mbtc_ust = "terra1prfcyujt9nsn5kfj5n925sfd737r2n8tk5lmpv"
miau_ust = "terra15kkctr4eug9txq7v6ks6026yd4zjkrm3mc0nkp"
mko_ust = "terra1y7vdguewgus669kcxjlwughyxtdt3kheys05q0"
mspy_ust = "terra14hklnm2ssaexjwkcfhyyyzvpmhpwx6x6lpy39s"
mtsla_ust = "terra1pdxyk2gkykaraynmrgjfq2uu7r9pf5v8x7k4xk"
mtwtr_ust = "terra1ea9js3y4l7vy0h46k4e5r5ykkk08zc3fx7v4t8"

# TOKEN CONTRACTS
bluna_contract = "terra1kc87mu460fwkqte29rquh4hc20m54fxwtsx7gp"
maapl_contract = "terra1vxtwu4ehgzz77mnfwrntyrmgl64qjs75mpwqaz"
mbtc_contract = "terra1rhhvx8nzfrx5fufkuft06q5marfkucdqwq5sjw"
miau_contract = "terra10h7ry7apm55h4ez502dqdv9gr53juu85nkd4aq"
mko_contract = "terra1qsnj5gvq8rgs7yws8x5u02gwd5wvtu4tks0hjm"
mspy_contract = "terra1aa00lpfexyycedfg5k2p60l9djcmw0ue5l8fhc"
mtsla_contract = "terra14y5affaarufk3uscy2vr6pe6w6zqf2wpjzn5sh"
mtwtr_contract = "terra1cc3enj9qgchlrj34cnzhwuclc4vl2z3jl7tkqg"

luna_info = {
    "native_token": {
        "denom": "uluna"
    }
}
ust_info = {
    "native_token": {
        "denom": "uusd"
    }
}
# has contract address of tokens used for querying
bluna_info = {
    "token": {
        "contract_addr": "terra1kc87mu460fwkqte29rquh4hc20m54fxwtsx7gp"
    }
}
mspy_info = {
    "token": {
        "contract_addr": "terra1aa00lpfexyycedfg5k2p60l9djcmw0ue5l8fhc"
    }
}

# ALPHABETICAL DICT OF mASSET: {PAIR_ADDRESS:TOKEN_ADDRESS}
massets: Dict[str, str] = {
    # mAAPL
    "terra1774f8rwx76k7ruy0gqnzq25wh7lmd72eg6eqp5": "terra1vxtwu4ehgzz77mnfwrntyrmgl64qjs75mpwqaz",
    # mBTC
    "terra1prfcyujt9nsn5kfj5n925sfd737r2n8tk5lmpv": "terra1rhhvx8nzfrx5fufkuft06q5marfkucdqwq5sjw",
    #mIAU
    "terra15kkctr4eug9txq7v6ks6026yd4zjkrm3mc0nkp": "terra10h7ry7apm55h4ez502dqdv9gr53juu85nkd4aq",
    #mKO
    "terra1y7vdguewgus669kcxjlwughyxtdt3kheys05q0": "terra1qsnj5gvq8rgs7yws8x5u02gwd5wvtu4tks0hjm",
    #mSPY
    "terra14hklnm2ssaexjwkcfhyyyzvpmhpwx6x6lpy39s": "terra1aa00lpfexyycedfg5k2p60l9djcmw0ue5l8fhc",
    #mTSLA
    "terra1pdxyk2gkykaraynmrgjfq2uu7r9pf5v8x7k4xk": "terra14y5affaarufk3uscy2vr6pe6w6zqf2wpjzn5sh",
    #mTWTR
    "terra1ea9js3y4l7vy0h46k4e5r5ykkk08zc3fx7v4t8": "terra1cc3enj9qgchlrj34cnzhwuclc4vl2z3jl7tkqg"
}
buy = 0
sell = 1

# -----------     loans     -----------
market_address = "terra1sepfj7s0aeg5967uxnfk4thzlerrsktkpelm5s"
overseer_address = "terra1tmnqgvg567ypvsvk6rwsga3srp7e3lg6u0elp8"
aust_address = "terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu"
market_api_url = "https://api.anchorprotocol.com/api/v1/market/ust"

# -----------     uncategorized     -----------
log_file = "out.log"
gas_price_url = "https://fcd.terra.dev/v1/txs/gas_prices"
# MAINNET
# chain_id = "columbus-5"
chain_id = "bombay-12"
lcd_url = "https://lcd.terra.dev"
