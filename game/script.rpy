# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pm = Character("Present Me", who_color = "#1c5593")
define m = Character("Me", who_color = "#2162a8")
define mt = Character("My Thoughts", who_color = "#143b66")
define dad = Character("Daddy", who_color = "#590b0b")
define mom = Character("Mommy")
define lisa = Character("Lisa", who_color = "#b50c98")
define jimmy = Character("Jimmy", who_color = "#db780f")
define dan = Character("Dan N", who_color = "#b5051f")
define sarah = Character("Sarah", who_color = "#c13007")

define will = Character("Will", who_color = "#02703c")
define jon = Character("Jon", who_color = "#060044")
define brendan = Character("Brendan", who_color = "#0f8c5e")
define patrick = Character("Patrick", who_color = "#1411b2")
define ambika = Character("Ambika", who_color = "#8918ba")
define danM = Character ("Dan M", who_color = "#3f7f11")

image black = "#000000"

transform center_above:
    xalign 0.5
    yalign 0.4


label splashscreen:
    # define fadehold = Fade(1.0, 2.0, 1.0)

    scene black with pixellate
    pause 0.5
    # $ renpy.transition(fadehold)
    return

label start:
    stop music fadeout 1.0
    scene black
    pause 1.0

    # jump in_progress

    pm "This... is a hard story to tell."

    pm "Thinking of {b}her{/b} floods me with emotions and memories. It makes me sad just looking back at old times."
    pm "I can’t talk to her, live with her, or embrace her anymore."
    pm "All I have left is memories in my head, pictures, and a few old videos."
    pm "They aren’t even close to the real thing though. They don’t show just how amazing, how caring she was."
    pm "This is my best attempt at recollecting what happened during the summer and fall of 2016. The year my mom, Kim Nen Thi Bui, passed away."

    scene main quad with dissolve
    #TODO: get picture with leaves on trees
    "August 6, Tuesday"

    scene main quad gray with dissolve
    pm "Before that though, some background on me and my family."
    pm "At the time, I was an incoming junior studying computer science at the University of Illinois Urbana Champaign. I lived on campus for the summer working as an intern."
    #pm "My family situation was fine from what I could tell. I called back home once in awhile to talk with my parents and talked with my older brother and sister on occasion."
    pm "My parents were immigrants from Vietnam. They fled the country after the war ended due to the oppression of the new government. They had me pretty late though, so I’m far removed from all of that."
    pm "Both of my siblings are a good deal older because of that. I just attended my brother’s wedding a month prior."
    pm "My dad’s english was pretty good, but my mom spoke to me in broken English interspersed with Vietnamese. It felt pretty natural to me though since I grew up with it."
    pm "The end of summer was approaching, and I was getting ready to drive back to the suburbs of Chicago with my roommate and a friend."


    jump chapter1
