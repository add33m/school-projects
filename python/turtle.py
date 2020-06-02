import turtle as tur

scr = tur.Screen()

px = 0
py = 0

def moveBy(t, x, y):
  t.up()
  if x >= 0:
    t.left(90)
    t.forward(x)
    t.right(90)
  else:
    t.right(90)
    t.forward(-x)
    t.left(90)

  if y >= 0:
    t.forward(y)
  else:
    t.right(180)
    t.forward(-y)
    t.left(180)
    
  t.down()

tur.right(90) # reset orientation to look down
tur.shape("turtle") # change shape to an actual turtle

moveBy(tur, -100, -100)

print("Done!")
