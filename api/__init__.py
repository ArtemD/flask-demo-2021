from flask import json, jsonify, abort
from werkzeug.wrappers import response
import database
from database.operations import search, get

def __generate_json(results):
    """
    Used to generate valid Flask JSON response from db results 
    
        Parameters:
            results (object): Database results
        
        Returns:
            response (object): Flask response object

    """
    data = []
    line = 0

    for row in results:
        r = [row.name, row.address, row.postcode, row.city, 
            row.license_granting_date, row.license_type, 
            row.business_id]
        data.insert(line, r)
        line+=1
    
    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_json(all=True, search_keyword=None):
    if all==True:
        results = get()
        return __generate_json(results)
    elif search_keyword!=None:
        results = search(search_keyword)
        return __generate_json(results)
    else:
        abort(404)
    