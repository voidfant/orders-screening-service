import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from psqlActions import PsqlActions

API_TOKEN = '5571330842:AAGKoBnF5XXumwCR5UisQQLs5o0xLwrCfEE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

chat_ids = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not PsqlActions().findUserInMailingList(message.chat.id):
        PsqlActions().addUserToMailingList(message.chat.id)
        await message.reply('Добавил Вас в список рассылки.\nЧтобы выйти из него, вызовите /quit', reply=False)
    else:
        await message.reply('Вы уже получаете рассылку.', reply=False)


@dp.message_handler(commands=['quit'])
async def quit(message: types.Message):
    PsqlActions().removeUserFromMailingList(message.chat.id)
    await message.reply('Удалил Вас из списка рассылки.\nЧтобы вернуться в него, вызовите /start', reply=False)


@dp.message_handler()
async def unrecognized(message: types.Message):
    await message.reply('Не распознал команду.\nДоступные команды: /start, /quit.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
