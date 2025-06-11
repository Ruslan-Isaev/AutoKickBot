import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ChatMemberUpdated, ChatJoinRequest, Message
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER

bot = Bot(token="")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Приветствую! Я бот для автоматического исключения новых участников из вашего чата или канала.")

@dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def handle_new_member(event: ChatMemberUpdated):
    new_status = event.new_chat_member.status
    old_status = event.old_chat_member.status
    if old_status in ("left", "kicked") and new_status == "member":
        inviter = event.from_user
        user = event.new_chat_member.user
        chat_admins = await bot.get_chat_administrators(event.chat.id)
        admins = [admin.user.id for admin in chat_admins]
        if inviter.id in admins:
            return
        await bot.ban_chat_member(
            event.chat.id,
            user.id
        )
        await asyncio.sleep(2)
        await bot.unban_chat_member(
            event.chat.id,
            user.id
        )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

