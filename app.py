import asyncio
import handlers
from loader import dp, bot
from utils.notify import start_up,shut_up
async def main():
    dp.startup.register(start_up)
    dp.shutdown.register(shut_up)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session().close()

if __name__ == "__main__":
    asyncio.run(main())