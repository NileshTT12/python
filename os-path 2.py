import os 
print(os.getcwd())
os.chdir("/Users/nthombre/Study/python/")
print(os.getcwd())
print(os.listdir())
#os.mkdir("Test")
print(os.listdir())
os.makedirs("Test2/Test3/Test4")
i=os.getcwd()
os.chdir(i)
print(os.chdir())