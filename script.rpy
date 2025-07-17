# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You", color = '#828282')
define h = Character("Hailey", color = '#f2d073')
define j = Character("Jericho",color = '#30732a')
define y = Character('Yun-Hee', color = '#870b0f')
define k = Character("Kenneth", color = '#5C0120')
define e = Character("Emily", color = '#5d0660')
define j2 = Character("Justin", color = '#211d1d')

# The game starts here.

label start:
    scene bg start
    with fade 

    label sprites:

        show mc neutral

        mc 'This must have been the shortest break everrrrr….'
        mc 'I just wanna sleep…maybe I could skip-'
        'I can feel the vibration of my phone as that stupid labubu song that Hailey setted up blasted loudly throughout the dorm room. '
        'It’s a good thing my roommate left for his morning run. '