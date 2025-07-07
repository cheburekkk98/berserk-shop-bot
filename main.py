from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '7998828472:AAGdcejf5ngVtcmKVXYWxvX97Ae0NSOAHiU'
ADMIN_ID = 135016702

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Магазин", url="https://t.me/Berserk_Shop_1"),
        InlineKeyboardButton("Цены", url="https://t.me/Berserk_Shop_1"),
        InlineKeyboardButton("О нас", callback_data="about")
    )
    await message.answer("Добро пожаловать в Berserk Shop!", reply_markup=keyboard)

@dp.callback_query_handler(text="about")
async def about(callback: types.CallbackQuery):
    await callback.message.edit_text("Проект от BerserkNet. Работаем 24/7.")

@dp.message_handler(commands=['stats'])
async def stats(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        members = await bot.get_chat_members_count(message.chat.id)
        await message.answer(f"👥 Участников: {members}")
    else:
        await message.answer("⛔ Нет доступа.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
