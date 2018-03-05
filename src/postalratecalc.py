# maybe have class parcel so that it can be imported into tests.py and tested
import argparse
import sys
import os

if not os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/../postalrate.csv'):
    import postalratecsvpop

from parcel import Parcel
from errors import Errors



parser = argparse.ArgumentParser(description='Parse the input tokens')
parser.add_argument('--from', dest='frm', help=' After typing "--from" enter the first three variables of a valid "From" postal code')
parser.add_argument('--to', dest='to', help='After typing "--to" enter the first three variables of a valid "To" postal code')
parser.add_argument('--length', dest='length', help='After typing "--length" enter the package length in cm 10 <= len <= 210')
parser.add_argument('--width', dest='width', help= 'After typing "--width" enter the package width in cm 7 <= w <= 275')
parser.add_argument('--height', dest='height', help='After typing "--height" enter the package height in cm 1 <= h <= 210')
parser.add_argument('--weight', dest='weight', help='After typing "--weight" enter the package weight in kg 0 < h <= 30')
parser.add_argument('--postal_type', default='Regular', dest='postal_type', help='Add postal type [Regular, Xpress, Priority]')

args = parser.parse_args()

try:
    Errors.no_args(len(sys.argv))
except Exception as error:
    print("No arguments entered! Please enter all 7 arguments in the format: --from A0A --to H1Y --length 20 --width 9 --height 100 --weight 10 --postal_type Regular")
    sys.exit()

try:
    Errors.missing_args(len(sys.argv))
except Exception as error:
    print("Please enter all 7 arguments in the format: --from A0A --to H1Y --length 20 --width 9 --height 100 --weight 10 --postal_type Regular ")
    sys.exit()

try:
    Errors.too_many_args(len(sys.argv))
except Exception as error:
    print("Too many arguments!Please enter all 7 arguments in the format: --from A0A --to H1Y --length 20 --width 9 --height 100 --weight 10 --postal_type Regular")
    sys.exit()

parcel = Parcel(args.frm, args.to, args.length, args.width, args.height, args.weight, args.postal_type)
# parcel = Parcel('V9B', 'H1Y', 50, 50, 50, 2, 'Regular')

total = parcel.verify()

if total < 0:
    sys.exit()

print('total: ' + str(total) + "$")
