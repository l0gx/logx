#!/usr/bin/python
import random
s = (" ");
print(70*s + "-----------------------");
print(70*s + "|  PRO TOOL" + 7*s + "      >BETA    |");
print(70*s + "----------------------- \n");
print("1-Random Number");
print("2-Random Name");
print("3-Random Country");
def numcho():
  listc= str(input("Choose a number: "));
  ctf = listc.isdigit();
  while ctf != True:
    listc= int(input("Choose a number: "));
    break
  while int(listc) < 1 or int(listc) > 4:
    listc= str(input("Choose a number: "));
  if int(listc) > 0 < 4:
    if int(listc) == 1:
       min= int(input("Choose the minimum number: "));
       max= int(input("Choose the maxmum number: "));
       print (random.randint(min,max));
    if int(listc) == 2:
       names=["mohammed","ahmed","moustafa","omer","mousa","jack","locas","willim","tomas","netwan"];
       nm = random.randint(0,9);
       print(names[nm]);
       print("the code is end thanks for trying");
    if int(listc) == 3:
       countey=["USA","UEA","UK","canada","iraq","jordan","germany","sudia arbaia","moroco","netherland"];
       nc = random.randint(0,9);
       print(countey[nc]);
       print("the code is end thanks for trying");
while True:
   numcho();
