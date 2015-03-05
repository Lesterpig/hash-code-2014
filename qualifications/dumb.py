# A dumb approach of the problem

# Reading dimensions

dimensions = input().split(" ");
rows       = int(dimensions[0]);
cols       = int(dimensions[1]);

# Reading image description

image = []
instructions = []

for r in range(rows):
  
  row = list(input())
  
  for c in range(cols):
    if row[c] == ".":
      row[c] = False
    else:
      row[c] = True
      instructions.append("PAINTSQ " + str(r) + " " + str(c) + " 0")

  image.append(row)


# Print solution

print(len(instructions))

for i in range(len(instructions)):
  print(instructions[i])