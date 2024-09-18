from aiogram import Router, F
from Config import bot, States, get_language as gl, get_translation as gt, messages_ids
from Keyboards import menu_kb, back_kb
from DB import set_info

rq = Router()


@rq.message(F.text, States.about)
@rq.message(F.text, States.day)
@rq.message(F.text, States.meeting)
@rq.message(F.text, States.secret)
@rq.message(F.text, States.rate)
@rq.message(F.text, States.rwushi)
async def questions_handler(message, state):
    user_id = message.from_user.id
    chat_id = message.chat.id
    lc = await gl(user_id)
    message_id = messages_ids[user_id]

    state_str = await state.get_state()
    column = state_str.split(':')[1]

    if column in ('about', 'rwushi'):
        await bot.edit_message_text(
        text=await gt(lc, 'Questions', 'no_need'),
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=await back_kb(lc)
    )

    else:
        await set_info(user_id, message.text, column)
        await bot.edit_message_text(
            text=await gt(lc, 'Questions', 'reply'),
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=await back_kb(lc)
        )

    await message.delete()