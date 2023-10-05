# All code should be Pep8 compliant (i hope)
from math import trunc

POSSIBLE_ANSWER = "abcd"
QUESTIONS_LIST = ["What variable names should never be used?"
                  "\na. A, S, d\nb. A, B, C\nc. I, O, l\nd. M, N, O",
                  "What case should be used for constant variables?"
                  "\na. camelCase\nb. SCREAMING_SNAKE_CASE\nc. PascalCase"
                  "\nd. kebab-case",
                  "What is the maximum line length recommended by PEP 8?"
                  "\na. 79\nb. 120\nc. 80\nd. 119",
                  "How can you check if your code follows PEP 8 guidelines?"
                  "\na. Linter\nb. Duster\nc. Fuzzer\nd. Fluffer",
                  "What does PEP stand for?"
                  "\na. Parsnip Eradication Platoon"
                  "\nb. Python's Energetic Prince"
                  "\nc. Phenomenal Elimination Penguins"
                  "\nd. Python Enhancement Protocol",
                  "How many blank lines should be used between functions?"
                  "\na. 0\nb. 1\nc. 2\nd. 86 million, 230 thousand, 708.",
                  "What case should be used for functions?"
                  "\na. camelCase\nb. snake_case\nc. PascalCase"
                  "\nd. kebab-case",
                  "What case should be used for classes?"
                  "\na. camelCase\nb. snake_case\nc. PascalCase"
                  "\nd. kebab-case",
                  ]
ANSWERS_LIST = ["c", "b", "a", "a", "d", "c", "b", "c"]
HINTS_LIST = ["They can be easily mistaken for numbers!",
              "Very loud.",
              "The answer is a prime number.",
              "Short, fine fibres which separate from the "
              "surface of cloth or yarn during processing.",
              "There's no way you need a hint for this LMAO",
              "The answer isn't d!",
              "🐍🐍🐍",
              "ILikeThisCaseALot!"
              ]


def quiz(question, answer, score, hint):
    player_input = ""
    while not player_input:
        player_input = input(f"{question}\n"
                             f"type h for a hint!\n").lower().strip("")
        if player_input == "h":
            print(hint)
        elif player_input == answer:
            print("♿ correct!!!! ♿")
            score += 1
            return score
        elif player_input in POSSIBLE_ANSWER and player_input != answer:
            print(f"wrong, it was {answer}")
            return score
        else:
            print("invalid input")
        player_input = ""


def main():
    print("pep 8 quiz!!!!! ♿♿♿")
    score = 0
    i_index = 0
    for i in QUESTIONS_LIST:
        i_index = QUESTIONS_LIST.index(i)
        question = i
        answer = ANSWERS_LIST[i_index]
        hint = HINTS_LIST[i_index]
        score = quiz(question, answer, score, hint)
    percentage = trunc((score/(i_index + 1)) * 100.0)
    print(f"you got through all the questions with a final score "
          f"of {score} out of {i_index + 1}!\nthat's {percentage}%!")


if __name__ == "__main__":
    main()
