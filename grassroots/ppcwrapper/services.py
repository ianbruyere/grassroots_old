from django.conf import settings
import os
import requests
import json

class HelperMixIn(object):
    """this contains all the stuff universal to the ProPublica Data Store"""
    def __init__(self):
	    pass
	
    @staticmethod
    def version():
	    return 'v1'

    @staticmethod
    def requester(path):
	    return requests.get('https://api.propublica.org/congress/v1/ ' + path, 
	                        headers={'X-API-Key' : settings.PPC_API_KEY}).json()

class CongressMembersClient(HelperMixIn):
	"""This will contain all the possibilties for CongressMembersClient"""

	def __init__(self):
		super()
		self.congressSession = '115'
    
	def get_members(self, chamber):
		path='{}/{}/members.json'.format(self.congressSession, chamber)
		return super().requester(path)
	
	def get_vote_positions(self, memberId):
		path='members/{}/votes.json'.format(memberId)
		return super().requester(path)

	def get_cosponsored_bills(self, memberId, cosponoredOrWithdrawn):
		path='members/{}/bills/{}.json'.format(memberId, cosponoredOrWithdrawn)
		return super().requester(path)
	
	def raw_requester(path):
		return requests.get(path, headers={'X-API-Key' : settings.PPC_API_KEY}).json()


class BillClient(HelperMixIn):
	"""Bill-related calls """
	def __init__(self):
		super()
		self.congressSession = '115'

	def get_specific_bill(self, billId):
		path='{}/bills/{}.json'.format(self.congressSession, billId)
		return super().requester(path)

	def get_recent_bills(self, chamber, typeOfBill):
		path='{}/{}/bills/{}.json'.format(self.congressSession, chamber, typeOfBill)
		return super().requester(path)
	
	def get_upcoming_bills(self, chamber):
		path='bills/upcoming/{}.json'.format(chamber)
		return super().requester(path)

	def get_amendments_for_bill(self, billId):
		path='{}/bills/{}/amendments.json'.format(self.congressSession, billId)
		return super().requester(path)

	def get_subjects_for_bill(self, billId):
		path='{}/bills/{}/subjects.json'.format(self.congressSession, billId)
		return super().requester(path)


    def get_votes():
	    pass	

	def get_related_bills(self, billId):
		path='{}/bills/{}/related.json'.format(self.congressSession, billId)
		return super().requester(path)
	
	def raw_requester(self, path):
		return requests.get(path, headers={'X-API-Key' : settings.PPC_API_KEY}).json()

	def get_related_bills(self, billId):
		path='{}/bills/{}/related.json'.format(self.congressSession, billId)
		return super().requester(path)


class VoteClient(HelperMixIn):
	"""Vote Related Calls"""

	def __init__(self):
		super()
		self.congressSession = '115'

	def get_recent_votes(self, chamber):
		path='{}/votes/recent.json'.format(chamber)
		return super().requester(path)

	def get_party_votes(self, chamber):
		"""Gets how often someone votes with their party"""
		path='{}/{}/votes/party.json'.format(self.congressSession, chamber)
		return super().requester(path)

	def get_specific_roll_call(self, chamber, session):
		"""gets the votes and positions for a specfic roll call"""
		#TODO some of this is going to be hardcoded until I can figure
		# out a way to get the proper latest set of roll calls and year for 
		# now just trying to stub out data format
		path='{}/{}/sessions/{}/votes/{}.json' \
		.format(self.congressSession, chamber, session, '17')
		return super().requester('115/senate/sessions/1/votes/17.json')

