from flask_restful import Resource, reqparse
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'}, 404



    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':"sorry my man but the Store: {0} is already stored, pun intended".format(name)}, 400

        data= Store.parser.parse_args()
        store = StoreModel(name)

        try:
            store.save_to_db()

        except:
            return {'return':'An error occurred while creating te store.'}

        return store.json(),201





    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
             store.delete_from_db()

        return {'message':'Store Deleted'}



class StoreList(Resource):
    def get(self):
        return {'message':[x.json() for x in StoreModel.query.all()]}
