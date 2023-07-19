from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    CallbackQuery,
    ReplyKeyboardRemove,
    Message,
    ContentType,
    InputFile,
)
from config import CHAT, TOPIC_ID
from dispatcher import bot, dp
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("start"))
async def start_message(message: Message):
    id_user = message.from_user.id

    await message.answer(message.chat.id)
    # await message.answer('Привет, отправь мне файл')


@dp.message_handler(content_types=ContentType.TEXT)
async def text_answer(message: Message):
    await bot.send_message(message.chat.title)
    # await message.answer(message)


@dp.message_handler(content_types=[ContentType.DOCUMENT, ContentType.VIDEO])
async def get_file(message: Message):
    # if message.content_type == 'document':
    #     file_id = message.document.file_id
    #     file = await bot.get_file(file_id)
    #     await bot.send_document(
    #         chat_id=CHAT,
    #         document=file.file_id,
    #         message_thread_id=TOPIC_ID,
    #         caption=f'@{message.from_user.username}'
    #     )
    # else:
    await message.forward(chat_id=CHAT, message_thread_id=TOPIC_ID)
