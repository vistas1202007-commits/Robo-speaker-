import os 
print("welcomwe to robo speaker 2.0 created by shivani sharma")
while True :
 x = input("what you want to speak:")
 if x == "q":
  os.system("say bye bye friend")
  break
command =f"say{x}"
os.system=(command)
