# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Mother")
image Morning=im.Scale("morning.png",1920,1080)
image Bed=im.Scale("Bed.png",1920,1080)
image livinarea=im.Scale("livinarea.png",1920,1080)
image Reached=im.Scale("reached.png",1920,1080)
image Gym=im.Scale("gym.png",1920,1080)
image Gymback=im.Scale("The gym.png",1920,1080)
image Study=im.Scale("study.png",1920,1080)
image laptop=im.Scale("laptop.png",1920,1080)
image studylap=im.Scale("studylap.png",1920,1080)
image popup=im.Scale("popup.png",800,424)
image hub=im.Scale("hub.png",800,424)
image hub1=im.Scale("hub1.png",800,424)
image room1=im.Scale("room1.png",1920,1080)
image gift=im.Scale("gift.png",1920,1080)
image birthday=im.Scale("birthback.png",1920,1080)
image College=im.Scale("college.png",1920,1080)
image Back=im.Scale("back.png",1920,1080)
image Return=im.Scale("return.png",1920,1080)
image Think=im.Scale("think.png",1920,1080)
image Study1=im.Scale("study.png",1920,1080)
image future=im.Scale("fut.png",1920,1080)
image Rich=im.Scale("rich.png",1920,1080)
image Avg=im.Scale("avrg.png",1920,1080)
image Cop=im.Scale("cop.png",1920,1080)
image Cell=im.Scale("cell.png",1920,1080)
image Consult=im.Scale("consult.png",1920,1080)
image YT=im.Scale("yt.png",1920,1080)
image WEB=im.Scale("website.png",1920,1080)
image thanks=im.Scale("tks1.png",1920,1080)



# The game starts here.

