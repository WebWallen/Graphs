from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
flip_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversal_path = []

def explore(room, visited=None):
    # If no rooms have been visited yet...
    if visited is None:
        # Assign an empty set to visited
        visited = set()
    # Assign an empty array to explored_path
    explored_path = []
    # Add the current room's ID to visited
    visited.add(room.id)                                            # Note 1: room objects have an .id attached inside their class
    # For each potential exit we can choose in this room...
    for this_exit in room.get_exits():                              # Note 2: this method returns an [array] of valid directions
        # Move the player to a room in direction of exit
        new_room = room.get_room_in_direction(this_exit)            # Note 3: this method moves the player to a new room
        # If the new room hasn't been visited yet...
        if new_room.id not in visited:
            # Explore the new room, update visited, and check to see if it's a valid path (read: not a dead-end)
            valid_path = explore(new_room, visited)                 # Note 4: this logic restarts the loop in chosen room
            # If it is indeed a valid path (we can move deeper into the maze)...
            if valid_path:
                # Update our current path to include valid path     # Note 5: this logic moves player deeper into maze
                current_path = [this_exit] + valid_path + [flip_directions[this_exit]]
            # Otherwise (it's not a valid path)...
            else:
                # Update our current path and exclude invalid path  # Note 6: this logic allows player to backtrack
                current_path = [this_exit, flip_directions[this_exit]]
            # Whether the path was valid or not, add the current path to our explored path and reassign variable
            explored_path = explored_path + current_path
    # After all the loops and conditionals are complete, return the explored path
    return explored_path
# Assign the provided initial traversal_path variable to our explore function and pass in the player's current room to begin the game
traversal_path = explore(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
