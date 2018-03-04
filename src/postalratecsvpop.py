# if postalrates.csv is not found, this script will be called

# script should generate n number of letter-number-letter, then
# will go through all combinations (where not same code with itself)
# and will generate same rand limits for size for all three prority
# but three diff rand rate per gram (can have base and simply add percentage
# of rate for next higher tier)

import csv

postal_codes = ['H1Y',          # Montreal
                'V9A',          # Victoria
                'M3C',          # Toronto
                'B3H',          # Halifax
                'S4P',          # Regina
                'T6X',          # Edmonton
                'A1B',          # StJohn's
                'C1A',          # Charlottetown
                'R2C',          # Winnipeg
                'E3B',          # Fredericton
                'Y0B',          # Whitehorse
                'X1A',          # Yellowknife
                'X0A']          # Iqaluit
csv_entries = []

# generates all possible codes
# for i in range(10):
#     firstletter = chr(randint(65, 90))
#     number = randint(0, 9)
#     secondletter = chr(randint(65, 90))
#
#     code = str(firstletter) + str(number) + str(secondletter)
#
#     postal_codes.append(code)

with open('../postalrate.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['From', 'To', 'priority type', 'min length', 'max length', 'min height', 'max height', 'min width',
                         'max width', 'min weight', 'max weight', 'rate per g'])

    for i in range(len(postal_codes)):
        if i == 0:
            continue

        frompc = str(postal_codes[i])
        topc = str(postal_codes[0])

        min_length = 10
        max_length = 210
        min_height = 1
        max_height = 210
        min_width = 7
        max_width = 275

        rs_rate = 1.619
        xs_rate = 1.149
        ps_rate = 0.964

        entries = []
        for x in range(0, 9):
            if x < 3:
                entries.append([frompc, topc, 'Regular'])
            elif 3 <= x < 6:
                entries.append([frompc, topc, 'Xpress'])
            else:
                entries.append([frompc, topc, 'Priority'])
        print(entries)

        for n, entry in enumerate(entries):
            entry.append(min_length)
            entry.append(max_length)
            entry.append(min_width)
            entry.append(max_width)
            entry.append(min_height)
            entry.append(max_height)
            if n % 3 == 0:
                entry.append(0)
                entry.append(10)
                entry.append(rs_rate)
            elif n % 3 == 1:
                entry.append(10)
                entry.append(20)
                entry.append(xs_rate)
            else:
                entry.append(20)
                entry.append(30)
                entry.append(ps_rate)


            spamwriter.writerow(entry)
