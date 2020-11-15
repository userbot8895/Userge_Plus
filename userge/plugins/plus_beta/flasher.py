# flasher
# Userge++ (beta)
# Licensed under the DBBPL
# (C) 2020 githubcatw

import time
import random

from userge import userge, Message, filters

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object

# add command handler
@userge.on_cmd("flash", about="flashes")
async def flash(message: Message):
	r = random.randint(1, 10000)
	text = message.input_str.strip().title()
	if len(text) == 0:
		await message.edit("`What should I flash?`")
		return
	if len(text.split(" ")) > 1:
		await message.edit("`Cannot flash file!`")
		return
	await message.edit(f"`Flashing` {text}.zip`...`")
	time.sleep(4)
	if r % 2 == 1:
		await message.edit(f"`Successfully flashed` {text}.zip`!`")
	elif r % 2 == 0:
		await message.edit(f"`Flashing` {text}.zip `failed successfully!`")