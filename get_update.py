import asyncio
import telegram


async def main():
    bot = telegram.Bot("5316370122:AAEwKTc3VvZPD1EBLzAtQ5gC9HO42YG0cFY")
    async with bot:
        for i in await bot.get_updates():
            print(i)
            print(type(i))
            print('----------')
            

if __name__ == '__main__':
    asyncio.run(main())
	
	
	