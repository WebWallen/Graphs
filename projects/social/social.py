import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        # Override print statement with something more helpful because it's an object
        return self.name

class SocialGraph:
    def __init__(self):
        # Assign last_id to 0 because we'll increment later and want it to start at 1
        self.last_id = 0
        # Users (nodes of graph)
        self.users = {}
        # Friendships (edges of graph)
        self.friendships = {}
        # Both are containned inside a dictionary

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        # If the user and friend ID are the same...
        if user_id == friend_id:
            # ...print an error message because they're trying to friend themselves
            print("WARNING: You cannot be friends with yourself")
        # If the friend_id is associated with a user_id  (or vice versa) in the friendships dictionary...
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # ...print an error because these two users are already connected
            print("WARNING: Friendship already exists")
        # Otherwise...
        else:
            # Add the friend_id to our user's friends list
            self.friendships[user_id].add(friend_id)
            # Add the user id to their new friend's connections
            self.friendships[friend_id].add(user_id)
            # Two-way connection just like on Facebook and LinkedIn

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # Increment last_id +1 and reassign (new friend automatically last id)
        self.last_id += 1 
        # Assign the new User('s name) to the users dictionary entry attached to [last key]
        self.users[self.last_id] = User(name)
        # Assign an empty set to the friendships dictionary entry attached to [last key]
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Set last_id to 0 because we're starting from scratch and need to increment
        self.last_id = 0
        # Assign an empty dictionary to users (where we'll place each user node)
        self.users = {}
        # Assign an empty dictionary to friendships (where we'll place each edge connecting users)
        self.friendships = {}
        # For each index in the range of num_users passed in as an argument
        for i in range (num_users):
            # Add the user and pass in placeholder textg plus their ID number
            self.add_user(f"User {i+1}") # Starts at 1, goes up for each user
        # Assign an empty array to possible_friendships so we can use in a loop
        possible_friendships = []
        # For each user ID in our users list...
        for user_id in self.users:
            # For each friend ID in between the user_id and last_id (add 1 to each)...
            for friend_id in range(user_id + 1, self.last_id + 1):
                # Append both the user and friend id to possible_friendships
                possible_friendships.append((user_id, friend_id))
        # Use the random.shuffle method on possible_friendships
        random.shuffle(possible_friendships)
        # Make space so our print statement is distinct
        print("-----")
        # Print every possible friendship
        print(possible_friendships)
        # Ditto first print
        print("-----")
        # Multiply num_users by the avg_friendships argument, divide by 2, and assign to friendships
        available_friendships = num_users * avg_friendships // 2
        # For each index in the range of available_friendships...
        for i in range(available_friendships):
            # Assign each index of possible_friendships to friendship
            friendship = possible_friendships[i]
            # Add both the first and second index to our friendships dictionary
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
