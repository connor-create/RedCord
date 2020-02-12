import praw
import requests
import discord

class Reddit:
    creatorId = 251912842700259328
    def __init__(self):


    def get_sr_feed(self, subreddit, sort, postAmount):           
        postList = []
        if sort == "hot":
            for submission in self.redditInstance.subreddit(subreddit).hot(limit=postAmount):
                postList.append(submission)
            return postList
        elif sort == "new":
            for submission in self.redditInstance.subreddit(subreddit).new(limit=postAmount):
                postList.append(submission)
            return postList
        elif  sort == "top":           
            for submission in self.redditInstance.subreddit(subreddit).top(limit=postAmount):
                postList.append(submission)
            return postList


    def check_sub(self, sub):
        try:
            subs = self.redditInstance.subreddit(sub).hot(limit=5)
            if len(subs) < 3:
                return False
            else:
                return True
        except:
            return False


    def generate_embed(self, submission):
        mediaType = "else"
        embed = discord.Embed(title=submission.title, 
                              colour=discord.Colour(0x2c2402),  
                              url=submission.url,
                              timestamp=discord.Embed.Empty)
        selftext = submission.selftext
        newSelfText = ""
        for i,letter in enumerate(selftext):
            newSelfText = newSelfText + letter
            if i > 999:
                newSelfText = newSelfText + "..."
                break
        if len(newSelfText) < 1:
            newSelfText = "reddit.com"
        embed.add_field(name = "/r/" + submission.subreddit.display_name, value = newSelfText)
        if self.check_url(submission.url) == 1:
            embed.set_image(url=submission.url)
        elif self.check_url(submission.url) == 2:
            mediaType = "gif"
            print("media1")
        elif self.check_url(submission.url) == 3:
            embed.title=""
            mediaType = "video"
            print("media")
        else:
            embed.set_image(url="https://i.redd.it/4tlipwxnbtdz.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_author(name=submission.author.name)
        embed.set_footer(text="Visit the docs for this bot at *website here*", icon_url="https://i.redd.it/4tlipwxnbtdz.jpg")
        return (embed, mediaType, submission.url)

                
                                                
    def check_url(self, url):
        if url.find(".jpg")  > -1 or url.find(".png") > -1:
            return 1
        elif url.find("gfy") > 1 or url.find(".gif") > -1 or url.find(".mp4") > -1  or url.find("vimeo.") > -1 or url.find("twitch.") > -1:
            return 2
        elif url.find("tube.") > -1 or url.find("youtu.") > -1:
            return 3
        else:
            return 4


    def nsfw_check(self):
        return is_nsfw










