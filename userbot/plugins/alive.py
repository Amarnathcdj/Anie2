# Thanks to Sipak bro and Aryan.. 
# animation Idea by @(ItzSipak) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Aɳιҽ"
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/74baa0fee2d1f3cc8112d.jpg"
file2 = "https://telegra.ph/file/897db0c5f8f06134556f2.jpg"
file3 = "https://telegra.ph/file/09c1cb99d4bd6f0b9cbad.jpg"
file4 = "https://telegra.ph/file/9271370fd1f5dd877388b.jpg"
file5 = "https://telegra.ph/file/6b5e21235cb7244560e1b.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "**Testing Updater**\n\n"
pm_caption += "**𝓑𝓸𝓼𝓼 𝓘 𝓐𝓶 𝓕𝓲𝓷𝓮 𝓐𝓯**\n\n"
pm_caption += "✘ 𝓐𝓫𝓸𝓾𝓽 𝓜𝔂 𝓢𝔂𝓼𝓽𝓮𝓶 ✘\n\n"
pm_caption += "➾ **𝓣𝓮𝓵𝓮𝓽𝓱𝓸𝓷 𝓥𝓮𝓻𝓼𝓲𝓸𝓷** ☞ 1.17.5\n"
pm_caption += "➾ **𝓛𝓲𝓬𝓮𝓷𝓼𝓮**  ☞ [Aɳιҽ2021](https://github.com/Amarnathcdj)\n"
pm_caption += "➾ **𝓒𝓸𝓹𝔂𝓻𝓲𝓰𝓱𝓽 𝓑𝔂** ☞ [Aɳιҽ](https://github.com/Amarnathcdj/Anie)\n\n"
pm_caption += f"➾ **𝓜𝔂 𝓜𝓪𝓼𝓽𝓮𝓻** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file5)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file5)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

