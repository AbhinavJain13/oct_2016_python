import random

def coin_toss(flips):
    heads, tails = 0, 0
    for num in range(1, flips + 1):
        random_num = round(random.random())
        if (random_num == 0):
            outcome = "head"
            heads += 1
        else:
            outcome = "tail"
            tails += 1
        print("Attempt #{}: Throwing a coin... It's a {}!... Got {} head(s) so far and {} tails(s) so far".format(num, outcome, heads, tails))

coin_toss(10)
