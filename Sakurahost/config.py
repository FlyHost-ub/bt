"""
All the things that should be easibly changable
"""

import strings

# bot
BOT_TOKENS = {
    "main": "5822354429:AAEQbhb44O4lKF1XdHNw5ziDrpnncKPRlNw",
    "test": "6258793753:AAHtEm0CVnpDJAlO1uEPBwN9oOW-K3zBIk0"
}
BOT_TOKEN = BOT_TOKENS["main"]

# cryptopay
CRYPTOPAY_TOKENS = {
    "mainnet": "83883:AA1tJUGzwfRsplVE3zddVMoYN5gllNlDL3f",
    "testnet": "83883:AA1tJUGzwfRsplVE3zddVMoYN5gllNlDL3f"
}
CRYPTOPAY_TOKEN = CRYPTOPAY_TOKENS["testnet"]
CRYPTOPAY_TESTNET = CRYPTOPAY_TOKEN == CRYPTOPAY_TOKENS["testnet"]
CRYPTOPAY_EXPIRE = 3600  # crypto bot payments expire time in seconds

# other
IP = "5.42.74.35"
FORBIDDEN_PORTS = [1]
ADMINS = [5602778747]
admin = 5602778747
PRICE = 45  # in RUB
CARD = "5536914042528210"
USERBOTS = {
    "hikka": strings.HIKKA,
}
