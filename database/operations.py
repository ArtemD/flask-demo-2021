from database import License, Session
from sqlalchemy import or_

def __get_session():
    return Session()

def insert(name, address, postcode, city, date, type, business_id):
    new_row=License(name=name, address=address, postcode=postcode, city=city, license_granting_date=date, 
                    license_type=type, business_id=business_id)
    db = __get_session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id

def search(keyword):
    return __get_session().query(License).filter(or_(
        License.name.ilike(f'%{keyword}%'), 
        License.business_id.ilike(f'%{keyword}%')))

def get():
    return __get_session().query(License).all()