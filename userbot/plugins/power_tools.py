"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown
.reboot"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="restart"))
async def _(event):
    await event.edit("Restarting ▰▱▱▱▱▱▱▱18%...")
    await asyncio.sleep(1)
    await event.edit("Restarting ▰▰▰▰▱▱▱▱48.6%...")
    await asyncio.sleep(1.5)
    await event.edit("Restarting ▰▰▰▰▰▰▰▰100%...")
    await asyncio.sleep(3)
    await event.edit("Restarted Master😘,Check Me By typing .king")
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning dyno off .....Turn Me On Manually")
    await borg.disconnect()

@borg.on(events.NewMessage(pattern=r"\.reboot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    
    await event.edit("executing endtask>>svchost.exe,dktwmr.exe")
    await asyncio.sleep(2)
    await event.edit("executing start>>ntoskernel.exe")
    await asyncio.sleep(0.1)
    await event.edit("Omk Reboooted..😗😗 = ✅")
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
