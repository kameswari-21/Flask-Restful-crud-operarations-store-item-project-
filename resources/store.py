from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message':'Store is not avilable'}

    def post(slef, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with this name is already exsits'}, 400
        
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'}

        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message':'store deleted form db'}

    
class StoreList(Resource):
    def get(self):
        return {'stores':list(map(lambda x:x.json(), StoreModel.query.all()))}

         
