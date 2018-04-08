#Source Code for Mining data on Google+ with Python Course by TigerStyle Code Academy 

import os
import json
from apiclient.discovery import build


if __name__ == '__main__':
	api_key = os.environ.get('GOOGLE_API_KEY')


	service = build('plus', 'v1', developerKey=api_key)

#	people_resource = service.people()
#	people_document = people_resource.search(maxResults=50,query=str(args.query)).execute()

#	if 'items' in people_document:
#	  print ('got page with %d' % len( people_document['items'] ))
#	  for person in people_document['items']:
#	    print (person['id'], person['displayName'])	


	people_feed = service.people()
	search_query = people_feed.search(query="Singh")
	search_results = search_query.execute()
	print(json.dumps(search_results, indent=4))