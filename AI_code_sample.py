import os
import numpy as np
import argparse
import cv2


def extract_faces(frame):

	#frame = cv2.equalizeHist(frame)

	face_cascade =   cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
	profile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')

	faces = face_cascade.detectMultiScale(frame,1.3,5)
	profiles = profile_cascade.detectMultiScale(frame,1.3,5)
	clone = frame.copy()
	len(faces)
	for (x,y,w,h) in faces:

		img = clone[y:y+h,x:x+w]
		#print(img)
		try:
			cv2.imshow('face',img)
			cv2.waitKey(1)
		except:
			print("hello")

def main():

	cap = cv2.VideoCapture(0)
	

	
	os.chdir("face I/")
	for img in os.listdir():
		frame = cv2.imread(img)	
		extract_faces(frame)

	# while True:
	# 	ret,frame = cap.read()

	# 	# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	# 	extract_faces(frame)


if __name__ == '__main__':
	main()

