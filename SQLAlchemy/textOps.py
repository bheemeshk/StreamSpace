__author__ = 'bheem'


def sanitize(textStr):
    textStr = [w.replace('.','_') for w in textStr]
    return textStr







#read file into List
def createSQL(fieldNames, tableName):

    str = "CREATE TABLE %s(" %tableName
    for i in fieldNames:
        str += i
        str += ', '
    str += ')'
    str = str.replace(', )',');')
    return str