from loader import *
from utils import get_insertable_data
from db.misc import update_data,get_info_from_db


@app.on_message(filters.command(commands=['refresh'],prefixes='%'))
async def refresh(client, message: Message):

    await message.reply('Userbot going to refresh please wait it may take a few minutes')
    update_data(await get_insertable_data())
    await message.reply('Userbot successfully refreshed')




@app.on_message(filters.regex(r"^\%\d+$"))
async def search_groups(client, message: Message):
    lst = []
    for i in get_info_from_db(int(message.text[1:])):
        url = (await app.get_chat(i[-2])).invite_link
        lst.append(f"[{i[-1]}]({url})")
    full_name = i[2]
    # print((await app.get_users([i[1]]))[0].username)
    # print((await app.get_users([i[1]]))[0].user.username)
    await message.edit(f"user: [{full_name}](https://t.me/{(await app.get_users([i[1]]))[0].username})",parse_mode=parse_mode.ParseMode.MARKDOWN)
    await message.reply("\n".join(lst))

# @app.on_message(filters.regex(r'^@[a-zA-Z0-9]+$'))
# async def search_groups_username(client, message:Message):
#     await message.reply('some text')


app.run()