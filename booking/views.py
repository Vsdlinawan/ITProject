from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Owned
from .libraries.PyCa.PyCa import PyCa as pc                     # From 'https://github.com/BeepBoopBit/PyCa' [Documentation Provided There]
from .libraries.PyMo.PyMoHandler import PythonToMongo as pm     # From 'https://github.com/ucelery/PyMo' [Make Some Changes To Reduce Complexity]
from .libraries.data import User

# Initializes the PyMo and PyCa for MongoDb and Calendar
PyMo = pm("mongodb+srv://tolosaAdmin:admin@tolosacluster.pavbu95.mongodb.net/?retryWrites=true&w=majority",'TolosaCluster', 'Users')
PyCa = pc()

# Global Variables
current_user = None
User_Data = User()

# ---------- PAGE RENDERERS ----------
def about(request):
    
    # Variables for the HTML page
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    # Render the page with the context
    return render(request, 'about.html', context)
def contact(request):
    
    # Variables for the HTML page
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    # Render the page with the context
    return render(request, 'contact.html', context)
def index(request):
    
    # Variables for the HTML page
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    # Render the page with the context
    return render(request, 'index.html', context)
def profile(request):
    
    if current_user == None:
        return redirect('/')
    
    # Variables for the HTML page
    tempContext = current_user
    tempContext['username'] = tempContext['username'] 
    tempContext['logged_in'] = User_Data.is_logged_in
    context = tempContext
    
    # Render the page with the context
    return render(request, 'profile.html', context)
def service(request):
    
    # Return to the index file if the user is not logged in
    if User_Data.is_logged_in == False:
        return redirect('/')
    
    # Variables for the HTML page
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    # Render the page with the context
    return render(request, 'services.html', context)
def administration(request):
    
    documents = PyMo.find({}, 'document_schedule')
    voters = PyMo.find({}, 'voting_schedule')
    businesses = PyMo.find({}, 'booking_schedules')
    users = PyMo.find({}, 'Users')
    
    
    context = {
        'documents': list(),
        'voters': list(),
        'businesses': list(),
        'users': list()
    }
    
    # Push all the data we got from the database to the context
    for document in documents:
        document['numberIndex'] = str(document['_id'])
        document['index'] = str(document['_id'])
        context['documents'].append(document)
        
    # Push all the data we got from the database to the context
    for voter in voters:
        voter['numberIndex'] = str(voter['_id'])
        voter['index'] = str(voter['_id'])
        context['voters'].append(voter)
        
    for business in businesses:
        business['numberIndex'] = str(business['_id'])
        business['index'] = str(business['_id'])
        context['businesses'].append(business)
        
    for user in users:
        user['numberIndex'] = str(user['_id'])
        user['index'] = str(user['_id'])
        user['password'] = '********'
        context['users'].append(user)
    
    print(context['businesses'])    
    return render(request, 'admin-dashboard.html',  context)

# ---------- END ----------


# ---------- PAGE HANDLERS ----------
@csrf_protect
def handle_signin(request):
    
    # Organize the value of the request
    values = organizeRequestValue(request)
    
    # Assign the latest user to the current_user
    global current_user
    current_user = PyMo.insert(values)
    
    # initialize the context
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    return render(request, 'index.html', context)
@csrf_protect
def handle_login(request):
    
    # Get the values of the dict
    values = request.POST.dict()
    
    # Remove the csrf token
    values.pop('csrfmiddlewaretoken')

    if values['email'] == 'administratorTolosa@gmail.com' and values['password'] == 'admin1234':
        return redirect('/administration')

    # Find the user
    global current_user
    current_user = PyMo.find_one(values)
    print(current_user)
    
    # Check if there exists a user and change the login status
    if(current_user == None):
        User_Data.is_logged_in = False
    else:
        User_Data.is_logged_in = True
    
    # initialize the context
    context = {
        'logged_in': User_Data.is_logged_in
    }
    
    return render(request, 'index.html', context)
def handle_logout(request):
    # Change the login status
    User_Data.is_logged_in = False
    global current_user
    current_user = None
    
    # Return to the index
    return redirect('/')
