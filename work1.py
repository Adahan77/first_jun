lang1 = 'Rust'
languages = ['Rust','go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if i==lang1:
        print('this languages is in list')
    else:
        pass

print('перебрать')
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    print(i)
    if i=='php':
        break

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a = 0
for i in languages:
    print((str(a)+i)) 
    a+=1
