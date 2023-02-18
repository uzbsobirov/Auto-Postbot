from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="E'lon joylash 🗣")
        ],
        [
            KeyboardButton(text="Hisobim 💰")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)