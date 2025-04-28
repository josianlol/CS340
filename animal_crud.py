# animal_crud.py
# CRUD class for managing the Animal collection in MongoDB

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """
    Handles basic CRUD operations for the 'animals' collection in MongoDB.

    Attributes:
    client: MongoClient instance connected to the database
    collection: MongoDB collection for animal records
    """


    def __init__(self, user, password):
        """
        Initializes MongoDB client and connects to the AAC database and animals collection.
        """
        
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31295
        DB = 'AAC'
        COL = 'animals'

        # Set up the MongoDB client connection
        self.client = MongoClient(f'mongodb://{user}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]


    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """
        Inserts a document into the animals collection.
        
        Returns True if successful, raises Exception if data is empty.
        """
        if data is not None:
            insertSuccess = self.database.animals.insert(data)  
            # data should be dictionary
            # Check insertSuccess for operation
            # if insertSuccess != 0:
            # return False
            # default return
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        """
        Finds document(s) in the collection matching the searchData.
        
        Returns a cursor (MongoDB iterable). If no searchData, returns all documents.
        """
        if searchData:
            # Return only documents that match the searchData
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            # Return all documents excluding the _id field
            data = self.database.animals.find({}, {"_id": False})
        return data

# Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        """
        Updates document(s) in the collection matching searchData.
        
        Applies updateData using $set. Returns the result object.
        """
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": updateData })
        else:
            return "{}"
        # Return the dataset else Let the error flow up
        return result.raw_result

# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        """
        Deletes document(s) from the collection matching deleteData.
        
        Returns the result object.
        """
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # Return the dataset else Let the error flow up
        return result.raw_result
