import random
import os.path
import os


def checker(ans, real_ans):
    bulls = 0
    cows = 0
    for i in range(0, len(ans)):
        if ans[i] == real_ans[i]:
            bulls += 1
        elif real_ans.find(ans[i]) != -1:
            cows += 1
    return str(cows) + str(bulls)


def check_answer(ans, real_ans):
    ans_pair = checker(ans, real_ans)
    print('You have {} cows and {} bulls'.format(ans_pair[0], ans_pair[1]))


def generate():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    res = str(a) + str(b) + str(c) + str(d)
    if len(set(res)) < len(res):
        res = generate()
    return res


def game_man(name):
    real_ans = generate()
    print('I guess number for you. Try to find it \nWrite your variants and I will say how many cows and bulls are there\nIf you want to throw in the towel write [end]')
    ans = input()
    count_attemt = 0
    while real_ans != ans:
        if ans == 'end':
            break
        if len(ans) != 4 or len(set(ans)) < len(ans) or not ans.isdigit():
            print('Incorrect input, try again')
            ans = input()
            continue
        count_attemt += 1
        check_answer(ans, real_ans)
        ans = input()
    if ans == 'end':
        print('Your number was {}'.format(real_ans))
    else:
        print('You found it! Count of attemts is {}'.format(count_attemt))
        update_rating(name, count_attemt)


def generate_list():
    res_list = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    s = str(a) + str(b) + str(c) + str(d)
                    if len(set(s)) == len(s):
                        res_list.append(s)
    return res_list


def optimizator_counter(s, answers):
    dict_counter = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '10': 0, '11': 0, '12': 0, '13': 0, '20': 0, '21': 0, '22': 0, '30': 0, '31': 0, '40': 0}
    list_ans = list(answers)
    for a in list_ans:
        k = checker(s, a)
        dict_counter[k] += 1
    return max(dict_counter.values())


def question(res_list, answers):
    min_res = 5040
    new = '1234'
    for a in res_list:
        k = optimizator_counter(a, answers)
        if k < min_res:
            min_res = k
            new = a
    return new


def update_answers(question, ans, answers):
    up_answers = list(answers)
    for a in up_answers:
        if checker(question, a) != ans:
            answers.discard(a)


def game_computer():
    print('Make your number and answer the question in format [num_cows num_bulls] ')
    res_list = generate_list()
    answers = set(res_list)
    new = '1234'
    while len(answers) > 1:
        print(new)
        inp = ''
        flag = False
        while len(inp) != 3 or not inp[0].isdigit() or not inp[2].isdigit() or inp[1] != ' ':
            if flag:
                print('Incorrect input. Answer format is [num_cows num_bulls]. Try again')
            inp = input()
            flag = True
        cows = inp[0]
        bulls = inp[2]
        update_answers(new, cows + bulls, answers)
        new = question(res_list, answers)
    if len(answers) == 1:
        print('Your number is {}'.format(list(answers)[0]))
    else:
        print('You had a mistake')


def update_rating(name, score):
    if not os.path.isfile('./rating.txt'):
        file = open('rating.txt', 'w')
        file.close()
    file = open('rating.txt', 'a')
    file.write('{} {}\n'.format(name, score))
    file.close()


def sort_by_rating(s):
    return int(s.split()[1])


def output_rating():
    if not os.path.isfile('./rating.txt'):
        print('There are no position in the rating')
    else:
        file = open('rating.txt', 'r')
        l = [line.strip() for line in file]
        l.sort(key=sort_by_rating)
        print(' {3} {0: <{2}}{1}'.format('PLAYER', 'ATTEMTS', 24, 'PLACE'))
        place = 1
        for s in l:
            h = s.split()
            print('{2: ^7}{0: <24}{1: ^7}'.format(h[0], h[1], place))
            place += 1
        file.close()


def reset_rating():
    if os.path.isfile('./rating.txt'):
        os.remove('./rating.txt')


def main_game(name):
    print('Hello, {}! \nDo you want to make a number or guess mine? You can see or reset the rating too. Input format is [make/guess/rating/reset/end]'.format(name))
    inp = ''
    flag = False
    while inp != 'make' and inp != 'guess' and inp != 'end':
        if flag and inp != 'rating' and inp != 'reset':
            print('Incorrect input. Input format is [make/guess/rating/reset/end]. Try again')
        inp = input()
        if inp == 'rating':
            output_rating()
            print('Choose new function [make/guess/rating/reset/end]')
        if inp == 'reset':
            reset_rating()
            print('Choose new function [make/guess/rating/reset/end]')
        flag = True
    if inp == 'make':
        game_computer()
    elif inp == 'guess':
        game_man(name)
    else:
        print('Bye!')
        return
    print('Do you want to continue? [yes/no]')
    ans = input()
    if ans == 'yes':
        main_game(name)
        return
    print('Bye!')
    return


def input_name():
    print('Write your name:')
    name = input()
    main_game(name)


input_name()
