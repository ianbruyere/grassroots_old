import unittest
import vcr
from ppcwrapper.services import CongressMembersClient, BillClient, VoteClient
import logging

my_vcr = vcr.VCR(cassette_library_dir='fixtures/cassettes', serializer='json', filter_headers=['X-API-Key'])

class CongressMembersClientTest(unittest.TestCase):
    'Testing Congress Member PPCWrapper Calls'

    @my_vcr.use_cassette()
    def test_get_congress_members(self):
        client = CongressMembersClient()
        data = client.get_members('senate')
        self.assertEqual(data['status'], 'OK')

    @my_vcr.use_cassette()
    def test_get_vote_positions(self):
        client = CongressMembersClient()
        data = client.get_vote_positions('B001282')
        self.assertEqual(data['status'], 'OK')

    @my_vcr.use_cassette()
    def test_get_cosponsored_bills(self):
        client = CongressMembersClient()
        data = client.get_cosponsored_bills('B001282', 'cosponsored')
        self.assertEqual(data['status'], 'OK')
        
  
class BillClientTest(unittest.TestCase):

    @my_vcr.use_cassette()
    def test_get_recent_bills(self):
        client = BillClient()
        data = client.get_recent_bills('senate', 'introduced')
        self.assertEqual(data['status'], 'OK')

    @my_vcr.use_cassette()
    def test_get_upcoming_bills(self):
        client = BillClient()
        data = client.get_upcoming_bills('senate')
        self.assertEqual(data['interactions'][0]['response']['status']['code'], 200)

    @my_vcr.use_cassette()
    def test_get_ammendment_for_bill(self):
        client = BillClient()
        data = client.get_amendments_for_bill('hr1628')
        self.assertEqual(data['status'], 'OK')

    @my_vcr.use_cassette()
    def test_get_subjects_for_bill(self):
        client = BillClient()
        data = client.get_subjects_for_bill('hr2810')
        self.assertEqual(data['headers']['status'], 'OK')

    @my_vcr.use_cassette()
    def test_get_related_bills(self):
        client = BillClient()
        data = client.get_related_bills('s1129')
        self.assertEqual(data['status'], 'OK')

class VoteClientTest(unittest.TestCase):
    
    @my_vcr.use_cassette()
    def test_get_recent_votes(self):
        client = VoteClient()
        data = client.get_recent_votes('senate')
        self.assertEqual(data['status'], 'OK')
    
    @my_vcr.use_cassette()
    def test_get_party_votes(self):
        client = VoteClient()
        data = client.get_party_votes('senate')
        self.assertEqual(data['status'], 'OK')
