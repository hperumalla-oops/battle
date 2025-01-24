import cv2
from pushbullet import Pushbullet
from time import sleep 

cam = cv2.VideoCapture(0)
image = 0
api="o.kWWLMHhCVKfYb5SiWkcnc6nihHkKfRPC"

def CaptureImage():
	print("Capturing Image :")
	ret, image = cam.read()
	k = cv2.waitKey(1000)
	print("Image Capture successfully")
	cv2.imwrite('testimage.jpg',image)
	cam.release()
	cv2.destroyAllWindows()
	print("Sending the Notification")

def SendNotification():
	pb = Pushbullet(api)
	dev = pb.get_device("Xiaomi 22120RN86I")  ##devic name
	with open('testimage.jpg','rb') as pic:
		file_data = pb.upload_file(pic,"Picture.jpg")
		push = pb.push_file(**file_data)
		Value = push["active"]
		if Value == True:
			print("Message sent successfully...")
		else:
			print("Sending Message Failed..")

CaptureImage()
SendNotification()
