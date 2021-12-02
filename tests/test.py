import sys
import unittest
from os.path import abspath, dirname

import requests

sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/src')

from models.ticket import Ticket
from models.ticket_viewer import TicketViewer


class TestTicket(unittest.TestCase):
    ticket_json = {
        "created_at" : "08/01/2021",
        "id": 1, 
        "assignee_id": "123456789",
        "submitter_id": "987654321",
        "subject": "Test Ticket",
        "description": "Test Ticket", 
        "requester_id": "111111111",
        "status": "closed"
    } 

    ticket = Ticket(ticket_json)

    def test_ticket_repr(self):
        ticket_string = str(self.ticket)
        self.assertEqual(ticket_string, "Ticket Id: 1 || Created At:08/01/2021 || Assigned To: 123456789 || Status: closed")
    
    def test_ticket_details(self):
        ticket_details = self.ticket.get_ticket_detail()
        self.assertEqual(ticket_details, "\n Ticket ID: 1 \n Created At: 08/01/2021 \n Assigned To: 123456789 \n Status: closed \n Subject: Test Ticket \n Description: Test Ticket \n")

class TestRetriever(unittest.TestCase):
    retriever = TicketRetriever()
    wrong_id = "ab2"

    def test_no_page(self):
        no_page = self.retriever.get_page_count()
        self.assertEqual(no_page, 4) 
    
    def test_wrong_id(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            self.retriever.retrieve_individual_ticket(self.wrong_id)

if __name__ == "__main__":
    unittest.main() 
