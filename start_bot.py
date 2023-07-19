import time
from aiogram import executor


from dispatcher import dp
from main import *

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=False)
    except Exception as e:
        pass
