# freestyle-project

# Suported Images
<pre>
The Cloud Vision API supports the following image types:

JPEG
PNG8
PNG24
GIF
Animated GIF (first frame only)
BMP
WEBP
RAW
ICO
PDF
TIFF

</pre>

# Image Sizing
<pre>
Image sizing

To enable accurate image detection within the Cloud Vision API, images should generally be a minimum of 640 x 480 pixels (about 300k pixels). Full details for different types of Vision API Feature requests are shown below:
FACE_DETECTION	1600 x 1200	Distance between eyes is most important

LANDMARK_DETECTION	640 x 480

LOGO_DETECTION	640 x 480

LABEL_DETECTION	640 x 480

TEXT_DETECTION and DOCUMENT_TEXT_DETECTION	1024 x 768	OCR requires more resolution to detect characters

SAFE_SEARCH_DETECTION	640 x 480
</pre>

# File Size
Image files sent to the Cloud Vision API should not exceed 20MB. Reducing your file size can significantly improve throughput; however, be careful not to reduce image quality in the process. Note that the Vision API imposes a 10MB JSON request size limit; larger files should be hosted on Cloud Storage or on the web, rather than being passed as base64-encoded content in the JSON itself.