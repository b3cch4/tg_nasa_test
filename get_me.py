import asyncio
import telegram


async def main():
    bot = telegram.Bot("5316370122:AAEwKTc3VvZPD1EBLzAtQ5gC9HO42YG0cFY")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())