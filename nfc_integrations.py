from src import nfc
import keyboard
from database import functions as func


# Initialize NFC tag


def read_uid():
    reader = nfc.Reader()
    number_list = reader.get_uid()
    hexadecimal_list = []
    for number in number_list:
        hexadecimal_list.append(hex(number)[2:])
    string = ''.join(hexadecimal_list)
    return int(string, 16)


def free_labor(class_list, year):
    dictionary = {}
    for item in class_list:
        print("Press 'a' To Scan \n")
        keyboard.wait("a")
        func.init_user_exact(item, '', '', '', read_uid(), year)
        dictionary[item] = read_uid()
        print(read_uid())
    return dictionary


def json_request_from_uuid(): 
    # sends json request for data which is returned with a 
    # subsequent link to open
    # e.g, 
    '''
    uuid = read_uuid() 
    packet = 
    {
    "uuid": uuid
    }
    json_response = requests.send(packet)
    # At this point it goes into a flask instance and turns into a web-page
    return json_request

    '''

    pass

print(free_labor(['Mark', 'James'], 7))

