#!/usr/bin/env python3
import json
import http.client
import datetime
import sys

def tstodate(ts):
	return datetime.datetime.fromtimestamp(ts*(10**(-3))).strftime('%Y-%m-%d %H:%M:%S')

def tstotime(ts):
	return datetime.datetime.fromtimestamp(ts*(10**(-3))).strftime('%H:%M:%S')


baseurl		= "ivu.aseag.de"
baseurl_stream	= "/interfaces/ura/stream_V1"
baseurl_instant	= "/interfaces/ura/instant_V1"
url_filter	= "?ReturnList=StopPointName,StopID,StopCode1,StopCode2,StopPointState,StopPointType,StopPointIndicator,Towards,Bearing,Latitude,Longitude,VisitNumber,TripID,VehicleID,RegistrationNumber,LineID,LineName,DirectionID,DestinationText,DestinationName,EstimatedTime,MessageUUID,MessageText,MessageType,MessagePriority,BaseVersion"
url_filter_stop	= "&StopID="

try:
	haltestelle = sys.argv[1]
except:
	haltestelle = "100111"

jsondecoder = json.JSONDecoder()

connection = http.client.HTTPConnection(baseurl)
connection.request("GET", baseurl_instant + url_filter + url_filter_stop + haltestelle)

response = connection.getresponse()
encoding = response.headers.get_content_charset()

info = response.read().splitlines()

ausgabe = []

for line in info:
	linearray = json.loads(line.decode(encoding))

	#Es ist nur eine Fahrplaninfo, wenn das erste Feld 0 ist
	if (linearray[0] == 1):
		# 21 = Zeit, 13 = Busnummer, 16 = Ziel
		formatinput = (linearray[21], linearray[13], linearray[16])
		ausgabe.append(formatinput)

#Sortierung nach der Zeit
ausgabe.sort(key=lambda tup: tup[0])
for elem in ausgabe:
	print("%s %s %s" % (tstotime(elem[0]), elem[1], elem[2]))
