import csv
#from os import name

print("Welcome to Vital Records Indexer Version 1.0.0! If there are any issues with the program, please let me know." + "\n")

file = input("Input File Location: ")
with open(file, "a", newline="") as file:

    selection = input("Please input..." + "\n" + "\n"
    "...1 for the marriage CSV file editor." + "\n"
    "...2 for the death CSV file editor." + "\n"
    "...3 for the birth CSV file editor." + "\n"
    "...anything else to close the program." + "\n" + "\n" + ">>")

    if selection == "1":

        print('Welcome to the marriage CSV file editor! If any time you would like to exit the program, please type BREAK. If there is a category that you would like to skip, just press "Enter".' + "\n")

        selection = input("Please input..." + "\n" + "\n"
    "...1 for groom first editing." + "\n"
    "...2 for bride first editing." + "\n" + "\n" + ">>")

        if selection == "1":

            writer = csv.writer(file)
            selection = input("Please input..." + "\n" + "\n"
                    "...1 if you would like to add a heading" + "\n"
                    "...press enter if you would like to skip." + "\n" + "\n" + ">>")
            if selection == "1":
                writer.writerow(["Groom Name:", "Groom Birth Town:", "Bride Name:", "Bride Birth Town:", "Date:", "Groom Father:", "Groom Mother", "Bride Father:", "Bride Mother:", "Notes:"])

            while True == True:
                writer = csv.writer(file)
                row_details = []

                groom_surname = input("Enter groom's surname: ")
                if groom_surname == "BREAK":
                    break
                groom_first_name = input("Enter groom's first name: ")
                if groom_first_name == "BREAK":
                    break
                groom_name = groom_surname + ", " + groom_first_name
                row_details.append(groom_name)

                selection = input("Please input..." + "\n" + "\n"
                "...1 if the groom was born in a town different from the one that he married in." + "\n"
                "...press enter if he was born in the same town that he married in." + "\n" + "\n" + ">>")
                if selection == "1":
                    birth_town = input("Please enter the birth town of the groom: ")
                    row_details.append(birth_town)
                else:
                    row_details.append("Same as death town.")

                bride_surname = input("Enter the bride's surname: ")
                if bride_surname == "BREAK":
                    break
                bride_first_name = input("Enter the bride's first name: ")
                if bride_first_name == "BREAK":
                    break
                bride_name = bride_surname + ", " + bride_first_name
                row_details.append(bride_name)

                selection = input("Please input..." + "\n" + "\n"
                "...1 if the bride was born in a town different from the one that she married in." + "\n"
                "...press enter if she was born in the same town that she married in." + "\n" + "\n" + ">>")
                if selection == "1":
                    birth_town = input("Please enter the birth town of the groom: ")
                    row_details.append(birth_town)
                else:
                    row_details.append("Same as death town.")

                date = input("Enter the date of the marriage: ")
                if date == "BREAK":
                    break
                row_details.append(date)

                groom_father_first_name = input("Enter the groom's father's first name: ")
                if groom_father_first_name == "BREAK":
                    break
                groom_father_name = groom_surname + ", " + groom_father_first_name
                row_details.append(groom_father_name)

                groom_mother_surname = input("Enter the groom's mother's surname: ")
                if groom_mother_surname == "BREAK":
                    break
                groom_mother_first_name  = input("Enter the groom's mother's first name: ")
                if groom_mother_first_name == "BREAK":
                    break
                groom_mother_name = groom_mother_surname + ", " + groom_mother_first_name
                row_details.append(groom_mother_name)

                bride_father_first_name = input("Enter the bride's father's first name: ")
                if bride_father_first_name == "BREAK":
                    break
                bride_father_name = bride_surname + ", " + bride_father_first_name
                row_details.append(bride_father_name)

                bride_mother_surname = input("Enter the bride's mother's surname: ")
                if bride_mother_surname == "BREAK":
                    break
                bride_mother_first_name  = input("Enter the bride's mother's first name: ")
                if bride_mother_first_name == "BREAK":
                    break
                bride_mother_name = bride_mother_surname + ", " + bride_mother_first_name
                row_details.append(bride_mother_name)

                notes = input('Enter any additional notes if you would like to. If not, just press "Enter".')
                if notes == "":
                    writer.writerow(row_details)
                    continue
                elif notes == "BREAK":
                    break
                else:
                    row_details.append(notes)
                    writer.writerow(row_details)
                    continue
        
        elif selection == "2":

            writer = csv.writer(file)
            selection = input("Please input..." + "\n" + "\n"
                    "...1 if you would like to add a heading" + "\n"
                    "...press enter if you would like to skip." + "\n" + "\n" + ">>")
            if selection == "1":
                writer.writerow(["Bride Name:", "Bride Birth Town:", "Groom Name:", "Groom Birth Town", "Date:", "Bride Father:", "Bride Mother:", "Groom Father:", "Groom Mother", "Notes:"])

            while True == True:
                writer = csv.writer(file)
                row_details = []

                bride_surname = input("Enter the bride's surname: ")
                if bride_surname == "BREAK":
                    break
                bride_first_name = input("Enter the bride's first name: ")
                if bride_first_name == "BREAK":
                    break
                bride_name = bride_surname + ", " + bride_first_name
                row_details.append(bride_name)

                selection = input("Please input..." + "\n" + "\n"
                "...1 if the bride was born in a town different from the one that she married in." + "\n"
                "...press enter if she was born in the same town that she married in." + "\n" + "\n" + ">>")
                if selection == "1":
                    birth_town = input("Please enter the birth town of the groom: ")
                    row_details.append(birth_town)
                else:
                    row_details.append("Same as death town.")

                groom_surname = input("Enter groom's surname: ")
                if groom_surname == "BREAK":
                    break
                groom_first_name = input("Enter groom's first name: ")
                if groom_first_name == "BREAK":
                    break
                groom_name = groom_surname + ", " + groom_first_name
                row_details.append(groom_name)

                selection = input("Please input..." + "\n" + "\n"
                "...1 if the groom was born in a town different from the one that he married in." + "\n"
                "...press enter if he was born in the same town that he married in." + "\n" + "\n" + ">>")
                if selection == "1":
                    birth_town = input("Please enter the birth town of the groom: ")
                    row_details.append(birth_town)
                else:
                    row_details.append("Same as death town.")

                date = input("Enter the date of the marriage: ")
                if date == "BREAK":
                    break
                row_details.append(date)

                bride_father_first_name = input("Enter the bride's father's first name: ")
                if bride_father_first_name == "BREAK":
                    break
                bride_father_name = bride_surname + ", " + bride_father_first_name
                row_details.append(bride_father_name)

                bride_mother_surname = input("Enter the bride's mother's surname: ")
                if bride_mother_surname == "BREAK":
                    break
                bride_mother_first_name  = input("Enter the bride's mother's first name: ")
                if bride_mother_first_name == "BREAK":
                    break
                bride_mother_name = bride_mother_surname + ", " + bride_mother_first_name
                row_details.append(bride_mother_name)

                groom_father_first_name = input("Enter the groom's father's first name: ")
                if groom_father_first_name == "BREAK":
                    break
                groom_father_name = groom_surname + ", " + groom_father_first_name
                row_details.append(groom_father_name)

                groom_mother_surname = input("Enter the groom's mother's surname: ")
                if groom_mother_surname == "BREAK":
                    break
                groom_mother_first_name  = input("Enter the groom's mother's first name: ")
                if groom_mother_first_name == "BREAK":
                    break
                groom_mother_name = groom_mother_surname + ", " + groom_mother_first_name
                row_details.append(groom_mother_name)

                notes = input('Enter any additional notes if you would like to. If not, just press "Enter".' + "\n" + ">>" )
                if notes == "":
                    writer.writerow(row_details)
                    continue
                elif notes == "BREAK":
                    break
                else:
                    row_details.append(notes)
                    writer.writerow(row_details)
                    continue

    elif selection == "2":

        print('Welcome to the death CSV file editor! If any time you would like to exit the program, please type BREAK. If there is a category that you would like to skip, just press "ENTER".' + "\n")

        writer = csv.writer(file)
        selection = input("Please input..." + "\n" + "\n"
                "...1 if you would like to add a heading" + "\n"
                "...press enter if you would like to skip." + "\n" + "\n" + ">>")
        if selection == "1":
            writer.writerow(["Date:", "Name", "Age", "Spouse:", "Birth town", "Father:", "Mother:", "Notes:"])

        while True == True:
            writer = csv.writer(file)
            row_details = []

            date = input("Enter the date of the death: ")
            if date == "BREAK":
                break
            row_details.append(date)

            person_surname = input("Enter the person's surname: ")
            if person_surname == "BREAK":
                break
            person_first_name = input("Enter the person's first name: ")
            if person_first_name == "BREAK":
                break
            person_name = person_surname + ", " + person_first_name
            row_details.append(person_name)

            age = input("Enter the age of the person at their death: ")
            if age == "BREAK":
                break
            row_details.append(age)

            spouse_surname = input("Enter the spouse's surname: ")
            if spouse_surname == "BREAK":
                break
            spouse_first_name  = input("Enter the spouse's first name: ")
            if spouse_first_name == "BREAK":
                break
            spouse_name = spouse_surname + ", " + spouse_first_name
            row_details.append(spouse_name)

            selection = input("Please input..." + "\n" + "\n"
                "...1 if the person was born in a town different from the one that they died in." + "\n"
                "...press enter if they were born in the same town that they died in." + "\n" + "\n" + ">>")
            if selection == "1":
                birth_town = input("Please enter the birth town of the person.")
                row_details.append(birth_town)
            else:
                row_details.append("Same as death town.")

            person_father_first_name = input("Enter the person's father's first name: ")
            if person_father_first_name == "BREAK":
                break
            person_father_name = person_surname + ", " + person_father_first_name
            row_details.append(person_father_name)

            person_mother_surname = input("Enter the person's mother's surname: ")
            if person_mother_surname == "BREAK":
                break
            person_mother_first_name  = input("Enter the person's mother's first name: ")
            if person_mother_first_name == "BREAK":
                break
            person_mother_name = person_mother_surname + ", " + person_mother_first_name
            row_details.append(person_mother_name)

            notes = input('Enter any additional notes if you would like to. If not, just press "Enter".' + "\n" + ">>")
            if notes == "":
                writer.writerow(row_details)
                continue
            elif notes == "BREAK":
                break
            else:
                row_details.append(notes)
                writer.writerow(row_details)
                continue

    elif selection == "3":
        
        print('Welcome to the birth CSV file editor! If any time you would like to exit the program, please type BREAK. If there is a category that you would like to skip, just press "ENTER".' + "\n")

        writer = csv.writer(file)
        selection = input("Please input..." + "\n" + "\n"
                "...1 if you would like to add a heading" + "\n"
                "...press enter if you would like to skip." + "\n" + "\n" + ">>")
        if selection == "1":
            writer.writerow(["Date:", "Name", "Father:", "Mother:", "Notes:"])

        while True == True:
            writer = csv.writer(file)
            row_details = []

            date = input("Enter the date of the birth: ")
            if date == "BREAK":
                break
            row_details.append(date)

            person_surname = input("Enter the person's surname: ")
            if person_surname == "BREAK":
                break
            person_first_name = input("Enter the person's first name: ")
            if person_first_name == "BREAK":
                break
            person_name = person_surname + ", " + person_first_name
            row_details.append(person_name)

            person_father_first_name = input("Enter the person's father's first name: ")
            if person_father_first_name == "BREAK":
                break
            person_father_name = person_surname + ", " + person_father_first_name
            row_details.append(person_father_name)

            person_mother_surname = input("Enter the person's mother's surname: ")
            if person_mother_surname == "BREAK":
                break
            person_mother_first_name  = input("Enter the person's mother's first name: ")
            if person_mother_first_name == "BREAK":
                break
            person_mother_name = person_mother_surname + ", " + person_mother_first_name
            row_details.append(person_mother_name)

            notes = input('Enter any additional notes if you would like to. If not, just press "Enter".' + "\n" + ">>")
            if notes == "":
                writer.writerow(row_details)
                continue
            elif notes == "BREAK":
                break
            else:
                row_details.append(notes)
                writer.writerow(row_details)
                continue

    else:
        print("The program has closed.")
