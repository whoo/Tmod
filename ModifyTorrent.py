#!/usr/bin/env python2

import sys
import bencode


if (len(sys.argv)<2):
	print "Need file to modify"
	exit(1)	


print "-"*80
TFile = sys.argv[1]
data=open(TFile,'rb').read()
info=bencode.bdecode(data)
print ("\033[94mOriginal tracker:%s\033[0m"% (info['announce']))
print "-"*80
try:
	tempTracker=open('Id.py','r').read()
	trackers= tempTracker.split('\n')
	trackers.pop()

except IOError:
	print "\033[91mIl faut mettre la liste des trackers dans Id.py\033[0m"
	exit(1)
	


info['announce']=trackers[0]
print ("New tracker:%s"% (trackers[0]))
info['announce-list']=[]

for idx,val in enumerate(trackers):
	info['announce-list'].append([val])
	print "Setting %s as Tracker %d"%(val,idx)

NFile="new.torrent"

try:
	Out=open(NFile,'wb')
	Out.write(bencode.bencode(info))
	Out.close()
except IOError:
	print '\033[91mIl faut les droits pour creer new.torrent '
	exit(2)

print "\033[92mFichier new.torrent is created\033[0m"
