import re

def arithmetic_arranger(expressions, solve=False):
  
  sum_sub = ""
  first_line = ""
  second_line = ""
  lines = ""
  res = "" 
  result_to_print = ""

  if len(expressions) > 5:
      return "Error: Too many problems."
    
  for expression in expressions:
    try:
        matches = re.match(r'(\d+)\s*([-+])\s*(\d+)$', expression)
                
        if matches is None:
            if '+' not in expression and '-' not in expression:
             return "Error: Operator must be '+' or '-'."
            else:
             return "Error: Numbers must only contain digits."
                
        number1 = matches.group(1)
        operator = matches.group(2)
        number2 = matches.group(3)

        # Check if numbers have more than four digits
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."
                
        if operator == "+":
            sum_sub = str(int(number1) + int(number2))
        elif operator == "-":
            sum_sub = str(int(number1) - int(number2))

        length = max(len(number1), len(number2)) + 2
        top = str(int(number1)).rjust(length) 
        bottom = operator + str(int(number2)).rjust(length - 1)
        line = "-" * length
        sum_sub = str(sum_sub).rjust(length)
    
        if expression != expressions[-1]:
            first_line += top + '    '
            second_line += bottom + '    '
            lines += line + '    '
            res += sum_sub + '    '
        else:
            first_line += top 
            second_line += bottom 
            lines += line 
            res += sum_sub

    except ValueError:
        return f"Error: {ValueError}"

  if solve:    
      result_to_print = first_line + "\n" + second_line + "\n" + lines + "\n" + res 
  else:
      result_to_print = first_line + "\n" + second_line + "\n" + lines 
    
  return result_to_print
