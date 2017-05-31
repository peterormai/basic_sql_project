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
    print("5: Add Markus Schaffarzyk to the Applicants and show his details")
    print("6: Update & Show the new phone number of Jemina Foreman")
    print("7: Delete Applicants with @mauriseu.net email adress ending" + "\n")


def query_menu(opened_con):
    running_app = True
    while running_app:
        print_query_menu()
        try:
            chosen_option = int(input("Choose an option: "))
            os.system('clear')
            valid_inputs = [1, 2, 3, 4, 5, 6, 7]
            if chosen_option in valid_inputs:
                options = {1: [queries.mentor_names()],
                           2: [queries.miskolc_mentor_nicknames()],
                           3: [queries.carol_name_and_phonenum()],
                           4: [queries.girl_from_adipiscingenimmi()],
                           5: [queries.add_new_applicant(), queries.show_new_applicant()],
                           6: [queries.update_phone_num(), queries.show_jemina_phone()],
                           7: [queries.del_mauriseu()]}
                for func in options[chosen_option]:
                    query_handler.query_result(opened_con, func)
            elif chosen_option == 0:
                running_app = False
            else:
                os.system('clear')
                print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7')
        except ValueError:
            os.system('clear')
            print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7')
