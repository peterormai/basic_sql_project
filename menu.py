import os
import query_handler
import queries


def print_query_menu():
    print("\n" + "Choose from the following options: " + "\n")
    print("0: Exit")
    print("1: Full name of all the mentors")
    print("2: Nick names of the mentors at Miskolc")
    print("3: Full name and phone number of Carol the applicant")
    print("4: Full name and phone number of Applicant from Adipiscingenimmi")
    print("5: Add Markus Schaffarzyk to the Applicants")
    print("6: Show details of Markus Schaffarzyk the Applicant")
    print("7: Update phone number of Jemina Foreman")
    print("8: Show phone number of Jemina Foreman")
    print("9: Delete Applicants with @mauriseu.net email adress ending" + "\n")


def query_menu(opened_con):
    running_app = True
    while running_app:
        print_query_menu()
        try:
            chosen_option = int(input("Choose an option: "))
            os.system('clear')
            valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if chosen_option in valid_inputs:
                options = {1: queries.mentor_names,
                           2: queries.miskolc_mentor_nicknames,
                           3: queries.carol_name_and_phonenum,
                           4: queries.girl_from_adipiscingenimmi,
                           5: queries.add_new_applicant,
                           6: queries.show_new_applicant,
                           7: queries.update_phone_num,
                           8: queries.show_jemina_phone,
                           9: queries.del_mauriseu}
                query_handler.query_result(opened_con, options[chosen_option]())
            elif chosen_option == 0:
                running_app = False
            else:
                os.system('clear')
                print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7,8,9')
        except ValueError:
            os.system('clear')
            print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7,8,9')
