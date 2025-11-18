def split_before_each_uppercases(formula):
    pass # Replace the pass with your code
    start = 0
    end = 0
    split_formula = []
    if not formula:
      return split_formula
    else:
      for char in formula[1:]:
        if char.isupper():
          split_formula.append(formula[start:(end+1)])
          start = end + 1 
        end += 1
      split_formula.append(formula[start:(end+1)])
      return split_formula


def split_at_first_digit(formula):
    pass # Replace the pass with your code
    digit_location = 1
    for char in formula[1:]:
      if (char.isdigit()):
        break
      digit_location += 1

    if digit_location == len(formula):
      return formula, 1
    else:
      return formula[0:digit_location], int(formula[digit_location:])
