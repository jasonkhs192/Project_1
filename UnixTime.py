from datetime import datetime

def time_convert():
    # utc = datetime.utcnow()
    timestamp = 1604042663
    dt_object = datetime.fromtimestamp(timestamp)
    utc_format = dt_object
    utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
    print(utc)