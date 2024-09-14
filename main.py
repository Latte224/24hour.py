import discord
from discord.ext import commands
import os
from discord import app_commands
import random
import subprocess
from discord import Intents, Client, Interaction, Game
from discord.app_commands import CommandTree
from datetime import timedelta, datetime, timezone
import aiohttp
from keep_alive import keep_alive

TOKEN=os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

@bot.event
async def on_ready ():
    activity_stetas=random.choice(("週末京都現実逃避","2:23 AM","SUMMER TRIANGLE","You and Me","10℃"))
    await bot.change_presence(activity=discord.Game(name="/help｜"f"Join server{len(bot.guilds)}｜""Listening "+activity_stetas))
    print("起動")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期")
    except Exception as e:
        print(e)

embed = [
    discord.Embed(description="## __Table of Contents__")
    .add_field(name="`Page1`",value="投票コマンドの説明",inline=False)
    .add_field(name="`Page2`",value="BAN・time outのコマンドの説明",inline=False)
    .add_field(name="`Page3`",value="その他のコマンドの説明",inline=False)
    .add_field(name="⇩ご不明点",value="<@795470464909836329>",inline=False)
    .set_author(name="by",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg"),
    discord.Embed(description="## Page1")
    .add_field(name="/yes-no",value="投票を開始",inline=False)
    .add_field(name="`title`",value="投票のタイトル",inline=True)
    .add_field(name="`q1`",value="1つ目の回答を作成",inline=True)
    .add_field(name="`q2`",value="2つ目の回答を作成",inline=True)
    .add_field(name="/question",value="複数投票(q3～q5)を開始",inline=False)
    .add_field(name="`q1`",value="1つ目の回答を作成",inline=True)
    .add_field(name="`q2`",value="2つ目の回答を作成",inline=True)
    .add_field(name="`q3`",value="3つ目の回答を作成",inline=True)
    .set_author(name="py",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg"),
    discord.Embed(description="## Page2")
    .add_field(name="/timeout",value="時間指定式タイムアウト",inline=False)
    .add_field(name="`member`",value="タイムアウトするメンバー",inline=True)
    .add_field(name="`duration`",value="時間を指定(秒単位)",inline=True)
    .add_field(name="/ban",value="指定式BAN",inline=False)
    .add_field(name="`member`",value="BANするメンバー",inline=True)
    .add_field(name="`reason`",value="BANする理由",inline=True)
    .set_author(name="py",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg"),
    discord.Embed(description="## Page3")
    .add_field(name="/mc",value="Minecraft Serverの情報を表示",inline=False)
    .add_field(name="/omikuzi",value="おみくじを開始",inline=False)
    .add_field(name="/server",value="サーバー情報を表示",inline=False)
    .add_field(name="/user",value="ユーザー情報を表示",inline=False)
    .add_field(name="/hurupa",value="ランダムでVALORANTのフルパを作成",inline=False)
    .set_author(name="py",icon_url="https://i.pinimg.com/564x/f2/bf/81/f2bf81b2bc34fbb6d5bc57dd33bfc551.jpg")
]

ce="◁"
ce2="▷"

class EmbedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.current_page = 0

    @discord.ui.button(label=ce, style=discord.ButtonStyle.primary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=embed[self.current_page], view=self)

    @discord.ui.button(label=ce2, style=discord.ButtonStyle.primary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page < len(embed) - 1:
            self.current_page += 1
            await interaction.response.edit_message(embed=embed[self.current_page], view=self)

@bot.tree.command(name="help",description="BOTの説明")
async def send_pages(interaction: discord.Interaction):
   view = EmbedView()
   await interaction.response.send_message(embed=embed[0],view=view)

list_ = ["⭕", "❌"]
list_1 = ['1️⃣', '2️⃣', '3️⃣']
list_2 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
list_3 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']

@bot.tree.command(name="yes-no",description="2択投票")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="⭕   "+q1,value="",inline=False)
    embed.add_field(name="❌   "+q2,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_)):
     await message.add_reaction(list_[i])

@bot.tree.command(name="question3",description="3択投票")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_1)):
     await message.add_reaction(list_1[i])
    return

