from game_models import Player


def check_answer(player: Player, answer):
    if player.questions:
        if player.questions[0]:
            if player.questions[0][0][1].lower() == answer.lower():
                player.questions[0].pop(0)
                player.opened_parts.append(player.hidden_parts[0].pop(0))
                if not player.hidden_parts[0]:
                    player.hidden_parts.pop(0)
                print("correct")

            else:
                print("incorrect")

            if not player.questions[0]:
                print("Susun kembali kalimat dari fragmen yang terkumpul")

        else:
            if player.hidden_words[0].lower() == answer.lower():
                player.opened_words.append(player.hidden_words.pop(0))
                player.questions.pop(0)
                player.opened_parts.clear()
                print("correct")

            else:
                print("incorrect")

        if player.questions[0]:
            print(player.opened_parts)
            print(player.questions[0][0][0])
            print(player.questions[0][0][1])
    else:
        print("The end")


p = Player(1, 1, 1)
print(p.questions[0][0][0])

while 1:
    check_answer(p, input())
