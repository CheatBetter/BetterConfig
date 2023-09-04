"""
Copyright 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Join Us
"""
"""

Some simple test just too make sure the config can be written and read

"""
from betterconfiguration import config
from betterconfiguration.types import discord, mongo

test_config = config.BaseConfig("test", "this is a test value")
bot = discord.DiscordConfig(token="38564653", default_prefix="!", reconnect=True, owner_id=4723646723)
database = mongo.MongoConfig(connection_url="some random url", database_name="some random db name", collection_name="some random collection name")

# Don't worry about your ide thinking it doesn't exist, it doesn't count the python code
# where it actually creates the variable

print(test_config.test)