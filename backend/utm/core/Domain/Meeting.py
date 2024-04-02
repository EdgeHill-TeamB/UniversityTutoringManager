from datetime import datetime


class Meeting:
    def __init__(self, meeting_id, tutor, student, start_time, end_time, location):
        self.meeting_id = meeting_id
        self.tutor = tutor
        self.student = student
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def remove_attendee(self, attendee):
        self.attendees.remove(attendee)

    def update_start_time(self, new_start_time):
        self.start_time = new_start_time

    def update_end_time(self, new_end_time):
        self.end_time = new_end_time

    def update_location(self, new_location):
        self.location = new_location

    def get_duration(self):
        return self.end_time - self.start_time
