# Uncertain Fuzzy Logic

```py
def low(x):
    return max(0, min((20-x)/10, 1))

def medium(x):
    return max(0, min(x-20)/10, 1, (40-x)/10)

def high(x):
    return max(0, min((x-30)/10, 1))

def rule1(temperature):
    return low(temperature)

def rule2(temperature):
    return medium(temperature)

def rule3(temperature):
    return high(temperature)

def defuzzify(outputs):
    return sum(outputs) / len(outputs)

temperature=25

outputs= [rule1(temperature),rule2(temperature),rule3(temperature)]

output=defuzzify(outputs)

print("Output (Fuzzy Temperature Regulartion):",output)
```