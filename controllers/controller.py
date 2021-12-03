import json
import sys
from typing import Any, List

import utils.helpers as helpers
from models.requestor import Requestor
from models.ticket import Ticket
from views.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.credentials = helpers.get_credentials("credentials.json")
        self.requestor = Requestor(
            self.credentials["username"], self.credentials["password"], self.credentials["subdomain"]
        )

    def start_application(self) -> None:
        self.view.render_header()

        selected_option = ""
        self.enter_credentials()

        while selected_option != "3":
            self.view.render_menu()
            selected_option = self.receive_input()

            if selected_option == "1":
                self.handle_tickets_request()
            elif selected_option == "2":
                self.handle_ticket_request()
            elif selected_option == "3":
                break
            else:
                self.view.render_incorrect_input()

        self.exit_application()

    def enter_credentials(self) -> None:
        helpers.render("Enter your username/email (format: example@example.com):")
        username = self.receive_input()

        helpers.render("Enter your password:")
        password = self.receive_input()

        helpers.render("Enter your subdomain:")
        subdomain = self.receive_input()

        credentials = {
            "username":username,
            "password":password,
            "subdomain":subdomain,
        }
        
        with open('credentials.json', 'w') as f:
            json.dump(credentials, f)

        self.credentials = helpers.get_credentials("credentials.json")
        self.requestor = Requestor(
            self.credentials["username"], self.credentials["password"], self.credentials["subdomain"]
        )

    def handle_ticket_request(self) -> None:
        selected_ticket_option = ""
        self.view.render_ticket_prompt_input()
        selected_ticket_option = self.receive_input()
        self.request(selected_ticket_option)
        self.handle_subticket_request()

    def handle_tickets_request(self) -> None:
        selected_tickets_option = ""
        page_number = 1
        page_count = self.request(count=True)

        self.request(multiple_tickets=True, page_number=page_number, page_count=page_count)

        while selected_tickets_option != "4":
            self.view.render_tickets_submenu()
            selected_tickets_option = self.receive_input()

            if selected_tickets_option == "1":
                page_number -= 1
                if page_number <= 0:
                    self.view.render_over_or_undershot_page()
                    page_number = 1
                self.request(multiple_tickets=True, page_number=page_number, page_count=page_count)
            elif selected_tickets_option == "2":
                page_number += 1
                if page_number > page_count:
                    self.view.render_over_or_undershot_page()
                    page_number = page_count
                self.request(multiple_tickets=True, page_number=page_number, page_count=page_count)
            elif selected_tickets_option == "3":
                break
            elif selected_tickets_option == "4":
                self.exit_application()
            else:
                self.view.render_incorrect_input()

    def handle_subticket_request(self) -> None:
        subticket_option = ""
        self.view.render_ticket_submenu()

        subticket_option = self.receive_input()
        if subticket_option == "1":
            self.handle_ticket_request()
        elif subticket_option == "2":
            return
        elif subticket_option == "3":
            self.exit_application()
        else:
            self.view.render_incorrect_input()

    def request(
        self,
        ticket_id: str = "",
        multiple_tickets: bool = False,
        page_number: int = None,
        page_count: int = None,
        count: bool = False,
    ) -> None:
        if count:
            return self.requestor.request(count=count)
        if not multiple_tickets:
            tickets = self.requestor.request(ticket_id)
        else:
            tickets = self.requestor.request(multiple_tickets=multiple_tickets, page=page_number)
        if tickets:
            if type(tickets) is str:
                self.handle_request_error(tickets)
            else:
                if ticket_id == "":
                    self.render_table(tickets, page=page_number, page_count=page_count)
                else:
                    self.render_table([tickets])
        else:
            self.view.render_incorrect_id()

    def handle_request_error(self, ticket: str) -> None:
        if ticket == "err_api_unavailable":
            self.view.render_error_api_unavailable()
        elif ticket == "err_bad_request":
            self.view.self.view.render_error_bad_request()
        else:
            self.render_unkown_error()

    def receive_input(self) -> Any:
        user_input = input()
        helpers.render("")
        return user_input

    def render_table(self, tickets: List[Ticket], page: int = None, page_count: int = None) -> None:
        self.view.render_table(tickets=tickets, page=page, page_count=page_count)

    def render_exit_screen(self) -> None:
        self.view.render_exit_screen()

    def exit_application(self) -> None:
        self.render_exit_screen()
        sys.exit()
