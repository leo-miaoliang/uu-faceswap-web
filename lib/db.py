import pymysql
from flask import current_app as app

def get_conn():
    return pymysql.connect(
        host=app.config.get('HOST'),
        port=app.config.get('PORT'),
        user=app.config.get('USER'),
        password=app.config.get('PASSWORD'),
        db=app.config.get('DB'),
        charset='utf8mb4',
    )

def insert_df(tch_id,tch_video_url,stu_id,stu_video_url):
    sql = 'INSERT INTO faceswap(tch_id,tch_video_url,stu_id,stu_video_url) VALUES ({0},\'{1}\',{2},\'{3}\')'.format(tch_id,tch_video_url,stu_id,stu_video_url)
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()