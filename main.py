from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    CallbackQuery,
    ReplyKeyboardRemove,
    Message,
    ContentType,
    InputFile,
)
from config import CHAT_STORAGE, TOPIC_ID_VIDEO, TOPIC_ID_PHOTO
from dispatcher import bot, dp
from aiogram.dispatcher.filters import Command


def chat_filter(chat: str):
    def actdec(func):
        async def wrapper(message: Message):
            if message.chat.id != chat:
                return await func(message)

        return wrapper

    return actdec


@dp.message_handler(Command("start"))
async def start_message(message: Message):
    await message.answer("Привет, отправь мне файл")


@dp.message_handler(content_types=ContentType.TEXT)
@chat_filter(chat='CHAT_STORAGE')
async def text_answer(message: Message):
    await message.answer("Привет, отправь мне файл")
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
    await message.forward(chat_id=CHAT_STORAGE, message_thread_id=TOPIC_ID_VIDEO)


@dp.message_handler(content_types=[ContentType.PHOTO])
async def get_photo(message: Message):
    await message.forward(chat_id=CHAT_STORAGE, message_thread_id=TOPIC_ID_PHOTO)
