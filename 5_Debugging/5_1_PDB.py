import pdb

def add_numbers(a, b):
    pdb.set_trace() # Set breakpoint, put n for next 
    result = a + b
    return result

add_numbers(2, 3)

# q --> quit the debugger.
# s --> step.
# r --> steps till gets to return.
# j --> jumps to specific line inside the current function.