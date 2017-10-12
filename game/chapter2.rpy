label chapter2:

    play music "music/everyday1.mp3"
    scene car_to_campus with dissolve
    "Just like all the other trips back to campus, I pick up both of my roommates, Will and Brendan, and any other friends that fit in my car."
    scene black with dissolve
    pause 0.5
    scene car_campus with dissolve
    "The two hour ride is uneventful. We pick up dinner then head back to my apartment to eat and relax."

    scene apartment with dissolve
    pause 1.0
    scene my_room_apartment_night with wipeleft
    m "Ah, finally back. Oh yeah. Have to call home."
    play sound "sfx/dial_tone.mp3"
    pause 2.3
    m "Hi Mommy. I'm at my apartment now."
    mom "Good! Did you eat dinner yet?"
    m "Not yet. Going to now though."
    mom "Ok. Don't forget to refrigerate the food I marinated for you."
    m "Yup. Bye Mommy!"
    mom "Bye Johnny."
    play sound "sfx/hangup.mp3"
    pause 0.5
    scene apartment with wiperight
    "Dinner passes by while we watch videos. We call it an early night since school starts the next day."
    scene my_room_apartment_night with wipeleft
    pause 1.0
    scene black with dissolve
    play sound "sfx/lightswitch.mp3"
    pause 2

    scene my_room_apartment with dissolve
    "August 22, Monday"
    m "Ughhh it's too early..."
    scene to school with wiperight
    pause 0.8
    scene siebel with dissolve
    "The first day of class flies by. I hardly pay attention to the professors as they go over the itineraries of each class."
    scene way home with dissolve
    pause 1.0
    scene apartment with dissolve
    mt "I have a lot of time before dinner. Guess I'll stop by the office."
    scene car_campus with dissolve
    "My internship is on campus and allows me to work part time during the school year. I've been working there since January."
    scene black with dissolve
    "Work passes by as I catch up with everyone. I take my work laptop back with me so I can work from home."
    scene car work with dissolve

    m "Hi Mommy. Just finished work."
    mom "Good. Did anything exciting happen today?"
    m "Not really. Class was boring and work was the same as usual."
    mom "What are you going to eat for dinner tonight?"
    m "I think the chicken with rice."
    mom "Ok. I already miss you Johnny!"
    m "Don't worry. I'll be home in two weeks."
    m "I'm almost back to the apartment, so I'm going to go now."
    mom "Ok. Bye Johnny."
    m "Bye Mommy."
    play sound "sfx/hangup.mp3"
    pause 0.5
    scene apartment with dissolve
    pause 1.0
    scene my_room_apartment_night with wipeleft
    pause 1.0
    scene black with dissolve
    play sound "sfx/lightswitch.mp3"
    pause 2

    scene my_room_apartment with dissolve
    "August 25, Thursday"
    scene to school with wiperight
    pause 0.6
    scene siebel with dissolve
    pause 0.6
    scene way home with dissolve
    pause 0.6
    scene apartment with dissolve
    play sound "sfx/ringtone.mp3"
    mt "Whoops. Guess I forgot to call home yesterday."
    m "Hello?"
    dad "Hi Johnny. You mom's CT scan results came in..."
    m "Oh ok..."
    stop music fadeout 0.5
    dad "She has a tumor in her lower stomach."
    m "Um... do they know if it's cancerous?"
    dad "Not yet. They're going to do more scans later. Do you want to talk to your mom?"
    m "Yeah."
    mom "Hi Johnny."
    m "Hi Mommy. How do you feel?"
    mom "Ok. A little tired."
    m "That's good. I'll be home next week too."
    mom "Yeah. Can't wait to see you again Johnny."
    m "It's only been five days. I'll call again this weekend."
    mom "Ok. Bye Johnny."
    m "Bye Mommy."
    play sound "sfx/hangup.mp3"
    pause 1.0
    scene my_room_apartment_night with wipeleft
    pause 0.5
    scene desk with dissolve
    "The first thing I do is look up as much as I can about stomach tumors."
    "While the results aren't good, I find that every tumor isn't necessarily cancerous."
    "With the lack of information I currently have though, I don't find anything concrete."
    "I eat dinner and go to sleep worried but hopeful."
    scene black with dissolve
    play sound "sfx/lightswitch.mp3"
    pause 2

    # play music "music/everyday1.mp3"
    # scene my_room_apartment with dissolve
    # "August 27, Saturday"
    # play sound "sfx/message.mp3"
    # jon "You wanna come to our place around 9.30?"
    # play sound "sfx/text_short.mp3"
    # m "Aight sure"
    # "Jon is one of my long running friends. I've known him since elementary school."
    # "He's one of the few drinking buddies I have on campus."
    # "I get ready and head to his place"
    #
    # scene black with dissolve
    # pause 1.0
    # scene jons with dissolve
    # jon "Yo Pham."
    # m "Hey"
    # "We chat and drink for a bit. The fact "
    #
