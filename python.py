import random

class Room:
    """Represents a room in the game."""
    def __init__(self, number, description, has_item=False):
        self.number = number
        self.description = description
        self.has_item = has_item
        self.item_name = f"Artifact {number}" if has_item else None

    def explore(self):
        """Displays the room description and checks for an item."""
        print(f"\nYou enter Room {self.number}: {self.description}")
        if self.has_item:
            return self.item_name
        return None

class Player:
    """Represents the player and their inventory."""
    def __init__(self):
        self.inventory = []

    def collect_item(self, item):
        """Adds an item to the player's inventory."""
        if item and item not in self.inventory:
            self.inventory.append(item)
            print(f"You found a hidden item: {item}!")
        elif item:
            print("You've already taken the item from this room.")

    def has_all_items(self):
        """Checks if the player has collected all required items."""
        return len(self.inventory) >= 5

class Game:
    """Handles game logic and progression."""
    def __init__(self):
        self.rooms = self.create_rooms()
        self.player = Player()
        self.visited_rooms = set()

    def create_rooms(self):
        """Creates 10 rooms with random hidden items."""
        descriptions = [
            "A dark hallway with flickering torches.",
            "A dusty library filled with ancient books.",
            "A flooded chamber with a narrow bridge.",
            "A mysterious room covered in glowing symbols.",
            "A collapsed passage with a small opening.",
            "A treasure vault with locked chests.",
            "A garden overgrown with thorny vines.",
            "A stairway leading deeper underground.",
            "A cave filled with strange echoes.",
            "A grand door with golden carvings."
        ]
        item_rooms = set(random.sample(range(1, 11), 5))  # Randomly pick 5 rooms for items
        return {i+1: Room(i+1, descriptions[i], i+1 in item_rooms) for i in range(10)}

    def play(self):
        """Main game loop."""
        print("Welcome to the Treasure Hunt Adventure!")
        print("Explore the 10 rooms, find 5 hidden items, and unlock the Treasure Room.")

        while not self.player.has_all_items():
            try:
                room_choice = int(input("\nEnter a room number (1-10) to explore: "))
                if room_choice in range(1, 11):
                    if room_choice not in self.visited_rooms:
                        self.visited_rooms.add(room_choice)
                        item = self.rooms[room_choice].explore()
                        self.player.collect_item(item)
                    else:
                        print("You've already explored this room.")
                else:
                    print("Invalid choice. Choose a number between 1 and 10.")
            except ValueError:
                print("Enter a valid number.")

        print("\nYou've collected all 5 items! The Treasure Room is now open.")
        print("You enter the final chamber and claim your reward. Congratulations, you win!")

# Start the game
if __name__ == "__main__":
    game = Game()
    game.play()
