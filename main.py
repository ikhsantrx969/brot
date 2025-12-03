import asyncio
from pyrogram import Client, idle
from aiohttp import web
from config import Config

# 1. Setup Bot (Official Bot)
bot = Client(
    "BotSession",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# 2. Setup Userbot (Akun Asli/Asisten)
# Kalau SESSION_STRING kosong, userbot gak bakal jalan (aman)
userbot = None
if Config.SESSION_STRING:
    userbot = Client(
        "UserSession",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        session_string=Config.SESSION_STRING,
        plugins=dict(root="plugins")
    )

# 3. Web Server Dummy (Biar HF Space Gak Error)
async def web_server():
    async def handle(request):
        return web.Response(text="Bot & Userbot Running 🔥")

    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Port 7860 itu WAJIB buat Hugging Face Space
    site = web.TCPSite(runner, '0.0.0.0', 7860)
    await site.start()
    print("✅ Web Server started on port 7860")

async def main():
    print("⚡ Starting Bot...")
    await bot.start()
    
    if userbot:
        print("⚡ Starting Userbot...")
        await userbot.start()
        
    print("✅ System Online! Jangan lupa ngopi bang.")
    
    # Jalanin Web Server
    await web_server()
    
    # Tahan biar gak close
    await idle()
    
    await bot.stop()
    if userbot:
        await userbot.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
