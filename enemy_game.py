import random
class Enemy:
    
    def __init__(self, name = "Enemy_df", remain_life = 50, power_of_atack = 10, number_of_bullet = 250):
        self.name = name
        self.remain_life = remain_life
        self.power_of_atack = power_of_atack
        self.number_of_bullet = number_of_bullet

    def attack(self):
        print(self.name + " " + "Attacking")
        waste_bullet = random.randrange(0, 10)
        print(str(waste_bullet) + " much of waste")
        self.number_of_bullet -= waste_bullet
        
        return (waste_bullet, self.power_of_atack)

    def is_attacked(self, waste_bullet, power_of_atack):
        print("I got shot")
        self.remain_life -= (waste_bullet * power_of_atack)

    def bullet_finish(self):
        if (self.number_of_bullet <= 0):
            print(self.name + "Talking : Out of game")
            return True
        return False

    def is_live(self):
        if (self.remain_life <=0):
            print("I'm going to be dead")

    def print(self):
        print("starting........")
        print("name:", self.name, "Remain Live:", self.remain_life, "Power of atack:", self.power_of_atack, "Number of bullet:", \
            self.number_of_bullet )

Enemies = []
i = 0

while (i < 100):
    random_live = random.randrange(100, 200)
    random_attack_pow = random.randrange(10, 20)
    random_bullet = random.randrange(20, 30)
    new_enemy = Enemy("Enemy " + str(i+1), random_live, random_attack_pow, random_bullet)
    Enemies.append(new_enemy)

    i += 1

i = 0

while (i < 3):
    randomenemy1 = random.randrange(0, 10)
    randomenemy2 = random.randrange(0, 10)
    randomenemy3 = random.randrange(0, 10)

    return_value = Enemies[randomenemy1].attack()

    Enemies[randomenemy2].is_attacked(return_value[0], return_value[1])

    print("Round is finished")

    i += 1




   