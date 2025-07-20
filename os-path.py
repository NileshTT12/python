import os
pathway="/Users/nthombre/Study/python/test"
print(list(os.walk(pathway)))
print("@@@@@@@@@@@@@@@@@")
for a,b,c  in os.walk(pathway):
    if len(c) !=0:
        for each in c:
            print(each)
            print(os.path.join(a,each))