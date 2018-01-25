import requests
import json 
from requests_toolbelt.multipart.encoder import MultipartEncoder


url = "https://api.einstein.ai/v2/vision/predict"

# {
#     "probabilities": [
#         {
#             "label": "UDAOne",
#             "probability": 0.79079205
#         },
#         {
#             "label": "UDAtwo",
#             "probability": 0.20920789
#         }
#     ],
#     "object": "predictresponse"
# }

def get_proper_output(response): 
	if(response['probabilities'][0]['probability'] > response['probabilities'][1]['probability']):
		return response['probabilities'][0]['label']
	else:
		return response['probabilities'][1]['label']

def get_relevant_tags(image_url):
	multipart_data = MultipartEncoder(fields={'sampleLocation': image_url, 'modelId' : "7V43R3TY2AHETRVPZLLVQ6MU6Y"})
	
	headers = {
	 		'Authorization': 'Bearer FF5I5TWAFP6FDYDGJQZIFG4JEJ6OMG5JDX3AQY3AQX6RKTJC4ESCWOZMNU6EYRFVPYCMXLLAEAWUIDVG7XWVPSEMJWUI3P4C3HMKMNA',
            'Content-Type': multipart_data.content_type
        }

	response = requests.post(url, headers=headers, data=multipart_data).json()

	return get_proper_output(response)