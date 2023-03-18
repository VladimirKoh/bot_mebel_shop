from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from config import *

from dotenv import load

from keyboards import *

import os


load()


ADMIN_CHAT = os.getenv('ADMIN_CHAT_ID')


storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1_WrV7BFeDaYDGweJhJYoqvaPouefqAZWlxMOm9INq0Q'


class StateUsersData(StatesGroup):
    address = State()
    type_production = State()
    material = State()
    number = State()
    finish_state = State()


async def connect_sheets(name, number, address='', type_production='', material=''):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http = httpAuth)
    range_ = 'Лист1!A1'  # TODO: Update placeholder value.
    value_input_option = 'RAW'  # TODO: Update placeholder value.
    value_range_body = {
        'values': [[name, number, address, type_production, material]]
    }
    values = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, 
                                                    range=range_, 
                                                    valueInputOption=value_input_option, 
                                                    body=value_range_body).execute()

async def edit_text_message(message: types.Message, status: bool):
    with suppress(MessageNotModified):
        if status:
            await message.edit_text("✅ Ваша заявка успешно отправлена\n\nДля возврата в главное меню введите команду <b>/start</b>")
        else:
            await message.edit_text("😞 Вы отменили отправку заявки\n\nДля возврата в главное меню введите команду <b>/start</b>")


@dp.message_handler(commands=['start'], state="*")
async def command_start_process(message: types.Message, state: FSMContext):
    if message.text[7:] == 'order_zamer':
        await state.set_state(StateUsersData.address.state)
        return await message.answer('Для того чтобы заказать замерщика необходимо заполнить данные.\nВсего 4 шага!\n\nВведите свой адрес:', reply_markup=ReplyKeyboardRemove())
    elif message.text[7:] == 'zakaz':
        return await message.answer('Для заказа необходимо оставить номер телефон', reply_markup=get_keyboard_number())
    await state.finish()
    await message.answer(TEXT1, reply_markup=get_keyboard_menu())
    await message.answer_photo(photo=open('./images/start.png', 'rb'), reply_markup=get_keyboard_consultation())


@dp.message_handler(commands=['add_startadmin'])
async def command_add_post_photo(message: types.Message):
    text = """<b>Мебель на заказ в Москве от производителя
"Круглый шкаф"</b>
12 летпроизводим мебель под заказ
7500+выполненных проектов
5 днейна изготовление мебели из ЛДСП
-25% скидки на сезонные предложения
Бесплатный выезд замерщика с образцами
Бесплатно выполним 3D-проект будущей мебели
Привезем вашу мебель по указанному адресу
Предоставим гарантию на всю продукцию нашей фабрики!
#мебельназаказ #шкафыназаказмосква #шкафыкупемосква #фабрикамебелимосква #шкафымосква #мебельотпроизводителя"""
    await bot.send_photo(chat_id=ADMIN_CHAT, photo=open('./images/00.png', 'rb'), caption=text, reply_markup=get_keyboard_chanel())



@dp.message_handler(content_types=types.ContentType.PHOTO)
async def command_add_post_photo_admin(message: types.Message):
    command, *text = message.caption.split()
    text = " ".join(text)
    if command == '/add_post_admin_with_photo':
        return await bot.send_photo(chat_id=ADMIN_CHAT, photo=message.photo[0].file_id, caption=text, reply_markup=get_keyboard_chanel())


@dp.message_handler(commands=['add_catalog_albumadmin'])
async def command_add_post(message: types.Message):
    # media = types.MediaGroup()
    # media.attach_photo(photo=open('./images/20-1.png', 'rb'), caption=a20)
    # media.attach_photo(photo=open('./images/20-2.png', 'rb'))
    # await bot.send_media_group(chat_id=ADMIN_CHAT, media=media)

    media = types.MediaGroup()
    media.attach_photo(photo=open('./images/21-1.png', 'rb'), caption=a21)
    media.attach_photo(photo=open('./images/21-2.png', 'rb'))
    await bot.send_media_group(chat_id=ADMIN_CHAT, media=media)

    media = types.MediaGroup()
    media.attach_photo(photo=open('./images/22-1.png', 'rb'), caption=a22)
    media.attach_photo(photo=open('./images/22-2.png', 'rb'))
    media.attach_photo(photo=open('./images/22-3.png', 'rb'))
    media.attach_photo(photo=open('./images/22-4.png', 'rb'))
    await bot.send_media_group(chat_id=ADMIN_CHAT, media=media)

    media = types.MediaGroup()
    media.attach_photo(photo=open('./images/23-1.png', 'rb'), caption=a23)
    media.attach_photo(photo=open('./images/23-2.png', 'rb'))
    media.attach_photo(photo=open('./images/23-3.png', 'rb'))
    media.attach_photo(photo=open('./images/23-4.png', 'rb'))
    await bot.send_media_group(chat_id=ADMIN_CHAT, media=media)



