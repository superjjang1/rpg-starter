"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Hero():
    def __init__ (self, health, power):
       
        self.health = health
        self.power = power
    def attack(self, Goblin):
        Goblin.health -= Hero.power
        print("You do %d damage to the goblin." % Hero.power)
        return Goblin.health
        # if Goblin.health <= 0:
        #     print("The goblin is dead.")

class Goblin():
    def __init__ (self, health, power):
    
        self.health = health
        self.power = power


def main():
    Hero.health = 10
    Hero.power = 5
    Goblin.health = 6
    Goblin.power = 2
    Ziro = Hero(Hero.health, Hero.power)
    Kiro = Goblin(Goblin.health, Goblin.power)

    while Goblin.health > 0 and Hero.health > 0:
        print("You have %d health and %d power." % Ziro)
        print("The goblin has %d health and %d power." % Kiro)
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            Goblin.health -= Hero.power
            Hero.attack(Goblin)
            # print("You do %d damage to the goblin." % Hero.power)
            # if Goblin.health <= 0:
            #     print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Goblin.health > 0:
            # Goblin attacks hero
            Hero.health -= Goblin.power
            print("The goblin does %d damage to you." % Goblin.power)
            if Hero.health <= 0:
                print("You are dead.")

main()
