import pandas as pd
import numpy as np
import time
import xlwt
from xlwt import Workbook
import cv2
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mail import send_mail

def norm():
	df = pd.read_excel('attentiondata.xls', sheet_name=0) # can also index sheet by name or fetch all sheets
	# print(df)


	time = df['Time'].tolist()
	blink = df['Blink count'].tolist()
	pixel = df['Pixel Similarity'].tolist()
	emotion = df['Emotion'].tolist()
	dist = df['Looking at'].tolist()
	noise = df['Noise level'].tolist()
	face = df['Face Auth'].tolist()

	fig = plt.figure(1)
	# set up subplot grid


	gridspec.GridSpec(3,3)

	# small subplot 0
	plt.subplot2grid((2,3), (0,0))
	plt.plot(time,blink)
	plt.title('Blink rate')
	plt.xlabel('Time (s)')
	plt.ylabel('Blinks')

	# small subplot 1
	plt.subplot2grid((2,3), (0,1))
	plt.plot(time,pixel)
	plt.title('Position change')
	plt.xlabel('Time (s)')
	plt.ylabel('Pixel Difference')

	# small subplot 2
	plt.subplot2grid((2,3), (0,2))
	plt.plot(time,emotion)
	plt.title('Emotion')
	plt.xlabel('Time (s)')
	plt.ylabel('Emotion detection')

	# small subplot 3
	plt.subplot2grid((2,3), (1,0))
	plt.plot(time,dist)
	plt.title('Looking at')
	plt.xlabel('Time (s)')
	plt.ylabel('Eye tracking')	

	# small subplot 4
	plt.subplot2grid((2,3), (1,1))
	plt.plot(time,noise)
	plt.title('Noise level')
	plt.xlabel('Time (s)')
	plt.ylabel('Noise level')

	# plt.subplot2grid((2,3), (1,2))
	# plt.plot(time,face)
	# plt.title('Face recognition')
	# plt.xlabel('Time (s)')
	# plt.ylabel('Face Match')


	bmin = min(blink)-0.1
	bmax = max(blink)+0.1
	blink = [1-((i-bmin)/(bmax-bmin)) for i in blink]  	# negative correlation
	pixel = [i for i in pixel]						# positive correlation

	nmin = min(noise)-1
	nmax = max(noise)+1
	noise = [1-((i-nmin)/(nmax-nmin)) for i in noise]				# negative correlation

	dist = [i for i in dist]						# positive correlation

	# print(noise)
	att = list()
	for i in range(len(time)):
		att.append((blink[i])*0.2 + emotion[i]*0.2 + pixel[i]*0.2 + dist[i]*0.2 + (noise[i])*0.2)

	# dfout = pd.DataFrame(list(zip(time, blink, pixel, emotion, dist, noise, att)), columns =['Time', 'Blink count', 'Pixel Similarity', 'Emotion', 'Looking at', 'Noise level', 'Average attention'])
	# print(dfout)


	# small subplot 5
	plt.subplot2grid((2,3), (1,2))
	plt.plot(time,att)
	plt.title('Attention level')
	plt.xlabel('Time (s)')
	plt.ylabel('Attention level')

	avgatt =  round(np.mean(att)*100, 2)
	out = "Your Average attention span is : " + str(avgatt) + "%"

	fig.suptitle(out)

	print(out)

	fig.tight_layout()
	fig.set_size_inches(w=15,h=8)
	fig_name = 'plot.png'

	fig.savefig(fig_name)

	# fig = plt.figure(2)
	# img = plt.imread(fig_name)
	# plt.imshow(img)
	# plt.show()

	# send_mail(out)
	# print("Mail sent !")

if __name__ == '__main__':
	while True:
		time.sleep(5)
		norm()
	# norm()
