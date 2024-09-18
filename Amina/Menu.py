from aiogram import Router
from Config import States, get_translation as gt, get_language as gl
from Keyboards import back_kb

rm = Router()


@rm.callback_query(States.menu)
async def menu_handler(callback, state):
    message = callback.message
    user_id = callback.from_user.id
    lc = await gl(user_id)
    key = callback.data
    await message.edit_text(await gt(lc, 'Questions', key), reply_markup=await back_kb(lc))
    await state.set_state(getattr(States, key))
