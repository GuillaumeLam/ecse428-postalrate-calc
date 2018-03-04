import csv


class Parcel:

    def __init__(self, from_pc, to_pc, length, height, width, weight, p_type):
        self.from_pc = from_pc
        self.to_pc = to_pc
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.p_type = p_type
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

    def to_pc_valid(self):
        for row in self.samefrom:
            if row[1] == self.to_pc:
                self.sameto.append(row)
                continue
        # for row in self.sameto:
        #     print(row)
        # print(len(self.sameto))
        if len(self.sameto) == 0:
            return False
        else:
            return True

    def is_postal_type_valid(self):
        if (self.p_type == 'Regular') or (self.p_type == 'Xpress') or (self.p_type == 'Priority'):
            return True
        else:
            return False

    def length_is_not_too_low(self):
        row = self.sameto[0]
        if self.length >= row[2]:
            return True
        else:
            return False

    def length_is_not_too_high(self):
        row = self.sameto[0]
        if self.length <= row[3]:
            return True
        else:
            return False

    def height_is_not_too_low(self):
        row = self.sameto[0]
        if self.height >= row[4]:
            return True
        else:
            return False

    def height_is_not_too_high(self):
        row = self.sameto[0]
        if self.height <= row[5]:
            return True
        else:
            return False

    def width_is_not_too_low(self):
        row = self.sameto[0]
        if self.width >= row[6]:
            return True
        else:
            return False

    def width_is_not_too_high(self):
        row = self.sameto[0]
        if self.width <= row[7]:
            return True
        else:
            return False

    def get_postal_p_type(self):
        return self.p_type

    def is_weight_not_too_low_for_regular(self):
        if (self.weight >= 0) and self.p_type == 'Regular':
            return True
        else:
            return False

    def is_weight_not_too_high_for_regular(self):
        if (self.weight <= 10) and self.p_type == 'Regular':
            return True
        else:
            return False

    def is_weight_not_too_low_for_priority(self):
        if (self.weight >= 11) and self.p_type == 'Xpress':
            return True
        else:
            return False

    def is_weight_not_too_high_for_priority(self):
        if (self.weight <= 20) and self.p_type == 'Xpress':
            return True
        else:
            return False

    def is_weight_not_too_low_for_xpress(self):
        if (self.weight >= 21) and self.p_type == 'Priority':
            return True
        else:
            return False

    def is_weight_not_too_high_for_xpress(self):
        if (self.weight <= 30) and self.p_type == 'Priority':
            return True
        else:
            return False

    def verify(self):
        if not self.from_pc_valid():
            print("oops")
            exit()
        if not self.to_pc_valid():
            print("")
            exit()