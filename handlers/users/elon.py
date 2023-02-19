from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, MediaGroup

from states.elon import Elon
from loader import dp, bot
from aiogram import types

from datetime import date


# User qaysi tugmani bosganini aniqlab olamiz
@dp.message_handler(text="E'lon joylash 🗣", state='*')
async def elon_joylash(message: types.Message, state: FSMContext):
    text = "E'lon joylash uchun mashinaning nomini yuboring\n\nExm: Nexia 2"
    await message.reply(text=text)
    await Elon.nomi.set()

@dp.message_handler(state=Elon.nomi)
async def elon_nomi(message: types.Message, state: FSMContext):
    nomi = message.text
    await state.update_data(
        {'nomi': nomi}
    )
    text = "Yaxshi endi mashina rasmini yuboring, bitta rasm yuboring!"
    await message.answer(text=text)
    await Elon.rasm_1.set()

@dp.message_handler(content_types=ContentType.PHOTO, state=Elon.rasm_1)
async def elon_nomi(message: types.Message, state: FSMContext):
    rasm_1 = message.photo[-1].file_id
    await state.update_data(
        {'rasm_1': rasm_1}
    )
    text = "Yaxshi endi mashinaning  2-rasmini yuboring"
    await message.answer(text=text)
    await Elon.rasm_2.set()

@dp.message_handler(content_types=ContentType.PHOTO, state=Elon.rasm_2)
async def elon_nomi(message: types.Message, state: FSMContext):
    rasm_2 = message.photo[-1].file_id
    await state.update_data(
        {'rasm_2': rasm_2}
    )
    text = "Endi mashinaning  3-rasmini yuboring"
    await message.answer(text=text)
    await Elon.rasm_3.set()

@dp.message_handler(content_types=ContentType.PHOTO, state=Elon.rasm_3)
async def elon_nomi(message: types.Message, state: FSMContext):
    rasm_3 = message.photo[-1].file_id
    await state.update_data(
        {'rasm_3': rasm_3}
    )
    text = "Endi mashina nechanchi yilda chiqqanini yuboring\n\nExm: 2019"
    await message.answer(text=text)
    await Elon.yili.set()

@dp.message_handler(state=Elon.yili)
async def elon_nomi(message: types.Message, state: FSMContext):
    yili = message.text
    now = date.today().year
    if int(yili) < now:
        await state.update_data(
            {'yili': yili}
        )
        text = "Mashina necha km yurganini yuboring\n\nExm: 34550"
        await message.answer(text=text)
        await Elon.probeg.set()
    else:
        await message.answer(text="Noto'g'ri yil kiritildi!")
        await Elon.yili.set()

@dp.message_handler(state=Elon.probeg)
async def elon_nomi(message: types.Message, state: FSMContext):
    probeg = message.text
    await state.update_data(
        {'probeg': probeg}
    )
    text = "Mashina nimada yurishini yuboring\n\nExm: Benzin"
    await message.answer(text=text)
    await Elon.yoqilgi.set()

@dp.message_handler(state=Elon.yoqilgi)
async def elon_nomi(message: types.Message, state: FSMContext):
    yoqilgi = message.text
    await state.update_data(
        {'yoqilgi': yoqilgi}
    )
    text = "Mashina haqida qoshimcha malumot kiriting"
    await message.answer(text=text)
    await Elon.malumot.set()

@dp.message_handler(state=Elon.malumot)
async def elon_nomi(message: types.Message, state: FSMContext):
    malumot = message.text
    await state.update_data(
        {'malumot': malumot}
    )
    text = "Mashina narxini yuboring\n\nExm: 10.000(Dollarda hisoblanadi!)"
    await message.answer(text=text)
    await Elon.narxi.set()

@dp.message_handler(state=Elon.narxi)
async def elon_nomi(message: types.Message, state: FSMContext):
    narxi = message.text
    narx = narxi.split('.')
    if len(narx) == 2:
        await state.update_data(
            {'narxi': narxi}
        )
        text = "Telefon raqam yuboring\n\nExm: +998996667788"
        await message.answer(text=text)
        await Elon.telefon.set()
    else:
        await message.answer(text="Bu raqam yaroqsiz, boshqattan kiriting!\n\nExm: 10.000(Dollarda hisoblanadi!)")
        await Elon.narxi.set()
@dp.message_handler(state=Elon.telefon)
async def elon_nomi(message: types.Message, state: FSMContext):
    telefon = message.text
    if len(telefon) == 13 and telefon.startswith('+998'):
        await state.update_data(
            {'telefon': telefon}
        )
        text = "Manzil yuboring\n\nExm: Xorazm, Urganch"
        await message.answer(text=text)
        await Elon.manzil.set()
    else:
        await message.answer(text="Bu raqam yaroqsiz, boshqa raqam kiriting\n\nExm: +998996667788")
        await Elon.telefon.set()

@dp.message_handler(state=Elon.manzil)
async def elon_nomi(message: types.Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {'manzil': manzil}
    )
    album = MediaGroup()

    data = await state.get_data()
    nomi = data.get('nomi')
    rasm_1 = data.get('rasm_1')
    rasm_2 = data.get('rasm_2')
    rasm_3 = data.get('rasm_3')
    yili = data.get('yili')
    probeg = data.get('probeg')
    yoqilgi = data.get('yoqilgi')
    malumot = data.get('malumot')
    narxi = data.get('narxi')
    telefon = data.get('telefon')
    manzil = data.get('manzil')

    album.attach_photo(photo=rasm_1)
    album.attach_photo(photo=rasm_2)
    album.attach_photo(photo=rasm_3)

    text = f"{nomi} Sotiladi\n\n" \
           f"📅 Yili: {yili}\n👣 Probegi: {probeg}\n" \
           f"Yoqilg'i: {yoqilgi}\n💰 Narxi: {narxi}\n" \
           f"✅ Qo'shimcha ma'lumot: {malumot}\n" \
           f"☎️ Tel: {telefon}\n🚩 Manzil: {manzil}"

    await bot.send_media_group(chat_id=message.chat.id, media=album)
    await message.answer(text=text)
    await state.finish()

