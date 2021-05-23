import random
from operator import add, sub, mul

def addition(x, y) -> int:
    return x + y

def subtraction(x, y) -> int:
    return x - y

def multiplication(x, y) -> int:
    return x * y
    


def mathQuationaire(name):
    print(f'Hello, {name}. You will be completing a quiz that will ask you 10 questions which will test you on \n adding, subtracting and multiplying two numbers together. Try your best at each question and good luck!')



    count = 0
    score = 0
    while count <= 9:
        ops = (add, sub, mul)
        op = random.choice(ops)
        x = random.randint(1,1000)
        y = random.randint(1,1000)

        if op == add:
            addition(x, y)
            print("What is", x, "+",y, "? ")
            answer_add = addition(x, y)
            question_add = int(input())
            if question_add == answer_add:
                print("Well done, this is correct!")
                score = score + 1
                count = count + 1
            else:
               print("Sorry, but this is incorrect.")
               count = count + 1

        elif op == sub:
            print("What is", x, "-", y, "? ")
            answer_sub = subtraction(x, y)
            question_sub = int(input())
            if question_sub == answer_sub:
                print("Well done, this is correct!")
                score = score + 1
                count = count + 1
            else:
                print("Sorry, but this is incorrect.")
                count = count + 1

        elif op == mul:
            print("What is", x, "x", y, "? ")
            answer_mul = multiplication(x, y)
            question_mul = int(input())
            if question_mul == answer_mul:
                print("Well done, this is correct!")
                score = score + 1
                count = count + 1
            else:
                print("Sorry, but this is incorrect.")
                count = count + 1

        if count == 10:
            print("Well done "+name+"! You have completed the quiz. Your final score out of 10 is "+str(score)+".")


mathQuationaire("Bucky")
