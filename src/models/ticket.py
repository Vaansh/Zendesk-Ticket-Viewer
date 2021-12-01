import json


class Ticket:
    def __init__(self, ticket):
        self.id = ticket["id"]
        self.subject = ticket["subject"]
        self.status = ticket["status"]
        self.created_at = ticket["created_at"]
        self.description = ticket["description"]

        self.json_dictionary = {
            "id": ticket["id"],
            "subject": ticket["subject"],
            "status": ticket["status"],
            "created_at": ticket["created_at"],
        }

    def __str__(self, detailed_dict: bool = False) -> str:
        to_str = ""

        detailed_json_dictionary = self.json_dictionary

        if detailed_dict:
            detailed_json_dictionary["description"] = self._description

        for attr in self.json_dictionary:
            to_str += "{} : {}\n".format(str(attr), self.json_dictionary[attr])

        return to_str

    def ticket_as_json(self, detailed: bool = False) -> str:

        if not detailed:
            return json.dumps(self.json_dictionary)

        detailed_json_dictionary = self.json_dictionary
        detailed_json_dictionary["description"] = self._description
        return json.dumps(detailed_json_dictionary)
