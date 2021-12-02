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

    def request(
        self, ticket_id: int = -inf, page: int = 1, multiple_tickets: bool = False, count: bool = False
    ) -> Union[List[Ticket], str, int, None]:
        if count:
            url = f"https://{self.domain}.zendesk.com/api/v2/tickets/count.json"
        else:
            if not multiple_tickets:
                url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets/{str(ticket_id)}.json"
            else:
                url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json?per_page={self.PAGINATION}&page={page}"

        response = requests.get(url, auth=(self.username, self.password), timeout=15)

        if response.ok:
            if count:
                counts = response.json()["count"]["value"] / self.PAGINATION
                if int(counts) == counts:
                    return int(counts)
                else:
                    return int(counts) + 1
            return self.handle_return_data(response, ticket_id)
        else:
            if count:
                return -1
            status = response.status_code
            if status >= 500:
                return "err_api_unavailable"
            elif status >= 400:
                return "err_bad_request"
            else:
                return None

    def handle_return_data(self, response: Any, ticket_id: int = -inf) -> Union[List[Ticket]]:
        ticket = response.json()["ticket"]

        if ticket_id == -inf:
            return
        else:
            return [Ticket(ticket)]

    def handle_errors(count: bool, response: Any) -> Union[str, int, None]:
        if count:
            return -1
        status = response.status_code
        if status >= 500:
            return "err_api_unavailable"
        elif status >= 400:
            return "err_bad_request"
        else:
            return None
