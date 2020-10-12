def parse(numeral):
  translator = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C": 100,
    "D": 500,
    "M": 1000
    }
  vals = [translator[c] for c in numeral]
  total = 0
  for i in range(len(vals)-1):
    if vals[i]>=vals[i+1]:
      total+=vals[i]
    else:
      total-=vals[i]
  total += vals[-1]
  return total


# print(parse("XIV"))
