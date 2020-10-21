import re
from math import ceil

from telethon import Button
from telethon import custom
from telethon import events
from telethon import functions
from telethon.tl.functions.users import GetFullUserRequest
import os
from userbot import ALIVE_NAME
from userbot import CMD_LIST
from userbot.plugins import inlinestats
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/53aed76a90e38779161b1.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Friday"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Friday"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s Friday** \nNote --> Only Owner Can Check This \n(C) @FridayOT",
                buttons=[
                    [custom.Button.inline("Show Stats ", data="terminator")],
                    [
                        Button.url(
                            "WW Jollibee",
                            "https://t.me/wwjollibee")
                    ],
                    [Button.url("Join Channel ❤️", "t.me/wwjollibeedumps")],
                ],
            )
        if event.query.user_id == bot.uid and query.startswith("**Hello"):
            result = builder.photo(
                file=WARN_PIC,
                text=query,
                buttons=[
                    [
                        Button.url(
                            "WW Jollibee",
                            "https://t.me/wwjollibee")
                    ],
                    [
                        custom.Button.inline(
                            "🛡️ Talk to Ryujin 🛡️",
                            data="whattalk")
                    ],
                    [
                        Button.url(
                            "WW Jollibee Dumps",
                            "https://t.me/wwjollibeedumps")
                    ],
                ],
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST,
                                    "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,
                "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                  © Userbot".format(plugin_name)
            try:
                await event.answer(reply_pop_up_alert,
                                   cache_time=0,
                                   alert=True)
            except BaseException:
                halps = "Do .help {} to get the list of commands.".format(
                    plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You can't view Ryujin's stats"
            await event.answer(txt, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        chat_k = await event.get_chat()
        text1 = "You have chosed a probhited option. Therefore, **You Have Been Blocked By UserBot.**"
        await event.edit("Choice not accepted ❌")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
    async def rip(event):
        chat_m = await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Requested ✔️")
        text2 = (
            "Requested, please wait..."
        )
        await borg.send_message(event.query.user_id, text2)
        await tgbot.send_message(LOG_CHAT, message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Talk With You.",
                                buttons=[
                                Button.url(
                                "Contact Him",
                                f"tg://user?id={him_id}")
                                ]
                                )
                                

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wwjollibee")))
    async def rip(event):
        chat_s = await event.get_chat()
        await event.edit("✅ Grouplink: t.me/wwjollibee ")
        text3 = "Click the link above to join."
        await borg.send_message(event.query.user_id, text3)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {} {}".format("🔶", x, "🔶"),
                             data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1], ))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows *
                      (modulo_page + 1)] + [(
                          custom.Button.inline("Previous",
                                               data="{}_prev({})".format(
                                                   prefix, modulo_page)),
                          custom.Button.inline("Next",
                                               data="{}_next({})".format(
                                                   prefix, modulo_page)),
                      )]
    return pairs
