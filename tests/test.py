import sys
import unittest
from os.path import abspath, dirname

import requests

from mock.requestor import Requestor
from mock.ticket import Ticket


class TestTicket(unittest.TestCase):
    ticket = Ticket(
        {
        "id": 100, 
        "created_at" : "02/02/2022",
        "subject": "example",
        "description": "example", 
        "status": "closed"
        }
    )

    def test_ticket_value(self):
        ticket_string = repr(self.ticket.render_header(False))        
        self.assertEqual(ticket_string, repr("id: 100\nsubject: example\nstatus: closed\ncreated_at: 02/02/2022\n"))

class TestTicketDescription(unittest.TestCase):
    ticket = Ticket(
        {
        "id": 10, 
        "created_at" : "01/01/2021",
        "subject": "example",
        "description": "example", 
        "status": "closed"
        }
    )

    def test_ticket_description(self):
        ticket_string_detailed = repr(self.ticket.render_header(True))
        self.assertEqual(ticket_string_detailed, repr("id: 10\nsubject: example\nstatus: closed\ncreated_at: 01/01/2021\ndescription: example\n"))

class TestRequestor(unittest.TestCase):
    requestor = Requestor("example","example","example")

    def test_invalid_credentials(self):
        response = self.requestor.request()
        self.assertEqual(response, "err_bad_request") 

if __name__ == "__main__":
    unittest.main()
