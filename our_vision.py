#vision.py

import io
import os
from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

def new_client():
    ##credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)

    client = vision.ImageAnnotatorClient() # todo: explicit credentials
    return client

def get_text_annotations(img_filepath):
    with io.open(img_filepath, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>

    client = new_client()
    response = client.text_detection(image=image) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    annotations = response.text_annotations #> <class 'google.protobuf.pyext._message.RepeatedCompositeContainer'>
    #print("ANNOTATIONS:", len(annotations))
    #for annotation in annotations:
    #    print("---------------")
    #    print(type(annotation), annotation.locale)
    #    print(annotation.description)
    # each  annotation is a <class 'google.cloud.vision_v1.types.EntityAnnotation'>
    descriptions = [a.description.strip() for a in annotations] #> ['1 7 6 3', '1', '7', '6', '3']
    return descriptions