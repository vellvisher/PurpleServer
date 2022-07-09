#!/bin/python3

"""
This class shouldn't be used and mime_to_html.py should be used instead.
Hacky script written on the flight as a proof of concept, needs improvement.
"""
import email

f = open("morning_brew_220702_raw_message.html")
lines = f.readlines()

i = 0
lines_unbreak = []
for line in lines:
    if i >= len(lines):
        break
    curr_line = lines[i]
    if i == len(lines)-1:
        lines_unbreak.append(curr_line)
        break
    if len(curr_line) > 1 and curr_line[-2] == "=":
        joined_line = curr_line[:-2]
        j = i + 1
        while j < len(lines) - 1 and lines[j][-2] == "=":
            joined_line = joined_line + lines[j][:-2]
            j = j + 1
        if j < len(lines):
            joined_line = joined_line + lines[j]
        lines_unbreak.append(joined_line)
        i = j + 1
        continue
    lines_unbreak.append(curr_line)
    i = i + 1

for line in lines_unbreak:
    # replace quotes
    line = line.replace('3D"', '"')
    # figure out unicode scheme
    # line = line.replace('=E2"', '"')
    print(line)
