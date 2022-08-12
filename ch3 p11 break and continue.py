# to print numbers

for i in range(1,11):
     print(i)

# but if you want to stop at a certain value we use break
# let's say we have to stop at 4

for i in range(1,11):
    if i == 5:
        break
    print(i)





#to skip a certain value we use continue
#let's say we have to skip 6
for i in range(1,11):
    if i == 6:
        continue
    print(i)