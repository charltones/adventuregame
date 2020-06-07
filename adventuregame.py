from adventurelib import *

Item.immobile = False
Room.items = Bag()
inventory = Bag()

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

@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)

@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj and not obj.immobile:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    elif obj:
        say('It is a bit too big!')
    else:
        say('There is no %s here.' % item)
        
@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

@when('inventory')
@when('i')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)
        
@when("brush teeth")
def brush_teeth():
    say("""
        You squirt a bit too much toothpaste onto your
        brush and dozily jiggle it round your mouth.

        Your teeth feel clean and shiny now, as you
        run your tongue over them.
    """)

#############################################################
    
main_cart_pass = Room("""
    Main cart pass description. There is a dark passageway to the east and a tunnel to the south.
""")

goblet = Item('jewel encrusted goblet', 'goblet')
rock = Item('huge old rock', 'rock')
rock.immobile = True
main_cart_pass.items.add(goblet)
main_cart_pass.items.add(rock)

rat_chamber = Room("""
    Rat chamber description
""")

main_cart_pass.east = rat_chamber
rat_chamber.west = main_cart_pass

storage_room = Room("""
    storage room description
""")

rat_chamber.north = storage_room
storage_room.south = rat_chamber

tigers_lair = Room("""
    tigers lair description
""")

tiger = Item('hungry and rapacious sabre-tooth tiger', 'tiger')
tiger.immobile = True
tigers_lair.items.add(tiger)

storage_room.west = tigers_lair
tigers_lair.east = storage_room

hole = Room("""
    hole description
""")

storage_room.north = hole
hole.south = storage_room

inferno_room = Room("""
    inferno room description
""")

hole.north = inferno_room
inferno_room.south = hole

monster_battle = Room("""
    monster battle description
""")

gate_key = Item('rusty steel key', 'steel key')
monster_battle.items.add(gate_key)

hole.east = monster_battle
monster_battle.west = hole

trap_room = Room("""
    trap room description
""")

end_key = Item('old iron key', 'iron key')
trap_room.items.add(end_key)

inferno_room.west = trap_room
trap_room.east = inferno_room

gate = Room("""
    gate description
""")

main_cart_pass.south = gate
gate.north = main_cart_pass

key = Room("""
    key description
""")

gate.south = key
key.north = gate

blue_room = Room("""
    blue room description
""")

key.east = blue_room
blue_room.west = key

rail_01 = Room("""
    rail 01 description
""")

blue_room.south = rail_01
rail_01.north = blue_room

rail_02 = Room("""
    rail 02 description
""")

rail_01.west = rail_02
rail_02.east = rail_01

railend = Room("""
    railend description
""")

rail_02.north = railend
railend.south = rail_02

disc_battle = Room("""
    disc battle description
""")

railend.west = disc_battle
disc_battle.east = railend

ultros = Room("""
    ultros description
""")

disc_battle.north = ultros
ultros.south = disc_battle

end = Room("""
    Well done! You have escaped the MasterMines.
""")

ultros.north = end
end.south = ultros

#############################################################

current_room = main_cart_pass

look()
start()
