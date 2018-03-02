import os
import requests
import json

#TODO: Need to migrate this 
PPC_API_KEY = 'xOE6X5gmCOiNu0BH7ksJJHnZVhmnmPQmri9QN2He' #os.environ.get('PPC_API_KEY', None)
	
<<<<<<< Updated upstream
=======
    # @property
    # def authentication():
    #     return {'X-API-Key' : settings.PPC_API_KEY}
	
    @staticmethod
    def version():
	    return 'v1'

    @staticmethod
    def requester(path):
	    return requests.get('https://api.propublica.org/congress/v1/' + path, 
	                        headers={'X-API-Key' : settings.PPC_API_KEY}).json()

	# @staticmethod
	# def raw_requester(path):
	# 	return requests.get(path, headers={'X-API-Key' : settings.PPC_API_KEY}).json())


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
	
	def get_vote_positions(self, memberId):
		path= 'members/{}/votes.json'.format(memberId)
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
>>>>>>> Stashed changes

def get_senate_members():
	return requests.get(_url('{}/{}/{}/members.json'.format(_version(),
	       '115','senate')), headers=_authentication()).json()
	pass

#TODO:Make other functions to other services
def get_bills():
	pass

<<<<<<< Updated upstream
def get_votes():
	pass	
=======
	def get_related_bills(self, billId):
		path='{}/bills/{}/related.json'.format(self.congressSession, billId)
		return super().requester(path)
	
	def raw_requester(self, path):
		return requests.get(path, headers={'X-API-Key' : settings.PPC_API_KEY}).json()
>>>>>>> Stashed changes

def get_statements():
	pass

def get_explanations():
	pass

def get_committees():
	pass

# Helper Functions
def _authentication():
	return {'X-API-Key' : PPC_API_KEY}

def _version():
	return 'v1'

def _url(path):
	return 'https://api.propublica.org/congress/' + path