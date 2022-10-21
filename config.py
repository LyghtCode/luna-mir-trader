#!/usr/bin/python3

from os import environ

# SETUP
# Replace the seed phrase with yours
# I strongly recommend to add your seed, API keys, passwords as an environment variable. You can find out how to set this up here: https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0
NETWORK = 'MAINNET' # TESTNET or MAINNET
if NETWORK == 'MAINNET':
    mnemonic = environ.get('MNEMONIC_MAIN', 'color private climb option speak refuse banana carpet pave gather corn horse fever sibling section enlist style kangaroo ugly neck grow frequent fog victory')
else:
    mnemonic = environ.get('MNEMONIC_TEST', 'color private climb option speak refuse banana carpet pave gather corn horse fever sibling section enlist style kangaroo ugly neck grow frequent fog victory')

MIR_min_price = 3  # Minimum price acceptable to sell in UST https://coinhall.org/charts/terra/terra1amv303y8kzxuegvurh0gug2xe9wkgj65enq2ux
MIR_min_total_value = 96 # Minimum amount (qty * price in UST) to claim and sell/deposit MIR tokens.

SPEC_min_price = 7 # https://coinhall.org/charts/terra/terra1tn8ejzw8kpuc87nu42f6qeyen4c7qy35tl8t20
SPEC_min_total_value = 138

ANC_min_price = 4 # https://coinhall.org/charts/terra/terra1gm5p3ner9x9xpwugn9sp6gvhd0lwrtkyrecdn3
ANC_min_total_value = 111

# WITHDRAWAL MIR, SPEC, ANC, UST FROM LIQUIDITY POOLS AND THEN SELL
MIR_withdraw_and_sell_if_min_price_is_reached = False
SPEC_withdraw_and_sell_if_min_price_is_reached = False
ANC_withdraw_and_sell_if_min_price_is_reached = False

# CLAIM MIR, SPEC, ANC REWARDS AND SELL THEM IMMEDIATELY
MIR_claim_and_sell_token = False
SPEC_claim_and_sell_token = False
ANC_claim_and_sell_token = False

# DEPOSIT MIR, SPEC, ANC REWARDS INTO LIQUIDITY POOLS
# min_price as well as min_total_value from the previous section will be both considered.
MIR_claim_and_deposit_in_LP = False
SPEC_claim_and_deposit_in_LP = False
ANC_claim_and_deposit_in_LP = False
Anchor_enable_withdraw_from_Anchor_Earn_to_deposit_in_LP = False

# MIRROR: CLAIMING UNLOCKED UST
Mirror_claim_unlocked_UST = False
Mirror_min_amount_UST_to_claim = 96

# ANCHOR BORROW: MAINTAIN LTV RATIO / REPAY BORROWED UST IF REQUIRED
# READ the example carefully, as Anchor works opposite for Mirror's liquidation ratio's logic.
# Example:  Let's say you would get liquidated at 60% or 0.6 LTV (borrowed_amount / deposited collateral).
#           The script will trigger a re-pay when 0.6 + lower_distance (by default: 0.6 + -0.1 = 0.5 = 50%) is reached.
#           It will repay debt to get back to 0.6 + target_distance (by default: 0.6 + -0.15 = 0.45 = 45%).
Anchor_enable_auto_repay_of_debt = False # Allow the script to withdraw deposited UST on Anchor Earn to repay the debt.
Anchor_enable_withdraw_of_deposited_UST = False # If even after a withdrawal of deposited UST, you don't have enough UST, you can perform a partial repayment.
Anchor_enable_partially_repay_if_not_enough_UST_in_wallet = False
Anchor_lower_distance = -0.1
Anchor_target_distance = -0.15
Anchor_min_repay_limit = 295 # Even if a re-pay is required to restore the required target_distance, it will not be executed if the _min_repay_limit is not met.

# ANCHOR: BORROW MORE UST FOR YOUR DEPOSITED COLLATERAL
Anchor_enable_auto_borrow_UST = False # If you want, you can tell the script to borrow more from Anchor if your set upper_distance allows it.
Anchor_upper_distance = -0.2  # Upper distance above that a withdrawal will be executed.
#           If the collateral ratio is bigger than 0.6 + upper_distance (by default: 0.6 + -0.2 = 0.40 = 40%) it will withdraw collateral.
#           It will borrow more UST to get back to 0.6 + target_distance (by default: 0.6 + -0.15 = 0.45 = 45%).
Anchor_min_borrow_limit = 295 # Set a minimum limit; otherwise the script may borrow continuously.
Anchor_borrow_cooldown = 1 # Cooldown in days after collateral has been withdrawn. Example: 3 means it happens only once every 3 days.

