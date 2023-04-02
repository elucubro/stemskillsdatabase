from src import nfc
import keyboard
# Initialize NFC tag


def read_uid():
    reader = nfc.Reader()
    number_list = reader.get_uid()
    hexadecimal_list = []
    for number in number_list:
        hexadecimal_list.append(hex(number)[2:])
    string = ''.join(hexadecimal_list)
    return int(string, 16)


def free_labor(class_list):
    dictionary = {}
    for item in class_list:
        print("Press 'a' To Scan \n")
        keyboard.wait("a")
        print("flag")
        dictionary[item] = read_uid()
        print(read_uid())
    return dictionary


print(read_uid())
print(free_labor(['Mark', 'James']))

