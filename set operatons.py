setx = {"green", "blue", }
sety = { "yellow" }
print("Original set elements:")
print(setx)
print(sety)
print("Intersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
print("Union of two said sets:")
setz1 = setx.union(sety)
print(setz1)

setz2 = setx.difference(sety)
print(setz2)

setz3 = sety = setx.difference(setx)
print(setz3)

setz4 = setx.difference(sety)
print(setz4)

setz5= sety.difference(setx)
print(setz5)