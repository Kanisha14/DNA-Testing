import sys
import csv
import re

# len(sys.argv) expresses the number of arguments provided
if len(sys.argv) != 3:
    print("Usage: missing file")
    exit(1)

else:
    # "with / as" does the job for you to close the file once the orders given are finished
    with open(sys.argv[1], "r") as database:
        # .reader reads the file as a list
        data = csv.reader(database)

        with open(sys.argv[2], "r") as sequence:
            # .read reads the file as a string
            seq = sequence.read()

            # Iterates through the rows from the database and breaks (gets the first row only)
            for row in data:
                # row[1:] ignores the first item ('name') and leaves the STRs (AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG, etc...)
                STRs = row[1:]
                break

            # Creates temporal lists to compare later
            temp0 = []
            temp1 = []

            # Iterates through the STR names and checks maximum consecutive ocurrences in the DNA sequence
            for i in STRs:

                # Determines the length of the STR analyzed
                STR = len(i)

                # Finds all of the ocurrences: [ABC, ABC, ABCABCABC, ABC]
                substring = re.findall(f'(?:{i})+', seq)

                # Finds the longest substring [max(iterable, key)] and divides it by the STR length
                subMax = len(max(substring, key=len)) // STR

                # Appends value to temporal list
                temp0.append(str(subMax))

            # Ignores first line
            for row in data:
                del row
                break

            # Initialize a variable to check if there is a match or not
            match = 0

            # Iterates through the database
            for row in data:

                # Hosts the values from the row in a temporal list
                temp1 = row[1:]

                if temp0 == temp1:
                    print(row[0])
                    match += 1
                    break

            # If no match, print "No match."
            if match == 0:
                print("No match.")