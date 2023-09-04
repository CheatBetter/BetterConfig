"""
Copyright 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Join Us
"""
"""

Used a basic discord.py bot config structure

"""
from betterconfiguration import config
from typing import Optional


class DiscordConfig(config.BaseConfig):
    """

    :param token The bots token
    :param default_prefix The bots default prefix
    :param reconnect If the bot reconnects once it disconnects, set this on the bot.run() func
    :param owner_id The user id of the bots owner

    """

    def __init__(self, token: str, default_prefix: str, reconnect: bool or Optional, owner_id: int) -> None:
        super().__init__("token", token, "default_prefix", default_prefix, "reconnect", reconnect, "owner_id", owner_id)
