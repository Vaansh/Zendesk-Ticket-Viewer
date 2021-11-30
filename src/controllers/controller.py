import sys

import lib.helpers as helpers
from views.view import View
from models.requestor import Requestor


class Controller:
    def __init__(self):
        self.view = View()
        self.credentials = helpers.get_credentials(
            "credentials/credentials.json")
        self.requestor = Requestor(
            self.credentials["username"], self.credentials["password"], self.credentials["subdomain"])

    def start_application(self) -> None:
        self.render_header()

        selected_option = ""
        application_exit = False

        while selected_option != "3":
            self.render_menu()
            selected_option = input()

            if application_exit:
                self.exit_application()

            if selected_option == "1":
                self.render_ticket_submenu()
                selected_ticket_option = ""

                while selected_ticket_option != "3":
                    selected_ticket_option = input()

                    if selected_ticket_option == "1":
                        # TODO: user input for ticket
                        print(self.requestor.request())
                        return
                    elif selected_ticket_option == "2":
                        continue
                    elif selected_ticket_option == "3":
                        application_exit = True
                    else:
                        self.render_incorrect_input()

            elif selected_option == "2":
                # TODO: code to render multiple tickets + flip through pages
                self.render_tickets_submenu()
                selected_tickets_option = ""

                while selected_tickets_option != "4":
                    selected_tickets_option = input()

                    if selected_tickets_option == "1":
                        # TODO: user input for tickets [prev page]
                        print(self.requestor.request())
                        return
                    elif selected_tickets_option == "2":
                        # TODO: user input for tickets [next page]
                        return
                    elif selected_tickets_option == "3":
                        continue
                    elif selected_tickets_option == "4":
                        application_exit = True
                    else:
                        self.render_incorrect_input()

            else:
                self.render_incorrect_input()

        self.exit_application()

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()

    def render_ticket_submenu(self) -> None:
        self.view.render_ticket_submenu()

    def render_exit_screen(self) -> None:
        self.view.render_exit_screen()

    def render_incorrect_input(self) -> None:
        self.view.render_incorrect_input()

    def exit_application(self) -> None:
        self.render_exit_screen()
        sys.exit()
