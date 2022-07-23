"""Telegram Ping / Pong Speed
Syntax: .ping"""
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter


# -- Constants -- #
ALIVE = "Glad to hear that and really nice to know that I am not talking to a ghost."
HELP = "CAACAgUAAxkBAAEBTsthlWY_Pte1RC4yhz3nD1utGagSSwAC0gIAAsaPcVUSPJS_m8rS5h4E"
REPO = "നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ..."
# -- Constants End -- #


@Client.on_message(
    filters.command(["alive", "mooooo"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("hi", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(HELP)


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(REPO)


