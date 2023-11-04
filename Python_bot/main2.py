from aiogram import Bot, Dispatcher , executor
from aiogram.types import Message
import wikipedia

BOT_TOKEN = '6322005642:AAF-x2u85Y4kp8ulLuzr2BeKdgXjqOHgeYU'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', ])
async def starttt(message : Message):
    await message.reply(f'Assalomu aleykum {message.from_user.full_name} Botga xush kelibsiz')

@dp.message_handler(commands=['help' , ])
async def help(msg : Message):
    await msg.reply(f'Assalomu aleykum {msg.from_user.full_name} Bot sizga qanday yordam bera oladi ?')

@dp.message_handler()
async def wikifun(msg : Message):
    try:
        response = wikipedia.summary(msg.text)
        await msg.reply(response)
    except:
        await msg.reply('Bunday maqola mavjud emas😔 ')

# @dp.message_handler()
# async def answer(msg : Message):
#     await msg.reply(msg.text)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)