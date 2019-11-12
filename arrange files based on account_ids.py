#!/usr/bin/python
import csv
import datetime
import os
import sys
import shutil

file = csv.reader(open('/Users/username/Desktop/file3.csv', 'rb'))
list_of_account_numbers = set()
accounts_in_drive=set()
for i in file:
    list_of_account_numbers.add((i[0]))
files=[]

total_account=list()
path='/Users/username/Desktop/File3-0128/'
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))
for f in files:
    if '/Users/rpendela/Desktop/File3-0128/bbdfmstmt' in f:
        pdf_name = str(f).split('/')[6]
        account_id = str(pdf_name).split('_')[0]
        # if account_id in list_of_account_numbers:
        if not os.path.exists('/Users/username/Desktop/test3' + '/' + account_id):
            os.makedirs('/Users/username/Desktop/test3' + '/' + account_id)
        shutil.copy(f, '/Users/username/Desktop/test3' + '/' + account_id)

import s3tree
s3tree.config.aws_access_key_id = 'access-key'
s3tree.config.aws_secret_access_key = 'secret-key'
tree = s3tree.S3Tree(bucket_name='bucket', path='/')
for obj in tree:
    print (obj)
