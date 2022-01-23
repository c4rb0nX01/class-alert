#this is testing of my webhook to log pc poweron info .

from discord_webhook import DiscordWebhook, DiscordEmbed
import time
n=0
for i in range(1,10,1):
    #webhook Url
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/909466908745695332/-YnmJ0W52TKoQRzB6X6rzWEQc78xEJWMDI-1O51ji2I-0NIDnhuElADhcQdPl0Lzi1lm')
    #content column---------------------------------------------------------------------------------------------!
    content="> :ninja:Class Alert! @everyone"
    webhook.content = content
    #embed column begins------------------------------------------------------------------------------------!
    #embed object
    My="This Bot wat developed by c4rb0n"
    embed = DiscordEmbed(title='System powered on and logged in Successfully! ', description=My, color='33ff00')
    #set author
    embed.set_author(name='Device: c4rb0nXnitro5')
    #set footer
    embed.set_footer(text=n)
    #time stamp of msg
    embed.set_timestamp()
    #final execution :
    response = webhook.add_embed(embed)
    response = webhook.execute()
    print(n)
    n+=1
    time.sleep(10)
