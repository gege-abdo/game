level1=" ........ is the core computer scince ,\
........ is a universal machine. We can program it to do essentially \
computation . ........ is given us away to tell the computer what steps \
to take . ........ is gives us away to tell the computer what steps to take .  "
level2="........ is a progam it runs programs on python , it interprets them ,\
executes the programs that we wrote in python language"
speace=["........"]
answer_level1=["programming","computer","program","python"]

def speace_in(levels,speace):
    for n in speace:
        if n in levels :
            return n
        return None
def right_answer(input_answer,answer_level1):
    count=0
    while count<4:
        if answer_level1[0+count] == input_answer:
            return input_answer
        else:
            return  "Error: please try again"
        count=count+1


def play_game(ml_string, speace):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = speace_in(word,speace)
        if replacement != None:
            user_input = raw_input("Type the answer: " + replacement + " ")
            is_right=right_answer(user_input,answer_level1)
            print is_right
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
user_input = raw_input("choose level is (easy-medium-hard):" )

def choose (level):
    if level=="easy":
        print level1
        print play_game(level1, speace)
    elif level=="medium":
        print level2
        print play_game(level2, speace)
    else:
        print raw_input("choose between three options (easy-medium-hard):  " )
choose (user_input)
