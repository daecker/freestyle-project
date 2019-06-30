#vision.py

import io
import os
from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

##SETUP

def to_percent(my_confidence):
    return "{:.2%}".format(my_confidence)


def new_client():
    
    client = vision.ImageAnnotatorClient() # todo: explicit credentials
    return client
    
    ##credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)

## INFORMATION INPUT

if __name__ == "__main__":

    while True:
        image_folder = input("Please Enter Folder Directory Containing your Image Files: ")
        if not os.path.exists(image_folder):
            print("Oops! You need to enter a valid path")
        else:
            break

    folder_content = os.listdir(image_folder)
    print(folder_content)
    
    while True:
        image_selection = input("Please Enter a Valid Image Name (Exactly as it appears, including .jpg): ")
        if image_selection not in folder_content:
            print("Oops! that is not a valid image name. Try Again")
            print(folder_content)
        else:
            break

    img_filepath = os.path.join(str(image_folder), str(image_selection))
    
    with io.open(img_filepath, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>


    client = new_client()
    response = client.landmark_detection(image=image)


    #used the following links for the below: https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1
    #https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.EntityAnnotation

    image_name = response.landmark_annotations[0].description
    image_score = response.landmark_annotations[0].score
    image_latitude = response.landmark_annotations[0].locations[0].lat_lng.latitude #type float
    image_longitude = response.landmark_annotations[0].locations[0].lat_lng.longitude #type float

## INFORMATIN OUTPUT
    print("We are identifying your landmark now...")
    print("We found a match!")
    print("The landmark is named:  " + image_name)
    print("We can say that with a confidence of: " + to_percent(image_score))
    print("Landmark Location Latitude: " + str(image_latitude))
    print("Landmark Location Longitude: " + str(image_longitude))

 

   
    


  