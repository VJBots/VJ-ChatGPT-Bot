from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
        "droplink search bot",
         api_id=API_ID,
         api_hash=API_HASH,
         bot_token=BOT_TOKEN,
         plugins=dict(root="plugins"),
         workers=50,
         sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
            
        print('Bot Started Powered By @VJ_Botz')


    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
