from questions import Question

question_promts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow \n\n",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer==question.answer:
            score += 1
    print("You got a score of " + str(score) + "/ " + str(len(questions)))

run_test(questions)