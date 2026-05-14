from helloworld_print import helloworld

print_okak = input("Write your penis: ")
six_seven = helloworld(print_okak)

if six_seven == "67":
    for i in range(67):
        with open("67.txt", mode='a', encoding='utf-8') as file:
            file.write("\n" + print_okak + "\n")