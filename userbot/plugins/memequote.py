"""
# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# custom cmds by @heyworld to make it look more gayish
# Thanks to @AbhinavShinde @jisan7509 for strings
# Edited by @Jisan7509
Sing credits :By @PhycoNinja13b
Userbot module for having some fun with people.
"""
import asyncio
import random
from random import choice
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

# ================= CONSTANT =================


@bot.on(admin_cmd(pattern=f"logic$", outgoing=True))
@bot.on(sudo_cmd(pattern="logic$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event,"getting a logic...")
    await asyncio.sleep(2)
    x = random.randrange(1, 104)
    if x == 1:
        await event.edit(
            '`"Underwater bubbles and raindrops are total opposites of each other."`'
        )
    if x == 2:
        await event.edit(
            '`"If you buy an eraser you are literally paying for your mistakes."`'
        )
    if x == 3:
        await event.edit(
            '`"The Person you care for most has the potential to destroy you the most."`'
        )
    if x == 4:

        await event.edit(
            '`"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."`'
        )

    if x == 5:

        await event.edit(
            '`"Any video with ?wait for it? in the title is simply too long."`'
        )

    if x == 6:

        await event.edit(
            '`"Your age in years is how many times you?ve circled the Sun, but your age in months is how many times the Moon has circled you."`'
        )

    if x == 7:

        await event.edit(
            '`"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."`'
        )

    if x == 8:

        await event.edit(
            '`"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."`'
        )

    if x == 9:

        await event.edit(
            '`"The most crushing feeling is when someone smiles at you on the street and you don?t react fast enough to smile back."`'
        )

    if x == 10:

        await event.edit(
            '`"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."`'
        )

    if x == 11:

        await event.edit('`"A folder is for things that you don\'t want to fold."`')

    if x == 12:

        await event.edit(
            '`"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."`'
        )

    if x == 13:

        await event.edit(
            '`"If everything goes smoothly, you probably won\'t remember today."`'
        )

    if x == 14:

        await event.edit(
            '`"When you meet new people in real life, you unlock more characters for your dream world."`'
        )

    if x == 15:

        await event.edit(
            '`"Maybe if they renamed sunscreen to ?anti-cancer cream? more people would wear it."`'
        )

    if x == 16:

        await event.edit(
            '`"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."`'
        )

    if x == 17:

        await event.edit(
            '`"Parents worry about what their sons download and worry about what their daughters upload."`'
        )

    if x == 18:

        await event.edit(
            '`"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."`'
        )

    if x == 19:

        await event.edit(
            "`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`"
        )

    if x == 20:

        await event.edit('`"Technically, no one has ever been in an empty room."`')

    if x == 21:

        await event.edit(
            '`"An onion is the bass player of food. You would probably not enjoy it solo, but you?d miss it if it wasn?t there."`'
        )

    if x == 22:

        await event.edit(
            "`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`"
        )

    if x == 23:

        await event.edit(
            '`"Every single decision you ever made has brought you to read this sentence."`'
        )

    if x == 24:

        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    if x == 25:

        await event.edit(
            '`"Everybody wants you to work hard, but nobody wants to hear about how hard you work."`'
        )

    if x == 26:

        await event.edit(
            '`"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."`'
        )

    if x == 27:

        await event.edit(
            '`"No one remembers your awkward moments but they?re too busy remembering their own."`'
        )

    if x == 28:

        await event.edit(
            '`"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."`'
        )

    if x == 29:

        await event.edit(
            "`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`"
        )

    if x == 30:

        await event.edit(
            '`"The biggest irony is that computers & mobiles were invented to save out time!"`'
        )

    if x == 31:

        await event.edit(
            '`"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."`'
        )

    if x == 32:

        await event.edit(
            '`"You know you?re getting old when your parents start disappointing you, instead of you disappointing them."`'
        )

    if x == 33:

        await event.edit(
            '`"Humans are designed to learn through experience yet the education system has made it so we get no experience."`'
        )

    if x == 34:

        await event.edit(
            '`"By focusing on blinking, you blink slower... Same for breathing."`'
        )

    if x == 35:

        await event.edit(
            '`"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."`'
        )

    if x == 36:

        await event.edit(
            '`"Characters that get married in fiction were literally made for each other."`'
        )

    if x == 37:

        await event.edit(
            '`"Babies are a clean hard drive that can be programmed with any language."`'
        )

    if x == 38:

        await event.edit(
            "`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`"
        )

    if x == 39:

        await event.edit(
            "`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`"
        )

    if x == 40:

        await event.edit(
            '`"Maybe we don\'t find time travelers because we all die in 25-50 years."`'
        )

    if x == 41:

        await event.edit(
            '`"Sleep is the trial version of death, It even comes with ads based on your activity."`'
        )

    if x == 42:

        await event.edit(
            '`"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"`'
        )

    if x == 43:

        await event.edit(
            '`"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."`'
        )

    if x == 44:

        await event.edit(
            '`"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."`'
        )

    if x == 45:

        await event.edit('`"If Greenland actually turns green, we\'re all screwed."`')

    if x == 46:

        await event.edit(
            '`"If someone says clever things in your dream, it actually shows your own cleverness."`'
        )

    if x == 47:

        await event.edit(
            '`"Famous movie quotes are credited to the actor and not the actual writer who wrote them."`'
        )

    if x == 48:

        await event.edit(
            '`"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."`'
        )

    if x == 49:

        await event.edit('`"Ask yourself why the the brain ignores the second the."`')

    if x == 50:

        await event.edit(
            '`"You?ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."`'
        )

    if x == 51:

        await event.edit(
            '`"It will be a lot harder for kids to win against their parents in video games in the future."`'
        )

    if x == 52:

        await event.edit(
            '`"Everyone has flaws, if you don\'t recognize yours, you have a new one."`'
        )

    if x == 53:

        await event.edit('`"Raising a child is training your replacement."`')

    if x == 54:

        await event.edit(
            "`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`"
        )

    if x == 55:

        await event.edit(
            '`"There\'s always someone who hated you for no reason, and still does."`'
        )

    if x == 56:

        await event.edit(
            '`"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."`'
        )

    if x == 57:

        await event.edit(
            '`"The more important a good night\'s sleep is, the harder it is to fall asleep."`'
        )

    if x == 58:

        await event.edit(
            '`"Blessed are those that can properly describe the type of haircut they want to a new stylist."`'
        )

    if x == 59:

        await event.edit(
            "`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`"
        )

    if x == 60:

        await event.edit(
            '`"Theme park employees must be good at telling the difference between screams of horror and excitement."`'
        )

    if x == 61:

        await event.edit('`"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"`')

    if x == 62:

        await event.edit(
            '`"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."`'
        )

    if x == 63:

        await event.edit(
            '`"Listening to podcasts before bed is the adult version of story-time."`'
        )

    if x == 64:

        await event.edit(
            '`"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."`'
        )

    if x == 65:

        await event.edit('`"A ton of whales is really only like half a whale."`')

    if x == 66:

        await event.edit(
            '`"When you get old, the old you is technically the new you, and your young self is the old you."`'
        )

    if x == 67:

        await event.edit(
            '`"You probably won\'t find many negative reviews of parachutes on the Internet."`'
        )

    if x == 68:

        await event.edit(
            '`"We show the most love and admiration for people when they\'re no longer around to appreciate it."`'
        )

    if x == 69:

        await event.edit(
            "`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`"
        )

    if x == 70:

        await event.edit(
            '`"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."`'
        )

    if x == 71:

        await event.edit(
            "`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`"
        )

    if x == 72:

        await event.edit('`"The most effective alarm clock is a full bladder."`')

    if x == 73:

        await event.edit(
            '`"You probably just synchronized blinks with millions of people."`'
        )

    if x == 74:

        await event.edit(
            '`"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."`'
        )

    if x == 75:

        await event.edit(
            '`"Night before a day off is more satisfying than the actual day off."`'
        )

    if x == 76:

        await event.edit('`"We put paper in a folder to keep it from folding."`')

    if x == 77:

        await event.edit(
            '`"Somewhere, two best friends are meeting for the first time."`'
        )

    if x == 78:

        await event.edit(
            '`"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."`'
        )

    if x == 79:

        await event.edit(
            '`"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."`'
        )

    if x == 80:

        await event.edit(
            '`"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."`'
        )

    if x == 81:

        await event.edit('`"Wikipedia is what the internet was meant to be."`')

    if x == 82:

        await event.edit(
            '`"A theme park is the only place that you can hear screams in the distance and not be concerned."`'
        )

    if x == 83:

        await event.edit(
            '`"A wireless phone charger offers less freedom of movement than a wired one."`'
        )

    if x == 84:

        await event.edit(
            "`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`"
        )

    if x == 85:

        await event.edit(
            '`"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."`'
        )

    if x == 86:

        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    if x == 87:

        await event.edit(
            '`"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"`'
        )

    if x == 88:

        await event.edit(
            '`"Doing something alone is kind of sad, but doing it solo is cool af."`'
        )

    if x == 89:

        await event.edit(
            '`"Your brain suddenly becomes perfect at proofreading after you post something."`'
        )

    if x == 90:

        await event.edit(
            '`"There\'s always that one song in your playlist that you always skip but never remove."`'
        )

    if x == 91:

        await event.edit(
            '`"Kids next century will probably hate us for taking all the good usernames."`'
        )

    if x == 92:

        await event.edit('`"Bubbles are to fish what rain is to humans."`')

    if x == 93:

        await event.edit(
            '`"The more people you meet, the more you realise and appreciate how well your parents raised you."`'
        )

    if x == 94:

        await event.edit('`"A comma is a short pause, a coma is a long pause."`')

    if x == 95:

        await event.edit('`"Someday you will either not wake up or not go to sleep."`')

    if x == 96:

        await event.edit(
            '`"Bermuda Triangle might be the exit portal of this simulation."`'
        )

    if x == 97:

        await event.edit(
            '`"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."`'
        )

    if x == 98:

        await event.edit(
            "`Do You Know, Some Mosquitos Became Ghosts, When you *Killed* Them...`"
        )

    if x == 99:

        await event.edit("`Do You Know, Mosquitoes has Teleportation Power...`")

    if x == 100:

        await event.edit(
            "`Do You Know, When you see a bearded Goat, that means you juat saw a *Smarter Goat* than YOU....`"
        )

    if x == 101:

        await event.edit(
            "`Do You Know, when You give some ruppess to a Bus Conductor, He will give You a Piece of Paper, *Called Ticket*...`"
        )

    if x == 102:

        await event.edit("`Do You Know, Bus are called Bus, Because they are Bus....`")

    if x == 103:

        await event.edit(
            "`Do You Know, There's a Huge Difference between *Cartoon amd Anime*...`"
        )

    if x == 104:

        await event.edit("`Do You Know, We can't see Ghosts But Ghosts Can see Us...`")
        
        
@bot.on(admin_cmd(pattern=f"sing$", outgoing=True))
@bot.on(sudo_cmd(pattern="sing$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event,"singing...")
    await asyncio.sleep(2)
    x = random.randrange(1, 33)
    if x == 1:
        await event.edit(
            "🎶 I'm in love with the shape of you \n We push and pull like a magnet do\n Although my heart is falling too \n I'm in love with your body \n And last night you were in my room \n And now my bedsheets smell like you \n Every day discovering something brand new 🎶  \n 🎶  I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body \n Oh—I—oh—I—oh—I—oh—I \n I'm in love with your body 🎶 \n **-Shape of You**"
        )
    if x == 2:
        await event.edit(
            "🎶 I've been reading books of old \n The legends and the myths \n Achilles and his gold \n Hercules and his gifts \n Spiderman's control \n And Batman with his fists \n And clearly I don't see myself upon that list 🎶 \n **-Something Just Like This **"
        )
    if x == 3:
        await event.edit(
            "🎶 I don't wanna live forever \n 'Cause I know I'll be livin' in vain \n And I don't wanna fit wherever \n I just wanna keep callin' your name \n Until you come back home \n I just wanna keep callin' your name \n Until you come back home \n I just wanna keep callin' your name \n Until you come back home 🎶 \n **-I don't Wanna Live Forever **"
        )
    if x == 4:
        await event.edit(
            "🎶 Oh, hush, my dear, it's been a difficult year \n And terrors don't prey on \n Innocent victims \n Trust me, darling, trust me darling \n It's been a loveless year \n I'm a man of three fears \n Integrity, faith and \n Crocodile tears \n Trust me, darling, trust me, darling 🎶 \n **-Bad Lier"
        )
    if x == 5:
        await event.edit(
            "🎶 Walking down 29th and Park \n I saw you in another's arms \n Only a month we've been apart \n **You look happier** \n \n Saw you walk inside a bar \n He said something to make you laugh \n I saw that both your smiles were twice as wide as ours \n Yeah, you look happier, you do 🎶 \n **-Happier **"
        )
    if x == 6:
        await event.edit(
            "🎶 I took the supermarket flowers from the windowsill \n I threw the day old tea from the cup \n Packed up the photo album Matthew had made \n Memories of a life that's been loved \n Took the get well soon cards and stuffed animals \n Poured the old ginger beer down the sink \n Dad always told me, 'don't you cry when you're down' \n But mum, there's a tear every time that I blink 🎶 \n **-Supermarket Flowers**"
        )
    if x == 7:
        await event.edit(
            "🎶 And you and I we're flying on an aeroplane tonight \n We're going somewhere where the sun is shining bright \n Just close your eyes \n And let's pretend we're dancing in the street \n In Barcelona \n Barcelona \n Barcelona \n Barcelona 🎶 \n **-Barcelona **"
        )
    if x == 8:
        await event.edit(
            "🎶 Maybe I came on too strong \n Maybe I waited too long \n Maybe I played my cards wrong \n Oh, just a little bit wrong \n Baby I apologize for it \n \n I could fall, or I could fly \n Here in your aeroplane \n And I could live, I could die \n Hanging on the words you say \n And I've been known to give my all \n And jumping in harder than \n Ten thousand rocks on the lake 🎶 \n **-Dive**"
        )
    if x == 9:
        await event.edit(
            "🎶 I found a love for me \n Darling just dive right in \n And follow my lead \n Well I found a girl beautiful and sweet \n I never knew you were the someone waiting for me \n 'Cause we were just kids when we fell in love \n Not knowing what it was \n \n I will not give you up this time \n But darling, just kiss me slow, your heart is all I own \n And in your eyes you're holding mine 🎶 \n **-Perfect**"
        )
    if x == 10:
        await event.edit(
            "🎶 I was born inside a small town, I lost that state of mind \n Learned to sing inside the Lord's house, but stopped at the age of nine \n I forget when I get awards now the wave I had to ride \n The paving stones I played upon, they kept me on the grind \n So blame it on the pain that blessed me with the life 🎶 \n **-Eraser**"
        )
    if x == 11:
        await event.edit(
            "🎶 Say, go through the darkest of days \n Heaven's a heartbreak away \n Never let you go, never let me down \n Oh, it's been a hell of a ride \n Driving the edge of a knife. \n Never let you go, never let me down \n \n Don't you give up, nah-nah-nah \n I won't give up, nah-nah-nah \n Let me love you \n Let me love you 🎶 \n **-Let me Love You**"
        )
    if x == 12:
        await event.edit(
            "🎶 I'll stop time for you \n The second you say you'd like me to \n I just wanna give you the loving that you're missing \n Baby, just to wake up with you \n Would be everything I need and this could be so different \n Tell me what you want to do \n \n 'Cause I know I can treat you better \n Than he can \n And any girl like you deserves a gentleman 🎶 **-Treat You Better**"
        )
    if x == 13:
        await event.edit(
            "🎶 You're the light, you're the night \n You're the color of my blood \n You're the cure, you're the pain \n You're the only thing I wanna touch \n Never knew that it could mean so much, so much \n You're the fear, I don't care \n 'Cause I've never been so high \n Follow me through the dark \n Let me take you past our satellites \n You can see the world you brought to life, to life \n \n So love me like you do, lo-lo-love me like you do \n Love me like you do, lo-lo-love me like you do 🎶 \n **-Love me Like you Do**"
        )
    if x == 14:
        await event.edit(
            "🎶 Spent 24 hours \n I need more hours with you \n You spent the weekend \n Getting even, ooh ooh \n We spent the late nights \n Making things right, between us \n But now it's all good baby \n Roll that Backwood baby \n And play me close \n \n 'Cause girls like you \n Run around with guys like me \n 'Til sundown, when I come through \n I need a girl like you, yeah yeah 🎶 \n **-Girls Like You**"
        )
    if x == 15:
        await event.edit(
            "🎶 Oh, angel sent from up above \n You know you make my world light up \n When I was down, when I was hurt \n You came to lift me up \n Life is a drink and love's a drug \n Oh, now I think I must be miles up \n When I was a river dried up \n You came to rain a flood 🎶**-Hymn for the Weekend ** "
        )
    if x == 16:
        await event.edit(
            "🎶 I've known it for a long time \n Daddy wakes up to a drink at nine \n Disappearing all night \n I don’t wanna know where he's been lying \n I know what I wanna do \n Wanna run away, run away with you \n Gonna grab clothes, six in the morning, go 🎶 \n **-Runaway **"
        )
    if x == 17:
        await event.edit(
            "🎶 You were the shadow to my light \n Did you feel us \n Another start \n You fade away \n Afraid our aim is out of sight \n Wanna see us \n Alive 🎶 \n **-Faded**"
        )
    if x == 18:
        await event.edit(
            "🎶 It's been a long day without you, my friend \n And I'll tell you all about it when I see you again \n We've come a long way from where we began \n Oh I'll tell you all about it when I see you again \n When I see you again 🎶 \n **-See you Again**"
        )
    if x == 19:
        await event.edit(
            "🎶 I can swallow a bottle of alcohol and I'll feel like Godzilla \n Better hit the deck like the card dealer \n My whole squad's in here, walking around the party \n A cross between a zombie apocalypse and big Bobby 'The \n Brain' Heenan which is probably the \n Same reason I wrestle with mania 🎶 \n **-Godzilla**"
        )
    if x == 20:
        await event.edit(
            "🎶 Yeah, I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more \n I'm gonna take my horse to the old town road \n I'm gonna ride 'til I can't no more (Kio, Kio) 🎶 \n **-Old Town Road**"
        )
    if x == 21:
        await event.edit(
            "🎶 Oh-oh, ooh \n You've been runnin' round, runnin' round, runnin' round throwin' that dirt all on my name \n 'Cause you knew that I, knew that I, knew that I'd call you up \n You've been going round, going round, going round every party in L.A. \n 'Cause you knew that I, knew that I, knew that I'd be at one, oh 🎶 \n **-Attention **"
        )
    if x == 22:
        await event.edit(
            "🎶 This hit, that ice cold \n Michelle Pfeiffer, that white gold \n This one for them hood girls \n Them good girls straight masterpieces \n Stylin', wilin', livin' it up in the city \n Got Chucks on with Saint Laurent \n Gotta kiss myself, I'm so pretty \n \n I'm too hot (hot damn) \n Called a police and a fireman \n I'm too hot (hot damn) \n Make a dragon wanna retire man \n I'm too hot (hot damn) \n Say my name you know who I am \n I'm too hot (hot damn) \n And my band 'bout that money, break it down 🎶 \n **-Uptown Funk**"
        )
    if x == 23:
        await event.edit(
            "🎶 Just a young gun with the quick fuse \n I was uptight, wanna let loose \n I was dreaming of bigger things \n And wanna leave my own life behind \n Not a yes sir, not a follower \n Fit the box, fit the mold \n Have a seat in the foyer, take a number \n I was lightning before the thunder \n \n Thunder, feel the thunder \n Lightning then the thunder \n Thunder, feel the thunder \n Lightning then the thunder \n Thunder, thunder 🎶 \n **-Thunder**"
        )
    if x == 24:
        await event.edit(
            "🎶 Oh, love \n How I miss you every single day \n When I see you on those streets \n Oh, love \n Tell me there's a river I can swim that will bring you back to me \n 'Cause I don't know how to love someone else \n I don't know how to forget your face \n No, love \n God, I miss you every single day and now you're so far away \n So far away 🎶 \n **-So Far Away**"
        )
    if x == 25:
        await event.edit(
            "🎶 And if you feel you're sinking, I will jump right over \n Into cold, cold water for you \n And although time may take us into different places \n I will still be patient with you \n And I hope you know 🎶 \n **-Cold Water**"
        )
    if x == 26:
        await event.edit(
            "🎶 When you feel my heat \n Look into my eyes \n It's where my demons hide \n It's where my demons hide \n Don't get too close \n It's dark inside \n It's where my demons hide \n It's where my demons hide 🎶 \n **-Demons**"
        )
    if x == 27:
        await event.edit(
            "🎶 Who do you love, do you love now? \n I wanna know the truth (whoa) \n Who do you love, do you love now? \n I know it's someone new \n You ain't gotta make it easy, where you been sleepin'? 🎶 \n **-Who do  Love? **"
        )
    if x == 28:
        await event.edit(
            "🎶 Your touch is magnetic \n 'Cause I can't forget it \n (There's a power pulling me back to you) \n And baby I'll let it \n 'Cause you're so magnetic I get it \n (When I'm waking up with you, oh) 🎶 \n **-Magnetic**"
        )
    if x == 29:
        await event.edit(
            "🎶 Girl my body don't lie, I'm outta my mind \n Let it rain over me, I'm rising so high \n Out of my mind, so let it rain over me \n \n Ay ay ay, ay ay ay let it rain over me \n Ay ay ay, ay ay ay let it rain over me 🎶 \n **-Rain over Me**"
        )
    if x == 30:
        await event.edit(
            "🎶 I miss the taste of a sweeter life \n I miss the conversation \n I'm searching for a song tonight \n I'm changing all of the stations \n I like to think that we had it all \n We drew a map to a better place \n But on that road I took a fall \n Oh baby why did you run away? \n \n I was there for you \n In your darkest times \n I was there for you \n In your darkest night 🎶 \n **-Maps**"
        )
    if x == 31:
        await event.edit(
            "🎶 I wish—I wish that I was bulletproof, bulletproof \n I wish—I wish that I was bulletproof, bulletproof \n (Bullet-bulletproof, bullet-bullet-bulletproof) \n I'm trippin' on my words and my patience \n Writing every verse in a cadence \n To tell you how I feel, how I feel, how I feel (Yeah) \n This is how I deal, how I deal, how I deal (Yeah) \n With who I once was, now an acquaintance \n Think my confidence (My confidence) is in the basement \n Tryin' to keep it real, keep it real, keep it real (Yeah) \n 'Cause I'm not made of steel, made of steel 🎶 \n **-Bulletproof**"
        )
    if x == 32:
        await event.edit(
            "🎶 You won't find him down on Sunset \n Or at a party in the hills \n At the bottom of the bottle \n Or when you're tripping on some pills \n When they sold you the dream you were just 16 \n Packed a bag and ran away \n And it's a crying shame you came all this way \n 'Cause you won't find Jesus in LA \n And it's a crying shame you came all this way \n 'Cause you won't find Jesus in LA 🎶 \n **-Jesus in LA**"
        )
    if x == 33:
        await event.edit("Not in a mood to sing. Sorry!")


LOVESTR = [
    "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
    "Love recognizes no barriers. It jumps hurdles, leaps fences, penetrates walls to arrive at its destination full of hope.",
    "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
    "The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.",
    "I swear I couldn't love you more than I do right now, and yet I know I will tomorrow.",
    "When I saw you I fell in love, and you smiled because you knew it.",
    "In all the world, there is no heart for me like yours. / In all the world, there is no love for you like mine.",
    "To love or have loved, that is enough. Ask nothing further. There is no other pearl to be found in the dark folds of life.",
    "If you live to be a hundred, I want to live to be a hundred minus one day, so I never have to live without you.",
    "Some love stories aren't epic novels. Some are short stories. But that doesn't make them any less filled with love.",
    "As he read, I fell in love the way you fall asleep: slowly, and then all at once.",
    "I've never had a moment's doubt. I love you. I believe in you completely. You are my dearest one. My reason for life.",
    "Do I love you? My god, if your love were a grain of sand, mine would be a universe of beaches.",
    "I am who I am because of you.",
    "I just want you to know that you're very special... and the only reason I'm telling you is that I don't know if anyone else ever has.",
    "Remember, we're madly in love, so it's all right to kiss me any time you feel like it.",
    "I love you. I knew it the minute I met you.",
    "I loved her against reason, against promise, against peace, against hope, against happiness, against all discouragement that could be.",
    "I love you not because of who you are, but because of who I am when I am with you.",
]

DHOKA = [
    "Humne Unse Wafa Ki, Aur Dil Bhi Gya Toot, Wo Bhi Chinaal Nikli, Uski Maa ki Chut.",
    "Dabbe Me Dabba, Dabbe Me Cake ..Tu Chutiya Hai Zara Seesha To Dekh.",
    "Kaam Se Kaam Rakhoge Toh Naam Hoga, Randi Log Ke Chakkkar Me Padoge to Naam Badnaam Hoga.",
    "Usne Kaha- Mah Lyf maH Rule, Maine Kaha Bhag BSDK , Tujhy Paida Karna hi Teri Baap ki Sabse Badi Vul.",
    "Humse Ulajhna Mat, BSDK Teri Hasi Mita Dunga, Muh Me Land Daal Ke..Sari Hosiyaari Gand Se Nikal Dunga.",
    "Aur Sunau Bhosdiwalo ..Kya Haal Hai?..Tumhare Sakal Se Zayda Toh Tumhare Gand Laal Hai!!",
    "Pata Nhi Kya Kashish Hai Tumhare Mohabbat Me,Jab Bhi Tumhe Yaad Karta Hu Mera Land Khada Ho Jata Hai.",
    "Konsa Mohabbat Kounsi Story, Gand Faad Dunga Agr Bolne Aayi Sorry!",
    "Naam Banta Hai Risk Se, Chutiya Banta Hai IshQ Se.",
    "Sun Be, Ab Tujhy Mere Zindegi Me Ane ka Koi Haq Nhi,,Aur Tu 1 Number Ki Randi Hai Isme KOi Saq Nhi.",
    "Beta Tu Chugli Karna Chor De , Hum Ungli Karna Chor Dengy.",
]

METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]


GDNOON = [
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good Afternoon Dear!`",
    "`With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!`",
    "`The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!`",
    "`Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.`",
    "`With you, every part of a day is beautiful. I live every day to love you more than yesterday. Wishing you an enjoyable afternoon my love!`",
    "`This bright afternoon sun always reminds me of how you brighten my life with all the happiness. I miss you a lot this afternoon. Have a good time`!",
    "`Nature looks quieter and more beautiful at this time of the day! You really don’t want to miss the beauty of this time! Wishing you a happy afternoon!`",
    "`What a wonderful afternoon to finish you day with! I hope you’re having a great time sitting on your balcony, enjoying this afternoon beauty!`",
    "`I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!`",
    "`As you prepare yourself to wave goodbye to another wonderful day, I want you to know that, I am thinking of you all the time. Good afternoon!`",
    "`This afternoon is here to calm your dog-tired mind after a hectic day. Enjoy the blessings it offers you and be thankful always. Good afternoon!`",
    "`The gentle afternoon wind feels like a sweet hug from you. You are in my every thought in this wonderful afternoon. Hope you are enjoying the time!`",
    "`Wishing an amazingly good afternoon to the most beautiful soul I have ever met. I hope you are having a good time relaxing and enjoying the beauty of this time!`",
    "`Afternoon has come to indicate you, Half of your day’s work is over, Just another half a day to go, Be brisk and keep enjoying your works, Have a happy noon!`",
    "`Mornings are for starting a new work, Afternoons are for remembering, Evenings are for refreshing, Nights are for relaxing, So remember people, who are remembering you, Have a happy noon!`",
    "`If you feel tired and sleepy you could use a nap, you will see that it will help you recover your energy and feel much better to finish the day. Have a beautiful afternoon!`",
    "`Time to remember sweet persons in your life, I know I will be first on the list, Thanks for that, Good afternoon my dear!`",
    "`May this afternoon bring a lot of pleasant surprises for you and fills you heart with infinite joy. Wishing you a very warm and love filled afternoon!`",
    "`Good, better, best. Never let it rest. Til your good is better and your better is best. “Good Afternoon`”",
    "`May this beautiful afternoon fill your heart boundless happiness and gives you new hopes to start yours with. May you have lot of fun! Good afternoon dear!`",
    "`As the blazing sun slowly starts making its way to the west, I want you to know that this beautiful afternoon is here to bless your life with success and peace. Good afternoon!`",
    "`The deep blue sky of this bright afternoon reminds me of the deepness of your heart and the brightness of your soul. May you have a memorable afternoon!`",
    "`Your presence could make this afternoon much more pleasurable for me. Your company is what I cherish all the time. Good afternoon!`",
    "`A relaxing afternoon wind and the sweet pleasure of your company can make my day complete. Missing you so badly during this time of the day! Good afternoon!`",
    "`Wishing you an afternoon experience so sweet and pleasant that feel thankful to be alive today. May you have the best afternoon of your life today!`",
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good afternoon dear!`",
    "`Noon time – it’s time to have a little break, Take time to breathe the warmth of the sun, Who is shining up in between the clouds, Good afternoon!`",
    "`You are the cure that I need to take three times a day, in the morning, at the night and in the afternoon. I am missing you a lot right now. Good afternoon!`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`I pray to god that he keeps me close to you so we can enjoy these beautiful afternoons together forever! Wishing you a good time this afternoon!`",
    "`You are every bit of special to me just like a relaxing afternoon is special after a toiling noon. Thinking of my special one in this special time of the day!`",
    "`May your Good afternoon be light, blessed, enlightened, productive and happy.`",
    "`Thinking of you is my most favorite hobby every afternoon. Your love is all I desire in life. Wishing my beloved an amazing afternoon!`",
    "`I have tasted things that are so sweet, heard words that are soothing to the soul, but comparing the joy that they both bring, I’ll rather choose to see a smile from your cheeks. You are sweet. I love you.`",
    "`How I wish the sun could obey me for a second, to stop its scorching ride on my angel. So sorry it will be hot there. Don’t worry, the evening will soon come. I love you.`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`With you every day is my lucky day. So lucky being your love and don’t know what else to say. Morning night and noon, you make my day.`",
    "`Your love is sweeter than what I read in romantic novels and fulfilling more than I see in epic films. I couldn’t have been me, without you. Good afternoon honey, I love you!`",
    "`No matter what time of the day it is, No matter what I am doing, No matter what is right and what is wrong, I still remember you like this time, Good Afternoon!`",
    "`Things are changing. I see everything turning around for my favor. And the last time I checked, it’s courtesy of your love. 1000 kisses from me to you. I love you dearly and wishing you a very happy noon.`",
    "`You are sometimes my greatest weakness, you are sometimes my biggest strength. I do not have a lot of words to say but let you make sure, you make my day, Good Afternoon!`",
    "`Every afternoon is to remember the one whom my heart beats for. The one I live and sure can die for. Hope you doing good there my love. Missing your face.`",
    "`My love, I hope you are doing well at work and that you remember that I will be waiting for you at home with my arms open to pamper you and give you all my love. I wish you a good afternoon!`",
    "`Afternoons like this makes me think about you more. I desire so deeply to be with you in one of these afternoons just to tell you how much I love you. Good afternoon my love!`",
    "`My heart craves for your company all the time. A beautiful afternoon like this can be made more enjoyable if you just decide to spend it with me. Good afternoon!`",
]


CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "`Get back here!`",
    "`Not so fast...`",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "`Jokes on you, I'm everywhere`",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "`Go bother someone else, no-one here cares.`",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]


HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "`Hey, howdy, hi!`",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`I come for peace!`",
    "Ahoy, matey!",
    "`Hi !`",
]

CONGRATULATION = [
    "`Congratulations and BRAVO!`",
    "`You did it! So proud of you!`",
    "`This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]

BYESTR = [
    "`Nice talking with you`",
    "`I've gotta go!`",
    "`I've gotta run!`",
    "`I've gotta split`",
    "`I'm off!`",
    "`Great to see you,bye`",
    "`See you soon`",
    "`Farewell!`",
]

GDNIGHT = [
    "`Good night keep your dreams alive`",
    "`Night, night, to a dear friend! May you sleep well!`",
    "`May the night fill with stars for you. May counting every one, give you contentment!`",
    "`Wishing you comfort, happiness, and a good night’s sleep!`",
    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",
    "`Good night to a friend who is the best! Get your forty winks!`",
    "`May your pillow be soft, and your rest be long! Good night, friend!`",
    "`Let there be no troubles, dear friend! Have a Good Night!`",
    "`Rest soundly tonight, friend!`",
    "`Have the best night’s sleep, friend! Sleep well!`",
    "`Have a very, good night, friend! You are wonderful!`",
    "`Relaxation is in order for you! Good night, friend!`",
    "`Good night. May you have sweet dreams tonight.`",
    "`Sleep well, dear friend and have sweet dreams.`",
    "`As we wait for a brand new day, good night and have beautiful dreams.`",
    "`Dear friend, I wish you a night of peace and bliss. Good night.`",
    "`Darkness cannot last forever. Keep the hope alive. Good night.`",
    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",
    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",
    "`Good night, friend! May you be filled with tranquility!`",
    "`Wishing you a calm night, friend! I hope it is good!`",
    "`Wishing you a night where you can recharge for tomorrow!`",
    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",
    "`Wishing my good friend relief from a hard day’s work! Good Night!`",
    "`Good night, friend! May you have silence for sleep!`",
    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",
    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",
    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",
    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",
    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",
    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",
    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",
    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",
    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",
    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",
]

GDMORNING = [
    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",
    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good morning!`",
    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",
    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",
    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",
    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",
    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",
    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",
    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it. Good morning!`",
    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",
    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",
    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",
    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",
    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",
    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",
    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",
    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",
    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",
    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",
    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",
    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",
    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",
    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",
    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",
    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",
    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",
    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",
    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",
    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",
    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",
    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",
    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",
    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",
]

    
@bot.on(admin_cmd(pattern=f"love$", outgoing=True))
@bot.on(sudo_cmd(pattern="love$", allow_sudo=True))
async def suru(chutiyappa):
    await edit_or_reply(chutiyappa,choice(LOVESTR))
    
    
@bot.on(admin_cmd(pattern=f"dhoka$", outgoing=True))
@bot.on(sudo_cmd(pattern="dhoka$", allow_sudo=True))
async def katgya(chutiya):
    await edit_or_reply(chutiya,choice(DHOKA))
    

@bot.on(admin_cmd(pattern=f"metoo$", outgoing=True))
@bot.on(sudo_cmd(pattern="metoo$", allow_sudo=True))
async def metoo(hahayes):
    await edit_or_reply(hahayes,choice(METOOSTR))

    
@bot.on(admin_cmd(pattern=f"gnoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="gnoon$", allow_sudo=True))
async def noon(noon):
    await edit_or_reply(noon,choice(GDNOON))


@bot.on(admin_cmd(pattern=f"chase$", outgoing=True))
@bot.on(sudo_cmd(pattern="chase$", allow_sudo=True))
async def police(chase):
    await edit_or_reply(chase,choice(CHASE_STR))


@bot.on(admin_cmd(pattern=f"congo$", outgoing=True))
@bot.on(sudo_cmd(pattern="congo$", allow_sudo=True))
async def Sahih(congrats):
    await edit_or_reply(congrats,choice(CONGRATULATION))


@bot.on(admin_cmd(pattern=f"qhi$", outgoing=True))
@bot.on(sudo_cmd(pattern="qhi$", allow_sudo=True))
async def hoi(hello):
    await edit_or_reply(hello,choice(HELLOSTR))


@bot.on(admin_cmd(pattern=f"qbye$", outgoing=True))
@bot.on(sudo_cmd(pattern="qbye$", allow_sudo=True))
async def bhago(bhagobc):
    await edit_or_reply(bhagobc,choice(BYESTR))


@bot.on(admin_cmd(pattern=f"gn$", outgoing=True))
@bot.on(sudo_cmd(pattern="gn$", allow_sudo=True))
async def night(night):
    await edit_or_reply(night,choice(GDNIGHT))


@bot.on(admin_cmd(pattern=f"gm$", outgoing=True))
@bot.on(sudo_cmd(pattern="gm$", allow_sudo=True))
async def morning(morning):
    await edit_or_reply(morning,choice(GDMORNING))
