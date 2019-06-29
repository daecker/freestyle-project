#vision.py

import io
import os
from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

##SETUP

def new_client():
    
    client = vision.ImageAnnotatorClient() # todo: explicit credentials
    return client
    
    ##credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)

if __name__ == "__main__":

    #print("CREDENTIALS FILEPATH:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

    img_filepath = os.path.join(os.path.dirname(__file__), "images", "Angkor.jpg") #TODO this is currently set to single file
    #print("IMAGE FILEPATH:", os.path.isfile(img_filepath), img_filepath)
    #print(os.path.isfile(img_filepath))

    with io.open(img_filepath, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>


    client = new_client()

    #print(type(client))
    response = client.landmark_detection(image=image)
    #print(type(response))
    #print(response)

    #used the following links for the below: https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1
    #https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.EntityAnnotation

    image_name = response.landmark_annotations[0].description
    image_score = response.landmark_annotations[0].score
    image_latitude = response.landmark_annotations[0].locations[0].lat_lng.latitude #type float
    image_longitude = response.landmark_annotations[0].locations[0].lat_lng.longitude #type float

    print(image_name)
    print(image_score)
    print(image_latitude)
    print(image_longitude)

 

   
    


  