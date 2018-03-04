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
        self.from_pc_valid('U4D')
        self.to_pc_valid('M4N')

    def from_pc_valid(self, from_pc):
        reader = csv.reader(open('postalrate.csv', 'r', newline=''), delimiter=',', quotechar='|')
        for i, row in enumerate(reader):
            if i == 0:
                print(row)
            elif row[0] == from_pc:
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

    def valid_size(self, length, width, height):
        row = self.sameto[0]
        if length <= row[2] and width <= row[3] and height <= row[4]:
            return True
        else:
            return False

    def get_postal_type(self):
        return self.type
