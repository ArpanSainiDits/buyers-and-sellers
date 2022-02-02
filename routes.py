from flask_restful import Api

from Services.views import buyerRegister, buyerLogin, sellerRegister, sellerLogin, lendInformation, PropertyQuoteView, SellerInfoView, LandListView, BuyerBuddingView, HighestBidView


def view_routes(app):
    api = Api(app)
    api.add_resource(buyerRegister, '/api/buyerRegister'),
    api.add_resource(buyerLogin, '/api/buyerLogin'),
    api.add_resource(sellerRegister, '/api/sellerRegister'),
    api.add_resource(sellerLogin, '/api/sellerlogin'),
    api.add_resource(lendInformation, '/api/lendInformation'),
    api.add_resource(PropertyQuoteView, '/api/propertyQuote'),
    api.add_resource(SellerInfoView, '/api/sellerInformation'),
    api.add_resource(LandListView, '/api/LandListView'),
    api.add_resource(BuyerBuddingView, '/api/BuyerBuddingView'),
    api.add_resource(HighestBidView, '/api/HighestBidView')