@bot.tree.command(name="question4",description="4択投票")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_2)):
     await message.add_reaction(list_2[i])
    return

@bot.tree.command(name="question5",description="5択投票")
async def test(interaction: discord.Interaction, title:str, q1:str, q2:str, q3:str, q4:str, q5:str):
    embed = discord.Embed(title="",description="## "+title)
    embed.add_field(name="1   "+q1,value="",inline=False)
    embed.add_field(name="2   "+q2,value="",inline=False)
    embed.add_field(name="3   "+q3,value="",inline=False)
    embed.add_field(name="4   "+q4,value="",inline=False)
    embed.add_field(name="5   "+q5,value="",inline=False)
    message = await (await commands.Context.from_interaction(interaction)).send(embed=embed)
    for i in range(len(list_3)):
     await message.add_reaction(list_3[i])
    return

@bot.tree.command(name="omikuzi",description="おみくじ")
async def omikuazi(interaction: discord.Interaction):
   text_random=random.choice(("大吉","中吉","小吉","吉","末吉","凶","大凶"))
   text_message=str(text_random)
   await interaction.response.send_message(text_message,ephemeral=True)

@bot.tree.command(name="mc",description="Minecraftserverの詳細")
async def mc(interaction: discord.Interaction): 
   embed = discord.Embed(description="### [MOD](https://d.kuku.lu/d87h2ccud) ＆ [Minecraft](https://www.youtube.com/watch?v=xt_1ASLcdY4)")
   embed.add_field(name="java : `java 17`",value="",inline=False)
   embed.add_field(name="mod : `dimension`",value="",inline=False)
   embed.add_field(name="ver : `FORGE 1.20.1`",value="",inline=False)
   embed.add_field(name="address : `black-tar.gl.joinmc.link`",value="",inline=False)
   embed.add_field(name="・黄昏の森",value="The Twilight Forest",inline=False)
   embed.add_field(name="・ディープアンドダーカー",value="Deeper and Darker",inline=False)
   embed.add_field(name="・ビヨンドアース",value="Beyond Earth",inline=False)
   embed.add_field(name="・ブルースカイズ",value="Blue Skies",inline=False)
   embed.add_field(name="・トロピクラフト",value="Tropicraft",inline=False)
   embed.add_field(name="・エーテル",value="The Aether",inline=False)
   user_id = "795470464909836329"
   member_list = list(bot.get_all_members())
   for i in range(len(member_list)):
        if str(member_list[i].id) == user_id:
            user = member_list[i]
   latte = f"{user._user.mention} "
   embed.add_field(name="⇩ご不明点",value=latte,inline=False)
   await interaction.response.send_message(embed=embed)

