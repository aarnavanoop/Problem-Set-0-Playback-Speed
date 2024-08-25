
def reduce_speed(saying):
    new_saying = saying.replace(" ", "...")
    print(new_saying)


def main():
    user_saying = input("What would you like to say? ")
    reduce_speed(user_saying)

main()