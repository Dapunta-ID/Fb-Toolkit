from fp.modul import *
from fp import program, action

udata = {}
menu = {
    'friends':[
        'Mass Confirm Friend Request '+ warn, 
        'Mass Delete Friend Request '+ warn, 
        'Mass Auto Add Friend From Suggestion '+ warn, 
        'Mass Auto Add Friend From Welcome Search Name '+ warn,
        'Mass Unfriends '
    ], 
    'groups':[
        'Mass Join Group From Search Name '+ warn, 
        'Mass Leave Groups '+ warn
    ], 
    'message':[
        'Mass Send Message ( text only )', 
        'Mass Send Message ( text & images )', 
        'Mass Send Message ( Like Sticker Only )', 
        'Mass Auto Delete Chat '+ warn,
        'Mass Auto Block Chat '+ warn,
    ], 
    'profile':[
        'Mass Delete Post In Timeline', 
    ]
}

def header():
    system('clear')
    print(f'''
 {m}╔═╗{p}┌┐   {m}╔╦╗{p}┌─┐┌─┐┬  ┬┌─┬┌┬┐
 {m}╠╣ {p}├┴┐───{m}║ {p}│ ││ ││  ├┴┐│ │ 
 {m}╚  {p}└─┘   {m}╩ {p}└─┘└─┘┴─┘┴ ┴┴ ┴ 
 {bgm}{p} FACEBOOK TOOLKIT BY ERRUCHA v1.0 {n}

 {p}Fb Name: {h}{udata['name']}
 {p}Fb UID : {h}{udata['id']}

 {p}List Menu
 {o}---------''')

def main():
    header()
    print(f' {m}1).{p} Friends Manager')
    print(f' {m}2).{p} Groups Manager')
    print(f' {m}3).{p} Chat Manager')
    print(f' {m}4).{p} Profile Manager')
    print(f' {m}0).{u} Logout')
    print()
    chsr = input(f'{p} Chose Number:{o} ')
    if '1' in chsr:
        header()
        num = 1
        for listm in menu['friends']:
            print(f' {m}{num}).{p} {listm}')
            num +=1
        print(f' {m}0).{u} Back To Main Menu')
        print()
        chx = input(f'{p} Chose Number:{o} ')
        if '1' in chx:
            action.massAFR()
        elif '2' in chx:
            action.massDFR()
        elif '3' in chx:
            action.massAFFS()
        elif '4' in chx:
            action.massAFFWS()
        elif '5' in chx:
            action.massUnfriends()
        elif '0' in chx:
            main()
    elif '2' in chsr:
        header()
        num = 1
        for listm in menu['groups']:
            print(f' {m}{num}).{p} {listm}')
            num +=1
        print(f' {m}0).{u} Back To Main Menu')
        print()
        chx = input(f'{p} Chose Number:{o} ')
        if '1' in chx:
            action.massJGFSN()
        elif '2' in chx:
            action.massLG()
        elif '0' in chx:
            main()
        else:
            print(m +' Pilih Yang Bener Anjing!!!')
            time.sleep(3)
    elif '3' in chsr:
        header()
        num = 1
        for listm in menu['message']:
            print(f' {m}{num}).{p} {listm}')
            num +=1
        print(f' {m}0).{u} Back To Main Menu')
        print()
        chx = input(f'{p} Chose Number:{o} ')
        if '1' in chx:
            action.massSMTOO()
        elif '2' in chx:
            action.massSMTIO()
        elif '3' in chx:
            action.massSMSOO()
        elif '4' in chx:
            action.massDLC()
        elif '5' in chx:
            action.massBLC()
        elif '0' in chx:
            main()
        else:
            print(m +' Pilih Yang Bener Anjing!!!')
            time.sleep(3)
    elif '4' in chsr:
        header()
        num = 1
        for listm in menu['profile']:
            print(f' {m}{num}).{p} {listm}')
            num +=1
        print(f' {m}0).{u} Back To Main Menu')
        print()
        chx = input(f'{p} Chose Number:{o} ')
        if '1' in chx:
            action.massDLP()
        elif '0' in chx:
            main()
        else:
            print(m +' Pilih Yang Bener Anjing!!!')
            time.sleep(3)
    elif '0' in chsr:
        system('rm user/.cookies')

    


if __name__ == '__main__':
    program.login()
    udata.update({'name':program.userData()[0], 'id':program.userData()[1]})
    main()
