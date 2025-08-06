expresion = input("Expresion: ")
x, y, z = expresion.split()
x = float(x)
z = float(z)

if y == "+":
    var = x+z
elif y == "-":
    var = x - z
elif y == "/":
    var = x / z
elif y == "*":
    var = x * z

print(var)



