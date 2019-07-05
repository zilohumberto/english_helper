import random
from simple_practice.csv_read import CsvUploader

elements, row_fields = CsvUploader().process_csv('../sources/irregular_verbs_list.csv')

questions = {i: 'what is the '+row_fields[i]+' of {word}' for i in range(0, len(row_fields))}

keys = {i: row_fields[i] for i in range(0, len(row_fields))}
ok, not_ok = 0, 0
cases = 10

for i in range(0, cases):
    random_line = random.randint(0, len(elements)-1)
    random_question = random.randint(1, len(row_fields)-1)

    random_word = 0
    while random_word == random_question:
        random_word = random.randint(0, len(row_fields)-1)

    question = questions[random_question]
    word = elements[random_line][keys[random_word]]
    print(question.format(word=word.upper()), "...the tense is in '", keys[random_word].upper(), "'")

    answer = input('Enter your answer: ').lower()

    real_answer = elements[random_line][keys[random_question]].lower()
    if (
            answer == real_answer or
            real_answer.startswith(answer) or
            real_answer.endswith(answer)
    ):
        ok += 1
        print("perfect! You answer correctly")
    else:
        not_ok += 1
        print("ERROR NOT FOUND", elements[random_line][keys[random_question]])

print("{ok}/{sum} {per}% ".format(ok=ok, sum=(not_ok+ok), per=round(ok / (ok+not_ok), 4)*100))