label start:
    define m=Character("Mom",color="#ec2eca")
    define d=Character("Dad",color="#eb0909")
    define empty=Character(None,window_background=None,what_color="#ffffff",what_size=100,what_font="GTA.ttf",what_outlines=[( 1, "#000000", 0, 0 )])
    define frnd=Character("Friend",color="#3af800")
    define Trnr=Character("Trainer",color="#06ebf3")
    define u=Character("Uncle",color="#d9ff01")
    define c=Character(None,window_background=None,what_color="#fff")
    scene yagami
    play music"death_note.mp3"
    $ name=renpy.input("What's your name?")
    $ name=name.strip() or "Ethan"
    define e=Character("[name]")
    $ boy1.name = name
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    e"Click to continue"
    stop music
    play music "theme.mp3"
    $ renpy.movie_cutscene("./images/NEW.webm")
    #DAY1
    scene Morning 
    empty"{cps=5.0}A typical morning{/cps}"
    scene Bed
    with fade  
    play sound "ring.mp3"
   

    show character:
        xpos 0.7
        ypos 0.29
    # Yawns
    e "Another day, another early start."
    hide character 
    show mother:
        xpos 0.1
        ypos 0.21
    stop sound
    queue music "theme.mp3"
    m "Good morning, [e]. Breakfast is ready."
    hide mother
    show character:
        xpos 0.7
        ypos 0.29
    e "Thanks, Mom. I'll be down in a minute."
    hide character
    show father:
        xpos 0.7
        ypos 0.22
    d "Don't forget to grab your lunch before you go."
    hide father
    show character:
        xpos 0.7
        ypos 0.29
    e "Got it, Dad. Thanks."

    scene Reached
    with fade
    empty"{cps=5.0}Reached college!{/cps}"
    scene College
    show friend:
        xpos 0.7
        ypos 0.29
    frnd"Hey, [e]! Ready for another day of classes?"
    hide friend
    show char college:
        xpos 0.7
        ypos 0.29
    e "Ready as I'll ever be. How about you?"
    hide char college
    show friend:
        xpos 0.7
        ypos 0.29
    frnd"Same here. Let's try to make the most of it."
    hide friend
    
    scene Gym
    with fade
    play music "gym.mp3"
    empty"{cps=5.0}The gym!{/cps}"
    scene Gymback
    show trainer:
        xpos 0.1
        ypos 0.3
    Trnr"Looking good, [e]! Keep up the great work."
    hide trainer
    show character:
        xpos 0.7
        ypos 0.29
    e "Thanks, Coach. I'm trying to stay on track."
    hide character
    show trainer:
        xpos 0.1
        ypos 0.3
    Trnr"You're doing great. Just keep pushing yourself."
    hide trainer
    
    scene birthday
    play sound "bday.mp3"
    empty"It's [e]'s birthday"
    with fade 
    scene gift
    u "Happy birthday, [e]! I hope you like your gift."
    e "Wow, a laptop! Thank you so much, Uncle."
    show father at right
    with moveinright
    d"Happy birthday, [e]!"
    show mother at left
    with moveinleft
    m"Happy birthday, [e]!"
    hide father
    with moveoutright
    hide mother
    with moveoutleft

    play music "theme.mp3"
    scene Study
    empty"{cps=5.0}Alright, time to hit the books.{/cps}"
    scene room1
    with fade
    show character at left
    with moveinleft
    e"Ahh too tired. Gotta get some sleep. Good night!"
    empty"DAY-ENDS"


    #end day1
    #Day2 start
    show screen gameUI
    scene Morning 
    empty"{cps=5.0}A typical morning{/cps}"
    scene Bed
    with fade
    play sound "ring.mp3"
   
    menu:
        "stay in bed a little longer":
            show character at left
            with moveinleft
            e"Ahh a moment more"
            hide character
            with moveoutleft
            jump repeat
        "Get ready for school":
            label repeat:
                    scene livinarea
                    with wipeleft
                    show char college at left
                    with moveinleft
                    stop sound
                    queue music "theme.mp3"
                    e"Another day, another start"
                    show mother at right
                    with moveinright
                    m"Good Morning, [e]. Breakfast?"
                    hide mother
                    with moveoutright
                    show father at right
                    with moveinright
                    d"Dont forget your lunch before you go"
                    e"Yep [d]. Thanks!"
                    hide father
                    with moveoutright
                    hide char college
                    with moveoutleft
    scene Reached
    with fade
    empty"{cps=5.0}Reached college!{/cps}"
    scene bg classroom
    with wipeup
    show friend at right
    with moveinright
    frnd"Hey, [e]! Ready for classes?"
    show char college at left
    with moveinleft
    e"Yeah yeah. As I'll ever be. How about you?"
    frnd"Same here. Let's try to make the most of it."
    hide friend
    with moveoutright
    hide char college
    with moveoutleft
    menu:
        "Participate actively in interaction and discussion":
            $ boy1.Socialskill+=2
            $ boy1.Intelligence+=2 
        "Stay quiet and listen to lecture":
            $ boy1.Intelligence+=2 
    play sound "ring.mp3"
    "Sound of bell ringing signaling end of class"
    stop sound
    scene Gym
    with fade
    play music "gym.mp3"
    empty"{cps=5.0}The gym!{/cps}"
    scene Gymback
    with fade
    menu:
        "Increase intensity of your exercise":
            show trainer at right
            with moveinright 
            Trnr"Looking good,[e]! Keep up the great work"
            show character at left
            with moveinleft
            e"Thanks, Coach. I'm trying to do better!"
            $ boy1.Health+=1
            $ boy1.Intelligence+=1
            hide trainer
            with moveoutright
            hide character
            with moveoutleft
        "Take it easy and stick to your usual routine":
            show trainer at right
            with moveinright 
            Trnr"Looking good, [e]. Try working harder for higher gains."
            show character at left
            with moveinleft
            e"Yes Coach. I'll do my best."
            $ boy1.Health+=1
            hide trainer
            with moveoutright
            hide character
            with moveoutleft
    scene Study
    with fade
    play music "theme.mp3"
    empty"{cps=5.0}Study time{/cps}"
    scene laptop 
    with fade
    show character at left
    with moveinleft
    e"Alright, it's study time."
    e"I'll try to get better searches and notes online in my lap."
    scene studylap
    with fade
    show character at left
    with moveinleft
    show popup :
        xalign 0.5
        yalign 0.3
    with zoominout
    "A malicious pop appears..."
    e"Huh? An Ad? What's this?"
    hide character 
    with moveoutleft
    menu:
        "Explore the contents of the Ad":
            label rep:
                play music "watching.mp3"
                show character at left
                with moveinleft
                e"Looks kind of exciting. Let me give it a glance."
                hide popup
                with zoominout
                show hub :
                    xalign 0.5
                    yalign 0.3
                with zoominout
                "Opens to a world of adult movies, explicit screens flashes across his eyes"
                e"Umm. Woah! What on Earth is-"
                menu:
                    "watch more-yes":
                        show character at left
                        with moveinleft 
                        show hub1 :
                            xalign 0.5
                            yalign 0.3
                        with zoominout
                        e"Damn. Cool! This is legit! Really fun to watch!"
                        "Enjoys watching"
                        $ boy1.Intelligence-=1
                        $ boy1.Pornaddiction+=1
                        menu:
                            "continue watching-yes":
                                e"It's really vast! This is crazy!"
                                $ boy1.Intelligence-=1
                                $ boy1.Health-=1
                                $ boy1.Pornaddiction+=2
                                jump here
                            "continue watching-no":
                                hide hub1
                                with zoominout
                                "Perhaps I must stop. This isn't good."
                                $ boy1.Intelligence-=1
                                $ boy1.Health-=1
                                jump here
    
                    "watch more-no":
                        e"I shouldn't be watching this. Ugh."
                        $ boy1.Intelligence-=1
                        jump here
    
        "Ignore and continue surfing study materials":
            e"Nevermind. Not interested. Just a waste of time."
            jump rep

    label here:
        scene room1
        with fade
        stop music fadeout 1.0
        play music "theme.mp3"
        show character at left
        with moveinleft
        e"Ahh too tired. Gotta get some sleep. Good night!"
        empty"Day-ends"
    # Day2 end
    # Day3-start
    scene Morning 
    empty"{cps=5.0}A typical morning{/cps}"
    scene Bed
    with fade
    play sound "ring.mp3"
    
    menu:
        "Stay in bed a little longer":
            show character at left
            with moveinleft
            e"Come on! Five minutes more..."
            hide character
            with moveoutleft
            jump rep1
        "Get ready for school":
            label rep1:
                scene livinarea
                with wipeleft
                show char college at left
                with moveinleft
                stop sound
                queue music "theme.mp3"
                e"Argh. Sleepy-eepy."
                show mother at right
                with moveinright
                m"[e]! Get out of your bed already! You're late for class!"
                e"Oops-"
                hide mother
                with moveoutright
                show father at right
                with moveinright
                d"Get ready quickly son."
                e"In a jippy."
                hide father
                with moveoutright
                hide char college
                with moveoutleft
    scene Reached
    with fade
    empty"{cps=5.0}Reached college!{/cps}"
    scene bg classroom
    with wipeup
    show friend at right
    with moveinright
    frnd"[e]! You're late!"
    show char college at left
    with moveinleft
    e"Yeah. Spent extra time studying at night."
    frnd"I see. Anyway, let's join in."
    hide friend
    with moveoutright
    hide char college
    with moveoutleft
    menu:
        "Participate actively in interaction and discussion":
            $ boy1.Socialskill+=2
            $ boy1.Intelligence+=2
        "Stay quiet and listen to lecture":
            $ boy1.Intelligence+=1 
        "Stay distracted, dreaming about the scenes of last night":
            $ boy1.Socialskill-=1
    play sound "ring.mp3"
    "Bell ringing"
    stop sound
    scene Back 
    empty"{cps=5.0}GYM OR HOME"
    with fade
    menu:
        "Hit the gym":
            scene Gym
            with fade
            play music "gym.mp3"
            menu:
                "Increase the intensity of your exercises.":
                    scene Gymback
                    with fade
                    show trainer at right
                    with moveinright 
                    Trnr"Body-cutting is shaping you well [e]. Good going!"
                    show character at left
                    with moveinleft
                    e"Hehe. Trying to achieve better results."
                    $ boy1.Health+=1
                    $ boy1.Intelligence+=1
                    hide trainer
                    with moveoutright
                    hide character
                    with moveoutleft

                "Take it easy and stick to your usual routine.":
                    scene Gymback
                    with fade
                    show trainer at right
                    with moveinright 
                    Trnr"Good gains, [e]. But not that good enough!"
                    show character at left
                    with moveinleft
                    e"Yes coach. Will work harder."
                    $ boy1.Health+=1
                    hide trainer
                    with moveoutright
                    hide character
                    with moveoutleft
        "Stay lazy, go home":
            scene Return
            with fade
            play music "theme.mp3"
            menu:
                "Try studying a few lately taught concepts":
                    scene Study
                    with fade
                    e"These topics seem to be hard! Let me work hard!"
                    $ boy1.Intelligence+=1
                    $ boy1.Pornaddiction-=1
                "Continue exploring the contents of the malicious site":
                    play music "watching.mp3"
                    scene studylap
                    with fade
                    show character at left
                    with moveinleft
                    show hub :
                        xalign 0.5
                        yalign 0.3
                    with zoominout
                    e"Good heavens! My curiosity seems to morph into an all-consuming addiction."
                    $ boy1.Intelligence-=1
                    $ boy1.Socialskill-=1
                    $ boy1.Pornaddiction+=1
                    hide character
                    with moveoutleft
                    stop music fadeout 1.0
    scene Think
    empty"Study/Leisure Time"
    with fade
    play music "theme.mp3"
    menu:
        "Continue to study":
            scene Study1
            with fade
            show character at left
            with moveinleft
            e"Alright. I'm kinda getting a hold of this topic."
            $ boy1.Intelligence+=1
            $ boy1.Pornaddiction-=1
            hide character
            with moveoutleft
        "Stumble upon the site for a while":
            play music "watching.mp3"
            scene studylap
            with fade
            show character at left
            with moveinleft
            e"Let's find something more entertaining in this domain."
            show hub :
                xalign 0.5
                yalign 0.3
            with zoominout
            $ boy1.Intelligence-=1
            $ boy1.Pornaddiction+=1
            menu:
                "Continue watching-Yes":
                    show hub1:
                        xalign 0.5
                        yalign 0.3
                    with zoominout
                    e"More! More! This makes me feel better."
                    $ boy1.Intelligence-=1
                    $ boy1.Health-=1
                    $ boy1.Pornaddiction+=1
                    jump there
                "Continue watching-No":
                    hide hub 
                    with zoominout
                    e"I gotta stop for a while"
                    jump there
    label there:
    scene room1
    with fade
    play music "theme.mp3"
    show character at left
    with moveinleft
    e"Alright. Enough for the day. It's late already. Nighty"
    empty"Day-ends evaluation begins"
    #day-3 end
    #day-4 start
    if boy1.Pornaddiction>=5:
        #"here[boy1.Pornaddiction] 4a"
        jump day4a
    else:
        #"here[boy1.Pornaddiction] 4b"
        jump day4b
    label day4a:
        #day4a-start
        scene Morning 
        empty"{cps=5.0}Day 4: A typical morning{/cps}"
        scene Bed
        with fade
        play sound "ring.mp3"
        
        menu:
            "Stay in bed a little longer":
                show character at left
                with moveinleft
                e"WHAT!? Morning already? Don't wanna wake up!"
                hide character
                with moveoutleft
                jump rep2
            "Get ready for school":
                label rep2:
                    scene livinarea
                    with wipeleft
                    show char college at left
                    with moveinleft
                    stop sound
                    queue music "theme.mp3"
                    e"Didn't sleep well at all."
                    show mother at right
                    with moveinright
                    m"[e]. You seem so tired and unwell!"
                    e"Stressed out a bit. All cool."
                    hide mother
                    with moveoutright
                    show father at right
                    with moveinright
                    d"Seems like you've been working yourself a bit too much son."
                    e"I'd manage well I believe."
                    hide father
                    with moveoutright
                    hide char college
                    with moveoutleft
        scene Reached
        with fade
        empty"{cps=5.0}Reached college!{/cps}"
        scene bg classroom
        with wipeup
        show friend at right
        with moveinright
        frnd"[e] You seem trippy buddy. You all good bro?"
        show char college at left
        with moveinleft
        e"I seem to have got addicted."
        frnd"Addicted to-?"
        e"Nevermind. I'll let you know soon. We're late to class! Let's hurry!"
        hide friend
        with moveoutright
        hide char college
        with moveoutleft
        menu:
            "Participate actively in interaction and discussion":
                $ boy1.Socialskill+=2
                $ boy1.Intelligence+=2 
            "Stay quiet and listen to lecture":
                $ boy1.Intelligence+=1 
            "Stay distracted, dreaming about the scenes of last night":
                $ boy1.Socialskill-=1
        play sound "ring.mp3"
        "Bell ringing"
        stop sound
        scene Back 
        empty"{cps=5.0}GYM OR HOME"
        with fade
        menu:
            "Hit the gym":
                play music "gym.mp3"
                scene Gym
                with fade
                menu:
                    "Increase the intensity of your exercises.":
                        scene Gymback
                        with fade
                        show trainer at right
                        with moveinright 
                        Trnr"You've been maintaining your body well! Good job kid!"
                        show character at left
                        with moveinleft
                        e"You know me well by now. Don't you?"
                        $ boy1.Health+=1
                        $ boy1.Intelligence+=1
                        hide trainer
                        with moveoutright
                        hide character
                        with moveoutleft
    
                    "Take it easy and stick to your usual routine.":
                        scene Gymback
                        with fade
                        show trainer at right
                        with moveinright 
                        Trnr"Hmm. How about adding up a few reps or weights to your workouts?"
                        show character at left
                        with moveinleft
                        e"I'll see to it coach..."
                        $ boy1.Health+=1
                        hide trainer
                        with moveoutright
                        hide character
                        with moveoutleft
            "Stay lazy, go home":
                scene Return
                with fade
                play music "theme.mp3"
                menu:
                    "Try studying a few lately taught concepts":
                        scene Study
                        with fade
                        e"Class gets harder day by day!"
                        $ boy1.Intelligence+=2
                        $ boy1.Pornaddiction-=1
                    "Continue exploring the contents of the malicious site":
                        play music "watching.mp3"
                        scene studylap
                        with fade
                        show character at left
                        with moveinleft
                        show hub :
                            xalign 0.5
                            yalign 0.3
                        with zoominout
                        e"My addiction seems to run out of my control. I gotta seek help maybe."
                        $ boy1.Intelligence-=1
                        $ boy1.Socialskill-=1
                        $ boy1.Pornaddiction+=1
                        hide character
                        with moveoutleft
        scene Think
        empty"Study/Leisure Time"
        with fade
        menu:
            "Continue to study":
                play music "theme.mp3"
                scene Study1
                with fade
                show character at left
                with moveinleft
                e"Okay. This isn't that hard as I thought. I can do well in this subject I guess hehe."
                e"It's 2AM already. I did my assignments and homeworks anyway."
                $ boy1.Intelligence+=1
                $ boy1.Pornaddiction-=1
                hide character
                with moveoutleft
            "Stumble upon the site for a while":
                play music "watching.mp3"
                scene studylap
                with fade
                show character at left
                with moveinleft
                e"Let's surf something trending today."
                show hub :
                    xalign 0.5
                    yalign 0.3
                with zoominout
                $ boy1.Intelligence-=1
                $ boy1.Pornaddiction+=1
                menu:
                    "continue watching-yes":
                        show hub1:
                            xalign 0.5
                            yalign 0.3
                        with zoominout
                        e"My addiction seems to push me into the abyss. "
                        $ boy1.Intelligence-=1
                        $ boy1.Health-=1
                        $ boy1.Pornaddiction+=1
                        $ boy1.Socialskill-=1
                        jump there1
                    "continue watching-no":
                        hide hub 
                        with zoominout
                        e"I can't handle so much pressure. I have to try quitting."
                        e"It's 2AM already. What am I doing? I feel so ashamed of this. I don't think I can wake up for school on time. Good morning I suppose."
                        jump there1
                        stop music fadeout 1.0
        label there1:
        scene room1
        with fade
        show character at left
        with moveinleft
        e"Alright. Enough for the day. It's late already. Nighty"
        empty"Day-ends(judgement)"
        jump judgement
        #day41-end
    label day4b:
        #day42-start
        scene Morning 
        empty"{cps=5.0}Day 4:A typical morning{/cps}"
        scene Bed
        with fade
        play sound"ring.mp3"
        
        menu:
            "Stay in bed a little longer":
                show character at left
                with moveinleft
                e"Feeling fresh. Still, five minutes won't bother!"
                hide character
                with moveoutleft
                jump rep3
            "Get ready for school":
                label rep3:
                    scene livinarea
                    with wipeleft
                    show char college at left
                    with moveinleft
                    stop sound
                    queue music "theme.mp3"
                    e"Slept well. Feeling energetic!"
                    show mother at right
                    with moveinright
                    m"[e]. Good morning!"
                    e"Morning mom."
                    hide mother
                    with moveoutright
                    show father at right
                    with moveinright
                    d"Someone's woke up on time."
                    e"I know right! Morning dad."
                    hide father
                    with moveoutright
                    hide char college
                    with moveoutleft
        scene Reached
        with fade
        empty"{cps=5.0}Reached college!{/cps}"
        scene bg classroom
        with wipeup
        show friend at right
        with moveinright
        frnd"[e]! You seem happy and excited! Sup?"
        show char college at left
        with moveinleft
        e"Is it? I don't know."
        frnd"Alright. Did homework right?"
        e"Yep. Let's go to class!"
        hide friend
        with moveoutright
        hide char college
        with moveoutleft
        menu:
            "Participate actively in interaction and disscusion":
                $ boy1.Socialskill+=2
                $ boy1.Intelligence+=2 
            "Stay quiet and listen to lecture":
                $ boy1.Intelligence+=1 
            "Stay distracted, dreaming about the scenes of last night":
                $ boy1.Socialskill-=1
        play sound"ring.mp3"
        "Bell ringing"
        stop sound
        scene Back 
        empty"{cps=5.0}GYM OR HOME"
        with fade
        menu:
            "Hit the gym":
                play music "gym.mp3"
                scene Gym
                with fade
                menu:
                    "Increase the intensity of your exercises.":
                        scene Gym
                        with fade
                        show trainer at right
                        with moveinright 
                        Trnr"Mark my words. You seem to surpass your daily targets."
                        show character at left
                        with moveinleft
                        e"I'd take that as a compliment. Thanks!"
                        $ boy1.Health+=1
                        $ boy1.Intelligence+=1
                        hide trainer
                        with moveoutright
                        hide character
                        with moveoutleft
                        stop music fadeout 1.0
    
                    "Take it easy and stick to your usual routine.":
                        scene Gym
                        with fade
                        show trainer at right
                        with moveinright 
                        Trnr"You could do better by having lesser calories and more protein kid."
                        show character at left
                        with moveinleft
                        e"Umm about that... Yes coach."
                        $ boy1.Health+=1
                        hide trainer
                        with moveoutright
                        hide character
                        with moveoutleft
                        stop music fadeout 1.0

            "Stay lazy, go home":
                scene Return
                with fade
                menu:
                    "Try studying a few lately taught concepts":
                        play music "theme.mp3"
                        scene Study
                        with fade
                        e"Class gets harder day by day!"
                        $ boy1.Intelligence+=1
                        $ boy1.Pornaddiction-=1
                    "Continue exploring the contents of the malacious site":
                        play music "watching.mp3"
                        scene studylap
                        with fade
                        show character at left
                        with moveinleft
                        show hub :
                            xalign 0.5
                            yalign 0.3
                        with zoominout
                        e"My addiction seems to run out of my control. I gotta seek help maybe."
                        $ boy1.Intelligence-=1
                        $ boy1.Socialskill-=1
                        $ boy1.Pornaddiction+=1
                        hide character
                        with moveoutleft
                        stop music fadeout 1.0
        scene Think
        empty"Study/Leisure Time"
        with fade
        menu:
            "Continue to study":
                play music "theme.mp3"
                scene Study1
                with fade
                show character at left
                with moveinleft
                e"Okay. This isn't that hard as I thought. I can do well in this subject I guess hehe."
                e"It's 2AM already. I did my assignments and homeworks anyway."
                $ boy1.Intelligence+=1
                $ boy1.Pornaddiction-=1
                hide character
                with moveoutleft
            "Stumble upon the site for a while":
                play music "watching.mp3"
                scene studylap
                with fade
                show character at left
                with moveinleft
                e"Let's surf something trending today."
                show hub :
                    xalign 0.5
                    yalign 0.3
                with zoominout
                $ boy1.Intelligence-=1
                $ boy1.Pornaddiction+=1
                menu:
                    "continue watching-yes":
                        show hub1:
                            xalign 0.5
                            yalign 0.3
                        with zoominout
                        e"My addiction seems to push me into the abyss. "
                        $ boy1.Intelligence-=1
                        $ boy1.Health-=1
                        $ boy1.Pornaddiction+=1
                        $ boy1.Socialskill-=1
                        jump there2
                    "continue watching-no":
                        hide hub 
                        with zoominout
                        e"I can't handle so much pressure. I have to try quitting."
                        e"It's 2AM already. What am I doing? I feel so ashamed of this. I don't think I can wake up for school on time. Good morning I suppose."
                        jump there2
        label there2:
        scene room1
        with fade
        show character at left
        with moveinleft
        e"Alright. Enough for the day. It's late already. Nighty"
        empty"Day-ends(judgement)"  
        jump judgement
        #day42-end
    label judgement:
        scene future
        empty"{cps=8.0}Analyzing Result...{/cps}"
        empty"{cps=13.0}Analyzing Result...{/cps}"
        empty"{cps=13.0}Analyzing Result...{/cps}"
        if boy1.Pornaddiction >=8:
            jump high
            label high:
                play sound "fbi.mp3"
                queue music "theme.mp3"
                scene Cop
                with fade
                empty"{cps=7.0}OOPS!!{/cps}"
                scene Cell
                with fade
                "[e] NEEDS SERIOUS CONSULTATION!"
                scene Consult
                with fade
                scene WEB
                with fade
                "click on this{a}https://www.defendyoungminds.com/post/my-story-healing-from-pornography-addiction-7-step-plan-every-kid-can-use-change-their-habits-one-day-at-time{/a}"
                scene YT
                with fade
                "watch this{a}https://youtu.be/4ZtcbYGUwf8?si=K8-cR-4u3-y122_n{/a}" 
                with fade

        elif boy1.Pornaddiction >=5 and boy1.Pornaddiction <8:
            jump avg  
            label avg:
                play music "happy_happy.mp3"
                scene Avg
                empty"{cps=6.0}{size=50}Good! [e] managed to handle decisions well and ended up living a normal, happy lifestyle.{/size}{/cps}"
                with fade
        
        else:
            jump low
            label low:
                play music "gigachad.mp3"
                scene Rich
                empty"{cps=6.0}{size=50}Wow. [e] chose the right path to success and has become a billionare!{/size}{/cps}"
                with fade

    play music "credits.mp3"
    scene thanks 
    c"Created by"
    empty"Abel Saji"
    empty"Anandu Raveendran"
    empty"Dhanush P N"
    empty"Abhijith Mohan"
    stop music fadeout 1

       
return