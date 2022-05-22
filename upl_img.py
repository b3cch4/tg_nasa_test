import asyncio
import telegram


async def main():
    bot = telegram.Bot("5316370122:AAEwKTc3VvZPD1EBLzAtQ5gC9HO42YG0cFY")
    async with bot:
        await bot.send_document(
            chat_id=-1001633682543, 
            document=open('images/apod/0.jpg', 'rb')
        )
        
        
if __name__ == '__main__':
    asyncio.run(main())
    