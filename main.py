import os
from pyrogram import Client, filters
from openai import OpenAI

API_ID = int(os.environ.get("33807423", 0))
API_HASH = os.environ.get("20d3f5b17118afbf804eca961d787f56", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DEEPSEEK_API_KEY = os.environ.get("sk-4dbcad99fa0041df80b3758853784716", "")

ai_client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

app = Client("userbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & (filters.private | filters.group))
async def handle_message(client, message):
    if message.from_user.is_self:
        return
    await client.send_chat_action(message.chat.id, "typing")
    try:
        response = ai_client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "تو یک دستیار هوشمند و فارسی‌زبان هستی."},
                {"role": "user", "content": message.text}
            ],
            max_tokens=1000
        )
        await message.reply(response.choices[0].message.content)
    except Exception as e:
        await message.reply(f"❌ خطا: {str(e)}")

if __name__ == "__main__":
    print("🤖 بات روشن شد!")
    app.run()