setx={1,2,3,4,56,7,8,9,0}
sety={1,2,3,4,5,6,7,8,90}


setz=setx.intersection(sety)
print(setz)

setz=setx.union(sety)
print(setz)

setz=setx.difference(sety)
print(setz)

setz=setx.symmetric_difference(sety)
print(setz)
