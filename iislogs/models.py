from mongoengine import *
#from py_sfa.settings import MONGODB,MONGODB_HOST,MONGODB_PORT

#connect('test', host='mongodb://localhost/test')
#connect(MONGODB, host = MONGODB_HOST, port = MONGODB_PORT)

class iis_logs(Document):
    requestIP = StringField()
    url = StringField()
    ip = StringField()
    port = IntField()
    timeTaken = FloatField()
    method = StringField()
    user = StringField()
    date = DateTimeField()
    userAgent = StringField()
    responseStatus = IntField()

class hit_stat_key(Document):
    url = StringField()
    year = StringField()
    month = StringField()
    day = StringField()


class hit_stat_result(Document):
    count = IntField()    


class hit_stats(Document):
    id = StringField(primary_key=True)
    value = StringField()