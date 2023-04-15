from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','18722297'))
    API_HASH = getenv('API_HASH','32c669fd369c589c3b62eb16531c42e6')
    BOT_TOKEN = getenv('BOT_TOKEN','5599241378:AAHudNN_qNUiqjy4W1mJg6Ei99JW8Z2IjAM')

config = Config()
