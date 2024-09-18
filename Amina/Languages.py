from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import BotCommand
from Config import bot, get_translation as gt, set_language as sl, States
from CGM import languages, menu
from DB import add_new_user as anu, language_set as ls

rl = Router()


@rl.message(CommandStart())
async def start_handler(message, state):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username
    await anu(user_id, username)
    await languages(chat_id, state)


@rl.callback_query(States.languages)
async def language_handler(callback, state):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    lc = callback.data
    await sl(user_id, lc)
    await callback.message.delete()
    await callback.answer(await gt(lc, 'Languages', 'language_chosen'), show_alert=True)
    await set_commands(lc)
    await menu(lc, chat_id, state)
    await ls(user_id, lc)


async def set_commands(lc):
    commands = [
        BotCommand(command="/start", description=await gt(lc, 'Commands', 'start'))
    ]
    await bot.set_my_commands(commands)
