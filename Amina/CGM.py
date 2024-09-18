from Keyboards import languages_kb, menu_kb
from Config import bot, get_translation as gt, States, messages_ids


async def languages(chat_id, state):
    text = (
    "Choose your language\n"
    "选择你的语言\n"
    "Выбери язык"
    )
    await bot.send_message(chat_id, text, reply_markup=languages_kb)
    await state.set_state(States.languages)


async def menu(lc, chat_id, state):
    text = await gt(lc, 'Menu', 'menu')
    kb = await menu_kb(lc)
    msg = await bot.send_message(chat_id, text, reply_markup=kb)
    messages_ids[chat_id] = msg.message_id
    await state.set_state(States.menu)
