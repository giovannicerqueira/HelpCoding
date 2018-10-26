import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='31a0b567-7c67-4000-90a9-12ff29f56446',
  password='OWY6mgLqVLSX',
  version='2018-03-16')

response = natural_language_understanding.list_models()

print(json.dumps(response, indent=2))
