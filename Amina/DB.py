from Config import DB


async def add_new_user(user_id, username):
    async with DB() as conn:
        await conn.execute('''
            INSERT INTO amina (id, username) 
            VALUES ($1, $2) ON CONFLICT (id) DO NOTHING
        ''', user_id, username)


async def language_set(user_id, language_code):
    async with DB() as conn:
        await conn.execute('UPDATE amina SET language = $2 WHERE id = $1', user_id, language_code)


async def set_info(user_id, info, column):
    async with DB() as conn:
        query = f'UPDATE amina SET {column} = $2 WHERE id = $1'
        await conn.execute(query, user_id, info)
