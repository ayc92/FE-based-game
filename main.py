import config

level = config.Level()
level.load_file()
running = True
while running:
  gameGrid = level.render()
  print gameGrid
  x = raw_input("What is your move?\n")
  if x == 'x':
    running = False
  elif x == 'w':
    level.move(0, -1)
  elif x == 'a':
    level.move(-1, 0)
  elif x == 's':
    level.move(0, 1)
  elif x == 'd':
    level.move(1, 0)