# ANCHOR EARN: DEPOSIT UST FROM SELLING ANC, MIR, SPEC
Anchor_Earn_enable_deposit_UST = False
Anchor_Earn_min_deposit_amount = 148
Anchor_Earn_min_balance_to_keep_in_wallet = 150 # This this bot also deposits token in LP, you should have a UST balance in your wallet.

# MIRROR: MAINTAIN COLLATERAL RATIO / DEPOSIT COLLATERAL IF REQUIRED
# Example:  Let's say the minimum ratio for the given mAsset on Mirror is 150% or 1.5.
#           The script will trigger a collateral deposit when 1.5 + lower_distance (by default: 1.5 + 0.25 = 1.75 = 175%) is reached.
#           It will deposit enough collateral to get back to 1.5 + target_distance (by default: 1.5 + 0.5 = 2.00 = 200%).
Mirror_enable_deposit_collateral = False
Mirror_lower_distance = 0.25
Mirror_target_distance = 0.50
Mirror_min_deposit_limit_in_UST = 295 # Even if a deposit is required to restore the required target_distance, it will not be executed if the min_deposit_limit_in_UST is not met.

# MIRROR: WITHDRAWAL OF COLLATERAL
# If you want, you can tell the script to withdraw collateral if your set upper_distance allows it.
# Withdrawals are only allowed for legacy assets within the market hours of the NYSE. The script checks for that.
Mirror_enable_withdraw_collateral = False
Mirror_upper_distance = 0.75  # Upper distance above that a withdrawal will be executed.
#           If the collateral ratio is bigger than 1.5 + upper_distance (by default: 1.5 + 0.75 = 2.25 = 225%) it will withdraw collateral.
#           It will deposit enough collateral to get back to 1.5 + target_distance (by default: 1.5 + 0.2 = 1.7 = 170%).
Mirror_min_withdraw_limit_in_UST = 295
Mirror_withdraw_cooldown = 1 # Cooldown in days after collateral has been withdrawn. Example: 3 means it happens only once every 3 days. 0 means it will always happen.

# NOTIFICATIONS
Send_me_a_report = True # Logs summary of what has happened, if something has happened send as by NOTIFICATIONS below defined.
                        # Also, this report will always include WARNINGS about failed transactions or insufficient wallet balance.
Notify_Slack = False
Notify_Telegram = False
Notify_Gmail = False
Email_format = 'HTML' # Define to receive the report and status update in TEXT or HTML
Send_me_a_status_update = True # Even if nothing is done by the script, you can receive a status update with your key infos your Anchor / Positions.
Status_update_frequency = 24 # In hours. 24 means once per 24h.
Status_update_time = '14:00' # Time to send you the status_update based on server time

# SCHEDULER
Run_interval_for_Scheduler = 5 # in minutes. 5 means every 5 minutes

# DEBUGGING
Debug_mode = True  # If False, default.log will include almost everything. If False only WARNINGs and ERRORs will be logged.
Disable_all_transaction_defs = True # So you can test the script with your Mainnet account, but no transaction will be executed.
Return_failed_tx = False # If Disable_all_transaction_def is False, you can return for all transaction_defs a failed transaction to test.

# LOGGING
Logging_detail = 'simple'  # detailed, moderate, simple. Recommended: simple.

# OTHER
Safety_multiple_on_transaction_fees = 3 # Multiplier for Anchor Borrow, Repay, Deposit. So you will have a bit of UST in your wallet left for future transactions.
Block_failed_transaction_cooldown = 6 # In hours. In case a transaction fails that transaction can be blocked for a certain amount of time.

# NOTIFICATION SETUP
# I strongly recommend to add your seed, API keys, passwords as an environment variable. You can find out how to set this up here: https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0
TELEGRAM_TOKEN = environ.get('TELEGRAM_TOKEN', '') # See readme.md how to get this.
TELEGRAM_CHAT_ID = environ.get('TELEGRAM_CHAT_ID', '') # See readme.md how to get this.
SLACK_WEBHOOK_URL = environ.get('SLACK_WEBHOOK_URL', '') # See readme.md how to get this.

GMAIL_APP_PASSWORD = environ.get('GMAIL_APP_PASSWORD', 'cjutfanqprdodiby') # See readme.md how to get this.
GMAIL_ACCOUNT = 'myamazingemailaddress@gmail.com' # Your Gmail address you use for logging into your account.
EMAIL_SUBJECT = 'Terra One-Stop-Bot'
EMAIL_FROM = GMAIL_ACCOUNT # Normally the same as your main Gmail address.
EMAIL_TO = GMAIL_ACCOUNT # Normally the same as your main Gmail address.