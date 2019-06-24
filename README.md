# freestyle-project

# SETUP

## Initial setup

Fork the repository and clone your forked repository to a location on your computer

## Google Cloud API Access

  1. Create account on console.cloud.google.com #you may be asked to enter your CC information. 
  2. Create "new project".
  3. Add team members as needed to your project. When adding team members, be sure to set their preferences #editor preferred
  4. In the search bar, search for the  "Cloud Vision API" and click enable.
  5. Click "create credentials" and download the credentials to your computer.
        + you will be asked to create a service account. Be sure to give service account editor access
  6. See section below on credentials

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

