# Задача №3

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

def lesson_edges(arr, lesson_start, lesson_end):
    # редактируем списки учителя и ученика так, чтобы они всегда были внутри границ урока (или на его границах)
    for i in range(len(arr)):
        if arr[i] < lesson_start:
            arr[i] = lesson_start
        elif arr[i] > lesson_end:
            arr[i] = lesson_end
    return arr

def appearance(test):
    lesson_start = test['lesson'][0]
    lesson_end = test['lesson'][1]
    pupil = lesson_edges(test['pupil'], lesson_start, lesson_end)
    tutor = lesson_edges(test['tutor'], lesson_start, lesson_end)

    start = tutor[0]
    result = 0
    for i in range(0, len(tutor), 2):
        for j in range(0, len(pupil), 2):
            # нижняя граница нового интервала должно быть меньше верхней границы следующего проверяемого интервала ученика
            if start < pupil[j+1]:
                enter = max(tutor[i], pupil[j])
                exit = min(tutor[i+1], pupil[j+1])
                # если полученные значения дают интервал, никак не пересекающийся с интервалом учителя, то пропускаем его
                if (exit - enter) <= 0:
                    continue
                # задаем новую нижнюю границу следующего интервала, вычисляем и записываем в секундах проверенный интервал
                if (enter - start) > 0:
                    start = enter
                result += exit - start
                start = exit
    return result

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'







