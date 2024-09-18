from aiogram import Router
from Config import States, get_language as gl, get_translation as gt
from Keyboards import menu_kb

rb = Router()


@rb.callback_query(States.about)
@rb.callback_query(States.day)
@rb.callback_query(States.meeting)
@rb.callback_query(States.secret)
@rb.callback_query(States.rate)
@rb.callback_query(States.rwushi)
async def back_handler(callback, state):
    message = callback.message
    user_id = callback.from_user.id
    lc = await gl(user_id)
    await message.edit_text(await gt(lc, 'Menu', 'menu'), reply_markup=await menu_kb(lc))
    await state.set_state(States.menu)
