from functools import reduce
from dataclasses import dataclass

def balls_in_bins(balls, bins):
    if bins == 0:
        yield []
    elif bins == 1:
        yield [balls]
    elif balls == 0:
        yield [0]*bins
    else:
        for i in range(balls + 1):
            for j in balls_in_bins(i, bins - 1):
                yield [balls - i] + j

def readfile(filename):
    ingredients = []
    with open(filename) as f:
        for raw_line in f:
            name, raw_props = raw_line.strip().split(":")
            raw_prop_list = raw_props.strip().split(", ")
            props = {}
            for raw_prop in raw_prop_list:
                (prop, val) = raw_prop.split(" ")
                props[prop] = int(val)
            ingredients.append(props)
    return ingredients

def p1_score_comb(comb, ingredients):
    total_vals = {}
    for i in range(len(comb)):
        num = comb[i]
        for key in ingredients[i]:
            if key == "calories":
                continue
            total_vals.setdefault(key, 0)
            total_vals[key] += ingredients[i][key] * num
    for key in total_vals:
        total_vals[key] = max(total_vals[key], 0)
    return reduce(lambda acc, x: acc * x, total_vals.values(), 1)

def p2_score_comb(comb, ingredients):
    total_vals = {}
    for i in range(len(comb)):
        num = comb[i]
        for key in ingredients[i]:
            total_vals.setdefault(key, 0)
            total_vals[key] += ingredients[i][key] * num
    for key in total_vals:
        total_vals[key] = max(total_vals[key], 0)
    if total_vals["calories"] != 500:
        return float("-inf")
    total_vals.pop("calories")
    return reduce(lambda acc, x: acc * x, total_vals.values(), 1)

def p1(tbsps, ingredients):
    score = float("-inf")
    for comb in balls_in_bins(tbsps, len(ingredients)):
        comb_score = p1_score_comb(comb, ingredients)
        score = max(score, comb_score)
    return score

def p2(tbsps, ingredients):
    score = float("-inf")
    for comb in balls_in_bins(tbsps, len(ingredients)):
        comb_score = p2_score_comb(comb, ingredients)
        score = max(score, comb_score)
    return score

if __name__ == "__main__":
    ingredients = readfile("input")
    print(p1(100, ingredients))
    print(p2(100, ingredients))
