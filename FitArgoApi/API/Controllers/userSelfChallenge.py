from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin
from API.selfChallenge import add_self_challenge,get_self_challenge


user_challenge=Blueprint('user_challenge',__name__)

@user_challenge.route('/api/userSelfChallenge/addchallenge/',methods=['GET','POST'])
def user_challenges_handler():
    c_id=request.args.get("cid")
    user_id=request.args.get("id")
    descripition=request.args.get("descripition")
    imageurl=request.args.get("imageurl")
    eventname=request.args.get("eventname")
    steps=request.args.get("steps")
    calories=request.args.get("calories")
    status=add_self_challenge.add_self_challenge_details(c_id,user_id,descripition,imageurl,eventname,steps,calories)
    ## call add challenge method

    return jsonify({"status":status})


@user_challenge.route('/api/userSelfChallenge/getChallenge',methods=['GET','POST'])
def get_challenege_info():
    user_id=request.args.get('user_id')
    response=get_self_challenge.get_self_challenge(user_id)
    return jsonify({'result':response})


# user id, 