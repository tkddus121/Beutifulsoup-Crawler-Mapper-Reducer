execfile('20141549.conf')

from boto.dynamodb2.table import Table
from boto.dynamodb2.exceptions import ItemNotFound
from sys import stdin, stdout

myTable = Table('proj6')  # TABLE NAME HERE

# get item

while True:
    string = stdin.readline().strip()
    if string == "":
        stdout.write('<End Searching>\n')
        break
    try:
       item = myTable.get_item(words=string)
    except ItemNotFound:
        stdout.write("0\n")
        results = None
    else:
        if item != None:
#help(myTable)
            print item['counts']

