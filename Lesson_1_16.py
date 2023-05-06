''''
    CHORAK__CRAED = []

    chorak = {
        'id': 1,
        'pasword': 2008,
        'another': 'Kamoljon',
        'title': 'matematika',
        'mathematics': 5,
        'mother__tongue': 5,
        'history': 5,
        'total__score': 5,
        'descrption': 'Matematikadan chorakli bahoni bilish'
    }
    shunday data bo'ladi

    Menyuda

        ************************************
        *****     1) Mathematics       *****
        *****     2) Mother tangue     *****
        *****     3) History           *****
        *****     4) Total Score       *****       
        *****     5) EXIT              *****
        ************************************

        menyuda shular bo'ladi
'''

CHORAK__CRAED = []

chorak = {
    'id': 1,
    'pasword': 2008,
    'user__name': 'Kamoljon',
    'title': 'matematika',
    'mathematics': 5,
    'mother__tangue': 5,
    'history': 5,
    'descrption': 'Matematikadan chorakli bahoni bilish'
}

CHORAK__CRAED.append(chorak)

pasword__global = 0

def LOGIN():
    while True:
        print("*** LOGIN bo'limiga xush kelibsiz ***")

        pasword__global = int(input("Siz paswordingizni kiriting: "))

        if len(str(pasword__global)) == 4:
            break
        else:
            print("Siz kiritgan parol xato.")

    for i in CHORAK__CRAED:

        if i['pasword'] == pasword__global:
            MENU(i)
        else:
            continue

def MATHEMATICS(i):
    print("*** MATHEMATICS bo'limiga xush kelibsiz ***")

    print(f"Sizning matematika fanidan olgan chorak bahoyingiz {i['mathematics']}")
    MENU(i)

def MOTHER__TANGUE(i):
    print("*** MOTHER TANGUE bo'limiga xush kelibsiz ***")

    print(f"Sizning ona tili fanidan olgan chorak bahoyingiz {i['mother__tangue']}")
    MENU(i)

def HISTORY(i):
    print("*** HISTORY bo'limiga xush kelibsiz ***")

    print(f"Sizning tarix fanidan olgan chorak bahoyingiz {i['history']}")
    MENU(i)

def CONSOLE__PRINT(chorak__data):
    print(f"=======================================")
    print(f"===> mathematics: {chorak__data['mathematics'] }")
    print(f"===> mother__tangue: {chorak__data['mother__tangue']}")
    print(f"===> history: {chorak__data['history']}")
    print(f"=======================================\n")

def TOTAL__SCORE(i):
    print("*** TOTAL SCORE bo'limiga xush kelibsiz ***")

    k = (i['mathematics'] + i['mother__tangue'] + i['history']) / 3
    print(f"Sizning umumiy balingiz {k}")
    MENU(i)

def EXIT():
    print("*** EXIT bo'limiga xush kelibsiz ***")
    print("Chorak bahoyingizni bilib olgan bo'lsangiz biz xursandmiz.")
    print("O'qishlaringizga omad.")

def MENU(i):
    print("*** MENU bo'limiga xush kelibsiz ***")
    print("""
        ***********************************
        *****     1) Mathematics      *****
        *****     2) Mother tangue    *****
        *****     3) History          *****
        *****     4) Total Score      *****       
        *****     5) Exit             *****
        ***********************************
        """)

    input__menu__number = int(input("Menudan birini tanlang: "))

    if input__menu__number == 1: MATHEMATICS(i)
    elif input__menu__number == 2: MOTHER__TANGUE(i)
    elif input__menu__number == 3: HISTORY(i)
    elif input__menu__number == 4: TOTAL__SCORE(i)
    elif input__menu__number == 5: EXIT() 
    else: print("Menudagi sonlardan birini tanlang: ")

def MAIN():
    LOGIN()

MAIN()