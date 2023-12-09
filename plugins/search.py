from pyrogram import Client, filters
from config import *
import openai
import asyncio

openai.api_key = OPENAI_API

@Client.on_message(filters.private & filters.text & ~filters.command(['start']))
async def ai_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                msg = await message.reply_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ᴡʜɪʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ʀᴇsᴘᴏɴᴅs ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ . . .**")
                users_message = message.text
                user_id = message.from_user.id
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
                    temperature=0.6
                )
                footer_credit = "<b><a href='https://t.me/vj_bot_disscussion'>• ʀᴇᴘᴏʀᴛ ɪꜱꜱᴜᴇ •</a>══<a href='https://t.me/kingvj01'>• ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ •</a></b>"
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await message.reply_texg(f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀɴsᴡᴇʀ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ** 👇\n\n{ai_response}\n\n\n{footer_credit}")
            except Exception as error:
                print(error)
                await message.reply_text(f"**An error occurred:**\n\n**{error}**\n\n**Forward This Message To @KingVJ01**")
    else:
        return
