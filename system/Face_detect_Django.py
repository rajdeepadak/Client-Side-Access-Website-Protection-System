import cv2

cap = cv2.VideoCapture(0)  # Initiates camera
cap.open(0)  # Opens First available camera device
print(cap.open(0))  # True if camera is successfully opened

if cap.isOpened():
    retval, frame = cap.read()  # retval is True if image is obtained
    # Frame is RGB List of Image
    print(retval)
    print(frame)

else:
    retval = False
    print("Error Opening Camera")

    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

outpath = "C:\\Users\\rajde\\Desktop\\Django\\Django Project\\website\\music\\static\\music\\images\\User.jpeg"
cv2.imwrite(outpath, frame)

imagePath = "C:\\Users\\rajde\\Desktop\\Django\\Django Project\\website\\music\\static\\music\\images\\User.jpeg"

cascPath = "C:\\Users\\rajde\\Desktop\\My Stuff\\Image Processing Database\\DIP Files\\FaceDetect-master\\haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    # flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

facenos = len(faces)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.imwrite(outpath, image)
cv2.waitKey(0)


