class Game:
  remainingCards = {}

  def Game():
    initCards()

  def initCards():
    colors = ["red", "yellow", "green", "blue"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actions = ["+2", "reverse", "skip"]
    wilds = ["+4", "wild"]

    for color in colors:
      for number in numbers:
        remainingCards[color + number] = 2
      remainingCards[color + 0] = 1
      
      for action in actions:
        remainingCards[color + action] = 2
      for wild in wilds:
        remainingCards[wild] = 4