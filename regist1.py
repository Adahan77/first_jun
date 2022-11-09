'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta'] 
print(menu)
'''

'''
a={}
c=0
while c<3:
    login=input('Введите имя:') 
    password=input('Введите пароль:')
    a[login]=password
    c+=1
    print(a)
    a.update()
'''

'''
a={'maks': 'pevec',
   'luis':'pilot',
   'dima':'povar',
   'victor':'bankir',
   'beka':'it'}
for k,v in a.items():
     print(f'Здравствуйте {k}  Прекрасная профессия {v}')

'''

menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
menu['besh_barmak']='130'
menu.update({'lagman':135})
menu.pop('borsh')
print(menu)
