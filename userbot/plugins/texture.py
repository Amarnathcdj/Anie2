

from telethon.tl.types import MessageMediaPhoto
import os, urllib, requests, asyncio
from userbot.utils import admin_cmd
from userbot import CMD_HELP

DARKCOBRA = Config.DEEP_AI if Config.DEEP_AI else "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
@borg.on(admin_cmd(pattern="tex$", outgoing=True))
async def _(event):
    
               
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit(
           "Reply to any image or non animated sticker !"
        )
    devent = await event.edit("`Downloading Media...`")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await event.edit(
             "Reply to any image or non animated sticker !"
        )
    devent = await event.edit("`Redesigning Textural Deepness...`")#hehehhehehhe
    r = requests.post(
        "https://api.deepai.org/api/deepdream",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": DARKCOBRA},
    )
    os.remove(media)
    if "status" in r.json():
        return await devent.edit( r.json()["status"])
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]
    
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"
    
    await devent.delete()
    await borg.send_message(#hehehhehehehehheh
        event.chat_id,
        file=result
    )


#hehehehehe
CMD_HELP.update(
    {
        "Enhance Texture Depth Of Image": 
    ".tex <reply to any media> "
    "\nIncreases Depth Of Textures   `Enjoy`"
    })
