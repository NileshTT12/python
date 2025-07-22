import platform
print(dir(platform))
print (f"This is the platform of my workstation {platform.system()}")
print(f"Version of Java in this MAc is {platform.java_ver()}")
print(help(platform.java_ver)) 
print(platform.python_version_tuple())
print(platform.uname())