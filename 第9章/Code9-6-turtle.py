import turtle
import time
from my_package import my_tools

# print(my_tools.get_time())
#
pen = turtle.Turtle()
pen.speed(0)
# for i in range(100):
#     pen.forward(100 + i)
#     pen.left(61)

while True:
    time.sleep(1)
    times = my_tools.get_time()
    pen.clear()
    pen.write(times, font=("Arial", 20, 'normal'))
