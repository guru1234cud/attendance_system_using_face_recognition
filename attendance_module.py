import csv
from datetime import datetime

class AttendanceSystem:
    def __init__(self, attendance_file="attendance.csv"):
        self.attendance_file = attendance_file
        self.attended_names = set()

    def mark_attendance(self, name):
        if name not in self.attended_names:
            self.attended_names.add(name)
            with open(self.attendance_file, 'a') as f:
                now = datetime.now()
                time_string = now.strftime('%H:%M:%S')
                date_string = now.strftime('%Y-%m-%d')
                f.writelines(f'{name},{time_string},{date_string}\n')

    def load_attendance(self):
        with open(self.attendance_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.attended_names.add(row[0])

obj=AttendanceSystem()
obj.mark_attendance("guru")
