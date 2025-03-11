from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Вставляем сюда токен от BotFather
TOKEN = "7984586246:AAH_OXaiElz5cmxpHW1muDxmXn771_U7pGQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Создаем клавиатуру с кнопкой
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton("📞 Контакты магазина")
keyboard.add(button)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Нажмите кнопку ниже, чтобы получить контакты магазина. 👇", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "📞 Контакты магазина")
async def send_contacts(message: types.Message):
    contacts = """📍 **EVILCO Тайланд Бали**  
🌐 Сайт: www.evil24.vip  
🤖 Бот: @trswewwbot
📞 Оператор: @evcdady   
📚 Канал: https://t.me/+O3qPoX7gNpc4ZjIx
🕘 Чат: https://t.me/+qsaow2M-J-NlNDNi"""
    await message.answer(contacts, parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)