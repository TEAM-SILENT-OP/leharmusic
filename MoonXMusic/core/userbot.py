
from pyrogram import Client
import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="MoonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistant...")

        if not config.STRING1:
            LOGGER(__name__).warning("STRING1 is empty. Assistant skipped.")
            return

        await self.one.start()

        self.one.id = self.one.me.id
        self.one.name = self.one.me.mention
        self.one.username = self.one.me.username

        if 1 not in assistants:
            assistants.append(1)

        if self.one.id not in assistantids:
            assistantids.append(self.one.id)

        try:
            await self.one.send_message(
                config.LOGGER_ID,
                "Assistant Started"
            )
        except Exception as e:
            LOGGER(__name__).warning(
                f"Assistant could not send log message: {e}"
            )

        try:
            await self.one.join_chat("world_friend_chatting_zone")
        except Exception as e:
            LOGGER(__name__).warning(
                f"Assistant group join skipped: {e}"
            )

        LOGGER(__name__).info(
            f"Assistant Started as {self.one.name}"
        )

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistant...")

        try:
            if self.one.is_connected:
                await self.one.stop()
        except Exception as e:
            LOGGER(__name__).warning(
                f"Assistant stop warning: {e}"
            )

        assistants.clear()
        assistantids.clear()
