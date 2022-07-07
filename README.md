
# College Event Portal

This web application will be built using django. Django is a python web framework. Through this system we bring all the college fests and events in a single place.
There are 3 main users in this system. The event coordinators can host events and track participations in their events.
The admin can track all the user activities and make other user as coordinators.
The normal users or participants can view and register for events and track the registered events.




## Features

- User authentication(login & signup)
- View, Create and delete fests and events
- Role based users students and coordinators and admin
- Event register and unregister
- Payment Integration
- Providing email remainders to participants before the event is going to happen
- coordinators get a summary about the participation's and participants in the event.
- participants can track registered events


## Installation

first install virtualenv using pip

```bash
  pip install virtualenv
```

create a virtual environment and activate it

```bash
  virtualenv my_name
  cd my_name
  cd Scripts
  activate
```

install following libraries after activating environment

```bash
  pip install django
  pip install djongo
  pip install pillow
  pip install dnspython
  pip install pytz
```

go to project folder run server
```bash
  python manage.py run server
```


    