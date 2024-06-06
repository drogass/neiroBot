from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TELEGRAM_TOKEN
from neiro.neiro_gen import generate_image
from neiro.neiro_assistent import get_response
from neiro.neiro_consult import get_sovet

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Попробуй мою нейронку')

@dp.message_handler(commands= 'sovet')
async def analize_message(message:types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message .answer(response_text)

@dp.message_handler(commands= 'generate_image')
async def handle_message(message: types.Message):
    user = message.get_args()
    response_text = await get_response(user)
    user_text = response_text
    await message.reply(f'Вот твой улучшенный промт{user_text}')
    print(user_text)
    await message.reply('Идет генерация')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
