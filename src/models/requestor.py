import requests

from numpy import inf
from models.ticket import Ticket
from typing import List, Union


class Requestor:
    PAGINATION = 25

    def __init__(self, username: str, password: str, subdomain: str):
        self.username = username
        self.password = password
        self.subdomain = subdomain

    def request(self, id: int = -inf, page: int = 1, multiple_tickets: bool = False) -> Union[Ticket, List[Ticket]]:
        if not multiple_tickets:
            url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets/{str(id)}.json"
        else:
            url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json?per_page={self.PAGINATION}&page={page}"

        response = requests.get(url, auth=(self.username, self.password))

        if response.ok:
            self.handle_return_data()
        else:
            return None

    def handle_return_data(id: int):
        if id == -inf:
            return
        else:
            return
