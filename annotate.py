import cv2

cam = cv2.VideoCapture(0)
image = 0


def CaptureImage():
	global image
	print("Capturing Image :")
	ret, image = cam.read()
	k = cv2.waitKey(1000)
	print("Image Capture successfully")
	cv2.imwrite('/home/pi/pictures/testimage.jpg',image)
	cam.release()
	cv2.destroyAllWindows()

def AnnotateImage():
	print("print Annotation Completed..")
	ImageCopy = cv2.imread('/home/pi/Picture/testimage.jpg',image)
	ImageDimension = ImageCopy.shape
	print("Dimension of the Image :",str(ImageDimension))
	Start = (0,340)
	End = (100,480)
	cv2.rectangle(ImageCopy , Start,End,(0,0,255),thickness = 3, lineType = cv2.LINE_8)
	cv2.putText(ImageCopy, "pen_stand", (0,330), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),1)
	
	cv2.imshow('AnnotatedImage', ImageCopy)
	cv2.waitKey(10000)

CaptureImage()
AnnotateImage()