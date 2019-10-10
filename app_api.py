from flask import Flask, request
from flask_restful import Resource, Api
import token
import json


app = Flask(__name__)
api = Api(app)

merchants = [[0,1], [0], [1]]

products = [
    {
     'id': '0',
     'title': 'blusa do imperio',
     'price' : 1990,
     'zipcode': '22200-000',
     'seller': 'joao',
     'thumbnailHd':'https://http2.mlstatic.com/camisa-camiseta-unissex-jogo-pubg-pochinki-is-my-city-D_NQ_NP_771884-MLB30216931397_052019-F.webp',
     'date':'10/10/2019'   
    },
    {
     'id': '1',
     'title': 'blusa do rebelde',
     'price' : 2000,
     'zipcode': '22200-000',
     'seller': 'joao',
     'thumbnailHd':'https://http2.mlstatic.com/camiseta-original-dry-fit-branca-black-skull-exclusivo-D_NQ_NP_976916-MLB31120087364_062019-F.webp',
     'date':'10/10/2019' 
    }
]

#devolve um produto pelo id e também altera e deleta um produto
class Products(Resource):
    def get(self, id):
       try:
           response = products[id]
       except IndexError:
           mensagem = 'Product ID {} not found.'
           response = {'status':'error', 'message':message}
       return response

    def put(self):
        dados = json.loads(request.data)
        products[id] = dados
        return dados

    def delete(self):
        products.pop(id)
        dados = json.loads(request.data)
        return {'status':'sucesso', 'mensagem': 'Registro Excluido'}

class Merchants(Resource):
    def get(self, id):
        prods = []
        for prod in merchants[id]:
            prods.append(products[prod])
        return prods
        

api.add_resource(Products, '/products/<int:id>/')
api.add_resource(Merchants, '/api/v1/merchant/<int:id>/products/')
#api.add_resource(ListaProducts, '/products/')

if __name__ == '__main__':
    app.run(debug=True)