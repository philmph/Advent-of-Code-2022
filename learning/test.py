l = list(range(0, 100))

filtered = list(filter(
    lambda i: i <= 10,
    l
))

print(filtered)
