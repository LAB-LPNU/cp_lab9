from spaceship import reusable_spaceship as rs
from spaceship import spaceship as sp

spaceship = sp.Spaceship("Voyager-2, but spaceship")
reusable_spaceship = rs.ReusableSpaceship("Space discover")

spaceship.fly()
spaceship.fly()
del spaceship

reusable_spaceship.fly()
reusable_spaceship.fly()
reusable_spaceship.land()
reusable_spaceship.land()
reusable_spaceship.fly()
del reusable_spaceship
