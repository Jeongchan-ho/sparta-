import random


class Character:
    def __init__(self, name, hp, mp, luck):
        self.name = name
        self.hp = hp * 5
        self.mp = mp * 5
        self.luck = luck

    def Character_info(self):
        return "name: {0}, hp: {1}, mp: {2}, luck: {3}".format(self.name, self.hp, self.mp, self.luck)

    def attack_style(self):
        roll_dice = dice(self)
        return roll_dice.roll()

    def attack_ada(self, m, damage=0):
        if isinstance(m, Monster):
            m.hp = m.get_hp - damage
            if m.hp <= 0:
                m.hp = 0
                print("승리했다!")

    def attack_apa(self, m, player, damage=0):
        if isinstance(m, Monster):
            damage *= 2
            if player.mp >= 10:
                player.mp -= 10
                m.get_hp -= damage
            if m.hp == 0:
                print('승리했다!')

    def Character_status(self):
        print(f"{self.name} hp:{self.hp} mp:{self.mp} luck:{self.luck}")


class Monster:
    def __init__(self, name, hp, mp, luck):
        self.name = name
        self.hp = hp * 5
        self.mp = mp * 5
        self.luck = luck

    def Monster_attack_style(self, ada, apa):
        roll_dice = dice()
        roll = roll_dice.roll

        if roll >= 4:
            apa(roll)
        elif roll >= 3:
            ada(roll)
        else:
            ada(roll)

    def Monster_attack_ada(self, damage):
        damage = dice.roll
        c.hp = c.hp - damage
        print(f"{self.name}의 공격! {damage}의 데미지를 주었습니다!!")
        if c.hp == 0:
            print()

    def Monster_attack_apa(self, damage, result):
        damage = dice.roll * 2
        self.mp = self.mp - 10
        if self.mp >= 10:
            c.hp = c.hp - damage
        else:
            print('mp가 부족합니다')
            self.Monster_attack_ada(result)

        print(f"{self.name}의 마법공격! {damage}의 데미지를 주었습니다!!")
        if c.hp == 0:
            print('모험가를 처치했다!')

    def Monster_status(self):
        print(f"{self.name} hp:{self.hp} mp:{self.mp}")

    def get_hp(self):
        return self.hp


class slime(Monster):
    def __init__(self, name, hp, mp, luck):
        super().__init__(name, hp, mp, luck)

    def Monster_status(self):
        print(f"{self.name} hp:{self.hp} mp:{self.mp} luck:{self.luck}")


class goblin(Monster):
    def __init__(self, name, hp, mp, luck):
        super().__init__(name, hp, mp, luck)

    def Monster_status(self):
        print(f"{self.name} hp:{self.hp} mp:{self.mp} luck:{self.luck}")


class zombie(Monster):
    def __init__(self, name, hp, mp, luck):
        super().__init__(name, hp, mp, luck)

    def Monster_status(self):
        print(f"{self.name} hp:{self.hp} mp:{self.mp} luck:{self.luck}")


c = Character
m = Monster


class dice:
    def __init__(self, Character):
        if Character.luck >= 15:
            self.roll_func = lambda: random.randrange(4, 6)
        elif Character.luck >= 10:
            self.roll_func = lambda: random.randrange(2, 5)
        else:
            self.roll_func = lambda: random.randrange(1, 4)

    def roll(self):
        return self.roll_func()

    def __str__(self):
        return str(self.roll_func())


print('이름을 정해주세요')
NAME = str(input(" "))


print('기초 스텟 포인틀 분배해주세요 포인트:1')
print(f"{NAME}:'hp: 5, mp: 5 luck: 14'")
Point = 1
hp = 5
mp = 5
luck = 14
while Point > 0:
    re = str(input(" "))
    if re == 'hp':
        hp += 1
        Point -= 1
        print(f"hp +1,Point:{Point}")
        print(f"hp:{hp}, mp{mp}, luck{luck}")
        continue
    elif re == 'mp':
        Point -= 1
        mp += 1
        print(f"mp +1,Point:{Point}")
        print(f"hp:{hp}, mp{mp}, luck{luck}")
        continue
    elif re == 'luck':
        Point -= 1
        luck += 1
        print(f"luck +1,Point:{Point}")
        print(f"hp:{hp}, mp{mp}, luck{luck}")
        continue
    elif re != 'hp' or 'mp' or 'luck':
        print('hp, mp, luck 중 하나를 입력해주세요')
    else:
        break

print(f"{NAME}님이 부여한 스텟은 hp:{hp} mp:{mp} luck:{luck} 입니다")

player = Character(NAME, hp, mp, luck)
print(c.Character_info(player))

print('전투를 진행할 몬스터의 정보를 확인해 주세요!')
while True:
    ans = int(input("1.slime 2.goblin 3.zombie 4.전투진행 "))
    if ans == 1:
        name = 'slime'
        hp = 5
        mp = 5
        luck = 5

        monster1 = slime(name, hp, mp, luck)
        monster1.Monster_status()

    elif ans == 2:
        name = 'goblin'
        hp = 7
        mp = 2
        luck = 15

        monster2 = goblin(name, hp, mp, luck)
        monster2.Monster_status()

    elif ans == 3:
        name = 'zombie'
        hp = 15
        mp = 1
        luck = 5

        monster3 = zombie(name, hp, mp, luck)
        monster3.Monster_status()

    elif ans == 4:
        break

    else:
        print('올바른 번호를 입력하세요')

print('전투 할 몬스터를 선택해 주세요')
choice = int(input("1.slime  2.goblin  3.zombie  "))
if choice == 1:
    print('전투 시작합니다')
    print(f"{c.Character_info(player)}")

    name = 'slime'
    hp = 5
    mp = 5
    luck = 5

    monster1 = slime(name, hp, mp, luck)
    monster1.Monster_status()

    print('공격 타입을 정하기 위해 주사위를 굴립니다')

    style_result = player.attack_style()
    print(f"주사위의 값은 {style_result} 입니다!")
    player = Character(NAME, hp, mp, luck)
    att_cho = int(input("1.물리공격  2.마법공격  "))
    if att_cho == 1:
        damage = style_result
        c.attack_ada(monster1, player, int(damage))
        print(f"{player.name}은 {damage}의 데미지를 주었습니다!!")
    elif att_cho == 2:
        if style_result < 4:
            print('마법공격은 주사위의 값이 4 이상 일 때 가능합니다.')
        elif player.mp < 10:
            print('mp가 부족합니다!')
        else:
            damage = style_result
            c.attack_apa(monster1, player, int(damage))
            print(f"{player.name}의 마법공격! {damage}의 데미지를 주었습니다!!")
    else:
        print('1, 2 중에 골라주세요')
    print(c.Character_status(player))
