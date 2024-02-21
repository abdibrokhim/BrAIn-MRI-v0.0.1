from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from bson import ObjectId


uri = "mongodb+srv://abdibrokhim:i42uybEpICWl8Rax@brain-mri-data-v1.2qisc99.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['BrAInMRI']
collection = db['patients-records']

def save_data(data):
    """
    Save data to the database.
    """
    data['created_at'] = datetime.now()
    data['updated_at'] = datetime.now()
    data['isApproved'] = False
    data['isValidated'] = True
    data['observed_at'] = datetime.now()
    data['head_doctor_name'] = None
    result = collection.insert_one(data)
    return result.inserted_id

def update_data(record_id, update_fields):
    """
    Update specific fields in a record.
    """
    try:
        update_fields['updated_at'] = datetime.now()
        record_id = ObjectId(record_id) if type(record_id) == str else record_id
        collection.update_one({'_id': record_id}, {'$set': update_fields})
        return retrieve_data(record_id)
    except Exception as e:
        return f"An error occurred: {str(e)}"

def retrieve_data(record_id):
    """
    Retrieve a specific record by its ID.
    """
    try:
        record_id = ObjectId(record_id)
        result = collection.find_one({'_id': record_id})
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

def delete_data(record_id):
    """
    Delete a specific record by its ID.
    """
    try:
        record_id = ObjectId(record_id)
        result = collection.delete_one({'_id': record_id})
        return result.deleted_count
    except Exception as e:
        return f"An error occurred: {str(e)}"

def retrieve_all_data():
    """
    Retrieve all records from the database.
    """
    try:
        results = collection.find()
        return list(results)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def update_approve_field(record_id, name):
    """
    Update the 'isApproved' field for a specific record.
    """
    try:
        record_id = ObjectId(record_id)
        result = collection.update_one({'_id': record_id}, {'$set': {'isApproved': True, 'head_doctor_name': name}})
        return result.modified_count
    except Exception as e:
        return f"An error occurred: {str(e)}"
    


# # Sample usage
# if __name__ == '__main__':
#     # Sample data
#     data = {
#         'full_name': 'John Doe',
#         'b_year': 1985,
#         'observation': 'Multiple sclerosis',
#         'observed_at': datetime.now(),
#         'conclusion': 'Early signs of multiple sclerosis',
#         'radiologist_name': 'Dr. Smith',
#         'head_doctor_name': 'Dr. Johnson',
#         'isValidated': False,
#         'isApproved': False
#     }

#     # Save data
#     record_id = save_data(data)
#     print(f'Data saved with ID: {record_id}')

#     # Update data
    # update_result = update_data("65d1084ce636d676f8e91d0c", {'conclusion': "MRI signs of vascular encephalopathy with the presence of multiple small ischemic foci and atrophy of the frontotemporal areas on both sides."})
    # print(f'Data updated: {update_result} record(s)')

#     # Retrieve data
#     retrieved_data = retrieve_data(record_id)
#     print(f'Retrieved data: {retrieved_data}')

#     # Retrieve all data
    # all_data = retrieve_all_data()
    # print(f'All data: {all_data}')

#     # Update approve field
#     approve_result = update_approve_field(record_id, True)
#     print(f'Approve field updated: {approve_result} record(s)')

#     # Delete data
#     delete_result = delete_data(record_id)
#     print(f'Data deleted: {delete_result} record(s)')

#     # Retrieve all data
#     all_data = retrieve_all_data()
#     print(f'All data: {all_data}')
