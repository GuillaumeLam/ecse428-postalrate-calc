# maybe have class parcel so that it can be imported into tests.py and tested


import argparse

parser = argparse.ArgumentParser(description='Do stuff.')
parser.add_argument("--From", default ="A0A", help="Enter the first three variables of your local postal code")
parser.add_argument("--To", default="A0A", dest="To", help="Really? You don't know your fucking Postal Code?")
parser.add_argument("--Length",default="0",help="Enter the package length in cm <3")
parser.add_argument("--Width",  default="0",help="Enter the package width in cm <3")
parser.add_argument("--Height", default="0",help="Enter the package height in cm <3")
parser.add_argument("--Weight", default="0",help="Enter the package mass in kg")
parser.add_argument("--Postal Type",  default= "Regular", help="Add postal type [Regular, Xpress, Priority]")

args = parser.parse_args()
print(args.To)