label in_progress:
    #
    "Throughout the week, my dad texts me and close family status updates."
    "August 26, Friday"
    play sound "sfx/message.mp3"
    pause 0.2
    dad "Sorry for this bad news: She has 2 problems: kidney and stomach that may require a surgery but at this time, to make sure, our family doctor sent her to kidney specialist tomorrow at 11am and stomach specialist Monday at noon."
    "August 27, Saturday"
    play sound "sfx/message.mp3"
    pause 0.2
    dad "We just came back from the urologist (kidney doctor) and he told us that she has a large tumor in her stomach that blocks solid food and causes 2 side problems: water in her lungs and left kidney & back pain."
    dad "The good news is her urine test passed so it seems her kidneys are still working properly but he still recommends for a surgery procedure to insert a left ureter stent"
    "August 29, Monday"
    play sound "sfx/message.mp3"
    pause 0.2
    dad "Today update: The gastroenterologist has scheduled Nen for a 3-hour endoscopy procedure at Lutheran General hospital at 12:30 pm tomorrow to find out the root cause of her stomach tumor and determine if this is a cancer or not then figure out the next steps."
    "August 30, Tuesday"
    play sound "sfx/message.mp3"
    pause 0.2
    dad "The endoscopy with biopsy procedure just completed which made the gastroenterologist suspect the tumor might be cancerous but he can't tell for sure until he get the biopsy test result from the lab by the end of this week."
    dad "At the mean time, he suggested taking some protein shakes like Ensure because her stomach wasn't completely blocked which allowed his scope go through during the procedure."

    "I just take these updates in stride hoping for the best."
    "At the same time, I still have to worry about classes and upcoming job fairs."
    scene siebel with dissolve
    play music "music/everyday1.mp3"
    "September 1, Thursday"
    mt "Man this lecture is impossible."
    mt "I wonder if I can drop this class... It's way too hard."
    "As I browse through my requirements, I find something odd."
    "I only had to complete 30 more hours to graduate."
    mt "No way. I can graduate a whole year early?"
    scene way home with dissolve
    play sound "sfx/dial_tone.mp3"
    pause 2.3
    m "Hi Mommy. How are you doing today?"
    mom "Hi Johnny. I'm ok."
    m "So, I think I'm able to graduate a year early."
    mom "Wow that's great!"
    m "I'll tell you more details when I get back tomorrow though. I'm going to talk to my advisor now."
    mom "Ok."
    m "Bye mommy."
    mom "Bye Johnny."
    play sound "sfx/hangup.mp3"
    pause 1.0
    scene black with dissolve
    "The meeting with my advisor reaffirms what I found out."
    "I would be able to graduate with my degree in only three years of study."
    "It's a lot to think about. I'd have to start applying for full time jobs instead."
    "I'd also be leaving college before a lot of my friends..."
    "I head home with a lot on my mind."
    scene apartment with dissolve
    pause 1.0
    scene my_room_apartment_night with wipeleft
    play sound "sfx/message.mp3"
    pause 0.2
    dad "Sorry for sharing this bad news: we just got the biopsy test result that indicates the tumor is definitely cancerous :-( Now, she is referred to an oncologist who is booked for next 10 days!"
    dad "Therefore, we will have to see one of his partners soon because her problem can't be waited for that long. It seems there are too many cancer patients nowadays!"
    mt "...I'll get to see her tomorrow. People beat cancer anyways."
    pause 1.0
    scene black with dissolve
    play sound "sfx/lightswitch.mp3"
    pause 2

    scene my_room_apartment with dissolve
    "September 2, Friday"
    mt "Last day of class before heading back to the suburbs."
    mt "Good thing I only have one lecture today."
    scene to school with wiperight
    pause 0.6
    scene siebel with dissolve
    pause 0.6
    scene way home with dissolve
    pause 0.6
    scene apartment with dissolve
    mt "Everyone isn't done with class until later. I can work from home for a bit."
    scene my_room_apartment with wipeleft
    play sound "sfx/message.mp3"
    pause 0.2
    play sound "sfx/message.mp3"
    mt "Probably more updates from Daddy."
    stop music fadeout 1.0
    show 9-2 at center_above_03 with dissolve
    "..."
    mt "What... does this even mean?"
    hide 9-2 with dissolve
    scene desk with dissolve
    "I hurry to look up stage 4 stomach cancer."
    show search at center_above with dissolve
    "The first thing that shows up is a 4\% survival statistic."
    hide search with dissolve
    mt "This can't be real..."
    scene sideways with dissolve
    "I slump over on my bed."
    scene sideways blurred with dissolve
    "Tears start to well up in my eyes when I think about my mom being gone."
    scene black with dissolve
    "I close my eyes and try to process everything."
    "Forget everything..."

    scene sideways with hpunch
    play sound "sfx/door.mp3"
    patrick "Yo! Who wants to play smash? I brought Tad too."
    "I hear my friends arrive through the front door."
    will "I want to play!"
    scene my_room_apartment with dissolve
    "I collect myself for a few moments then head to the living room with my work laptop."
    scene living apartment with wiperight
    m "Hey."
    tad "Hey John. Do you want to play?"
    m "Maybe in a bit."
    "I stare half at the TV and half at my work laptop."
    "I can't really even concentrate on anything."
    "There are just sounds of Smash Bros. and banter between my friends."
    "After their match finishes, I speak up."
    m "Hey... I have something to tell you guys."
    scene living apartment blurred with dissolve
    "I try to push more words out but start choking on them. Tears form up again."
    m "Sorry. One sec."
    patrick "Yeah. Take your time."
    scene living apartment with dissolve
    "I calm down over the course of their next match."
    m "Ok..."
    m "My mom was just diagnosed with stage 4 cancer."
    scene living apartment blurred with dissolve
    "I bury my mind back to my work as tears start forming again."
    "..."
    tad "...What kind of cancer is it?"
    m "Stomach."
    "..."
    m "And stage 4 is practically a death sentence."
    "..."
    patrick "We're here for you if you need someone to talk to."
    will "Yeah."
    m "Thanks guys. I'm going to go back to my room."
    scene my_room_apartment with wipeleft
    "Oh yeah... I know someone that went through something similar..."
    scene desk with dissolve
    "I process out an email while trying to think straight."
    m "You were absent for the first couple of weeks for an unknown reason to us all. When you came back, you made a very sad announcement yet stayed strong. I've suddenly ran into the same situation."
    m "My mom was just diagnosed with stage 4 stomach cancer. I'd like to meet with you and discuss how you coped with the death of your mother. Anytime is fine, just tell me when and where."
    m "Thanks for taking the time to read this, John"
    scene sideways with dissolve
    "I go back to my bed and try to relax until it was time to leave."
    scene black with dissolve
    pause 0.5

    scene my_room_apartment with dissolve
    play music "music/everyday1.mp3"
    "I compose myself again and pack everything I need."
    scene apartment with wiperight
    "Dan and Joe are here now and Brendan is finally awake two rooms over."
    m "Hey everyone ready? I'm going to start packing the car."
    joe "Yeah. Give me your bags so I can organize them."
    "I wasn't sure if anyone outside of Will, Patrick, and Tad knew about my mom, but I just try to act normal."
    scene black with wipeleft
    play sound "sfx/car_door1.mp3"
    pause 1.0
    scene apartment with wiperight
    joe "Alright we're all packed."
    patrick "Cool. Tad and I are going to head out then. Have a safe ride!"
    m "Yup. See ya guys."
    scene black with dissolve
    play audio "sfx/car_door1.mp3"
    pause 0.4
    play audio "sfx/car_door1.mp3"
    "Will, Brendan, Joe, Dan, and I cram into my small Honda Civic."
    scene car uofi with wipeleft
    pause 1.5
    scene car midway1 with dissolve
    "The ride goes by as usual. Most my mind is on just getting home though."
    scene black with dissolve
    "I drop off everyone then finally head back to my house."
    scene car_suburb_night with dissolve
    stop music fadeout 1.0
    pause 1.0
    scene front door night with dissolve
    play music ["music/Home.mp3", "music/normal.mp3"] fadeout 1.5 fadein 1.5
    "I ring the doorbell and head inside with my bags."
    scene dining room night with irisout
    dad "Hi Johnny. Are you hungry?"
    m "Yeah."
    dad "We have some good t-bone steaks for dinner. Lisa helped grill them."
    dad "Your mom is resting on the couch right now."
    m "Ok."


    jump chapter3
