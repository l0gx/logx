#!/usr/bin/python
import random
print("PRO TOOL      >BETA");
print("1-random number");
print("2-random name");
print("3-random country");
listc= int(input("chosse a number: "));
while listc < 1 or listc > 4 :
  listc= int(input("chosse a number: "));
if listc > 0 < 4:
  if listc == 1:
     min= int(input("chosse a minmum: "));
     max= int(input("chosse a maxmum: "));
     print (random.randint(min,max));
     print("the code is end thanks for trying");
     while listc < 1 or listc > 4 :
          listc= int(input("chosse a number: "));
  if listc == 2:
     names=["mohammed","ahmed","moustafa","omer","mosa","jack","locas","willim","tomas","netwan"];
     nm = random.randint(0,9);
     print(names[nm]);
     print("the code is end thanks for trying");
  if listc == 3:
     countey=["USA","UEA","UK","canada","iraq","jordan","germany","sudia arbaia","moroco","netherland"];
     nc = random.randint(0,9);
     print(countey[nc]);
     print("the code is end thanks for trying");