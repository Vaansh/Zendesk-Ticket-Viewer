import json


class Ticket:
    def __init__(self, ticket):
        self._id = ticket["id"]
        self._subject = ticket["subject"]
        self._status = ticket["status"]
        self._created_at = ticket["created_at"]
        self._description = ticket["description"]

        self._json_dictionary = {
            "id": ticket["id"],
            "subject": ticket["subject"],
            "status": ticket["status"],
            "created_at": ticket["created_at"],
        }

    def ticket_as_json(self, detailed: bool = False) -> str:

        if not detailed:
            return json.dumps(self.json_dictionary)

        detailed_json_dictionary = self.json_dictionary
        detailed_json_dictionary["description"] = self._description
        return json.dumps(detailed_json_dictionary)
