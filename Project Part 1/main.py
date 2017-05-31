import query_handler
import menu


def main():
    opened_con = query_handler.open_con()
    menu.query_menu(opened_con)


if __name__ == '__main__':
    main()
