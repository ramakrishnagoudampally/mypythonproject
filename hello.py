#!/usr/bin/python3
import sys
print(sys.version)
print(sys.executable)
x = 10
y = 12
print("exiting..using sys.exit")
#sys.exit()
if(x > y):
    print("x>y")
else:
    print("y=%d> x=%d"%(y,x))
    print(dir(sys))
    print("argv is:",sys.argv)


x=input("enter value of x:")
print("user has entered %s for x"%(x))
print(sys.getprofile())
