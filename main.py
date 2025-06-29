import discord
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAIクライアントの初期化
openai_client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('起動にゃ！')
                return # 最初のチャンネルに送信したら終了

@client.event
async def on_message(message):
    print(f"Received message from {message.author}: {message.content}")
    if message.author == client.user:
        return

    # メンションが含まれている場合のみAIチャットを処理
    if client.user.mentioned_in(message):
        # メンション部分を削除
        text_content = message.content.replace(client.user.mention, '').strip()

        # メッセージに「占い」が含まれている場合
        if "占い" in text_content:
            await message.channel.send('占いにゃん！ちょっと待っててにゃ！')
            ai_persona_content = open('config/ai_persona.txt', 'r', encoding='utf-8').read().strip()

            messages = [
                {"role": "system", "content": ai_persona_content + "\nあなたは今日の運勢を占う猫耳メイドです。ユーザーに今日の運勢を教えてください。"},
                {"role": "user", "content": "今日の運勢を占って"},
            ]

            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=messages,
                )
                fortune = response.choices[0].message.content.strip()
                await message.channel.send(f'今日の運勢は… {fortune}')
            except Exception as e:
                await message.channel.send(f'占いに失敗したにゃん…エラー: {e}')
        else:
            response = openai_client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": open('config/ai_persona.txt', 'r', encoding='utf-8').read().strip()},
                    {"role": "user", "content": text_content},
                ],
            )
            ai_response_content = response.choices[0].message.content
            await message.channel.send(ai_response_content)

client.run(DISCORD_BOT_TOKEN)