
    duration = int(input('Введите колличество секунд: '))  # запрос промежутка времени в секундах\n",
    m = duration // 60  # вычисляем минуты\n",
    h = m // 60  # часы\n",
    d = h // 24  # дни\n",
    print(f'{d} day {h % 24} h {m % 60} min {duration % 60} sec')  # выводим в консоль остаток от колличества секунд"
   

    cube_list = []\n",
    total = 0\n",
    for i in range(1, 1000, 2):\n",
        cube_list.append(i ** 3)\n",
    for ind, value in enumerate(cube_list):\n",
        summ_of_digits = 0\n",
        while value > 0:\n",
            summ_of_digits += value % 10\n",
            value //= 10\n",
            if summ_of_digits % 7 == 0:\n",
                total += cube_list[ind]\n",
    print(total)\n",
    i += 17\n",
    for ind, value in enumerate(cube_list):\n",
        summ_of_digits = 0\n",
        while value > 0:\n",
            summ_of_digits += value % 10\n",
            value //= 10\n",
            if summ_of_digits % 7 == 0:\n",
                total += cube_list[ind]\n",
    "print(total)"
 
    for number in range(1, 101):\n",
        if 4 < number % 100 <= 20:\n",
            print(f'{number} процентов')\n",
        elif number % 10 == 1:\n",
            print(f'{number} процент')\n",
        elif 1 < number % 10 < 5:\n",
            print(f'{number} процента')\n",
        else:\n",
            print(f'{number} процентов')"
   

