import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="12345678", db="test")

cursor = db.cursor()
sql = """insert into em_h5_record (id,name,url,member_id,key1,key2,open_id,page_id,url_param,content_json,
del_flag,creator,creator_id,created_at,updator,updator_id,updated_at,privacy_policy) 
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

for i in range(1000, 10000):
    value = (i, '0325', 'http', '', '', '', 'oghzNwMfzmJJPICngsWvF8aooTuI', 1840, '?app', 'nj', 0, '', '', '2021-03-25 17:15:18', '', '', '2021-05-19 15:03:52', '')
    cursor.execute(sql, value)


cursor.close()
db.commit()
db.close()
