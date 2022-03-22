class Weapon:

    def __init__(self, bullets: int):  # should receive a number of bullets (integer)
        self.bullets = bullets     # an attribute called bullets to store that number

    def shoot(self):    # The class should also have the following methods
        if self.bullets > 0:  # If there are bullets in the weapon
            self.bullets -= 1  # reduce them by 1
            return "shooting..."
        return "no bullets left"  # else:

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"



# weapon = Weapon(5)           # weapon = self;   5 = bullets:int
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)




