import discord
from discord import app_command
from discord.ext import commands
import google.generativeai as genai

discord_api_key = "MTMxMjA4NDYyNTkwODA0MzgxNg.GfvCs4.gEUWVLKHm6r1Cv0496MXYItWWQT16bH4zFeOjc"
gemini_api_key = "AIzaSyBhS7lY9Dz4vfvNZHB-6B_W5uCRI3FIB7Q"

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')

@bot.tree.command(name="chat", description="Chat with the bot")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    response = chat.send_message(message)
    await interaction.followup.send(response.text)
bot.run(discord_api_key)

