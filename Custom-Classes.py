# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:24:09 2023

@author: Rizalyn
"""

class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

attendee1 = Attendee ("R. Aproda", 2)
attendee2 = Attendee ("M. Wong", 7)
attendee3 = Attendee ("R. Etiroza", 1)

attendee1.addTicket ()

attendee1.displayAttendee()
attendee3.displayAttendee()
attendee2.displayAttendee()

