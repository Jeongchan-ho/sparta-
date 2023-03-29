import random


class Character:
    def __init__(self, name, hp, mp, nomal_power, Magic_power):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.mp = mp
        self.mp = mp
        self.nomal_power = nomal_power
        self.magic_power = Magic_power

    def show_status(self):
        print(f"{self.name}의 정보: hp:{current_hp}")
        # 상태정보출력
        pass
# 마나 공격의 경우 current_mp -= 20, if문 사용 print 마나부족 return으로 돌아감

    def __init__(self, target):
        damage = random.randint(
            int(self.nomal_power*0.8, self.nomal_power*1.2))
        print(f"{self.name}의 물리공격!")
        target.current_hp = target.current_hp - 20

        if target.hp <= 0:
            print
        pass


print('캐락터를 생성합니다')
character_name = str(input(" "))

print('캐릭터의 스텟을 설정합니다')
player = Character(character_name, 100, 100, 30, 30)
print('hp:100  mp:100 nomal_power(pw):30  magic_power(mp):30  남은 포인트:20')
point = 20
while point > 0:
    new_status = str(input(" "))
    if new_status == 'hp':
        player.hp += 1
        point -= 1
        print(f"hp + 1  남은 point:{point}")
        print(f"""
        hp:{player.hp}  mp:{player.mp}  
        nomal_power:{player.nomal_power} magic_power:{player.magic_power}
        """)
        continue
    elif new_status == 'mp':
        player.mp += 1
        point -= 1
        print(f"mp + 1  남은 point:{point}")
        print(f"""
        hp:{player.hp}  mp:{player.mp}  
        nomal_power:{player.nomal_power} magic_power:{player.magic_power}
        """)
    elif new_status == 'pw':
        player.nomal_power += 1
        point -= 1
        print(f"nomal_power + 1  남은 point:{point}")
        print(f"""
        hp:{player.hp}  mp:{player.mp}  
        nomal_power:{player.nomal_power} magic_power:{player.magic_power}
        """)
    elif new_status == 'mp':
        player.magic_power += 1
        point -= 1
        print(f"magic_power + 1  남은 point:{point}")
        print(f"""
        hp:{player.hp}  mp:{player.mp}  
        nomal_power:{player.nomal_power} magic_power:{player.magic_power}
        """)
    else:
        break
print(f"{character_name}님의 스테이터스는 hp:{hp}  mp:{mp}  luck:{luck} 입니다")

player = Character(character_name, hp, mp, luck)
monster = Character('slime', 5, 5, 5)
