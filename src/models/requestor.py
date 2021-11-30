import requests

from ticket import Ticket
from typing import List, Union


class Requestor:
    PAGINATION = 25

    def __init__(self, credentials: List[str]):
        self.username = credentials["username"]
        self.password = credentials["password"]
        self.subdomain = credentials["subdomain"]

    def make_request(id: int = -inf, page: int = 1, multiple_tickets: bool = False) -> Union[Ticket, List[Ticket]]:
        url = f"https://{self.domain}.zendesk.com/api/v2/tickets/{id}.json" if multiple_tickets else f"https://{self.domain}.zendesk.com/api/v2/tickets.json?per_page={self.PAGINATION}&page={page}"
        response = requests.get(url, auth=(self.username, self.password))

        try:
            response.raise_for_status()
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            raise

        if id == -inf:
            return
        else:
            return

    # def error_handler():
