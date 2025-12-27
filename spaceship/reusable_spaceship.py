from typing import final
from .spaceship import Spaceship

class ReusableSpaceship(Spaceship):
    def __init__(self, name: str):
        self._is_landed = True
        super().__init__(name)
    
    def land(self):
        if(self._is_landed):
            print(f"Spaceship \"{self.name}\" can not land if it is already landed")
        else:
            print(f"Spaceship \"{self.name}\" landed")
            self._is_landed = True
    
    @final
    def fly(self):
        if self._is_landed:
            print(f"Spaceship \"{self.name}\" flew away")
            self._is_landed = False
            return
        print(f"Spaceship \"{self.name}\" is already in space")
        

