"""Telegram Ping / Pong Speed
Syntax: .ping"""
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter


# -- Constants -- #
ALIVE = "വെറുതെ Alive അടിച്ചു വെറുപ്പിക്കാതട ഞൻ ഇവട ജീവനോടെ ഒക്കെ തന്നെ ണ്ട് MANH ചത്തൊന്നും പോയിട്ടില്ല"
HELP = "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ...."
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


