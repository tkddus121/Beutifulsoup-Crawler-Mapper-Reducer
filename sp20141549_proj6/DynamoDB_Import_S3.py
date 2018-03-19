execfile('20141549.conf')

from boto.dynamodb2.table import Table
from boto.s3.connection import S3Connection

s3 = S3Connection()
bucket = s3.get_bucket('0602kiki')

ngram = Table('proj6')

temp = bucket.list()

for i in temp:
    if 'p5output' in i.key and 'part-' in i.key:
	content = i.get_contents_as_string()
	for line in content.split('\n'):
            if line == "":
                continue
	    words, counts = line.split('\t')
	    ngram.put_item(data={'words':words, 'counts':counts})

