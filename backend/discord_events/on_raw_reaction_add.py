import logging

import discord
import discord.state
from discord.ext import commands

import backend.config
import backend.discord_events.on_reaction_add
import backend.helpers
from bot import Bot as Client

log = logging.getLogger(__name__)


class OnRawReactionAdd(commands.Cog):
    def __init__(self, bot):
        self.bot: Client = bot

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        guild: discord.Guild = self.bot.get_guild(payload.guild_id)
        channel: discord.TextChannel = guild.get_channel(payload.channel_id)
        user: discord.Member = guild.get_member(payload.user_id)
        message: discord.Message = await channel.get_message(payload.message_id)

        cache = message._state._messages
        if discord.utils.get(cache, id=message.id) is None:
            log.info("{} {} {} {}".format(guild, channel, user, message))
            await backend.discord_events.on_reaction_add.on_reaction_add_main(user,
                                                                              payload.emoji,
                                                                              self.bot,
                                                                              True,
                                                                              message)


def setup(bot):
    bot.add_cog(OnRawReactionAdd(bot))
