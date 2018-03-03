# maybe have class parcel so that it can be imported into tests.py and tested
import argparse
import csv
import sys

parser = argparse.ArgumentParser(description='Do stuff.')
parser.add_argument('--from', dest='frm', help='Enter the first three variables of your local postal code')
parser.add_argument('--to', dest='to', help="Really? You don't know your fucking Postal Code?")
parser.add_argument('--length', dest='length', help='Enter the package length in cm <3')
parser.add_argument('--width', dest='width', help='Enter the package width in cm <3')
parser.add_argument('--height', dest='height', help='Enter the package height in cm <3')
parser.add_argument('--weight', dest='weight', help='Enter the package mass in kg')
parser.add_argument('--postal_type', default='Regular', dest='postal_type', help='Add postal type [Regular, Xpress, Priority]')

args = parser.parse_args()

if len(sys.argv) <= 1:
    print("no arguments")
    exit()

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

parcel = Parcel(args.frm, args.to, args.length, args.width, args.height, args.weight, args.postal_type)
