from flask import Flask
from flask_restplus import Resource, Api, Namespace, fields, model
from flask_restplus import reqparse
from restplus.createapp import app


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API'
    },
    'oauth2': {
        'type': 'oauth2',
        'flow': 'accessCode',
        'tokenUrl': 'https://somewhere.com/token',
        'authorizationUrl': 'https://somewhere.com/auth',
        'scopes': {
            'read': 'Grant read-only access',
            'write': 'Grant read-write access',
        }
    }
}

#app = Flask(__name__)
api = Api(app, title="STOCK MARKET OPERATIONS", version=1, description="Perform manipulation of stock market operations", authorizations=authorizations)
namespace = Namespace(name="stock_operations", description="returns stock price given an stock name")
api.add_namespace(namespace)


resource_fields = namespace.model('Resource', {
    'stock_name': fields.String
})


stock_price = {'HDFC':1255, 'Manappuram':189}
dict1 = {}


@namespace.route('/stockname', '/stockname/<string:stock_name>')
class Stock(Resource):
    #@namespace.expect(resource_fields)
    @namespace.doc(security='apikey')
    def get(self, stock_name=None):
        '''
        Fetches Stock price given the stockname
        :return:
        '''
        if not stock_name:
            return {'Error': 'Stock Name cannot be Empty'}, 200
        if stock_name in stock_price.keys():
            return {stock_name: stock_price[stock_name]}, 200
        else:
            return {'Error': 'No Such Stock'}, 200

    @namespace.expect(resource_fields)
    def post(self):
        response = self.getdata()
        print("stock name is", response)
        dict1['stockname'] = response.stock_name
        return dict1, 200

    @staticmethod
    def getdata():
        parser = reqparse.RequestParser()
        parser.add_argument('stock_name')
        args = parser.parse_args()
        return args

'''
if __name__ == '__main__':
    app.run(debug=True)
'''