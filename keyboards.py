from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import *


def get_keyboard_consultation():
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(BUT1, callback_data="call_manager")
    ib2 = InlineKeyboardButton(BUT2, url="https://t.me/korpusnay_mebeli")
    ikb.add(ib1, ib2)
    return ikb


def get_keyboard_check():
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton('✅ Верно', callback_data="yes_check")
    ib2 = InlineKeyboardButton('❌ Не верно', callback_data="no_check")
    ikb.add(ib1, ib2)
    return ikb


def get_keyboard_chanel():
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(BUT3, url="https://t.me/mebelshkaffbot?start=zakaz")
    ib2 = InlineKeyboardButton(BUT4, url="https://t.me/mebelshkaffbot?start=order_zamer")
    ikb.add(ib1, ib2)
    return ikb


def get_keyboard_menu():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton(BUT5, request_contact=True)
    kb2 = KeyboardButton(BUT8)
    kb3 = KeyboardButton(BUT6, request_contact=True)
    rkb.add(kb1)
    rkb.add(kb2)
    rkb.add(kb3)
    return rkb


def get_keyboard_type_production():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton(BUT10)
    kb2 = KeyboardButton(BUT11)
    kb3 = KeyboardButton(BUT12)
    kb4 = KeyboardButton(BUT101)
    kb5 = KeyboardButton(BUT123)
    kb6 = KeyboardButton(BUT112)
    rkb.add(kb1, kb4)
    rkb.add(kb2, kb5)
    rkb.add(kb3, kb6)
    return rkb


def get_keyboard_material():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton(BUT13)
    kb2 = KeyboardButton(BUT14)
    kb3 = KeyboardButton(BUT15)
    rkb.add(kb1)
    rkb.add(kb2)
    rkb.add(kb3)
    return rkb


def get_keyboard_number():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton(BUT9, request_contact=True)
    rkb.add(kb1)
    return rkb


def get_keyboard_manager():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton("📞 Связаться с менеджером", request_contact=True)
    rkb.add(kb1)
    return rkb


def get_keyboard_order():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1 = KeyboardButton(BUT7, request_contact=True)
    rkb.add(kb1)
    return rkb