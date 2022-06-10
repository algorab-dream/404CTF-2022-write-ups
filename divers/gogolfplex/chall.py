print('Bienvenue sur le goGOLFplex, le plus grand parcours de golf de l\'univers!')
print('Il comporte 10^16 trous mais le meilleur score que quelqu\'un ait fait dans l\'histoire est 10^25')
print('Si tu arrives à battre ou égaliser ce score tu rentreras dans l\'histoire !')
print('En revanche on a décidé de te mettre un petit handicap, ne t\'inquiète pas, ce n\'est pas gênant ;)')


a = input('En combien de coups essayez-vous de faire le parcours?\n').strip()

try:

    if a[0] in '-+0':
        print('Opération interdite! Je ne vais pas me faire avoir comme ça! Je ne suis pas un débutant!')
        exit()

    nb = int(f'{a:<051}')
    print(f'vous réussissez à finir le parcours en {nb} coups')
    if nb <= 10**25:
        with open('flag.txt', 'r') as f:
            print(f.readline())
        exit()
except Exception as e:
    print('Vous avez tout cassé....')
    exit()

print('Perdu! Mais vous pouvez retenter votre chance!')