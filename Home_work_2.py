{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb40ce61",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_types = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]\n",
    "for i in list_of_types:\n",
    "    print(type(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f7559f",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_to_change = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']\n",
    "new_list = []\n",
    "for item in list_to_change:\n",
    "    if item.isdigit():\n",
    "        new_list.extend(['\"', f'{int(item):02}','\"'])\n",
    "    elif item.startswith('+') and item[1:].isdigit():\n",
    "        new_list.extend(['\"', f'{item[0]}{int(item[1:]):02}', '\"'])\n",
    "    else:\n",
    "        new_list.append(item)\n",
    "        \n",
    "print(' '.join(new_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9765d4ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_prof = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']\n",
    "for name in list_prof:\n",
    "    print('Привет, ',name.split()[-1].title(), '!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f892417",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_prices = [43.33, 23.84, 5533.1, 234, 4467, 12.5, 5647.9, 345, 987.09, 1234, 5434, 668.56, 237, 122.8, 877, 9283, 754, 1762, 99.99]\n",
    "print(id(list_of_prices))\n",
    "list_of_prices.sort()\n",
    "print(id(list_of_prices))\n",
    "for price in list_of_prices:\n",
    "    rr = int(price)\n",
    "    kk = int(price * 100) % 100\n",
    "    print(f'{rr} рублей {kk:02.0f} копеек', end = ', ')\n",
    "print('--------------------------------------->>>>>>>>')\n",
    "\n",
    "new_list_of_prices = sorted(list_of_prices)[::-1][:5]\n",
    "for price in new_list_of_prices:\n",
    "    rr = int(price)\n",
    "    kk = int(price * 100) % 100\n",
    "    print(f'{rr} рублей {kk:02.0f} копеек', end = ', ')\n",
    "print('-------------------------->>> new id',id(new_list_of_prices))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
