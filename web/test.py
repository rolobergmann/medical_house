import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.conf import settings

DATABASES = settings.DATABASES
default_db = DATABASES['default']

import psycopg2

conn = psycopg2.connect(**default_db)
cursor = conn.cursor()
cursor.execute("SELECT 1")
result = cursor.fetchone()
print(result)

cursor.close()
conn.close()
