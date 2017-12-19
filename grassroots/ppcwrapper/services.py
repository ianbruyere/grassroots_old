import os
import requests
import json

#TODO: Need to migrate this 
PPC_API_KEY = 'xOE6X5gmCOiNu0BH7ksJJHnZVhmnmPQmri9QN2He' #os.environ.get('PPC_API_KEY', None)
	

def get_senate_members():
	return requests.get(_url('{}/{}/{}/members.json'.format(_version(),
	       '115','senate')), headers=_authentication()).json()
	pass

#TODO:Make other functions to other services
def get_bills():
	pass

def get_votes():
	pass	

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