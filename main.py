
while True:
  oddS = ["a","c","e","g"]
  evenS = ["b","d","f","h"]
  oddN = [1,3,5,7]
  evenN = [2,4,6,8]
  letter = input("Enter the letter: ")

  while True:
    try:
      number = int(input("Enter the number: "))
      break
    except ValueError:
      print("Number has to be an integer.")

  if letter.lower() in oddS and number in oddN:
    print("The square is white.")
  elif letter.lower() in evenS and number in oddN:
    print("The square is black.")
  elif letter.lower() in evenS and number in evenN:
    print("The square is black.")
  elif letter.lower() in oddS and number in evenN:
    print("The square is white.")
  else:
    print("Letter has to be single letter or from a to h")