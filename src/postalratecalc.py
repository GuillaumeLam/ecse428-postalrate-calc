# maybe have class parcel so that it can be imported into tests.py and tested
import argparse
import sys
from src.parcel import Parcel

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

parcel = Parcel(args.frm, args.to, args.length, args.width, args.height, args.weight, args.postal_type)

def is_to_postalcode_valid (postalcode):

        if postalcode == 'H1Y':
            result = True
        else:
            result = False
            print ("Incorrect postal code")

def is_postal_type_valid (postal_type):
    if (postal_type == 'Regular') or (postal_type == 'Xpress') or (postal_type == 'Priority'):
        return True