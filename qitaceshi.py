
import pymysql
db = pymysql.connect(host="rm-uf68a17r4vuc8v0oc.mysql.rds.aliyuncs.com", user="uat_ingestion", passwd="(O5WU08JsEc*wVSR6c4y7126*", db="ingestion_uat")
cursor = db.cursor()
sql="""CREATE TABLE autotest (
dl_auto_created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
dl_auto_updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
updated_at datetime(6) DEFAULT NULL);"""
cursor.execute(sql)
cursor.close()
db.commit()
db.close()
