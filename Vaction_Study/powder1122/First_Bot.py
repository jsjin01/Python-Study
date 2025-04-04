import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 읽기. 토큰을 .env 파일에 따로 저장함.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True  # 반응(이모지) 관련 이벤트 활성화

client = commands.Bot(command_prefix='!', intents=intents)
game_sessions = {}  

@client.event
async def on_ready():   #봇이 실행되면 한 번 실행됨
    print("온라인")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("파티원 모집 중")) #온라인 부분이 출력되는 메시지

@client.command()
async def 모집(ctx, 게임이름: str, 인원: int, 시간: str):
    session_id = len(game_sessions) + 1  # 고유 세션 ID 생성

    embed = discord.Embed(title="게임 모집", description=f"게임: {게임이름}\n인원: {인원}\n시간: {시간}\n참가 희망자는 아래 이모지 클릭!", color=0x00ff00)
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")

    game_sessions[ctx.author.id] = {"게임이름": 게임이름, "인원": 인원, "시간": 시간, "참가자": [], "메시지ID": message.id, "모집완료": False}

@client.command()
async def 겜팟(ctx):
    if ctx.author.id in game_sessions:
        session = game_sessions[ctx.author.id]
        embed = discord.Embed(title="현재 게임 모집 정보", description=f"게임: {session['게임이름']}\n인원: {session['인원']}\n시간: {session['시간']}\n참가자: {', '.join(session['참가자']) if session['참가자'] else '없음'}", color=0x00ff00)
        await ctx.send(embed=embed)
    else:
        await ctx.send("현재 진행 중인 게임 모집이 없습니다. 새로운 게임 모집을 시작하려면 `!모집 게임이름 인원 시간` 형식으로 입력하세요.")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    message = reaction.message
    if message.author != client.user:
        return

    for author_id, session in game_sessions.items():
        if message.id == session["메시지ID"]:
            if reaction.emoji == "✅":
                if user.display_name not in session["참가자"]:  #중복 참가 방지
                    session["참가자"].append(user.display_name)
                    await message.channel.send(f"{user.display_name}님이 {session['게임이름']} 게임에 참여했습니다!")
                    # 참가 인원이 모집 인원과 같아지면 모집 완료
                    if len(session["참가자"]) == session["인원"]:
                        session["모집완료"] = True
                        await message.channel.send(f"{session['게임이름']} 게임의 모집이 완료되었습니다!")
                    # 현재 참가자 목록 표시
                    await message.channel.send(f"현재 참가자: {', '.join(session['참가자'])}")
                else:
                    await message.channel.send("이미 이 게임 세션에 참가하셨습니다.")
@client.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    message = reaction.message
    if message.author != client.user:
        return

    for author_id, session in game_sessions.items():
        if message.id == session["메시지ID"]:
            if reaction.emoji == "✅":
                if user.display_name in session["참가자"]:
                    session["참가자"].remove(user.display_name)
                    await message.channel.send(f"{user.display_name}님이 {session['게임이름']} 게임에서 참가를 취소하셨습니다.")

                    # 현재 참가자 목록 표시
                    await message.channel.send(f"현재 참가자: {', '.join(session['참가자'])}")
                else:
                    await message.channel.send("이 게임 세션에 참가하지 않으셨습니다.")

#봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run(TOKEN)