@bot.tree.command(name="server",description="serverの詳細")
async def server(interaction: discord.Interaction): 
  guild = interaction.user.guild
  roles =[role for role in guild.roles]
  text_channels = [text_channels for text_channels in guild.text_channels]
  embed = discord.Embed(description="")
  embed.add_field(name="Adomin",value=f"{interaction.guild.owner}",inline=False)
  embed.add_field(name="ID",value=f"{interaction.guild.id}",inline=False)
  embed.add_field(name="Channel",value=f"{len(text_channels)}",inline=False)
  embed.add_field(name="Roll",value=f"{len(roles)}",inline=False)
  embed.add_field(name="Server Booster",value=f"{guild.premium_subscription_count}",inline=False)
  embed.add_field(name="Member",value=f"{guild.member_count}",inline=False)
  embed.add_field(name="Create Server",value=f"{guild.created_at}",inline=False)
  embed.add_field(name="Executor",value=f"{interaction.user}")
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="user",description="userの詳細")
async def user(interaction: discord.Interaction): 
  embed = discord.Embed(title=f"user {interaction.user.name}",description="userinfo")
  embed.add_field(name="Name",value=f"{interaction.user.mention}",inline=False)
  embed.add_field(name="ID",value=f"{interaction.user.id}",inline=False)
  embed.add_field(name="ACTIVITY",value=f"{interaction.user.activity}",inline=False)
  embed.add_field(name="TOP_ROLE",value=f"{interaction.user.top_role}",inline=False)
  embed.add_field(name="Discriminator",value=f"#{interaction.user.discriminator}",inline=False)
  embed.add_field(name="Join Server",value=f"{interaction.user.joined_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
  embed.add_field(name="Create Account",value=f"{interaction.user.created_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
  embed.set_thumbnail(url=f"{interaction.user.avatar.url}")
  embed.add_field(name="Executor",value=f"{interaction.user}")
  await interaction.response.send_message(embed=embed)
     
ID_ROLE_MEMBER = 1222196302780301335

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(ID_ROLE_MEMBER)
    await member.add_roles(role)

@bot.event
async def on_message(message):
 user_id=699823803924086794
 if message.author.id !=user_id:
    return
 text_random=random.choice(("ゆ♡い♡か♡だ♡い♡す♡き♡","ゆいちゃんのおしゃぶりはやっぱり甘いな～","ゆいちゃ～ん😀そんなこと言わないでおじさんと濃厚な夜をすごそーよ♡","僕がゆいちゃんを守るよ！","そんなのプンプンしないでw今日生理かな?wアイス食べる?w","ゆいちゃんの3日目の生理の血は少ししょっぱいね♡ww"))
 text_message=str(text_random)
 await message.reply(text_message)

@bot.tree.command(name="hurupa",description="VALORANTのキャラをランダムで決める(フルパ)")
async def hurupa(interaction: discord.Interaction):
   due=random.choice(("ジェット","レイズ","フェニックス","レイナ","ヨル","ネオン","アイソ"))
   senti=random.choice(("セージ","キルジョイ","サイファー","デッドロック","チェンバー","ヴァイス"))
   initiator=random.choice(("ソーヴァ","KAY/O","スカイ","フェイド","ブリーチ","ゲッコー"))
   controller=random.choice(("ブリム","アストラ","ヴァイパー","オーメン","ハーバ","クローヴ"))
   amari=random.choice(("ジェット","レイズ","フェニックス","レイナ","ヨル","ネオン","アイソ","セージ","キルジョイ","サイファー","デッドロック","チェンバー","ヴァイス","ソーヴァ","KAY/O","スカイ","フェイド","ブリーチ","ゲッコー","ブリム","アストラ","ヴァイパー","オーメン","ハーバ","クローヴ"))
   text_message=str(due+"、"+senti+"、"+initiator+"、"+controller+"、"+amari)
   await interaction.response.send_message(text_message)

intents = discord.Intents.default()
intents.members = True

HEADERS = {
    'Authorization': f'Bot {TOKEN}',
    'Content-Type': 'application/json'
}
@bot.tree.command(name="timeout",description="指定したユーザーをタイムアウト")
@app_commands.describe(member="timeout member", duration="秒")
async def timeout(interaction: discord.Interaction, member: discord.Member, duration: int):
    timeout_duration = timedelta(seconds=duration)
    end_time = (datetime.now(timezone.utc) + timeout_duration).isoformat()

    url = f"https://discord.com/api/v10/guilds/{interaction.guild_id}/members/{member.id}"

    json_data = {
        "communication_disabled_until": end_time
    }
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, json=json_data, headers=HEADERS) as response:
            if response.status == 200:
                await interaction.response.send_message(f'{member.mention} がタイムアウトされました。時間： {duration // 60} 分')
            else:
                await interaction.response.send_message(f'タイムアウトに失敗しました。 {member.display_name}: {response.status} - {await response.text()}')
@bot.tree.command(name="ban", description="指定したメンバーをBANします。")

@app_commands.describe(member="BANするメンバー", reason="BANの理由")
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    if interaction.user.guild_permissions.ban_members:
        try:
            await member.ban(reason=reason)
            await interaction.response.send_message(f"{member.name} がBANされました。理由: {reason}")
        except Exception as e:
            await interaction.response.send_message(f"エラー: {e}")
    else:
        await interaction.response.send_message("BANする権限がありません。")
keep_alive()
  
bot.run(TOKEN)