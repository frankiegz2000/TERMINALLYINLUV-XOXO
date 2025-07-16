# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You", color = '#828282')
define h = Character("Hailey", color = '#f2d073')
define j = Character("Jericho",color = '#30732a')
define y = Character('윤희', color = '#870b0f')
define k = Character("Kenneth", color = '#5C0120')
define e = Character("Emily", color = '#5d0660')
define j2 = Character("Justin", color = '#211d1d')

# The game starts here.

label start:
    scene bg start
    with fade 

    label sprites:

        show mc neutral
    

    'Im finally back to college after spring break. Thinking to themself'
    mc 'This must have been the shortest break ever…'
    mc 'I just wanna sleep…maybe I could skip-'
    j 'Rise and shine! First day back we cannot be late..amirite?'
    "He said with a cheeky grin, chuckling to himself as he stood over me. "


    menu:

        'morning ... .youre really excited about going to class':
            'my voice sounded sleepy as i yawned soon showing him a small smile'
            ' he sounded like Kylie Kardashian when he woke me up...'
            j 'Of course I am! How can one not?!'
            'he said really cheerfully as he smiled brightly.'
            'I groaned as I just wanted to lay in bed and continue to sleep.'

        'ugh…did you HAVE to yell…its seven in the morning':
            'I groaned as I stretched and yawned.'
            'Jericho looked at me as his smile faltered a bit.'
            j 'Yeah…who is this excited in the morning..haha..'
            'he chuckled awkwardly as he itched the back of his neck.'
label hallway:
    scene bg hallway
    with dissolve
    'Jericho kept rambling on about his break'
    'I tried to pay attention as I slowly walked to my class, yawing every couple of seconds.'
    j 'You know what I mean?'
    'Jericho suddenly said a bit too loud as I felt eyes on us.'
    mc 'Yeah..yeah…'
    'Straightening myself out as I responded.'
    'He waved to me goodbye as he joined the other jocks'
    'I didnt mind as I entered my class.'

label classroom: 
    scene bg classroom
    'Setting my stuff down as I sat on my seat.'

    show kenneth happy at Position (xpos=0.9, ypos=1.05)
    k 'Well well well…'
    k 'you look unwell..'
    'he snickered at me as he adjusted his glasses.'
    hide kenneth happy at left
    'I rolled my eyes as I ignored him.'
    'Setting my stuff down and taking out my laptop.'
    k 'Or wait…'
    k 'is it that you got an'
    k 'A on our midterm?'
    'he said, teasing he rested his elbow on the desk'
    'Testing his chin in the palm of his hand'
    menu:
        'An A- is still good. You shouldnt be talking..didnt you drop a class? Or was it that you got kicked out?':
            'Mocking him as a smirked…'
            'He didnt reply so i took it as a sign of victory.'
            
        'I didnt give him a reaction.':
            'The professor assigned us a book to read'
            'The professor assigned us a book to read'
            'A book from…Aliza Grace?'
            'I opened the book'
            'Its poetry.'
            'It read'
            'He found me crying.'
            'He crew too.'
            'We both crode.'
            'What did I just read?'
            'I look over to see Keenth tearing up.'
            'What a baby.'
            'I turned the page to read another poem?'
            'Mama a girl behind you.'
            'No there isnt.'
            'Or was there. I dont know'
            'What am I reading?'
            'Kenneth cannot seriously be crying to this!'
            'Looking at him tearing up and being vulnerable was kinda'
            '...............'
            'cute??'
            'He wasnt being all nonchalant at all'
            'or mean just…'
            'Just then he caught me'
            k 'What are you looking at'
            'he said, whispering to me cold and mean.'
    menu:
        'You look like a baby crying to ... .this…grow up': 

            ' I whispered back, as I chuckled at him. '
            'He rolled his eyes, adjusting his glasses..again? '
            'Like the ones in anime…nonetheless'
            'the teacher rambled on how this book is inspirational and how it shows emotions blah blah…really stupid.'
            ' I kept glancing back at him, making sure it wasnt too obvious.'
            'He was just reading the book, very concentrated.'
            'BRRRRRASNNNGGGGGG'
            'The bell made me snap back into reality'
            'I started to pack up, getting up from my seat.'
            'I looked back to see Kenneth just to see he was gone'
            'well talking to the professor that is. Probably for extra credit or something.'

        'Nothing':
            'I slightly shrugged, smiling in a making-fun way.'
            k 'Youre probably just admiring how smart and diligent I am'
            ' Kenneth said in a matter-of-fact tone. '
            mc 'totally'
            ' I said sarcastically, rolling my eyes as I did so.'
            k 'Yeah, you definitely are'
            'He smirked as I didnt pay any more attention to him'
            'BRRRAANNNNNNGGGGGGGGGGG'
            'I started to pack up, getting up from my seat.'
            'I looked back to see Kenneth just to see he was gone'
            'well talking to the professor that is'
            'Probably for extra credit or something.'

