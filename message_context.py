from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

import discord

from command import Command


@dataclass
class MessageContext:
    message: discord.Message
    result: str = ''
    command: Command = field(default_factory=Command.dummy)

    def updated(self, *, result: str | None = None, command: Command | None = None) -> MessageContext:
        if result is None and command is None:
            raise ValueError('Either result or command need to be updated')
        return MessageContext(
            message=self.message,
            result=result or self.result,
            command=command or self.command,
        )
