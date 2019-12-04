# permainan tebak tebakan angka

import random

playerName = input('Selamat datang, silahkan ketikan nama kamu: ')
print()
secretNumber = random.randint(1, 20)
print(playerName + ', kita sudah memilih angka secara acak (1-20), batas menebak hanya 4 kali :)')
print()

for tebak in range(1, 5):
    print('ayo coba tebak!')
    playerNumber = int(input('masukan angka: '))
    if playerNumber > secretNumber:
        print('tebakan kamu terlalu tinggi')
        print()
    elif playerNumber < secretNumber:
        print('tebakan kamu terlalu rendah')
        print()
    else:
        break

if playerNumber == secretNumber:
    print()
    print('selamat ' + playerName + ' tebakan kamu benar')
else:
    print()
    print(playerName + ' kamu kurang beruntung')