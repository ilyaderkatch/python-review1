import random
import os.path
import os
import pickle

number_list = list(range(10)) #комментарий

def num_correct_sequences(n):
    return 10**n


def checker(ans, real_ans):
    bulls = 0
    cows = 0
    for i in range(0, len(ans)):
        if ans[i] == real_ans[i]:
            bulls += 1
        elif ans[i] in real_ans:
            cows += 1
    return (str(cows), str(bulls))


def check_answer(ans, real_ans):
    ans_pair = checker(ans, real_ans)
    print('You have {} cows and {} bulls'.format(ans_pair[0], ans_pair[1]))


def generate(num_length):
    num_list = []
    while num_length != len(set(num_list)):
        num_list = random.choices(number_list, k=num_length)
    num_list = ''.join([str(i) for i in num_list])
    return num_list


def game_man(name):
    num_length = 0
    while num_length < 4 or num_length > 10:
        print('Write correct length of the number: [from 4 to 10]')
        num_length = int(input())
    real_ans = generate(num_length)
    print('I guess number for you')
    print('Try to find it \nWrite your variants and I will say how many cows and bulls are there')
    print('If you want to throw in the towel write [end]')
    ans = input()
    count_attempt = 0
    while real_ans != ans:
        if ans == 'end':
            break
        if len(ans) != num_length or len(set(ans)) < len(ans) or not ans.isdigit():
            print('Incorrect input, try again')
            ans = input()
            continue
        count_attempt += 1
        check_answer(ans, real_ans)
        ans = input()
    if ans == 'end':
        print('Your number was {}'.format(real_ans))
    else:
        print('You found it! Count of attemts is {}'.format(count_attempt))
        update_rating(name, count_attempt)


def generate_list(n):
    if n == 1:
        return number_list

    gen_list = generate_list(n - 1)
    new_list = []
    for i in gen_list:
        for a in range(0, 10):
            if len(set(str(i * 10 + a))) == len(str(i)) + 1:
                new_list.append(i * 10 + a)
    return new_list


def generate_dict_counter(n):
    dict_counter = {}
    for a in range(0, n + 1):
        b = 0
        while a + b <= n:
            dict_counter[str(a) + str(b)] = 0
            b += 1
    return dict_counter


def optimizator_counter(s, answers):
    dict_counter = generate_dict_counter(4)
    list_ans = list(answers)
    for a in list_ans:
        k = checker(s, str(a))
        dict_counter[k[0] + k[1]] += 1
    return max(dict_counter.values())


def clever_question(res_list, answers):
    min_res = num_correct_sequences(4)
    new = '1234'
    for a in res_list:
        k = optimizator_counter(str(a), answers)
        if k < min_res:
            min_res = k
            new = a
    return str(new)


def question(answers):
    return str(list(answers)[0])


def update_answers(question, ans, answers):
    up_answers = list(answers)
    for a in up_answers:
        if checker(question, str(a)) != ans:
            answers.discard(a)


def first_number_computer_game(n):
    return ''.join([str(i) for i in [x for x in range(0, n)]])


def game_computer():
    print('Make your number (quantity of digits from 4 to 10) and answer the question in format [num_cows num_bulls] ')
    print("Please, write quantity of digits")
    num_len = int(input())
    res_list = generate_list(num_len)
    answers = set(res_list)
    new = first_number_computer_game(num_len)
    while len(answers) > 1:
        print(new)
        ans = input()
        ans = ans.split(' ')
        update_answers(new, (ans[0], ans[1]), answers)
        if num_len == 4:
            new = clever_question(res_list, answers)
        elif len(answers) != 0:
            new = question(answers)
    if len(answers) == 1:
        print('Your number is {}'.format(list(answers)[0]))
    else:
        print('You had a mistake')


def update_rating(name, score):
    if not os.path.isfile('./rating.txt'):
        with open('rating.txt', 'wb') as file:
            a = [(name, score)]
            pickle.dump(a, file)
    else:
        with open('rating.txt', 'rb') as f:
            a = pickle.load(f)
            a.append((name, score))
        with open('rating.txt', 'wb') as f:
            pickle.dump(a, f)


def sort_by_rating(s):
    return s[1]


def output_rating():
    if not os.path.isfile('./rating.txt'):
        print('There are no positions in the rating')
    else:
        with open('rating.txt', 'br') as f:
            a = list(pickle.load(f))
            a.sort(key=sort_by_rating)
            print(' {3} {0: <{2}}{1}'.format('PLAYER', 'ATTEMTS', 24, 'PLACE'))
            place = 1
            for s in a:
                print('{2: ^7}{0: <24}{1: ^7}'.format(s[0], s[1], place))
                place += 1


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


def input_name():
    print('Write your name:')
    name = input()
    main_game(name)


if __name__ == '__main__':
    input_name()
