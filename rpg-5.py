"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Hero():
    def __init__ (self, health, power):
        self.hero_health = health
        self.hero_power = power

    def attack(self, goblin):
        goblin.goblin_health -= self.hero_power
        print("You do %d damage to the goblin." % self.hero_power)
        return goblin.goblin_health

class Goblin(Hero):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.goblin_health = health
        self.goblin_power = power

    def attack(self, hero):
        hero.hero_health -= self.goblin_power
        print("Goblin did %d damage to Sean." % self.goblin_power)
        return hero.hero_health

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    Sean = Hero(hero_health, hero_power)
    Gobbi = Goblin(goblin_health, goblin_power)
    

    while goblin_health > 0 and hero_health > 0:
        print("You have %d health and %d power." % (hero_health, hero_power))
        print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do %d damage to the goblin." % hero_power)
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does %d damage to you." % goblin_power)
            if hero_health <= 0:
                print("You are dead.")

main()