label halls:
    scene bg halls
    with fade 
    'Hailey was down the hall on her phone.'
    'Walking up to her as I decided to scare her.'
    mc 'Boo!!'
    h 'WHAT THE HELL'
    'she jumped as she turned to see me, her sunglasses showing my reflection'
    'I laughed as she was clearly annoyed.'
    'I didnt care, it was funny.'
    'Im gonna kill you for that!!'
    menu:
        'Walk with her':
            h "your funny, Hailey!"
        
        'kill her.':
            'wait........'
            'shes a woman, Im not winning this. EVEN if its self defense'
            'Ill follow her'

label characterintro:
    'Walking to class as Hailey was beside me'
    'I can feel the sensation of the sun hitting my face as I try to fight the sun'
    'I can hear Hailey cackling.'
    h 'This is why you bring sunglasses dude'
    'She says in a mocking voice, snickering to herself as she watches me fight the sun.'
    mc 'Oh shut up, Im not wearing sunglasses for one minute to walk to class.'
    'Making sure my point is heard as I spoke in a defensive voice'
    'I turned to look at her as shes just staring at me.'
    ' Probably thinking of a comeback'
    'The rest of the walk was awkward'
    'neither of us said anything.'
    'I made it to my class, looking back as I gave a German bye.'
    'Walking into class, sitting in my usual seat.'
    'Hello ____'
    'I heard a soft sounding UwU catgirl voice and recognized it as Emily'
    'looking over at her and smiled'
    e 'Hey M&M'
    'I simply said as I waved. Pulling out my laptop and notebook'
    'Slightly turning as I see Emily just staring at me'
    menu: 
        'ignore':
            'Ignoring it as class went on'
            'remembering how Kenneth bickered about this teacher.'
            'Why am I even thinking about him?'
            e 'are you okay?'
            'Em said she saw me zoning out.'
            'she looked at me with concern in her eyes, examining my face.'

        'Are you good?':
            'I spoke in an annoyed tone as I looked at her nonchalantly cause Im just that guy fr.'
            'She looked at me with a blank expression'
            'quickly looking away'
            e 'mb'
            'she said in a more quiet and soft tone.'
            'I then remembered how Kenneth bickered about this teacher.'
            'Why am I even thinking about him?'
            e 'are you okay?'
            'Em said she saw me zoning out.'
            'Are…you good?'
            'she looked at me with concern in her eyes, examining my face.'
            mc 'Yeah. its chill'
            'her face showed she didnt believe me.'

    'The bell saved me as it rang, quickly packing up my stuff.'
    e 'hey, w-wanna head to the cafe..together'
    'She looked at me with a bit of desperation'
    'like she was pleading for me to go with her.I didnt even get an option as she took me by the hand.'
    'Her grip was oddly strong, considering her build.'
    'Walking down the hallway with her was weird'
    'no one was there.'
    'The soft sound of our footsteps was the only sound I could hear.'
    'Reaching outside as the sun shined bright.'
    'Too light. Not even being hot.'
    'he turned to look at me with her usual soft smile.'
    'Nothing feels right. Probably because its the first day back…?'
