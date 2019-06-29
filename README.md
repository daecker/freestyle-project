# freestyle-project

# SETUP

## Initial setup

Fork the repository and clone your forked repository to a location on your computer
This file is preloaded with landmark images. Future iterations of this program we hope to have the user load new images and expand beyond landmarks.

## Google Cloud API Access

  1. Create account on console.cloud.google.com #you may be asked to enter your CC information. 
  2. Create "new project".
  3. Add team members as needed to your project. When adding team members, be sure to set their preferences #editor preferred
  4. In the search bar, search for the  "Cloud Vision API" and click enable.
  5. Click "create credentials" and download the credentials to your computer.
        + you will be asked to create a service account. Be sure to give service account editor access
  6. See section below on credentials

Cloud Vision API Documentation: https://cloud.google.com/vision/?hl=en_US&_ga=2.234184030.-1556885463.1560810554


## Credentials

Navigate to the folder where you downloaded the "freestyle-project". You will want to create a folder called "auth" and drop in your downloaded credentials. Please rename the file to "credentials_freestyle.json"

note: the gitignore file is set up to ignore your json file. Any deviations from app/credentials_freestyle.json will require an update to the gitignore file.

gitignore file current setup:
```sh
auth/credentials_freestyle.json
auth/credentials.json
```

create a .env file and add the following
```sh
GOOGLE_APPLICATION_CREDENTIALS = "auth/credentials_freestyle.json"
```



## Enviornment
Open comand line and change directory to where you stored the "freestyle-project" folder. 

Create a new virtual enviornment

```sh
conda create -n vision-env python=3.7
conda activate vision-env
```

From within the virtual enviornment
```sh
pip install -r requirements.txt
```

# Run Application

```sh
python our_vision.py
```

# Suported Images

## File Formats

The Cloud Vision API supports the following image types:

  + JPEG
  + PNG8
  + PNG24
  + GIF
  + Animated GIF (first frame only)
  + BMP
  + WEBP
  + RAW
  + ICO
  + PDF
  + TIFF

## Image Sizing

Image sizing

To enable accurate image detection within the Cloud Vision API, images should generally be a minimum of 640 x 480 pixels (about 300k pixels). Full details for different types of Vision API Feature requests are shown below:

FACE_DETECTION	1600 x 1200	Distance between eyes is most important

LANDMARK_DETECTION	640 x 480

LOGO_DETECTION	640 x 480

LABEL_DETECTION	640 x 480

TEXT_DETECTION and DOCUMENT_TEXT_DETECTION	1024 x 768	OCR requires more resolution to detect characters

SAFE_SEARCH_DETECTION	640 x 480


## File Size
Image files sent to the Cloud Vision API should not exceed 20MB. Reducing your file size can significantly improve throughput; however, be careful not to reduce image quality in the process. Note that the Vision API imposes a 10MB JSON request size limit; larger files should be hosted on Cloud Storage or on the web, rather than being passed as base64-encoded content in the JSON itself.

# Future State

## Language Support
Language Support: https://cloud.google.com/vision/docs/languages
There are three levels of language support in the text recognition feature:
  1. Supported languages are those we prioritize and regularly evaluate performance against.
  2. Experimental languages are those under active development but not regularly evaluated against.
  3. Mapped languages are those supported by mapping them to another language code or to a general character recognizer. For example, "en-GB" is supported, but it is not treated any differently than "en" for the purposes of recognizing text. We make a best-effort to return the correct mapped language code in the Entity locale field, but mapped languages are more likely than fully supported or experimentally supported languages to be misidentified as a similar language.

## Additional Capabilities and Tutorials 

https://cloud.google.com/vision/docs/tutorials

## Geocoding API instructions 

Go to https://opencagedata.com/api and follow the below instructions: 
  1. Sign up for your free API Key
  2. Sign up with Google, Github, or register a new email
  3. For this application, choose "Reverse Geocoding"
You will be send an API key, which you should then add to the .env file and assign a variable, in this case you can name the variable "OPEN_CAGE_API"
Start geocoding by requesting a URL:
  1. Reverse geocoding: https://api.opencagedata.com/geocode/v1/json?q=LAT+LNG&key=YOUR-API-KEY

### Things to Note

Rate Limiting
  The OpenCage Geocoder uses a rate limiting mechanism to ensure that the service stays available to all users. Quota information for free trial users is returned by the API in the HTTP response headers as well as in the rate element of the response body.
  Free trial usage is limited to 2,500 requests per day. If you need more, please see the pricing page. We would love to have you as a customer. If you are not a customer and continually request beyond the free trial usage limit (ie you ignore the 402 status) you will eventually be blocked and see a 403 - Forbidden response. So don't do that. Thanks.
  If a geocoding request is issued that either exhausts your available transactions for the day or your available transactions are already used, a status of 402 - Payment Required will be returned in both the HTTP headers and in the response status field.
Rate Limit Headers
X-RateLimit-Limit   the total number of transactions that your account is limited to over a 24 hour period
X-RateLimit-Remaining   the number of transactions remaining in the current 24 hour period
X-RateLimit-Reset   the date and time, in UNIX format, at which your transaction count will reset
Requests per second
Free trial users are limited to 1 request per second and if you exceed that rate you may be blocked. Paying customers can use our service at a much faster rate, ranging from 10-15 requests per second depending on pricing tier. Please see the exact levels on our pricing page. If you need more than 15 requests per second please get in touch to discuss your exact needs.
If you request too quickly you will eventually see a 429 - Too many requests response.
