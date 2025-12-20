import asyncio
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info("🛠️ Initializing LearningBots Bot...")
        super().__init__(
            name="LearningBots",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<b>✅ Bot Started Successfully!</b>\n\n"
                    f"<b>Name:</b> {self.name}\n"
                    f"<b>Username:</b> @{self.username}\n"
                    f"<b>User ID:</b> <code>{self.id}</code>"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "❌ Bot ကို log group/channel ထဲ add မထားပါ"
            )
            raise SystemExit
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Log group access မရပါ | {type(ex).__name__}"
            )
            raise SystemExit

        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "⚠️ Bot ကို admin မပေးထားပါ"
                )
                raise SystemExit
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Admin status စစ်မရ | {type(ex).__name__}"
            )
            raise SystemExit

        LOGGER(__name__).info(
            f"🎶 Bot Online: {self.name} (@{self.username})"
        )

    async def stop(self):
        LOGGER(__name__).info("🛑 Stopping bot...")
        await super().stop()
