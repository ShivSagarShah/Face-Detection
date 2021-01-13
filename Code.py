import cv2  # This is used to import Open CV

FaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# The above snippet creates a face cascade

VideoCapture = cv2.VideoCapture(0)

# The above line sets the video source to default webcam

while True:
    ret, frame = VideoCapture.read()

# The above code reads the video frame bye frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = (FaceCascade.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE))
# The above snippet is used to search the face in the video

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Video", frame)

# The above snippet is used to draw rectangles around the face

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# The above code needs the user to press 'q' to quit "You can Keep any variable instead of 'q'"

VideoCapture.release()
cv2.destroyAllWindows()

# The above code is used to terminate the video.
