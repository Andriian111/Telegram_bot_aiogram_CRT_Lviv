
from environs import Env
import logging
import os

env = Env()
env.read_env() 

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = env.str('BOT_TOKEN')
admins= env.list('admin_id')
ip=env.str('ip')
BLOCKCYPHER=env.str('BLOCKCYPHER')
qiwi=env.str('qiwi')
wallet=env.int('wallet')

aiogram_redis = {
    'host': ip,
}
redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
