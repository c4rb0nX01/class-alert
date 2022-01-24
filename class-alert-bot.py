import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

#real webhooks assigned here
webhook=DiscordWebhook(url='your webhook here')
content="> Class Alert @everyone "#change it to what ever you want
webhook.content = content
#embed object
des="Join ASAP!" #description
#class links replace here with your link
mde=''
phy=''
che=''
beee=''
eng=''
psp=''

while True:
    ctime = datetime.datetime.now().strftime("%H:%M:%S")#current time
    cday = datetime.datetime.today().strftime("%A")#current day (format : 'Aaaaaa...') example: Sunday
    if ctime == '09:25:00':                                                #1st hr........replace with your time 
        print("first class")
        if cday=='Monday' or cday=='Wednesday':                                
            embed = DiscordEmbed(title=mde, description=des, color='33ff00')
            embed.set_author(name='Maths')
            embed.set_footer(text='footer here'')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Tuesday':                                                  
            embed = DiscordEmbed(title=psp, description=des, color='33ff00')
            embed.set_author(name='PSP')
            embed.set_footer(text='footer here'')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Thursday':
            embed = DiscordEmbed(title=che, description=des, color='33ff00')
            embed.set_author(name='Chemistry')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Friday':
            embed = DiscordEmbed(title=phy, description=des, color='33ff00')
            embed.set_author(name='Physics')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday == 'Saturday':
            embed = DiscordEmbed(title=beee, description=des, color='33ff00')
            embed.set_author(name='BEEE')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;   
        else:
            print("holiday. i'm sleeping for 6 hours")#change it to whatever you want
            time.sleep(21600)# in seconds
    elif ctime == '10:40:00':                                               #2nd hour
        print("2nd class vro")
        if cday=='Monday':                                                  
            embed = DiscordEmbed(title=eng, description=des, color='33ff00')
            embed.set_author(name='English')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Tuesday':                                                  
            embed = DiscordEmbed(title=psp, description=des, color='33ff00')
            embed.set_author(name='PSP')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Wednesday':                                                  
            embed = DiscordEmbed(title=phy, description=des, color='33ff00')
            embed.set_author(name='Physics')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Thursday':
            embed = DiscordEmbed(title=beee, description=des, color='33ff00')
            embed.set_author(name='BEEE')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Friday':
            embed = DiscordEmbed(title=mde, description=des, color='33ff00')
            embed.set_author(name='Maths')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday == 'Saturday':
            embed = DiscordEmbed(title=che, description=des, color='33ff00')
            embed.set_author(name='Chemistry')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;   
        else:
            print("Holiday :)")
            time.sleep(21600)

    elif ctime == "11:35:00":                                               #3rd hour
        print("3rd class")
        if cday=='Monday':                                                  
            embed = DiscordEmbed(title=che, description=des, color='33ff00')
            embed.set_author(name='Chemistry')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Tuesday':                                                  
            embed = DiscordEmbed(title=phy, description=des, color='33ff00')
            embed.set_author(name='Physics')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Wednesday':                                                  
            embed = DiscordEmbed(title=eng, description=des, color='33ff00')
            embed.set_author(name='English')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Thursday':
            embed = DiscordEmbed(title=eng, description=des, color='33ff00')
            embed.set_author(name='English')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Friday':
            embed = DiscordEmbed(title=psp, description=des, color='33ff00')
            embed.set_author(name='PSP')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday == 'Saturday':
            embed = DiscordEmbed(title=phy, description=des, color='33ff00')
            embed.set_author(name='Physics')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;   
        else:
            print("Holiday :)")
            time.sleep(21600)

    elif ctime == "13:25:00":                                                       #4th hour
        print("4th class")
        if cday=='Monday':                                                  
            embed = DiscordEmbed(title=beee, description=des, color='33ff00')
            embed.set_author(name='BEEE')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Tuesday':                                                  
            embed = DiscordEmbed(title=mde, description=des, color='33ff00')
            embed.set_author(name='Maths')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Wednesday':                                                  
            embed = DiscordEmbed(title=che, description=des, color='33ff00')
            embed.set_author(name='Chemistry')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Thursday':
            embed = DiscordEmbed(title=psp, description=des, color='33ff00')
            embed.set_author(name='PSP')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Friday':
            embed = DiscordEmbed(title=beee, description=des, color='33ff00')
            embed.set_author(name='BEEE')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday == 'Saturday':
            embed = DiscordEmbed(title=mde, description=des, color='33ff00')
            embed.set_author(name='Maths')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;   
        else:
            print("Holiday :)")
            time.sleep(21600)

    elif ctime == "14:20:00":                                                   #5th hr
        print("5th class")
        if cday=='Monday':                                                  
            embed = DiscordEmbed(title=phy, description=des, color='33ff00')
            embed.set_author(name='Physics')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Tuesday':                                                  
            embed = DiscordEmbed(title=che, description=des, color='33ff00')
            embed.set_author(name='Chemistry')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Wednesday':                                                  
            embed = DiscordEmbed(title=beee, description=des, color='33ff00')
            embed.set_author(name='BEEE')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Thursday':
            embed = DiscordEmbed(title=psp, description=des, color='33ff00')
            embed.set_author(name='PSP')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday=='Friday':
            embed = DiscordEmbed(title=eng, description=des, color='33ff00')
            embed.set_author(name='English')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;
        elif cday == 'Saturday':
            embed = DiscordEmbed(title=eng, description=des, color='33ff00')
            embed.set_author(name='English')
            embed.set_footer(text='footer here')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            time.sleep(1800)
            continue;   
        else:
            print("Holiday :)")
            time.sleep(21600)

    else:
        #print(ctime)
        continue;
