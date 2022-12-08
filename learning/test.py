l = list(range(0, 100))
l2 = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]

filtered = list(filter(
    lambda i: i <= 10,
    l
))

print(filtered)

print(l2[6:].index(5))

dic = {
    "/": {
        "depth": 0,
        "filesize": 500
    },
    "//": {
        "depth": 1,
        "filesize": 500
    }
}

print(dic)

for i in dic.values():
    print(i)
    print(i["depth"])
