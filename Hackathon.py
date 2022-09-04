from pyrogram import *
from Config import *
from GNews import *
from Reddit import *
from Wiki import *
try:
    gotcha = Client(name="bot", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN )
except:
    print("Enter Your credentials in Config.py")
    exit()
prefixChars=['!','/']
memeId = 0
memes = []
subredditTitle = ""
@gotcha.on_message(filters.command(["start"],prefixChars))
async def start(client, message):
    await message.reply_text(
        text=f"Gotcha!!!!!!!"
        "\nclick /help for help",
    )
@gotcha.on_message(filters.command(["help"],prefixChars))
async def start(client, message):
    await message.reply_text(
        text=f"This is Help text"
        "\nclick /reddit for reddit"
        "\nclick /news for news"
        "\nclick /wiki for wiki"
    )
@gotcha.on_message(filters.command(["reddit"],prefixChars))
async def startReddit(client, message):
    await message.reply_text(
        text=f"Send a Subrreddit Name:"
    )
    @gotcha.on_message()
    async def getSubreddit(client,message):
        global subredditTitle, memes, memeId
        if subredditTitle != message.text:
            memeId=0
            subredditTitle = message.text
        if memeId<=0 or memeId>=9:
            memeId=0
            memes=getMemes(subredditTitle)
        while(memeId<len(memes)):
            try:
                try:
                    await message.reply_video(
                    video=memes[memeId]['postImgUrl'],
                    caption=memes[memeId]['title']
                    )
                    memeId+=1
                    break
                except:
                    await message.reply_photo(
                        photo=memes[memeId]['postImgUrl'],
                        caption=memes[memeId]['title']
                    )
                    memeId+=1
                    break
            except:
                try:
                    try:
                        await message.reply_animation(
                            animation=memes[memeId]['postImgUrl'],
                            caption=memes[memeId]['title']
                        )
                        memeId+=1
                        break
                    except:
                        if meme[postText] == "":
                            raise ValueError()
                        await message.reply_text(
                            text=f"{memes[memeId]['title']}\n{memes[memeId]['postText']}"
                        )
                        memeId+=1
                        break
                except:
                    memeId+=1
                    if memeId >=9:
                        await message.reply_text(
                                text=f"Post Cannot be fetched......"
                        )    
                    continue
@gotcha.on_message(filters.command(["news"],prefixChars))
async def start(client,message):
    news=getNews()
    for newsItem in news:
        try:
            await message.reply_photo(
                disable_web_page_preview=True,
                photo=newsItem['image'],
                caption=f"**{newsItem['title']}**"
                f"\n\n{newsItem['description']}"
                f"\n\nFor more info: {newsItem['url']}",
            )
        except:
            continue
@gotcha.on_message(filters.command(["wiki"],prefixChars))
async def start(client, message):
    await message.reply_text(
        text=f"Send a Topic to Search:"
    )
    @gotcha.on_message()
    async def getSubreddit(client,message):
        wikiTitle=message.text
        wiki=getWiki(wikiTitle)
        await message.reply_text(
            disable_web_page_preview=True,
            text=f"{wiki}",
        )

gotcha.run()