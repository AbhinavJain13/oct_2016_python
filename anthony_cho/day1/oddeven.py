def odd_even():
    for num in range(1, 2000):
        if num % 2 == 0:
            evenodd = "even"
        else:
            evenodd = "odd"
        print("Number is {}. This is an {} number".format(num, evenodd))


odd_even()
