"""
Jakiel David 
Task4

"""

import statistics
import turtle

ready_for_chart = True #change to True forchart

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# Descriptive:averages and measire of Central Tendency
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

#Descriptive: Measure of spread
var = statistics.variance(scores)
stdev = statistics.stdev(scores)

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

slope, intercept=statistics.linear_regression(x_times,y_temps)
future_x = 13
future_y = round(slope * 13 + intercept)

print()
print("Descriptive statistics include measures of central tendancy:")
print(f"   mean={mean:.2f}")
print(f"   median={median:.2f}")
print(f"   mode={mode:.2f}")
print()
print("Descriptive statistics include measures of spread:")
print(f"   var={var:.2f}")
print(f"   stddev={stdev:.2f}")
print()
print("=============================================================")
print()
print(f"Here's some UNIVARIANT data (1 variable, many readings): {scores}")
print()
print(f"x (hour of day):{x_times}")
print()
print(f"y (temperature):{y_temps}")
print()
print("Calculate the slope and intercept of a best fit straight line:")
print(f"   slope = {slope:.2f}")
print(f"   intercept = { intercept:.2f}")
print()
print("Let's use our best fit line to PREDICT a future value.")
print()
print(f"   In the {13:d}th hour, the temp. will be { future_y:d} degrees.")
print()
print("How'd we do? Does this make sense given the data?")
print()

if ready_for_chart:
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)

    w, h = screen.window_width(), screen.window_height()

    t.penup()
    t.goto(w / 1, 0)
    t.pendown()
    t.goto(-w / 1, 0)
    t.penup()
    t.goto(0, h / 1)
    t.pendown()
    t.goto(0, -h / 1)

    # draw points
    for index, year in enumerate(x_times):
        t.penup()
        t.goto(x_times[index], y_temps[index])
        t.pendown()
        t.pencolor("blue")
        t.dot(15)

    # draw best-fit line
    h = int(slope * w + intercept)
    t.penup()
    t.goto(w, h)
    w = -w
    h = int(slope * w + intercept)
    t.pencolor("orange")
    t.pensize(2)
    t.pendown()
    t.goto(w, h)

    # draw prediction dot
    t.penup()
    t.goto(future_x, future_y)
    t.pendown()
    t.pencolor("red")
    t.dot(20)

    turtle.done()
    screen.mainloop()
    print("Remember to close the app. CONTROL c will close it.")
    print()

else:
    print("Ready for a chart? Edit this program to see an illustration.")
    print()








