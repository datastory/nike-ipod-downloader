# coding=utf-8
from xml.dom import minidom
import csv
import os
from os import listdir
from os.path import isfile, join
from sys import exit

outputFile = '/Users/jancibulka/Documents/NikeOutput.csv' #edit as you wish
#Edit name of yout iPod, instead of 'CibaPod'. Edit 'pedometer' for selecting another sensor. On Windows you have to change the whole path according to win file system.
ipodPath = '/Volumes/CibaPod/iPod_Control/Device/Trainer/Workouts/Empeds/pedometer/latest/' 

def writeNew(file):
	parsed = minidom.parse(file)
	type =  parsed.firstChild.childNodes[1].childNodes[0].firstChild.data
	dateTime =  parsed.firstChild.childNodes[1].childNodes[1].firstChild.data
	duration = parsed.firstChild.childNodes[1].childNodes[2].firstChild.data
	distance =  parsed.firstChild.childNodes[1].childNodes[4].firstChild.data
	paceRaw =  parsed.firstChild.childNodes[1].childNodes[6].firstChild.data
	calories =  parsed.firstChild.childNodes[1].childNodes[8].firstChild.data
	steps =  parsed.firstChild.childNodes[1].childNodes[9].childNodes[1].firstChild.data
	
	output = [type, dateTime, duration, distance, paceRaw, calories, steps]
	with open(outputFile, 'a') as f:
		writer = csv.writer(f, delimiter=';', quotechar='"')
		writer.writerow(output)

def actual(file):
	parsed = minidom.parse(file)
	lastDateTime =  parsed.firstChild.childNodes[1].childNodes[1].firstChild.data
	with open(outputFile, 'rb') as f:
		reader = csv.reader(f, delimiter=';', quotechar='"')
		dates = []
		for row in reader:
			dates.append(row[1])
		if lastDateTime in dates:
			pass
		else:
			writeNew(file)

if (os.path.exists(ipodPath) == True): 
	pass
else:
	exit(0)

try:
   with open(outputFile): pass
except IOError:
   fil = open(outputFile, 'w+')
   fil.close()

files = [f for f in listdir(ipodPath) if isfile(join(ipodPath,f))]
for file in files:
	actual(str(ipodPath + file))
	os.remove(str(ipodPath + file)) #this removes old workout files from iPod