from django.db import connection
cursor = connection.cursor()
cursor.execute("alter table userapp_csreport DROP column t24")