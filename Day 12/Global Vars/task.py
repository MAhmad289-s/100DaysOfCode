enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# def is_prime(num):
#     if num<= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(5))

