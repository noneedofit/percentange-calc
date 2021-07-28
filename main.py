## Max Marks of a subject check
from prettytable import PrettyTable
while True:
    try:
        print("")
        max = float(input("Every subject is of how many maximum marks? "))
    except ValueError:
        print("Please enter the number in numbers.")
        continue
    if max < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break
max = float(max*6)

## Subject 1
print("")
print("──────────────────────────────────────────")
print("")
subject1 = input("Name your first subject: ")
while True:
    try:
        subject1m = float(input("- Enter your marks for " + subject1 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject1m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject1ms = float(input("- Enter your enrichment activity marks for " + subject1 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject1ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject1msn = float(input("- Enter your notebook marks for " + subject1 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject1msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 2 ooff
print("")
print("──────────────────────────────────────────")
print("")
subject2 = input("Name your second subject: ")
while True:
    try:
        subject2m = float(input("- Enter your marks for " + subject2 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject2m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 2 ENRICHMENT

while True:
    try:
        subject2ms = float(input("- Enter your enrichment activity marks for " + subject2 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject2ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject2msn = float(input("- Enter your notebook marks for " + subject2 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject2msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## SUBJECT 3
print("")
print("──────────────────────────────────────────")
print("")
subject3 = input("Name your third subject: ")
while True:
    try:
        subject3m = float(input("- Enter your marks for " + subject3 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject3m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 3 ENRICHMENT

while True:
    try:
        subject3ms = float(input("- Enter your enrichment activity marks for " + subject3 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject3ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject3msn = float(input("- Enter your notebook marks for " + subject3 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject3msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 4
print("")
print("──────────────────────────────────────────")
print("")
subject4 = input("Name your fourth subject: ")
while True:
    try:
        subject4m = float(input("Enter your marks for " + subject4 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject4m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 4 ENRICHMENT

while True:
    try:
        subject4ms = float(input("- Enter your enrichment activity marks for " + subject4 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject4ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject4msn = float(input("- Enter your notebook marks for " + subject4 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject4msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subeject 5
print("")
print("──────────────────────────────────────────")
print("")
subject5 = input("Name your fifth subject: ")
while True:
    try:
        subject5m = float(input("Enter your marks for " + subject5 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject5m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 5 ENRICHMENT

while True:
    try:
        subject5ms = float(input("- Enter your enrichment activity marks for " + subject5 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject5ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject5msn = float(input("- Enter your notebook marks for " + subject5 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject5msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 6
print("")
print("──────────────────────────────────────────")
print("")
subject6 = input("Name your sixth subject: ")
while True:
    try:
        subject6m = float(input("Enter your marks for " + subject6 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject6m < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

## Subject 6 ENRICHMENT

while True:
    try:
        subject6ms = float(input("- Enter your enrichment activity marks for " + subject6 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject6ms < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        subject6msn = float(input("- Enter your notebook marks for " + subject6 + ": "))
    except ValueError:
        print("Please enter your marks in numbers.")
        continue
    if subject6msn < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break
print("")
print("──────────────────────────────────────────")
print("")
## Input Done

subjectallm1 = subject1m + subject1ms + subject1msn 
subjectallm2 = subject2m + subject2ms + subject2msn 
subjectallm3 = subject3m + subject3ms + subject3msn
subjectallm4 = subject4m + subject4ms + subject4msn
subjectallm5 = subject5m + subject5ms + subject5msn
subjectallm6 = subject6m + subject6ms + subject6msn

total = subjectallm1 + subjectallm2 + subjectallm3 + subjectallm4 + subjectallm5 + subjectallm6 
percentage = float(total) / float(max) * 100

t = PrettyTable(['Subject', 'Examination','Enrichment', 'Notebook', 'Total'])
t.add_row([subject1, subject1m, subject1ms, subject1msn, subjectallm1])
t.add_row([subject2, subject2m, subject2ms, subject2msn, subjectallm2])
t.add_row([subject3, subject3m, subject3ms, subject3msn, subjectallm3])
t.add_row([subject4, subject4m, subject4ms, subject4msn, subjectallm4])
t.add_row([subject5, subject5m, subject5ms, subject5msn, subjectallm5])
t.add_row([subject6, subject6m, subject6ms, subject6msn, subjectallm6])
print(t)
print("Your percentage is " + str(percentage) + "%")
