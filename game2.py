level1=" ........ is the core computer scince ,\
........ is a universal machine. We can program it to do essentially \
computation . ........ is given us away to tell the computer what steps \
to take . ........ is a language for programming computer .   "

level2="........ is a progam it runs programs on python , it interprets them ,\
executes the programs that we wrote in python language. ........ was the lead designer\
of the fortran programming . ........ are nothing but reserved memory locations to store values.\
........ is a line containing at least one single equal sign (=) that is not inside parentheses "

level3="A ........ is everything that is delimited by quotation marks (" " or ' ').\
The ........ statement is used in Python for decision making.  \
........ are traditionally used when you have a block of code which you want \
to repeat a fixed number of times.  The ........ is a most versatile\
 datatype available in Python which can be written as a list of comma-separated values (items) between square brackets "
speace=["........"]
answer_level1=["programming","computer","program","python"]
answer_level2=["interpreter","john backus","variables","assignment statement"]
answer_level3=["string","if","for","list"]
'''speace_postion is a function it takes 2 inputs , it return speace postion'''
def speace_postion(levels,speace):
    for n in speace:
        if n in levels :
            return n
        return None
'''right_answer takes two inputs, second input is a list, the purpose of it is to
comparing the right answer with player answer'''
def right_answer(input_answer,answer_level):
    index=0
    for e in answer_level:
        if input_answer==e:
           input_answer=raw_input("Type the answer: ")
           index+=1
        else:
           return "Erorr: please try again"
        if index<len(e):
           break
'''play_game it takes 2 inputs.  A player is prompted to isnert the right answer '''

def play_game(string, speace):
    replaced = []
    string = string.split()
    for word in string:
        replacement =speace_postion(word,speace)
        if replacement != None:
            user_input = raw_input("Type the answer: " + replacement + " ")
            is_right=right_answer(user_input,answer_level)
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
user_input = raw_input("choose level is (easy-medium-hard):" )
'''choose takes 1 input , the purpose of it is to make the player to choose
level (easy-meduim-hard) '''

def choose (level):
    if level=="easy":
        print level1
        print play_game(level1, speace)
        return  right_answer(user_input,answer_level1)
    elif level=="medium":
        print level2
        print play_game(level2, speace)
        return right_answer(user_input,answer_level2)
    elif level=="hard":
        print level3
        print play_game(level3, speace)
        return right_answer(user_input,answer_level3)
    else:
        print raw_input("choose between three options (easy-medium-hard):  " )

choose (user_input)
