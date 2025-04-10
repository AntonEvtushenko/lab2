from itertools import product
#Вариант 12
#Задание 1
letters = ['Ш', 'К', 'О', 'Л', 'А']
all_words = product(letters, repeat=3)
valid_words = [''.join(word) for word in all_words if word.count('К') == 1]
print("Ответ на задание 1:", len(valid_words))

#Задание 2
x=3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
print("Ответ на задание 2:",(hex(x).count('0')-1))

#Задание 3
print("Ответ на задание 3:")
a = 600000
count = 0
while count < 5:
    a+=1
    for i in range(17,a//2+1,10):
        if a%i==0:
            print(a, i)
            count+=1
            break