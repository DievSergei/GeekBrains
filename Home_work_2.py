list_of_types = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for i in list_of_types:
    print(type(i))
--------------------------------------------------

list_prof = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in list_prof:
    print('Привет, ',name.split()[-1].title(), '!')
  
---------------------------------------------------
list_to_change = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for item in list_to_change:
    if item.isdigit():
        new_list.extend(['"', f'{int(item):02}','"'])
    elif item.startswith('+') and item[1:].isdigit():
        new_list.extend(['"', f'{item[0]}{int(item[1:]):02}', '"'])
    else:
        new_list.append(item)
        
print(' '.join(new_list))

------------------------------------------------------

list_of_prices = [43.33, 23.84, 5533.1, 234, 4467, 12.5, 5647.9, 345, 987.09, 1234, 5434, 668.56, 237, 122.8, 877, 9283, 754, 1762, 99.99]
print(id(list_of_prices))
list_of_prices.sort()
print(id(list_of_prices))
for price in list_of_prices:
    rr = int(price)
    kk = int(price * 100) % 100
    print(f'{rr} рублей {kk:02.0f} копеек', end = ', ')
print('--------------------------------------->>>>>>>>')

new_list_of_prices = sorted(list_of_prices)[::-1][:5]
for price in new_list_of_prices:
    rr = int(price)
    kk = int(price * 100) % 100
    print(f'{rr} рублей {kk:02.0f} копеек', end = ', ')
print('-------------------------->>> new id',id(new_list_of_prices))



