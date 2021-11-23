from elasticsearch import Elasticsearch, helpers
import pandas as pd

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'cricketers'

df = pd.read_excel('cricketersNew.xlsx')
print(df.columns)
df2 = df.to_dict('records')
print(df2[0])


def generator(df2):
    for c, line in enumerate(df2):
        yield {
            '_index': INDEX,
            '_type': '_doc',
            '_id': c,
            '_source': {
                'முழு பெயர்': line.get('fullname', None),
                'பட்டப்பெயர்': line.get('nickname', None),
                'மட்டையாட்ட நடை': line.get('battingstyle', None),
                'பந்துவீச்சு நடை': line.get('bowlingstyle', None),
                'பங்கு': line.get('role', None),
                'நாட்டு அணி': line.get('nationalteam', None),
                'அறிமுகம்': line.get('introduction', None),
                'உள்ளடக்கம்': line.get('content', None)
            }
        }


settings = {
    'settings': {
        'analysis': {
            'analyzer': {
                'my_analyzer': {
                    'type': 'custom',
                    'tokenizer': 'standard',
                    'filter': [
                        'tamil_synonym',
                        'tamil_stop',
                        'tamil_stemmer'
                    ]
                }
            },
            'filter': {
                'tamil_synonym': {
                    'type': 'synonym',
                    'synonyms_path': 'analysis/synonym.txt'
                },
                "tamil_stop": {
                    "type": "stop",
                    "stopwords": ['ஒரு',
                                  'என்று',
                                  'மற்றும்',
                                  'இந்த',
                                  'இது',
                                  'என்ற',
                                  'கொண்டு',
                                  'என்பது',
                                  'பல',
                                  'ஆகும்',
                                  'அல்லது',
                                  'அவர்',
                                  'நான்',
                                  'உள்ள',
                                  'அந்த',
                                  'இவர்',
                                  'என',
                                  'முதல்',
                                  'என்ன',
                                  'இருந்து',
                                  'சில',
                                  'என்',
                                  'போன்ற',
                                  'வேண்டும்',
                                  'வந்து',
                                  'இதன்',
                                  'அது',
                                  'அவன்',
                                  'தான்',
                                  'பலரும்',
                                  'என்னும்',
                                  'மேலும்',
                                  'பின்னர்',
                                  'கொண்ட',
                                  'இருக்கும்',
                                  'தனது',
                                  'உள்ளது',
                                  'போது',
                                  'என்றும்',
                                  'அதன்',
                                  'தன்',
                                  'பிறகு',
                                  'அவர்கள்',
                                  'வரை',
                                  'அவள்',
                                  'நீ',
                                  'ஆகிய',
                                  'இருந்தது',
                                  'உள்ளன',
                                  'வந்த',
                                  'இருந்த',
                                  'மிகவும்',
                                  'இங்கு',
                                  'மீது',
                                  'ஓர்',
                                  'இவை',
                                  'இந்தக்',
                                  'பற்றி',
                                  'வரும்',
                                  'வேறு',
                                  'இரு',
                                  'இதில்',
                                  'போல்',
                                  'இப்போது',
                                  'அவரது',
                                  'மட்டும்',
                                  'இந்தப்',
                                  'எனும்',
                                  'மேல்',
                                  'பின்',
                                  'சேர்ந்த',
                                  'ஆகியோர்',
                                  'எனக்கு',
                                  'இன்னும்',
                                  'அந்தப்',
                                  'அன்று',
                                  'ஒரே',
                                  'மிக',
                                  'அங்கு',
                                  'பல்வேறு',
                                  'விட்டு',
                                  'பெரும்',
                                  'அதை',
                                  'பற்றிய',
                                  'உன்',
                                  'அதிக',
                                  'அந்தக்',
                                  'பேர்',
                                  'இதனால்',
                                  'அவை',
                                  'அதே',
                                  'ஏன்',
                                  'முறை',
                                  'யார்',
                                  'என்பதை',
                                  'எல்லாம்',
                                  'மட்டுமே',
                                  'இங்கே',
                                  'அங்கே',
                                  'இடம்',
                                  'இடத்தில்',
                                  'அதில்',
                                  'நாம்',
                                  'அதற்கு',
                                  'எனவே',
                                  'பிற',
                                  'சிறு',
                                  'மற்ற',
                                  'விட',
                                  'எந்த',
                                  'எனவும்',
                                  'எனப்படும்',
                                  'எனினும்',
                                  'அடுத்த',
                                  'இதனை',
                                  'இதை',
                                  'கொள்ள',
                                  'இந்தத்',
                                  'இதற்கு',
                                  'அதனால்',
                                  'தவிர',
                                  'போல',
                                  'வரையில்',
                                  'சற்று',
                                  'எனக்']
                },
                "tamil_stemmer": {
                    "type": "stemmer",
                    "rules_path": "analysis/stemmer.txt"
                }
            }
        },
        'number_of_shards': 1,
        'number_of_replicas': 0
    },
    'mappings': {
        'properties': {
            'முழு பெயர்': {
                'type': 'text'
            },
            'பட்டப்பெயர்': {
                'type': 'text'
            },
            'மட்டையாட்ட நடை': {
                'type': 'text'
            },
            'பந்துவீச்சு நடை': {
                'type': 'text'
            },
            'பங்கு': {
                'type': 'text'
            },
            'நாட்டு அணி': {
                'type': 'text'
            },
            'அறிமுகம்': {
                'type': 'text'
            },
            'உள்ளடக்கம்': {
                'type': 'text'
            }
        }
    }
}

response = client.indices.create(index=INDEX, ignore=[400, 404], body=settings)
print(response)

try:
    res = helpers.bulk(client, generator(df2))
    print('Working')
except Exception as e:
    print(e)
    pass
