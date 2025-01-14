from flask import Blueprint, request, make_response
import logging
from .validators import ClientRegistrationForm
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

client_bp = Blueprint('client', __name__)


# In-memory storage and ID counter
data_store = []
next_id = 1000  # Start ID from 1000

# Registar novo cliente
@client_bp.route('/register_client', methods=['POST'])
def register_client():
    global next_id  
    data = request.get_json()
    form = ClientRegistrationForm(data=data, data_store=data_store)
    
    logger.info(f"register_client request received: {data}")
    try:
        if form.validate():
            time = datetime.now()
            client_data = {
                
                "id": next_id,
                "first_name": data.get('first_name'),
                "other_names": data.get('other_names'),
                "email": data.get('email'),
                "address": data.get('address'),
                "date_created": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            # Increment the ID and add the record to the data store
            next_id += 1
            data_store.append(client_data)
            
            logger.info("register_client request {}".format(
                {
                    "message": "Client registered successfully!",
                    "data": client_data
                }
            ))
            
            return make_response({
                "success": True,
                "message": "Client registered successfully!",
                "data": client_data
            }, 201)
        else:
            logger.error({
                "message": "Validations errors",
                "errors": form.errors,
            })
            return make_response({
                "success": False,
                "message": "Validations errors",
                "errors": form.errors
            }, 409)
    
    except Exception as e:
        logger.error(e, exc_info=True)
        logger.info(f"error {e} occured on register_client api")
        return make_response({
            "message": "An unexpected error occurred. Please try again later!",
            "code": 500
        }, 500)

        
# Get Departamento     
@client_bp.route('/get_all_clients', methods=['GET'])
def get_all_clients():
    
    logger.info(f"get_all_clients request received")
    try:
        
        if len(data_store) == 0:
            logger.info("get_all_clients response: There is no client registred!")
            return make_response({
                "success": False,
                "message": "There is no client registred!",
                "code": 409
            }, 409)
            
            
        logger.info("get_all_clients response {}".format(
            {
                "message": "Clients found!"
            }
        ))
        
        return make_response({
            "success": True,
            "message": "Clients found!",
            "data": data_store,
            "code": 200
        })
    
    except Exception as e:
        logger.error(e, exc_info=True)
        logger.info(f"error {e} occured on get_all_clients api")
        return make_response({
            "message": "An unexpected error occurred. Please try again later!",
            "code": 500
        }, 500)
        

