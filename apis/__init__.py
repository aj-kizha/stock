from flask_restplus import Api
from .stockoperations import namespace as stock_namespace
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
api = Api(title="STOCK MARKET OPERATIONS", version=1, description="Perform manipulation of stock market operations", authorizations=authorizations)
api.add_namespace(stock_namespace)
