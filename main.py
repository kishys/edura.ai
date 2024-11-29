import discord
from discord import app_commands
from discord.ext import commands
import google.generativeai as genai
discord_api_key = ""
gemini_api_key = ""
import requests
import asyncio

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

@bot.tree.command(name="ai-tutor", description="Chat")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    full_message = f"Please avoid using LaTeX notation and provide a plain text solution for: {message}"
    response = chat.send_message(full_message) 
    if len(response.text) > 2000:
        for i in range(0, len(response.text), 2000):
            await interaction.followup.send(response.text[i:i+2000])
    else:
        await interaction.followup.send(response.text)


@bot.tree.command(name="educational-resource-hub", description="Learn about educational resources!")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    full_message = f"Please avoid using LaTeX notation and provide a plain text solution for: webpages and educational resources for {message}"
    response = chat.send_message(full_message)
    if len(response.text) > 2000:
        for i in range(0, len(response.text), 2000):
            await interaction.followup.send(response.text[i:i+2000])
    else:
        await interaction.followup.send(response.text)


@bot.tree.command(name="flashcard-generator", description="Generate flashcards!")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    full_message = f"Please avoid using LaTeX notation and provide a plain text solution for: flashcards for {message}"
    response = chat.send_message(full_message)
    if len(response.text) > 2000:
        for i in range(0, len(response.text), 2000):
            await interaction.followup.send(response.text[i:i+2000])
    else:
        await interaction.followup.send(response.text)




@bot.tree.command(name="study-clock-app", description="Learn and apply study clocks with different techniques!")
@app_commands.describe(
    technique="The study technique you'd like to apply (e.g., Pomodoro)",
    duration="Duration of the work session in minutes (e.g., 25)",
    break_time="Duration of the break in minutes (e.g., 5)"
)
async def study_clock_app(
    interaction: discord.Interaction, 
    technique: str, 
    duration: int = 25,  # Default duration is 25 minutes for work
    break_time: int = 5  # Default break time is 5 minutes
):
    """
    Handles requests for different study techniques and implements timers.
    """
    user = interaction.user  # Get the user who invoked the command
    await interaction.response.defer()

    # Dictionary of techniques (can be expanded)
    techniques = {
        "pomodoro": {
            "work_duration": duration,
            "break_duration": break_time,
            "message": (
                f"Starting a Pomodoro session for {duration} minutes. 🍅\n"
                f"After this, you'll take a {break_time}-minute break!"
            ),
        },
        # Add more techniques here if needed
    }

    technique_lower = technique.lower()
    if technique_lower in techniques:
        config = techniques[technique_lower]
        await interaction.followup.send(config["message"])

        # Start the work timer
        await run_timer(interaction, config["work_duration"], "Work session complete! Time for a break. {user.mention} ☕", user)

        # Start the break timer
        await run_timer(interaction, config["break_duration"], "Break time is over! Ready to start again? {user.mention}? 🎯", user)
    else:
        await interaction.followup.send(
            f"Sorry, the technique '{technique}' is not recognized. Supported techniques: Pomodoro."
        )


async def run_timer(interaction: discord.Interaction, minutes: int, completion_message: str, user: discord.User):
    """
    Runs a countdown timer and sends updates to the user.
    """
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        if remaining % 60 == 0:  # Update every minute
            mins, secs = divmod(remaining, 60)
            await interaction.followup.send(f"⏳ {mins:02d}:{secs:02d} remaining...")
        await asyncio.sleep(1)  # Wait for 1 second
    # Send the completion message with user mention
    await interaction.followup.send(f"⏰ {completion_message.format(user=user)}")


@bot.tree.command(name="note-enhancing-platform", description="Enhance notes!")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    full_message = f"Please avoid using LaTeX notation and provide a plain text solution for: Enhance the study notes in {message}"
    response = chat.send_message(full_message)
    if len(response.text) > 2000:
        for i in range(0, len(response.text), 2000):
            await interaction.followup.send(response.text[i:i+2000])
    else:
        await interaction.followup.send(response.text)

@bot.tree.command(name="quiz", description="Generate quizzes!")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    full_message = f"Please avoid using LaTeX notation and provide a plain text solution for: Generate a quiz with multiple choice and short-answer questions for {message}"
    response = chat.send_message(full_message)
    if len(response.text) > 2000:
        for i in range(0, len(response.text), 2000):
            await interaction.followup.send(response.text[i:i+2000])
    else:
        await interaction.followup.send(response.text)




bot.run(discord_api_key)
