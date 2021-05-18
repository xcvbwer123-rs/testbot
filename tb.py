from asyncio.tasks import wait
from logging import error
import discord
from discord import message
from discord import channel
from discord.utils import get
import time
import os
import random
import datetime

print("======로그인 하는중======")

def resource_path(relative_path):
    try:
        base_path = os.system._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

client = discord.Client()

@client.event
async def on_ready():
    print("이름 :",client.user.name)
    print("ID :",client.user.id)
    print("======로그인 성공======")
    s = random.randint(1,3)
    if s==1:
        game = discord.Game("안녕하세요!!")
    if s==2:
        game = discord.Game("하이예요!!!")
    if s==3:
        game = discord.Game("뉴하!!")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("뉴비야"):
        msg = message.content.split(" ")[1]
        if msg == "안녕":
            await message.channel.send("https://tenor.com/view/baby-girl-middle-finger-mood-screw-you-leave-me-alone-gif-10174031")
        elif msg == "손절":
            await message.channel.send("https://tenor.com/view/no-way-%EB%BD%80%EB%A1%9C%EB%A1%9C-%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98-%EC%95%84%EC%9D%B4%EC%BD%94%EB%8B%89%EC%8A%A4-pororo-gif-12634393")
        elif msg == "핵폭팔"or msg == "핵폭8":
            await message.channel.send("https://tenor.com/view/nuclear-catastrophic-disastrous-melt-down-gif-13918708")
        elif msg == "주인님" or msg == "작가님":
            await message.channel.send("나를 만들어준 주인님!")
            await message.channel.send(file=discord.File(resource_path("file/작가님.png")))
        elif msg == "루온":
            await message.channel.send("39!39!39!")
            await message.channel.send(file=discord.File(resource_path("file/rouon39.png")))
        elif msg == "이명박":
            await message.channel.send(file=discord.File(resource_path("file\lee.mp4")))
            await message.channel.send("ㅋㅋ")
        elif msg == "멘션":
            await message.channel.send("{} 이렇게요?".format(message.author.mention))
        elif msg == "정보":
            try:
                if message.mentions[0]:
                    suser = message.mentions[0]
                    if suser:
                        date = datetime.datetime.utcfromtimestamp(((int(suser.id) >> 22) + 1420070400000) / 1000)
                        embed = discord.Embed(color=0x00ff00)
                        embed.add_field(name="이름", value=suser.name, inline=True)
                        embed.add_field(name="서버 닉네임", value=suser.display_name, inline=True)
                        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
                        embed.add_field(name="유저 아이디", value=suser.id, inline=True)
                        embed.set_thumbnail(url=suser.avatar_url)
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send("오류발생")
                else:
                    date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="이름", value=message.author.name, inline=True)
                    embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
                    embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
                    embed.add_field(name="유저 아이디", value=message.author.id, inline=True)
                    embed.set_thumbnail(url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            except IndexError:
                await message.channel.send("올바를 사용법 : `정보 [유저멘션 또는 빈칸]`")
        elif msg == "죽어":
            await message.channel.send("༼ つ ◕_◕ ༽つ")
            msg = await message.channel.send("~~이런 C8 색이가 칵ㅌ..읍읍~~")
            time.sleep(1.5)
            await msg.delete()
        elif msg == "ID":
            try:
                await message.channel.send("{0}님의 ID는 `{1}` 이예요!".format(message.mentions[0],str(message.mentions[0].id)))
            except IndexError:
                await message.channel.send("{0}님의 ID는 `{1}` 이예요!".format(message.author.name,message.author.id))
        elif msg == "소환":
            try:
                for v in range(5):
                    await message.channel.send("{}".format(message.mentions[0].mention))
                    time.sleep(0.05)
            except IndexError:
                await message.channel.send("올바를 사용법 : `소환 [유저멘션]`")
        else:
            await message.channel.send("?? 그게 모에요?")
    if message.content.startswith("Clauboisllefs"):
        imsg = message
        await imsg.delete()
        msg = await message.channel.send("?? 잠만 그건 .......")
        time.sleep(1.5)
        amsg = await message.channel.send("`ErrorCode303`\n`StopCode`\n```roijhgihiurhuhiahheieuueyhndbnsghhakkfahehfhjskkjjeufudjjdjenndjhjsjehhfkskjefnjdjskejfhdjsjkkekkfhshkkeufudhsakkhejfj```")
        await msg.edit(content="c�8��E��Z��98_�eY�E��M`���=��1���!::�.N��=���QG���� D�4��V;Y7��4mbwar=wб���`�Ȯ�H;������]�]�0���t�`z�f8�7g�>>@��ܟ�ܦ�|T:qd���F\��e�����B2�N=#xr�'1kӠ5Td���}���v��h�����zk�%l�|�2ԈԨs������޴��.0�|g�Aec��T�H1v��eM^E�Ovr<����SJ�)�iJ�t�T�>�@�$�µ�W�g�@�&>D*��fN&l\F�b��W�vS�U�+���ڐ���i��oU�$'o.7$�.��S-���yg ���G`]�f�K�>&�b�91&ۍ�q�$  code  executed")
        time.sleep(0.5)
        for v in range(3):
            await msg.edit(content="Loading shutdown.")
            time.sleep(0.5)
            await msg.edit(content="Loading shutdown..")
            time.sleep(0.5)
            await msg.edit(content="Loading shutdown...")
            time.sleep(0.5)
        await msg.delete()
        await amsg.edit(content="```Don't stop Shutdown``` ```AccessCode : ``` `rxtyuhnfrdxestcygvhbnjiaygdkhujkdfhhkhehfjksajhkjkjee`")
        time.sleep(2)
        await amsg.delete()
        error("c�8��E��Z��98_�eY�E��M`���=��1���!::�.N��=���QG���� D�4��V;Y7��4mbwar=wб���`�Ȯ�H;������]�]�0���t�`z�f8�7g�>>@��ܟ�ܦ�|T:qd���F\��e�����B2�N=#xr�'1kӠ5Td���}���v��h�����zk�%l�|�2ԈԨs������޴��.0�|g�Aec��T�H1v��eM^E�Ovr<����SJ�)�iJ�t�T�>�@�$�µ�W�g�@�&>D*��fN&l\F�b��W�vS�U�+���ڐ���i��oU�$'o.7$�.��S-���yg ���G`]�f�K�>&�b�91&ۍ�q�$ code executed")
        exit(all)
client.run("ODQzNDUyMTY3NTE5MzM4NTQ3.YKEECw.YRjL7_2yOy9XlzNHx4YRWgSsflc")