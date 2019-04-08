from flask import Blueprint, jsonify, request
from lib import db
import json

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_video():
    try:
        # insert data
        tch_id = request.headers.get('tch_id')
        tch_video_url = request.headers.get('tch_video')
        stu_id = request.headers.get('stu_id')
        stu_video_url = request.headers.get('stu_video')
        
        db.insert_df(tch_id,tch_video_url,stu_id,stu_video_url)

        return jsonify({
            "is_success": True,
            "tch_id": tch_id,
            "stu_id": stu_id
        })
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": "execute query failed",
            "exception": str(e)
        })

@main.route('/health', methods=['GET'])
def get_data():
    return jsonify({
        'is_ok':True
    })