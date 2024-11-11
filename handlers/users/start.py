from aiogram.filters import Command, CommandStart
from loader import dp
from aiogram import types, F
from keyboards.defaults.buttons import button

@dp.message(CommandStart())
async def start_bot(message: types.Message):
    text = (
        f"Assalomu alaykum <b>{message.from_user.full_name}!</b> "
        f"Botimizga xush kelibsiz!\n"
        f"Sizning ID: <code>{message.from_user.id}</code>\n\n"
        "Agar boshqa kontaktlaringiz yoki guruhlaringizning ID sini bilmoqchi bo'lsangiz, kerakli tugmani bosing."
    )

    await message.answer(text, parse_mode="HTML", reply_markup=button)

@dp.message(F.user_shared)
async def contact_id(message:types.Message):
    user = message.user_shared
    await message.answer(f"Foydalanuvchi IDsi: {user.user_id}")

@dp.message(F.chat_shared)
async def chat_id(message:types.Message):
    chat = message.chat_shared
    await message.answer(f"Guruh IDsi: {chat.chat_id}")