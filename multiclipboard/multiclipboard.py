import sys
import clipboard
import json


SAVED_DATA = 'clipboard.json'


def save_items(filepath, data):
    with open('multiclipboard/' + filepath, 'w') as f:
        json.dump(data, f, indent=6)


def load_items(filepath):
    try:
        with open('multiclipboard/' + filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste
        save_items(SAVED_DATA, data)
        print("Data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied")
        else:
            print("Data not exist")
    elif command == "list":
        print(data)
    else:
        print("unknown command")
else:
    print("please pass exactly one command")
