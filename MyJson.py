import json

name = "Mark"
age = 30
m = True
d = False
k1 = "Ann"
k2 = "Billy"
p = None
m = "BMW 230"
mpg = 27.5
m2 = "Ford Edge"
mpg2 = 24.1


x = {
  "name": name,
  "age": age,
  "married": m,
  "divorced": d,
  "children": (k1, k2),
  "pets": p,
  "cars": [
    {"model": m, "mpg": mpg},
    {"model": m2, "mpg": mpg2}
  ]
}

# convert into JSON:
y = json.dumps(x, indent=2)

# the result is a JSON string:
print(y)

