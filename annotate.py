import cv2

cam = cv2.VideoCapture(0)
image = 0



def CaptureImage():
	print("Capturing Image :")
	ret, image = cam.read()
	print("Image Capture successfully")
	cv2.destroyAllWindows()
	return image
	

def AnnotateImage(image):
	print("print Annotation Completed..")
	print("Dimension of the Image :",image.shape)
	Start = (0,340)
	End = (100,480)
	cv2.rectangle(image , Start,End,(0,0,255))
	cv2.putText(image, "pen_stand", (0,330), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0))
	
	cv2.imshow('AnnotatedImage', image)
	cv2.waitKey(10000)


AnnotateImage(CaptureImage())
