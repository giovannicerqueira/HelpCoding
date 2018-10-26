import string

import cherrypy

import sys
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, CategoriesOptions


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="" name="duvida" />
              <button type="submit">Envie sua dúvida</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, duvida=8):
        natural_language_understanding = NaturalLanguageUnderstandingV1(
          username='31a0b567-7c67-4000-90a9-12ff29f56446',
          password='OWY6mgLqVLSX',
          version='2018-03-16')

        vr_text = duvida

        response = natural_language_understanding.analyze(
          text=vr_text,
          language='pt',
          features=Features(
            categories=CategoriesOptions(),
            entities=EntitiesOptions(
                model='7216ab41-66b8-4fd2-bbc2-0741e0a12f4f')
            ))

        resposta = ''

        for i in response['entities']:
            resposta.join(i['text'])
        
        return ''.join(resposta)


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
