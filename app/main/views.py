from . import main
from ..models import RfidCard
from .. import db
from flask import request,jsonify
@main.route('/rfidcard',methods=['POST'])
def putinfo():
	db.create_all()
	card_id=request.form['card_id']
	user_id=request.form['user_id']
	card_time=request.form['card_time']
	freeze=request.form['freeze']
	rfidcard=RfidCard(card_id=card_id,
						user_id=user_id,
						card_time=card_time,
						freeze=freeze)
	db.session.add(rdifcard)
	db.session.commit()
	return 'post success',200
@main.route('/card',methods=['GET'])
def putinfo():
	Rcard=RfidCard.query.filter_by(card_id=card_id).first()
	return Rcard.user_id,200