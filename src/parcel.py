import csv
import re

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
        self.total = 0

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

    def pc_valid_form(self, pc):
        if re.match(r'[A-Z][0-9][A-Z]', pc):
            return True
        else:
            return False

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

    def get_postal_p_type(self):
        return self.p_type

    def length_is_not_too_low(self):
        row = self.sameto[0]
        if self.length >= int(row[3]):
            return True
        else:
            return False

    def length_is_not_too_high(self):
        row = self.sameto[0]
        if self.length <= int(row[4]):
            return True
        else:
            return False

    def height_is_not_too_low(self):
        row = self.sameto[0]
        if self.height >= int(row[5]):
            return True
        else:
            return False

    def height_is_not_too_high(self):
        row = self.sameto[0]
        if self.height <= int(row[6]):
            return True
        else:
            return False

    def width_is_not_too_low(self):
        row = self.sameto[0]
        if self.width >= int(row[7]):
            return True
        else:
            return False

    def width_is_not_too_high(self):
        row = self.sameto[0]
        if self.width <= int(row[8]):
            return True
        else:
            return False

    def is_weight_not_too_low_for_small(self):
        if self.weight >= 0:
            return True
        else:
            return False

    def is_weight_not_too_high_for_small(self):
        if self.weight <= 10:
            return True
        else:
            return False

    def is_weight_not_too_low_for_medium(self):
        if self.weight > 10:
            return True
        else:
            return False

    def is_weight_not_too_high_for_medium(self):
        if self.weight <= 20:
            return True
        else:
            return False

    def is_weight_not_too_low_for_large(self):
        if self.weight > 20:
            return True
        else:
            return False

    def is_weight_not_too_high_for_large(self):
        if self.weight <= 30:
            return True
        else:
            return False

    def verify(self):

        if self.pc_valid_form(self.from_pc) and self.pc_valid_form(self.to_pc):
            if not self.from_pc_valid():
                print("oops! your postal code has not been found")
                exit()
            if not self.to_pc_valid():
                print("destination postal code not found")
                exit()
        else:
            print("entered postal codes not valid")
            exit()

        # if not self.from_pc_valid():
        #     print("oops! your postal code has not been found")
        #     exit()
        # if not self.to_pc_valid():
        #     print("destination postal code not found")
        #     exit()

        if not (self.length_is_not_too_high() and self.length_is_not_too_low()):
            print("package does not fit length dimension")
            exit()

        if not (self.height_is_not_too_high() and self.height_is_not_too_low()):
            print("package does not fit height dimension")
            exit()

        if not (self.width_is_not_too_high() and self.width_is_not_too_low()):
            print("package does not fit width dimension")
            exit()

        if self.is_weight_not_too_high_for_small() and self.is_weight_not_too_low_for_small():
            self.total = float(self.weight) * float(self.sameto[0][11])
        elif self.is_weight_not_too_high_for_medium() and self.is_weight_not_too_low_for_medium():
            self.total = float(self.weight) * float(self.sameto[1][11])
        elif self.is_weight_not_too_high_for_large() and self.is_weight_not_too_low_for_large():
            self.total = float(self.weight) * float(self.sameto[2][11])
        else:
            print("weight exceeds limit")
            exit()

        if self.is_postal_type_valid():
            if self.p_type == 'Xpress':
                self.total += 4
            elif self.p_type == 'Priority':
                self.total += 20
        else:
            print("Not a valid postal type!")
            exit()

        return self.total
