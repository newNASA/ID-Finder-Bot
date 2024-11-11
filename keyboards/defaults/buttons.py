from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat
from aiogram.types.keyboard_button_request_user import KeyboardButtonRequestUser

button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(
            text="👤 Foydalanuvchi IDsi",
            request_user=KeyboardButtonRequestUser(request_id=2300, user_is_bot=False)
        )],
        [KeyboardButton(
            text="👥 Guruh IDsi",
            request_chat=KeyboardButtonRequestChat(request_id=2301, chat_is_channel=False)
        )]
    ]
)