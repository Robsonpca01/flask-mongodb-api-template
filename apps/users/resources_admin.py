# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist

from apps.responses import resp_ok, resp_exception
from apps.messages import MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED

from .models import User
from .schema import UserSchema

import json

class AdminUserPageList(Resource):
    # Lembra-se do page_id criado na rota ele pode ser acessado como parâmetro
    # do metodo get

    def get(self, page_id=1):
        # inicializa o schema podendo conter varios objetos
        schema = UserSchema(many=True)
        # inicializa o page_size sempre com 10
        page_size = 10

        # se enviarmos o page_size como parametro
        if 'page_size' in request.args:
            # verificamos se ele é menor que 1
            if int(request.args.get('page_size')) < 1:
                page_size = 10
            else:
                # fazemos um type cast convertendo para inteiro
                page_size = int(request.args.get('page_size'))

        try:
            # buscamos todos os usuarios da base utilizando o paginate
            users = User.objects().paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception('Users', description=e.__str__())

        except Exception as e:
            return resp_exception('Users', description=e.__str__())



        # fazemos um dump dos objetos pesquisados
        print(users.items[0].pk)
        result = schema.dump(users.items)

        # criamos dados extras a serem respondidos
        extra = {
            'page': users.page,
            'pages': users.pages,
            'total': users.total,
            'params': { 'page_size': page_size }
        }

        return resp_ok('Users', MSG_RESOURCE_FETCHED_PAGINATED.format('usuarios'),
            data=result.data,
            **extra)

class AdminUserResource(Resource):
    def get(self, user_id):
        schema = UserSchema()

        try:
            user = User.objects().get(id=user_id)
        except Exception as e:
            return resp_exception('User', description=e.__str__())

        result = schema.dump(user)

        return resp_ok('User', MSG_RESOURCE_FETCHED.format('usuários'), result.data)