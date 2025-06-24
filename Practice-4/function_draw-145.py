def draw_line(ch="- ",size=20):
  for i in range(size):
    print(ch,end="")
  print()  # To move to the next line after drawing the line
draw_line()
draw_line(ch="* ", size=30)
draw_line(ch="= ", size=15)
draw_line(size=10, ch="# ")