# -*- coding: utf-8 -*-
# Sinuskvadraticus

import math, sys

def sink_funcvalue(value):
    if value == 1:
        return "45 - 135 grader"
    if value == -1:
        return "225 - 315 grader"
    if value > 0:
        return math.atan(value) * (360/(2*math.pi))
    if value < 0:
        value = -value
        return math.atan(value) * (360/(2*math.pi))
    if value == 0:
        return "0 eller 180 grader"

def sink(mode_func, value):
    if mode_func == "funktionsvärde":
        return sink_funcvalue(value)

    if value < 45:
        value = ((2 * math.pi)/360)*value
        return math.tan(value)
    if value < 135:
        return 1
    if value == 180:
        return 0
    if value < 225:
        value = ((2 * math.pi)/360)*value
        return -math.tan(value)
    if value < 315:
        return -1

def cosk_funcvalue(value):
    if value == 1:
        return "< 45 grader"
    if value == -1:
        return "135 - 225 grader"
    if value > 0:
        return -(math.atan(value) * (360/(2*math.pi)) - 90)
    if value < 0:
        value = -value
        return -(math.atan(value) * (360/(2*math.pi)) - 270)
    if value == 0:
        return "90 eller 270 grader"

def cosk(mode_func, value):
    if mode_func == "funktionsvärde":
        return cosk_funcvalue(value)

    if value < 45:
        return 1
    if value < 135:
        value = ((2 * math.pi)/360)*value
        ninety = ((2 * math.pi)/360)*90
        return math.tan(ninety - value)
    if value < 225:
        return -1
    if value < 315:
        value = ((2 * math.pi)/360)*value
        twosevenzero = ((2 * math.pi)/360)*270
        return -math.tan(twosevenzero - value)

print("")

mode_func = input("undersöka funktionsvärde eller vinkel (grader)? ")

if mode_func != "funktionsvärde" and mode_func != "vinkel":
    sys.exit(1)

mode = input("sink eller cosk? ")

if mode != "sink" and mode != "cosk":
    sys.exit(1)

value = float(input("Vad önskar du undersökning av, {0}, för? ({1}):\n".format(mode_func, mode)))
ask = value #0.0

if value > 360 and mode_func == "vinkel":
    divideby = int(value/360)
    value -= divideby*360

if value >= 315 and mode_func == "vinkel":
    value -= 360

adjust = False

if value < 0 and mode_func == "vinkel":
    value = -value
    if mode == "sink":
        adjust = True

if mode_func == "funktionsvärde":
    if value > 1 or value < -1:
        print("Omöjligt")
        sys.exit(1)

if mode == "sink":
    value = sink(mode_func, value)
else:
    value = cosk(mode_func, value)

if adjust:
    value = -value

print("")
print("Svar {0}, {1}: {2}".format(mode, ask, value))
print("Reservation: tangens används för vissa intervall, men bara ett svar ges")