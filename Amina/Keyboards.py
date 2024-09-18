from aiogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from Config import get_translation as gt

languages_kb = ikm(inline_keyboard=[
    [
        ikb(text="English🇺🇸", callback_data="EN"),
        ikb(text="中文🇨🇳", callback_data="ZH"),
        ikb(text="Русский🇷🇺", callback_data="RU")
    ]
])


async def menu_kb(lc):
    kb = ikm(inline_keyboard=[
        [ikb(text=await gt(lc, "Menu", "about"), callback_data="about")],
        [ikb(text=await gt(lc, "Menu", "day"), callback_data="day")],
        [ikb(text=await gt(lc, "Menu", "meeting"), callback_data="meeting")],
        [ikb(text=await gt(lc, "Menu", "secret"), callback_data="secret")],
        [ikb(text=await gt(lc, "Menu", "rate"), callback_data="rate")],
        [ikb(text=await gt(lc, "Menu", "rwushi"), callback_data="rwushi")]
    ])
    return kb


async def back_kb(lc):
    kb = ikm(inline_keyboard=[
        [ikb(text=await gt(lc, "Subcommon", "return_back"), callback_data="back")]
    ])
    return kb
