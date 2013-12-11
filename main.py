#!/usr/bin/env python3

import json
import http.client
import datetime

baseurl		= "ivu.aseag.de"
baseurl_stream	= "/interfaces/ura/stream_V1"
baseurl_instant	= "/interfaces/ura/instant_V1"
url_filter	= "?ReturnList=StopPointName,StopID,StopCode1,StopCode2,StopPointState,StopPointType,StopPointIndicator,Towards,Bearing,Latitude,Longitude,VisitNumber,TripID,VehicleID,RegistrationNumber,LineID,LineName,DirectionID,DestinationText,DestinationName,EstimatedTime,MessageUUID,MessageText,MessageType,MessagePriority,ExpireTime,BaseVersion"
url_filter_stop	= "&StopID="

jsondecoder = json.JSONDecoder()

connection = http.client.HTTPConnection(baseurl)
connection.request("GET", baseurl_stream + url_filter + url_filter_stop + "100625")

response = connection.getresponse()
encoding = response.headers.get_content_charset()

info = response.readline()

while (info):
	info = info.splitlines()

	for line in info:
		try:
			linearray = json.loads(line.decode(encoding))
		except:
			break
		if (linearray[0] == 1):
			time = datetime.datetime.fromtimestamp(linearray[22]*(10**(-3))).strftime('%H:%M:%S')
			formatinput = (time, linearray[13], linearray[16])
			print("%s %s %s" % formatinput)
	info = response.readline()
