def get_answer(prompt, reply):
    answer = input(prompt)
    print(reply)
    return answer

answer1 = get_answer('What is your name?', 'Thanks!')
answer2 = get_answer('What is your age?', 'Thanks again!')
answer3 = get_answer('What is your hobby?', 'Thank you!')

print('Your answers were...')
print(answer1, answer2, answer3)
