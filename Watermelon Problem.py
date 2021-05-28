def watermelon_prob(noOfwatermelon):
    if noOfwatermelon%2 == 0 and noOfwatermelon != 2:
        print("Yes")
    else:
        print("No")

num = int(input())
watermelon_prob(num)
