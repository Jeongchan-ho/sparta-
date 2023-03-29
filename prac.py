import random


class Character:
    def __init__(self, name, hp, mp, power, magic_power, luck):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic_power = magic_power
        self.luck = luck

# 게임 내 케릭터가 공유하는 스텟
# name
# he
# mp
# power
# magic_power
# attack
# magic_attack
# luck

    def dice(self):
        pass
    # dice 함수는 모든 액션에 사용됨
    # Character(player, monster)의 luck에 의해 출력되는 값의 범위를 다르게 함
    # ex)if self.luck >= 30:
    #       return random.randrange(4,7)
    #    elif self.luck >= 15:
    #       return radom.randrange(3,7)
    #    else:
    #       return radom.randrange(1,5)
    # 공격 타입(attack, magic_attack)을 강제함 4이상일 경우 magic_attack 사용가능
    # damage 주사위의 수+power 만큼 추가(다른 기능 생각 중)

    def nomal_attack(self, target):
        pass
    # damage는 주사위의 수 + power의 값
    # damage = self.dice() + self.power
    # targe.hp -= damage

    def magic_attack(self, target):
        pass
    # mp가 소모되어야 하기 때문에 if문 사용
    #   if self.mp >= 10:
    #       damage = self.dice() + self.magic_power
    #       self.mp -= 10
    #       target.hp -= damage
    #   else:
    #       print(f"{sekf.name}의 mp가 부족합니다")

    def attack_style(self, target):
        pass
    # self.dice의 값을 가져와 공격스타일에 조건을 줌
    # self.dice의 값이 4 이상이면 magic_attack와 nomal_attack 둘 다 사용가능
    # self.dice의 값이 3 이상이면 namal_attack만 사용가능
    # player의 경우에는 input값을 사용해야 하지만 monster는 자동적으로 선택하는 기능이 필요
    # 두 가지로 구현하여 각각 class에 넣어줘야 함 이건 예시
    # dice_vla = self.dice()

    # if dice_val >= 4:
    #   style_choice = input("공격 방법을 선택하세요! 일반공격: 1 | 마법 공격: 2")
    #   if style_choice == "1":
    #       self.nomal_attack(target)
    #   elif style_choice == "2":
    #       self.magic_attack(target)
    #   else:
    #       print('잘못된 선택입니다 일반공격: 1 | 마법공격: 2')
    # else:
    #   self.nomal_attack(target) < 4 미만일 때 자동적으로 nomal_attack

    def show_status(self):
        pass
    # 전투 시 이름, 남은 hp /총 hp, 남은 mp /총 mp를 보여줌
    # print(f"{self.name}  hp:{self.hp}/{self.max_hp} mp:{self.mp}/{self.max_mp}")

    # 기능 구현 (사용했던 코드 재활용/다듬어야 함)
    # 캐릭터 생성 및 스텟 찍는 코드
    # print('캐락터를 생성합니다')
    # character_name = str(input(" "))
    # print('캐릭터의 스텟을 설정합니다')
    # player = Character(character_name, 100, 100, 30, 30, 10) <=생성 시 이름 + 기초 포인트
    # print('hp:100  mp:100 nomal_power(pw):30  magic_power(mpw):30 luck:10  남은 포인트:20')
    # point = 20
    # while point > 0:
    #     new_status = str(input(" "))
    #     if new_status == 'hp':
    #         player.hp += 1
    #         point -= 1
    #         print(f"hp + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #         continue
    #     elif new_status == 'mp':
    #         player.mp += 1
    #         point -= 1
    #         print(f"mp + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     elif new_status == 'pw':
    #         player.nomal_power += 1
    #         point -= 1
    #         print(f"nomal_power + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     elif new_status == 'mpw':
    #         player.magic_power += 1
    #         point -= 1
    #         print(f"magic_power + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    # #     elif new_status == 'luck':
    #         player.luck += 1
    #         point -= 1
    #         print(f"luck + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     else:
    #         break
    # print(f"{character_name}님의 스테이터스는 hp:{hp}  mp:{mp} power:{power} magig_power:{magic_power}  luck:{luck} 입니다")
