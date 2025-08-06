var = {}

while True:
    try:
        user = input().lower()
        if user in var:
            var[user] += 1
        else:
            var[user] = 1
    except EOFError:
        for key in sorted(var.keys()):
            print(var[key], key.upper())
        break

