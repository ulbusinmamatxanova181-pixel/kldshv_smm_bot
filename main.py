import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

# Sozlamalar
API_TOKEN = '8710762001:AAEG-P8cvckH3SCdl3SBaEmKFhw8ezbhXRo'
SMM_API_URL = 'https://panelingiz-sayti.com/api/v2' # SMM panelingiz API manzili
SMM_API_KEY = 'd411f56336e40fe29c0e7750010c7545'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("SMM Nakrutka botiga xush kelibsiz!\nBuyurtma berish uchun: havola miqdor")

@dp.message_handler()
async def order(message: types.Message):
    try:
        parts = message.text.split()
        link = parts[0]
        qty = parts[1]
        
        # API so'rov
        data = {'key': SMM_API_KEY, 'action': 'add', 'service': 1, 'link': link, 'quantity': qty}
        res = requests.post(SMM_API_URL, data=data).json()
        
        if 'order' in res:
            await message.answer(f"✅ Buyurtma qabul qilindi! ID: {res['order']}")
        else:
            await message.answer(f"❌ Xatolik: {res.get('error', 'Noma\'lum xato')}")
    except:
        await message.answer("⚠️ Noto'g'ri format. Namuna: https://t.me/kanal 100")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
