import pandas as pd 
import random
from random import choice

meals = 7

def convert(stringIn):
    stringClean = stringIn[1:-1]
    li = list(stringClean.split(","))
    return li

def decide(data, number):
    choices = []
    data = data.values.tolist()
    i = 0
    while i <= number:
        newChoice = random.choice(data)
        if newChoice not in choices:
            choices.append(newChoice)
            i += 1
    return choices

def process_choice(choices):
    for choice in choices:
        choice[1] = convert(choice[1])
        choice[2] = convert(choice[2])
    return choices


def output(procesesd):
    items = []
    amounts = []
    for item in processed:
        print(item[0])
        for j, k in enumerate(item[1]):
            if item[1][j] not in items:
                items.append(item[1][j])
                try:
                    amounts.append(int(item[2][j]))
                except ValueError as e:
                    amounts.append(float(item[2][j]))
            else:
                i = items.index(item[1][j])
                try:
                    amounts[i] += int(item[2][j])
                except ValueError as e:
                    amounts[i] += float(item[2][j])
    for i in range(len(items)):
        print("{}: {}".format(items[i], amounts[i]))

data = pd.read_csv("recipe.csv")
choices = decide(data, meals)
processed = process_choice(choices)
output(processed)