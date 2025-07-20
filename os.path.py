import os
import platform
#print(dir(os))
print(os.path.sep)
path="/Users/nthombre/Study/python/Orelly/os.path.py"
print(os.path.basename(path))
path1="/Users/nthombre"
path2="Study"
print(os.path.join(path1,path2))
print(os.path.split(path))