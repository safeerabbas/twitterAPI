import requests
endpoint = 'https://api.twitter.com/2/tweets/search/recent'
BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAAC0ZwEAAAAAiyG6E8BK7ayHh2hZq7GPp7BVnvI%3DcRTs97kR9UV8H5uktjwhVKlhgGIQsObuN1m8GEY5ZT6QrIep4e'
headers = {'authorization': f'Bearer {BEARER_TOKEN}'}
query_string='sit in OR jaloos OR protest OR ehtijaj'
params = {
    'query': query_string,
    'max_results': '10',
    'expansions': 'geo.place_id',
    'place.fields': 'contained_within,country=pakistan,country_code,full_name,geo,id,name,place_type'
}
response = requests.get(endpoint,params=params,headers=headers)

print(response)
# {"errors":[{"parameters":{"tweet.fields":["created_at,lang,text,author_id,public_metrics,geo,geo.coordinates"]},
#             "message":"The `tweet.fields` query parameter value [geo.coordinates] is not one of [attachments,author_id,context_annotations,"
# "conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics"
#                       ",public_metrics,referenced_tweets,reply_settings,source,text,withheld]"}],"title":"Invalid Request",""
#     detail":"One or more parameters to your request was invalid.","type":"https://api.twitter.com/2/problems/invalid-request"}