from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def entity_sentiment_text(text):
    """Detects entity sentiment in the provided text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))
        
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

gcs_uri = 'gs://cloud-samples-data/language/president.txt'

client = language.LanguageServiceClient()

# Instantiates a plain text document.
document = types.Document(
    gcs_content_uri=gcs_uri,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects sentiment in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
entities = client.analyze_entities(document).entities

for entity in entities:
    entity_type = enums.Entity.Type(entity.type)
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('wikipedia_url',
          entity.metadata.get('wikipedia_url', '-')))
    print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))