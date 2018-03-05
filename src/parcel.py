import csv
import re
import os


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
        self.sameto = []
        with open(os.path.dirname(os.path.realpath(__file__)) + '/../postalrate.csv', 'r', newline='') as file:
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
        self.sameto = []
        for row in self.samefrom:
            if row[1] == self.to_pc:
                self.sameto.append(row)
                continue
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
        if float(self.length) >= float(row[3]):
            return True
        else:
            return False

    def length_is_not_too_high(self):
        row = self.sameto[0]
        if float(self.length) <= float(row[4]):
            return True
        else:
            return False

    def height_is_not_too_low(self):
        row = self.sameto[0]
        if float(self.height) >= float(row[5]):
            return True
        else:
            return False

    def height_is_not_too_high(self):
        row = self.sameto[0]
        if float(self.height) <= float(row[6]):
            return True
        else:
            return False

    def width_is_not_too_low(self):
        row = self.sameto[0]
        if float(self.width) >= float(row[7]):
            return True
        else:
            return False

    def width_is_not_too_high(self):
        row = self.sameto[0]
        if float(self.width) <= float(row[8]):
            return True
        else:
            return False

    def is_weight_not_too_low_for_small(self):
        if float(self.weight) > 0:
            return True
        else:
            return False

    def is_weight_not_too_high_for_small(self):
        if float(self.weight) <= 10:
            return True
        else:
            return False

    def is_weight_not_too_low_for_medium(self):
        if float(self.weight) > 10:
            return True
        else:
            return False

    def is_weight_not_too_high_for_medium(self):
        if float(self.weight) <= 20:
            return True
        else:
            return False

    def is_weight_not_too_low_for_large(self):
        if float(self.weight) > 20:
            return True
        else:
            return False

    def is_weight_not_too_high_for_large(self):
        if float(self.weight) <= 30:
            return True
        else:
            return False

    def pc_valid_form(self, pc):
        if re.match(r'[A-Z][0-9][A-Z]', pc):
            return True
        else:
            return False

    def numeric_entries_valid_form(self, number):
        try:
            number = float(number)
            return True
        except Exception as error:
            return False

    def verify(self):
        if self.pc_valid_form(self.from_pc) and self.pc_valid_form(self.to_pc):
            if not self.from_pc_valid():
                print("oops! your postal code has not been found")
                return -1
            if not self.to_pc_valid():
                print("destination postal code not found")
                return -1
        else:
            print("entered postal codes not valid")
            return -1

        if self.numeric_entries_valid_form(self.length):
            if not (self.length_is_not_too_high() and self.length_is_not_too_low()):
                print("package does not fit length dimension")
                return -1
        else:
            print("entered length is not a numeric value")
            return -1

        if self.numeric_entries_valid_form(self.height):
            if not (self.height_is_not_too_high() and self.height_is_not_too_low()):
                print("package does not fit height dimension")
                return -1
        else:
            print("entered height is not a numeric value")
            return -1

        if self.numeric_entries_valid_form(self.width):
            if not (self.width_is_not_too_high() and self.width_is_not_too_low()):
                print("package does not fit width dimension")
                return -1
        else:
            print("entered width is not a numeric value")
            return -1

        if self.numeric_entries_valid_form(self.width):
            if self.is_weight_not_too_high_for_small() and self.is_weight_not_too_low_for_small():
                self.total = float(self.weight) * float(self.sameto[0][11])
            elif self.is_weight_not_too_high_for_medium() and self.is_weight_not_too_low_for_medium():
                self.total = float(self.weight) * float(self.sameto[1][11])
            elif self.is_weight_not_too_high_for_large() and self.is_weight_not_too_low_for_large():
                self.total = float(self.weight) * float(self.sameto[2][11])
            else:
                print("weight exceeds limit")
                return -1
        else:
            print("entered weight is not a numeric value")
            return -1

        if self.is_postal_type_valid():
            if self.p_type == 'Xpress':
                self.total += 4
            elif self.p_type == 'Priority':
                self.total += 20
        else:
            print("Not a valid postal type!")
            return -1

        self.total = round(self.total, 2)
        return self.total
