# Facade does interface simplification.
# Use Facade pattern, when there's a lot of objects with many API methods
# and we need to create a sub-set of those methods, to ease the use of those objects.

# Delete this and do my own

class Car(object):

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level
