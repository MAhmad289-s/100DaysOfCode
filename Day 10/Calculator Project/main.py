import art
print(art.logo)
def add (n1, n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def mul (n1, n2):
    return n1 * n2
def div (n1, n2):
    return n1 / n2
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
for symbol in operations:
    print(symbol)
operation = input("Pick an operation: ")
answer = operations[operation](n1, n2)
print(f"{n1}{operation}{n2} = {answer}")


