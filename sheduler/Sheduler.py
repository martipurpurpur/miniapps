from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
from sheduler import views

TOKEN = "5059020279:AAF0uIZfsxlQrRiuWFqPTGmMxWu7P3jjBQM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f"Я бот. Приятно познакомиться, {msg.from_user.first_name}")

@dp.message_handler(commands=['shedule'])
async def send_shedule(msg: types.Message):
    shedule = views.get_all_days()
    print(shedule)
    await msg.reply_to_message(f"Расписание: {shedule}")

@dp.message_handler(commands=['today'])
async def send_day_shedule(msg: types.Message):
    current_day = datetime.date.today().strftime('%d')
    print(current_day)
    shedule_day = views.get_day(current_day)
    print(shedule_day)
    await msg.reply_to_message(f"Расписание на сегодня: {shedule_day}")

@dp.message_handler(commands=['time'])
async def send_time(msg: types.Message):
    current_day = datetime.date.today().strftime('%d')
    time_over = views.time_over(current_day)
    print(time_over)
    await msg.reply_to_message(f"Расписание на сегодня: {time_over}")

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    request_day = msg.text.lower()
    print(request_day)
    response_shedule = views.get_day(request_day)
    if response_shedule:
        await msg.answer(f'Расписание на {request_day}: {response_shedule}')
    else:
        await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
   executor.start_polling(dp)