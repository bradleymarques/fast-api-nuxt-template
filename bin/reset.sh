#!/bin/bash
rm db.sqlite3
python manage.py migrate
python manage.py seed
