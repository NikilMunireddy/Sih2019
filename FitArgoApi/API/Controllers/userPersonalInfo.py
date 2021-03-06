from flask import Blueprint,request,jsonify
from flask_cors import cross_origin,CORS
from ..UserPersonalInfo import add_user_info,get_user_info


user_personal_details=Blueprint('user_personal_details',__name__)

CORS(user_personal_details)




#'''--------ADD USER-------'''
# NOTE: Use 'POST' beacuse the data that can be encoded in URL is limited

@user_personal_details.route('/api/userPersonalDetails/adduser/',methods=['GET','POST'])
def add_user_personal_details():
    user_id=request.args.get('id')
    fullname=request.args.get('fullname')
    first_name=request.args.get('firstname')
    last_name=request.args.get('lastname')
    email_id=str(request.args.get('email'))
    photo_url=request.args.get('photourl')
    misc=None   # A Json column
    status=add_user_info.add_to_database(user_id,fullname,first_name,last_name,photo_url,misc,email_id)
    return jsonify({'status':status})


#'''-------------GET USER INFO-------------'''
#   returns the entire personal info in tuple

@user_personal_details.route('/api/userPersonalDetails/getUserInfo/<user_id>',methods=['GET','POST'])
def get_user_info_details(user_id):
    result=get_user_info.get_user_information(user_id)
    return jsonify({'result':result})

