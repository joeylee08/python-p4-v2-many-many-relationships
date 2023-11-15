#!/usr/bin/env python3
# server/seed.py

import ipdb
import datetime
from app import app
from models import db, Employee, Meeting, Project, Assignment, employee_meetings

with app.app_context():

    db.session.query(employee_meetings).delete()
    db.session.commit()
    # Delete all rows in tables
    Employee.query.delete()
    Meeting.query.delete()
    Project.query.delete()

    # Add employees
    e1 = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
    e2 = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
    e3 = Employee(name="Sasha Hao", hire_date=datetime.datetime(2021, 12, 1))
    e4 = Employee(name="Taylor Jai", hire_date=datetime.datetime(2015, 1, 2))
    m1 = Meeting(topic="Vacation days.", scheduled_time=datetime.datetime(2022, 10, 12), location='Conference Room.')
    m2 = Meeting(topic="Bathroom toilets always overflowing.", scheduled_time=datetime.datetime(2022, 1, 10), location='Conference Room.')
    db.session.add_all([e1, e2, e3, e4])
    db.session.commit()
    # Add meetings to an employee
    e1.meetings.append(m1)
    e1.meetings.append(m2)
    # Add employees to a meeting
    m2.employees.append(e2)
    m2.employees.append(e3)
    m2.employees.append(e4)
    db.session.commit()

    p1 = Project(title="XYZ Project Flask server",  budget=50000)
    p2 = Project(title="XYZ Project React UI", budget=100000)
    db.session.add_all([p1, p2])
    db.session.commit()

    a1 = Assignment(role='Project manager',
                start_date=datetime.datetime(2023, 5, 28),
                end_date=datetime.datetime(2023, 10, 30),
                employee=e1,
                project=p1)
    a2 = Assignment(role='Flask programmer',
                start_date=datetime.datetime(2023, 6, 10),
                end_date=datetime.datetime(2023, 10, 1),
                employee=e2,
                project=p1)
    a3 = Assignment(role='Flask programmer',
                start_date=datetime.datetime(2023, 11, 1),
                end_date=datetime.datetime(2024, 2, 1),
                employee=e2,
                project=p2)

    db.session.add_all([a1, a2, a3])
    db.session.commit()

    ipdb.set_trace()