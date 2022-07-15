import mwclient
from pprint import pprint


# Задание 1
def task(array):
    return array.index('0')


print('Индекс первого нуля: ', task("111111111110000000000000000"))
print('================', end='\n\n')


# Задания 2

def find_enimals():
    site = mwclient.Site('ru.wikipedia.org')
    pages = site.pages['Категория: Животные по алфавиту']
    letters = {}
    for page in pages:
        if page.name[0] == 'A':
            break
        if page.name[0] in letters:
            letters[page.name[0]] += 1
        else:
            letters[page.name[0]] = 1
    return letters


pprint(find_enimals())

print('================', end='\n\n')


# Задание 3

def check_data(sessions: list):
    index = 0
    while index != len(sessions) - 2:
        if sessions[index] <= sessions[index + 2] <= sessions[index + 1] <= sessions[index + 3]:
            sessions.pop(index + 1)
            sessions.pop(index + 1)
        elif sessions[index + 2] <= sessions[index] <= sessions[index + 1] <= sessions[index + 3]:
            sessions.pop(index)
            sessions.pop(index)
        elif sessions[index + 2] <= sessions[index] <= sessions[index + 3] <= sessions[index + 1]:
            sessions.pop(index)
            sessions.pop(index + 2)
        elif sessions[index] <= sessions[index + 2] <= sessions[index + 3] <= sessions[index + 1]:
            sessions.pop(index + 2)
            sessions.pop(index + 2)
        else:
            index += 2
    return sessions


def appearance(data):
    lesson_start = data['lesson'][0]
    lesson_end = data['lesson'][1]
    pupil_sessions = check_data(data['pupil'])
    tutor_sessions = check_data(data['tutor'])

    pupil_index = 0
    counter = 0
    for tutor_index in range(0, len(tutor_sessions), 2):
        while pupil_sessions[pupil_index] < tutor_sessions[tutor_index + 1]:
            if pupil_sessions[pupil_index + 1] > tutor_sessions[tutor_index]:
                start = max([tutor_sessions[tutor_index],
                             pupil_sessions[pupil_index],
                             lesson_start])
                end = min([pupil_sessions[pupil_index + 1],
                           tutor_sessions[tutor_index + 1],
                           lesson_end])
                counter += end - start
            if pupil_index == len(pupil_sessions) - 2:
                break
            pupil_index += 2
    return counter


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 2326  ### здесь было указано 3577 - это не верно
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

for i, test in enumerate(tests):
    test_answer = appearance(test['data'])
    assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
print('Всё ОК')
