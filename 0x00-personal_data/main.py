#!/usr/bin/env python3
"""
Main file
"""
import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter
filter_datum = __import__('filtered_logger').filter_datum
get_db = __import__('filtered_logger').get_db
hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

fields = ["password", "date_of_birth"]
messages = [
    "name=john doe;email=johndoe@example.com;password=supersecret;date_of_birth=01/01/1990;",
    "name=korir julius;email=korirjulius001@gmail.com;password=root;date_of_birth=22/11/1994;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

message = "name=korir julius;email=korirjulius001@gmail.com;ssn=000-123-0000;password=root;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT * FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(hash_password(password))
print(hash_password(password))
print(encrypted_password)
print(is_valid(encrypted_password, password))

