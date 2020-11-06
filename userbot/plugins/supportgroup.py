"""Emoji
Available Commands:
.support
Credits to noone
"""


import asyncio

from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("Friday"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("For Main Grouplink")
    animation_chars = [
        "Follow our Channel",
        "Bago namin i-promote ang inyong channel/link. I-follow muna ang https://t.me/promotelinksph.)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
