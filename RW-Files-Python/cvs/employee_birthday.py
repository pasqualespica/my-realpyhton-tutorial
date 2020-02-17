import csv
import os


print(f"My CWD {os.getcwd()}")


# Reading CSV Files With csv
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"There are {len(row)} columns ")
            print(f'Column names are {", ".join(row)}')
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

        line_count += 1

    print(f'Processed {line_count} lines.')

# Reading CSV Files Into a Dictionary With csv
with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(
            f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


# Writing CSV Files With csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# Writing CSV File From a Dictionary With csv
# Unlike DictReader, the fieldnames parameter is required when writing a dictionary. 
# This makes sense, when you think about it: without a list of fieldnames, 
# the DictWriter can’t know which keys to use to retrieve values 
# from your dictionaries. It also uses the keys in fieldnames 
# to write out the first row as column names
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith',
                     'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers',
                     'dept': 'IT', 'birth_month': 'March'})
