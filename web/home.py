from flask import Blueprint,render_template
from lib.db import get_conn

home = Blueprint('home',__name__)

@home.route('/table')
def video_table():
    db = get_conn()
    cur = db.cursor()
    cur.execute('select id,tch_id,stu_id,training_start,training_end,current_stage,stu_swapped_url from faceswap')
    data = cur.fetchall()
    cur.close()
    data = list(data)
    table_html = '<tr><th>ID</th><th>TchID</th><th>StuID</th><th>ProcessState</th><th>trainingStart</th><th>trainingEnd</th><th>Button</th></tr>'
    for i in data:
        i = list(i)
        i[-1] = '<a href="' + str(i[-1]) + '" class="videoPlayBtn" style="text-decoration:none;">Play</a>'
        table_html += '<tr><th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5}</th><th>{6}</th></tr>'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    return render_template('memList.html',data = table_html)