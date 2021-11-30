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
        while selected_option != "3":
            self.render_menu()
            selected_option = input()

            if selected_option == "1":
                print(self.requestor.make_request())

            # if selected_option == "2":

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()
