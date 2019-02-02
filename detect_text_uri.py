# def detect_text_uri(uri):
#     """Detects text in the file located in Google Cloud Storage or on the Web.
#     """
#     from google.cloud import vision
#     client = vision.ImageAnnotatorClient.from_service_account_json('cvai-b7aec9ac67ad.json')
#     image = vision.types.Image()
#     image.source.image_uri = uri

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print('Texts:')

#     for text in texts:
#         print('\n"{}"'.format(text.description))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])

#         print('bounds: {}'.format(','.join(vertices)))

# detect_text_uri('gs://cvai-testing/8766.jpg')

from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_json(
    'cvai-b7aec9ac67ad.json')
response = client.annotate_image({
    'image': {'source': {'image_uri': 'gs://cvai-testing/8766.jpeg'}},
    'features': [{'type': vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION}],
})
with open('detect_text_uri.txt', 'w+') as f:
  f.write(str(response.full_text_annotation))
# for text in response.text_annotations:
#     # print('\n"{}"'.format(text.description))
#     # vertices = (['({},{})'.format(vertex.x, vertex.y)
#     #              for vertex in text.bounding_poly.vertices])
#     # print('bounds: {}'.format(','.join(vertices)))
#     print(text)
