print('''
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


way = input("which way you want to go? Left or Right " ).lower()
if way == "right":
  print("fall into a hole, game over")
elif way == "left":
  swim = input("Do you want to swim or wait? ")
  if swim == "swim":
    print("attacked by sherk, Game over ")
  elif swim == "wait":
      door = input("which door you want to go? red,blue or yellow " )
      if door == "red":
        print("burnt by fire, Game over")
      elif door == "blue":
          print("Eaten by beasts, Game over")
      elif door == "yellow":
          print("you win")
      else:
        print("game over")
  
else:
    print("game over")
  