@csrf_protect
def handle_booking(request):
    
    # Get the global variable
    global current_user
    
    # Organize the value of the request
    values = organizeRequestValue(request)
    
    # Initializes the data to be pushed in the database
    data = {
        'username': current_user['username'],
        'email': current_user['email'],
        'mobile': current_user['mobile'],
        'birthdate': current_user['birthdate'],
        'businessName': values['businessName']
    }
    
    # if the data already exists, return to the index
    if PyMo.find_one(data) != None:
        return redirect('/')
    
    # Else, insert the data
    PyMo.insert(data, 'booking_schedules')
    
    # Return to the index
    return redirect('/')
@csrf_protect
def handle_voting(request):
    
    # Get the global variable
    global current_user
    print(current_user)
    
    # Organize the value of the request
    values = organizeRequestValue(request)
    
    # Initializes the data to be pushed in the database
    data = {
        'username': current_user['username'],
        'email': current_user['email'],
        'mobile': current_user['mobile'],
        'birthdate': current_user['birthdate'],
        'voterDate': values['voterDate'],
        'voterTime': values['voterTime']
    }
    
    # if the data already exists, return to the index
    if PyMo.find_one(data) != None:
        return redirect('/')
    
    # Else, insert the data
    PyMo.insert(data, 'voting_schedule')
    
    # Initializes the Date to adhere to the standard
    date = values['voterDate'] + 'T' + values['voterTime']
    
    # Split the data and time and add 1 hour to the time
    myDateTime = date.split("T")                                        # Split by 'T'
    d,t = myDateTime[0], myDateTime[1].split(':')                       # Split the time by ':'
    endDate = d + "T"+ str(int(t[0]) + 1) + ":" + t[1] + ":00.00Z"      # Add 1 hour to the time
    
    # Prepare the data for the event
    data = {
        'summary': "VOTING SCHEDULE",
        'location': 'Tolosa St, Makati, 1229 Metro Manila, Philippines',
        'description': data['username'] + ": Voting",
        'start': { 
            'dateTime': date + ":00.00Z",
            'timeZone': 'Asia/Hong_Kong',
        },
        'end': {
            'dateTime': endDate,
            'timeZone': 'Asia/Hong_Kong',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            # CHANGE THIS
            {'email': "water@example.com"}
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    
    # Create the Event
    PyCa.createEvent(calendarId='primary', event=data)
    
    return redirect('/')
@csrf_protect
def handle_document(request):
    
    # Get the global variable
    global current_user
    print(current_user)
    
    # Organize the value of the request
    values = organizeRequestValue(request)
    
    # Initializes the data to be pushed in the database
    data = {
        'username': current_user['username'],
        'email': current_user['email'],
        'mobile': current_user['mobile'],
        'birthdate': current_user['birthdate'],
        'documentDate': values['documentDate'],
        'documentTime': values['documentTime'],
    }
    
    # if the data already exists, return to the index
    if PyMo.find_one(data) != None:
        return redirect('/')
    
    # Else, insert the data
    PyMo.insert(data, 'document_schedule')
    
    # Initializes the Date to adhere to the standard
    date = values['documentDate'] + 'T' + values['documentTime']
    
    # Split the data and time and add 1 hour to the time
    myDateTime = date.split("T")                                        # Split by 'T'
    d,t = myDateTime[0], myDateTime[1].split(':')                       # Split the time by ':'
    endDate = d + "T"+ str(int(t[0]) + 1) + ":" + t[1] + ":00.00Z"      # Add 1 hour to the time
    
    # Prepare the data for the event
    data = {
        'summary': "DOCUMENT SCHEDULE",
        'location': 'Tolosa St, Makati, 1229 Metro Manila, Philippines',
        'description': data['username'] + ": Voting",
        'start': { 
            'dateTime': date + ":00.00Z",
            'timeZone': 'Asia/Hong_Kong',
        },
        'end': {
            'dateTime': endDate,
            'timeZone': 'Asia/Hong_Kong',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            # CHANGE THIS
            {'email': "water@example.com"}
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    
    # Create the Event
    PyCa.createEvent(calendarId='primary', event=data)
    
    return redirect('/')

def handle_deletion(request):
    values = organizeRequestValue(request)
    
    type = values['type']
    dict = {}
    dict['username'] = values['username']
    dict['email'] = values['email']
    
    PyMo.delete(dict, type)
    return redirect('/administration')
# ---------- END ----------
    
# ----------- Auxillary Functions -----------

def organizeRequestValue(request):
    # Get the items passed by the form
    values = dict(request.POST.items())
    
    # Remove the CSRF Value
    values.pop('csrfmiddlewaretoken')
    
    return values
# ---------- END ----------