from django.test import TestCase
from .libraries.PyMo.PyMoHandler import PythonToMongo as pm
from .libraries.PyCa.PyCa import PyCa as pc
# Create your tests here.


class DatabaseTestCase(TestCase):

    def test_PyCa(self):
        PyCa = None
        try:
            PyCa = pc()
        except:
            self.assertEqual("Calendar Connected", "Not Calendar Connected")

        try:
            data = {
                'summary': 'Google I/O 2015',
                'location': '800 Howard St., San Francisco, CA 94103',
                'description': 'A chance to hear more about Google\'s developer products.',
                'start': {
                    'dateTime': '2023-02-07T09:00:00-07:00',
                    'timeZone': 'Asia/Hong_Kong',
                },
                'end': {
                    'dateTime': '2023-02-07T17:00:00-07:00',
                    'timeZone': 'Asia/Hong_Kong',
                },
                'recurrence': [
                    'RRULE:FREQ=DAILY;COUNT=2'
                ],
                'attendees': [
                    {'email': 'cbgreywolfcb@gmail.com'}
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 10},
                    ],
                },
            }
            PyCa.createEvent(calendarId='primary', event=data)
        except:
            self.assertEqual("Event Created", "Failed to Create Event")

    def test_register_and_login(self):
        PyMo = None
        try:
            PyMo = pm("mongodb+srv://tolosaAdmin:admin@tolosacluster.pavbu95.mongodb.net/?retryWrites=true&w=majority",
                      'TolosaCluster', 'Tests')
        except:
            self.assertEqual("Connected", "Not Connected")

        data = {'username': 'test', 'password': 'test'}
        try:
            PyMo.insert(data)
        except:
            self.assertEqual("Registered", "Not Registered")
        try:
            PyMo.find(data)
        except:
            self.assertEqual("Logged In", "Not Logged In")
        try:
            PyMo.delete(data)
        except:
            self.assertEqual("Deleted", "Not Deleted")

    def test_insertion(self):
        PyMo = None
        try:
            PyMo = pm("mongodb+srv://tolosaAdmin:admin@tolosacluster.pavbu95.mongodb.net/?retryWrites=true&w=majority",
                      'tolosa_website', 'Tests')
        except:
            self.assertEqual("Connected", "Not Connected")

        data = {

        }

        keyNumber = 0
        for i in range(0, 100):
            newStr = "Test" + str(i)
            data[newStr] = {'username': 'test', 'password': 'test'}

        try:
            for i in range(0, 100):
                PyMo.insert(data["Test" + str(i)])
        except:
            self.assertEqual("Inserted", "Failed to Insert")
        try:
            for i in range(0, 100):
                try:
                    PyMo.delete(data["Test" + str(i)])
                except:
                    self.assertEqual("Deleted", "Not Deleted")
        except:
            self.assertEqual("Deleted", "Not Deleted")