class Spaceship:
    def __init__(self, name: str):
        if not len(name):
            self.name = "Unnamed Regular Spaceship"
        else:
            self.name = name
        self._is_used = False

    def __del__(self):
        print(f"Spaceship \"{self.name}\" is now a Spacetrash:(")

    def print_name(self):
        print("I am ", self.name)

    def fly(self):
        if not self._is_used:
            print(f"\"{self.name}\" flew")
            self._is_used = True
        else: 
            print(f"\"{self.name}\" is out of fuel:(")


