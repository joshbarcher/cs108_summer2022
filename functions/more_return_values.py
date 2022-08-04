def positiveOrNegative(num):
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    else:
        return "zero"

result = positiveOrNegative(0)
print(result)

