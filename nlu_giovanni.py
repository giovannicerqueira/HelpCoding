#
# This script uses a specific model for news
#

import sys
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='31a0b567-7c67-4000-90a9-12ff29f56446',
  password='OWY6mgLqVLSX',
  version='2018-03-16')

#vr_text = sys.argv[1]
vr_text = input("Dúvida: ")

response = natural_language_understanding.analyze(
  text=vr_text,
  language='pt',
  features=Features(
    categories=CategoriesOptions(),
    entities=EntitiesOptions(
        model='7216ab41-66b8-4fd2-bbc2-0741e0a12f4f')
    ))

#print("Palavras-chave encontradas:")
print(json.dumps(response, indent=2))
#for i in response['entities']:
#    print(i['text'])
