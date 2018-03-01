# if postalrates.csv is not found, this script will be called

# script should generate n number of letter-number-letter, then
# will go through all combinations (where not same code with itself)
# and will generate same rand limits for size for all three prority
# but three diff rand rate per gram (can have base and simply add percentage
# of rate for next higher tier)

from random import *
import csv

postal_codes = []
csv_entries = []

# generates all possible codes
for i in range(10):
    firstletter = chr(randint(65, 90))
    number = randint(0, 9)
    secondletter = chr(randint(65, 90))

    code = str(firstletter) + str(number) + str(secondletter)

    postal_codes.append(code)

with open('postalrate.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['From', 'To', 'max length', 'max height', 'max width', 'max weight', 'priority type', 'rate per g'])

    for i in range(len(postal_codes)):
        for j in range(len(postal_codes)):
            if j == i:
                continue

            max_length = str(randint(200, 220))
            max_height = str(randint(200, 220))
            max_width = str(randint(250, 300))
            max_weight = str(uniform(1, 2))

            entry0 = [str(postal_codes[i]), str(postal_codes[j]), max_length, max_height, max_width, max_weight, 'Regular']
            entry1 = [str(postal_codes[i]), str(postal_codes[j]), max_length, max_height, max_width, max_weight, 'Xpress']
            entry2 = [str(postal_codes[i]), str(postal_codes[j]), max_length, max_height, max_width, max_weight, 'Priority']

            rateperg = uniform(0.01, 0.05)

            for n, entry in enumerate([entry0, entry1, entry2]):
                entry.append(str(rateperg + 0.01 * n))
                spamwriter.writerow(entry)
