import csv


class Parcel:

    def __init__(self, from_pc, to_pc, length, width, height, weight, type):
        self.from_pc = from_pc
        self.to_pc = to_pc
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.type = type
        self.samefrom = []
        self.sameto = []

    def from_pc_valid(self):
        with open('../postalrate.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                    # print(row)
                elif row[0] == self.from_pc:
                    self.samefrom.append(row)

            """
            for row in self.samefrom:
                print(row)
            """

            if len(self.samefrom) == 0:
                return False
            else:
                return True

    def to_pc_valid(self, to_pc):
        for row in self.samefrom:
            if row[1] == to_pc:
                self.sameto.append(row)
                continue
        for row in self.sameto:
            print(row)
        if len(self.sameto) == 0:
            return False
        else:
            return True

    def length_is_not_too_low(self, length):
        row = self.sameto[0]
        if length >= row[2]:
            return True
        else:
            return False

    def length_is_not_too_high(self, length):
            row = self.sameto[0]
            if length <= row[3]:
                return True
            else:
                return False

    def height_is_not_too_low(self, height):
            row = self.sameto[0]
            if height >= row[4]:
                return True
            else:
                return False

    def height_is_not_too_high(self, height):
            row = self.sameto[0]
            if height <= row[5]:
                return True
            else:
                return False

    def width_is_not_too_low(self, width):
        row = self.sameto[0]
        if width >= row[6]:
            return True
        else:
            return False

    def width_is_not_too_high(self, width):
        row = self.sameto[0]
        if width <= row[7]:
            return True
        else:
            return False

    def get_postal_type(self, type):
        return self.type

    def is_postal_type_valid(self, type):
        if (type == 'Regular') or (type == 'Xpress') or (type == 'Priority'):
            return True
        else:
            return False

    def is_weight_not_too_low_for_regular(self, weight, type = 'Regular'):
        if (weight >= 0):
            return True
        else:
            return False

    def is_weight_not_too_high_for_regular(self, weight, type = 'Regular'):
        if (weight <= 10):
            return True
        else:
            return False

    def is_weight_not_too_low_for_priority(self, weight, type='Priority'):
        if (weight >= 11):
            return True
        else:
            return False

    def is_weight_not_too_high_for_priority(self, weight, type='Priority'):
        if (weight <= 20):
            return True
        else:
            return False
    def is_weight_not_too_low_for_xpress(self, weight, type='Xpress'):
        if (weight >= 21):
            return True
        else:
            return False

    def is_weight_not_too_high_for_xpress(self, weight, type='Xpress'):
        if (weight <= 30):
            return True
        else:
            return False

    

    def verify(self):
        if not self.from_pc_valid(self.from_pc):
            print("oops")
            exit()
        if not self.to_pc_valid(self.to_pc):
            print("")
            exit()