@dp.message_handler(commands=['add_catalogadmin'])
async def command_add_catalog(message: types.Message):
    # ,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19
    list_images = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19]
    for i in range(17, 20):
        await bot.send_photo(chat_id=ADMIN_CHAT, photo=open(f'./images/{i}.png', 'rb'), caption=list_images[i - 1], reply_markup=get_keyboard_chanel())


@dp.message_handler(Text(equals=BUT8))
async def commantd_zamer(message: types.Message, state: FSMContext):
    await message.answer("Укажите свои данные для вызова замерщика\n\nВведите адрес:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(StateUsersData.address.state)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=StateUsersData.number)
async def get_number_user(message: types.Message, state: FSMContext):
    name = message.contact.full_name
    number = message.contact.phone_number
    await state.update_data(name=name, number=number)
    user_data = await state.get_data()
    text = f"Ваша заявка:\n\n<b>Телефон:</b> {user_data.get('number', 'Не указан')}\n<b>Адрес доставки:</b> {user_data.get('address', 'Не указан')}\n<b>Вид продукции:</b> {user_data.get('type_production', 'Не указан')}\n<b>Материал:</b> {user_data.get('material', 'Не указан')}"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await message.answer('Проверьте данные, если все правильно то отправляем', reply_markup=get_keyboard_check())
    await StateUsersData.next()


@dp.message_handler(state=StateUsersData.address)
async def get_address_user(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)
    await message.answer("2/4\nВыберете тип продукции", reply_markup=get_keyboard_type_production())
    await StateUsersData.next()


@dp.message_handler(state=StateUsersData.type_production)
async def get_type_production_user(message: types.Message, state: FSMContext):
    type_production = message.text
    await state.update_data(type_production=type_production)
    await message.answer("3/4\nУкажите материал", reply_markup=get_keyboard_material())
    await StateUsersData.next()


@dp.message_handler(state=StateUsersData.material)
async def get_material_user(message: types.Message, state: FSMContext):
    material = message.text
    await state.update_data(material=material)
    await message.answer('4/4\nПредоставте ваш номер телефона', reply_markup=get_keyboard_number())
    await StateUsersData.next()


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contacts(message: types.Message):
    await connect_sheets(message.contact.full_name, message.contact.phone_number)
    await message.answer(TEXT2, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types=types.ContentType.all)
async def photo(message: types.Message):
    print(message)


@dp.callback_query_handler(Text(equals='order_zamer'))
async def command_order(callback: types.CallbackQuery):
    await callback.answer(None)
    await callback.bot.send_message(chat_id=callback.from_user.id, text=TEXT3, reply_markup=get_keyboard_order())



@dp.callback_query_handler(Text(equals='yes_check'), state=StateUsersData.finish_state)
async def callback_yes_check(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer('Отправлено')
    user_data = await state.get_data()
    name = user_data.get('name', 'Не указано')
    number = user_data.get('number', 'Не указано')
    address = user_data.get('address', 'Не указано')
    type_production = user_data.get('type_production', 'Не указано')
    material = user_data.get('material', 'Не указано')
    await connect_sheets(name, number, address, type_production, material)
    await edit_text_message(callback.message, True)
    await state.finish()


@dp.callback_query_handler(Text(equals='no_check'), state=StateUsersData.finish_state)
async def callback_no_check(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer('Заявка отменена')
    await edit_text_message(callback.message, False)
    await state.finish()


@dp.callback_query_handler(Text(equals='call_manager'))
async def callback_manager(callback: types.CallbackQuery):
    await callback.answer('Бесплатная консультация')
    await callback.message.answer('Для того чтобы заказать бесплатную консультацию нажмите кнопку <b>«Связаться с менеджером»</b>', reply_markup=get_keyboard_manager())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)