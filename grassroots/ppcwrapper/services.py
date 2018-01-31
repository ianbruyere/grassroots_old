from django.conf import settings
import os
import requests
import json

class HelperMixIn(object):
    """this contains all the stuff universal to the ProPublica Data Store"""
    def __init__(self):
	    pass

    def _authentication():
        return {'X-API-Key' : settings.PPC_API_KEY}

    def _version():
	    return 'v1'

    def _url(path):
	    return 'https://api.propublica.org/congress/' + path

#TODO:Make other functions to other services
def get_bills():
	return requests.get(_url())

def get_votes():
	pass	

def get_statements():
	pass

def get_explanations():
	pass

def get_committees():
	pass

# Helper Functions
class CongressMembers(HelperMixIn):
	"""This will contain all the possibilties for CongressMembers"""

	def __init__(self):
		super(CongressMembers, self).__init__()
		self.congressSession = '115'

	def get_members(memberType):
		return requests.get('https://api.propublica.org/congress/{}/{}/{}/members.json'
		.format('v1', '115', memberType), headers={'X-API-Key' : settings.PPC_API_KEY}).json()
	
	