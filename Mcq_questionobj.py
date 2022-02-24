from Mcq_question import Question

question_prompt = [
    "who is the best footballer?\n(a)CR7\n(b)Messi\n(c)Lewandoski\n\n",
    "who is the best manager?\n(a)Guardiola\n(b)Klopp\n(c)Tuchel\n\n",
    "who is the best young talent?\n(a)Haaland\n(b)Vinicius\n(c)Mbappe\n\n",
    "who is the best striker?\n(a)Benzema\n(b)Salah\n(c)Vlahovic\n\n",
    "who is the best goalkeeper?\n(a)De gea\n(b)Mendy\n(c)Neur\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b"),
    Question(question_prompt[3], "b"),
    Question(question_prompt[4], "a")
]

def run_test(questions):
    final_score=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            final_score += 1
    print("You got " + str(final_score) + "/" + str(len(questions)) + " correct")

run_test(questions)


