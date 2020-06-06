from adventurelib import *

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('e', direction='east')
@when('w', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        print(f'You go {direction}.')
        look()

space = Room("""
You are drifting in space. It feels very cold.

A slate-blue spaceship sits completely silently to your left,
its airlock open and waiting.
""")

spaceship = Room("""
The bridge of the spaceship is shiny and white, with thousands
of small, red, blinking lights.
""")

# current_room will be a global variable. Let's start out in
# space, so assign the 'space' room from above.
current_room = space


@when('enter airlock')
def enter_spaceship():
    # To set a global variable from within a function you have
    # to include the 'global' keyword, to avoid creating a
    # local variable instead.
    global current_room

    # Got to check if this action can be done here
    if current_room is not space:
        print('There is no airlock here.')
        return

    current_room = spaceship

    # You should include some narrative for every action to
    # ensure the transition doesn't feel abrupt.
    print(
        "You heave yourself into the airlock and slam your " +
        "hand on the button to close the outer door."
    )

    # Show the room description to indicate we have arrived.
    print(current_room)


Room.can_scream = True  # The default for all rooms
space.can_scream = False  # Set a value for a specific room.

@when('scream')
def scream():
    if current_room.can_scream:
        print(
            "You unleash a piercing shriek that " +
            "reverberates around you."
        )
    else:
        print(
            "You try to yell but there's no sound " +
            "in the vacuum of space."
        )


@when("brush teeth")
def brush_teeth():
    say("""
        You squirt a bit too much toothpaste onto your
        brush and dozily jiggle it round your mouth.

        Your teeth feel clean and shiny now, as you
        run your tongue over them.
    """)

print(current_room)
start()
