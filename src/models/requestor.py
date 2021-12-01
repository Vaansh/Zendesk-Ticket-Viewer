import requests

from numpy import inf
from models.ticket import Ticket
from typing import List, Union, Any


class Requestor:
    PAGINATION = 25

    def __init__(self, username: str, password: str, subdomain: str):
        self.username = username
        self.password = password
        self.subdomain = subdomain

    def request(self, ticket_id: int = -inf, page: int = 1, multiple_tickets: bool = False) -> Union[Ticket, List[Ticket]]:
        if not multiple_tickets:
            url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets/{str(ticket_id)}.json"
        else:
            url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json?per_page={self.PAGINATION}&page={page}"

        response = requests.get(url, auth=(self.username, self.password))

        if response.ok:
            return self.handle_return_data(response, ticket_id)
        else:
            return None

    def handle_return_data(self, response: Any, ticket_id: int = -inf) -> Union[Ticket, List[Ticket]]:
        ticket = response.json()["ticket"]

        if ticket_id == -inf:
            return
        else:
            return Ticket(ticket)
