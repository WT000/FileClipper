import os

class Renamer:
    def __init__(self):
        self.dir = os.curdir
        self.remove_amount = None
        self.file_types = None

    def format_amount(self, splitStr):
        if (len(splitStr) != 2):
            return False

        try:
            splitStr[0] = splitStr[0].lower()
            splitStr[1] = int(splitStr[1])

            if (splitStr[1] > 0):
                self.remove_amount = splitStr
                return True

        except(ValueError):
            pass

        return False

    def format_file_types(self, splitStr):
        if (len(splitStr) < 1):
            return False

        foundTypes = []

        for fileType in splitStr:
            if (fileType.startswith(".") and len(fileType) > 1):
                foundTypes.append(fileType)
            else:
                return False

        self.file_types = foundTypes
        return True

    def get_info(self):
        # Get an appropriate dir
        while True:
            dir = input("Enter the directory (leave blank if the exe is in the appropriate directory): ")

            if (dir != ""):
                # Check the dir exists
                if (not os.path.exists(dir)):
                    print("Path doesn't exist, ensure you remove any quotation marks.")

                else:
                    self.dir = dir
                    break

            else:
                break

        # Get an appropriate remove amount
        while True:
            remove_amount = input("Enter how many characters you want to remove (e.g. start 1, "
                                  "end 1 or both 1): ")

            if (remove_amount.startswith("start") or remove_amount.startswith("end") or remove_amount.startswith("both")):
                remove_amount = remove_amount.split(" ")

                if (self.format_amount(remove_amount)):
                    break

            print("Please enter an appropriate value.")

        # Get the file type(s)
        while True:
            file_type = input("Enter file type(s) to perform this operation on (e.g. .pdf), separate different file"
                              " types with a space: ")
            file_type = file_type.split(" ")

            if (self.format_file_types(file_type)):
                break

            print("Please enter appropriate file type(s).")

        return True

    def operate(self):
        files = os.listdir(self.dir)

        for file in files:
            for type in self.file_types:
                if (file.endswith(type)):
                    curr_file_name = os.path.splitext(file)[0]

                    # Note that the "both" option will remove by remove_amount[1] * 2
                    if (len(curr_file_name) > self.remove_amount[1] and self.remove_amount[0] != "both") \
                            or (len(curr_file_name) > self.remove_amount[1] * 2):

                        new_file_name = None
                        match self.remove_amount[0]:
                            case "start":
                                new_file_name = curr_file_name[self.remove_amount[1]:]

                            case "end":
                                new_file_name = curr_file_name[:len(curr_file_name)-self.remove_amount[1]]

                            case "both":
                                new_file_name = curr_file_name[self.remove_amount[1]:len(curr_file_name) - self.remove_amount[1]]

                        os.replace(file, new_file_name + type)

                        print("Renamed {} to {}".format(curr_file_name, new_file_name))

                    else:
                        print("Couldn't rename {}".format(curr_file_name))

                    break
