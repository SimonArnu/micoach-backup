#!/usr/bin/env python

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

import os, sys
from libmicoach.user import miCoachUser
from libmicoach.errors import *
from storage import Storage

email = 'simon@arnu.de'
pw = 'PupsNas3Mc'
user = miCoachUser(email, pw)
print user.screenName
user.workoutList = user.getSchedule().getWorkoutList()
#~ for workout in user.workoutList:
	#~ print workout['id'], workout
	
storage = Storage(user.screenName)
i = 0
newWorkouts = storage.compareWorkoutList(user.workoutList)
print newWorkouts
#~ log.info('Getting workouts %s' % ','.join(newWorkouts))
for w in newWorkouts:
	i += 1
	log.info('Getting workout %s' % w)
	#~ storage.addWorkout(user.getSchedule().getWorkout(w['id']))
	storage.addWorkout(user.getSchedule().getWorkout(w))
