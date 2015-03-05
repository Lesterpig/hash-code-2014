#!/usr/bin/python3
import sys,pprint

instru_n = input()
rows = int(sys.argv[1])
cols = int(sys.argv[2])

image = [[]]

for i in range(0,rows):
  if i != rows - 1:
    image.append([])
  for j in range(0,cols+1):
    image[i].append('.')


for x in range(0, int(instru_n)):
  cmd = input()
  cmd = cmd.split(' ')

  instruction = cmd[0]
  coord_x = int(cmd[1])
  coord_y = int(cmd[2])

  if instruction == "PAINTSQ":
    size = int(cmd[3])
    #print(size)
    for i in range(coord_x - size, coord_x + size + 1):
      for j in range(coord_y - size, coord_y + size + 1):
        #print("i -> "+ str(i) + " // j -> " + str(j))
        image[i][j] = "#"
        #pprint.pprint(image)
  else:
    image[coord_x][coord_y] = "."


for x in range(0, rows):
  print("")
  for y in range(0, cols):
    #print("x -> "+ str(x) + " // y -> " + str(y))
    sys.stdout.write(image[x][y])
