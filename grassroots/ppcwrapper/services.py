from django.conf import settings
import os
import requests
import json

class HelperMixIn(object):
    """this contains all the stuff universal to the ProPublica Data Store"""
    def __init__(self):
	    pass
	
    # @property
    # def authentication():
    #     return {'X-API-Key' : settings.PPC_API_KEY}
	
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
    
	def get_members(self, memberType):
		path='{}/{}/members.json'.format(self.congressSession, memberType)
		return super().requester(path)
	
	def get_vote_positions(self, memberId):
		path='members/{}/votes.json'.format(memberId)
		return super().requester(path)

	def get_cosponsored_bills(self, memberId, cosponoredOrWithdrawn):
		path='members/{}/bills/{}.json'.format(memberId, cosponoredOrWithdrawn)
		return super().requester(path)
	
class BillClient(HelperMixIn):
	"""Bill-related calls """
	def __init__(self):
		super()
		self.congressSession = '115'

	def get_recent_bills(self, chamber, typeOfBill):
		path='{}/{}/bills/{}.json'.format(self.congressSession, chamber, typeOfBill)
		return super().requester(path)
	
	def get_upcoming_bills(self, chamber):
		path='bills/upcoming/{}.json'.format(chamber)
		return super().requester(path)

	def get_amendments_for_bill(self, billId):
		path='{}/bills/{}/amendments.json'.format(self.congressSession, billId)
		super().requester(path)

	def get_subjects_for_bill(self, billId):
		path='{}/bills/{}/subjects.json'.format(self.congressSession, billId)
		super().requester(path)

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

