#
# This script uses a specific model for news
#

import sys
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='xxxxxxxxxxxx',
  password='xxxxxxxx',
  version='2018-03-16')

#vr_text = sys.argv[1]
vr_text = input("Dúvida: ")

response = natural_language_understanding.analyze(
  text=vr_text,
  language='pt',
  features=Features(
    categories=CategoriesOptions(),
    entities=EntitiesOptions(
        model='xxxxxxxxxxxxx')
    ))

#print("Palavras-chave encontradas:")
print(json.dumps(response, indent=2))
#for i in response['entities']:
#    print(i['text'])
