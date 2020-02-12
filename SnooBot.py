import discord
from discord.ext import commands
import reddit_interface
import nosql_interface
import error

# setup including Token and commands prefix

client = commands.Bot(command_prefix = '$')
redditFunctions = reddit_interface.Reddit()
databaseFunctions = nosql_interface.Database()
error = error.Error()
creatorId = '251912842700259328'


@client.event
async def on_ready():
    pass


@client.command()                  # latency
async def ping(ctx):
    await ctx.send(f'Ping! {int(client.latency*1000)} ms')


@client.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def feed(ctx, subreddit, postAmount = 5, sort = "hot"):
    postList = redditFunctions.get_sr_feed(subreddit, sort, postAmount)
    for submission in postList:
        postInfo = redditFunctions.generate_embed(submission)
        await ctx.send(embed=postInfo[0]) # testing
        if postInfo[1] == "video" or postInfo[1] == "gif":
            await ctx.send(postInfo[2])


@client.command()
async def add(ctx, rate, *argv):
    #error.check_args_add(rate, argv)
    badSubs = []
    success = False
    success = databaseFunctions.add(str(ctx.guild.id), str(ctx.channel.id), rate, argv)
    '''
    except:
        await ctx.send("It seems there's a problem at the moment.  The"
                       "subreddit you added was not added to your feed. "
                       "Sorry for the inconvenience. For more info visit"
                       "**docs website**.")
        success = False
        #error.database()
    '''
    if success:
        await ctx.send("Your sub(s) have been added to your feed successfully.")
    if not success:
        print('something went wrong')

@client.command()
async def amount(ctx, rate, amount):
    amount = error.amount_check(amount)
    if amount == -1:
        await ctx.send("There was an error with the amount entered.  Please make sure it's a number and in 1-30.")
        return
    databaseFunctions.set_amount(ctx.guild.id, rate, amount)

@client.command()
async def remove(ctx, rate, *argv):
    #error.check_args_add(rate, argv)
    success = False
    success = databaseFunctions.remove(str(ctx.guild.id), str(ctx.channel.id), rate, argv)
    '''
    except:
        await ctx.send("It seems there's a problem at the moment.  The"
                       "subreddit you added was not added to your feed. "
                       "Sorry for the inconvenience. For more info visit"
                       "**docs website**.")
        success = False
        #error.database()
    '''

@client.command()
async def removeall(ctx, rate):
    databaseFunctions.remove_all(ctx.guild.id, rate)











client.run(TOKEN)