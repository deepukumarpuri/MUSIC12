from pyrogram import Client
import asyncio
from VCsMusicBot.config import SUDO_USERS, PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from VCsMusicBot.services.callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Hi there, This is a music assistant service of @GROUPMUSICPLAYBOT.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND ONLY CHANNEL INVITE LINK OR USERNAME IF USERBOT JOIN YOUR IN CHANNEL FOR MUSIC PLAYING IN 24 HOUR.**\n\n WATCH THIS VIDEO TO KNOW HOW TO PLAY MUSIC IN CHANNEL LINK :- https://youtu.be/6GDIXeAhkH8**\n\n ⚠️ Disclamer:- YOU NOT WATCH MY VIDEO I DON'T JOIN YOUR CHANNEL. WATCH VIDEO AND SUBCRIBE MY CHANNEL AND SEND SCREENSHOT ME I JOIN YOUR CHANNEL IN 24 HOUR.VIDEO LINK :-https://youtu.be/6GDIXeAhkH8. MORE HELP CONTACT :- @DKBOTZHELP",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM due to outgoing messages")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
