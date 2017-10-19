label afterword:

label in_progress:

    play music "music/kim nen violin.mp3" noloop

    pm "The events in this game are as true as possible."
    show mom2 at leftAbove with dissolve
    pm "I tried to recreate everything as close as I could remember, but memory is always faulty. Especially during mundane moments."
    hide mom2 with dissolve
    show mom1 at rightAbove with dissolve
    pm "Honestly, the days around Labor day when my mom was diagnosed with stage 4 cancer I don't remember that well."
    hide mom1 with dissolve
    show mom3 at rightAbove with dissolve
    pm "What's in the game right now is the closest approximation I could make, although some parts may be omitted for brevity or privacy."
    hide mom3 with dissolve
    show mom4 at leftAbove with dissolve
    pm "I also apologize for putting words in people's mouths. I used whatever approximation my memory created. Please reach out if there's an issue."
    hide mom4 with dissolve
    show mom5 at rightAbove with dissolve
    pm "Special thanks to all the family and friends that supported me during the hardest time of my life,"
    hide mom5 with dissolve
    pm "RenPy for making this project much easier and possible,"
    pm "And you, for spending the time to read through this game."
    show momfinal at center_above_03 with dissolve
    pause 1

python:
    while (renpy.music.is_playing(channel='music')):
        renpy.pause()

return
