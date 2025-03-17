import json

class RWJson:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
        return self.data

    def write_json(self, key, value, index=""):

        try:
            new_list_of_dict = self.data["sessions"][index]
            new_list_of_dict[key] = value
        except:
            if value == "true":
                self.data[key] = True
            elif value == "false":
                self.data[key] = False
            else:
                self.data[key] = value
            print(self.data)

        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def delete(self, key, index):
        try:
            del self.data[key][index]
        except:
            del self.data[key]

        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

