from ..services import ContaProdutoServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_conta_produto', __name__, url_prefix='/api')


@bp.route("/conta_produto", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(ContaProdutoServices.create_conta_produto(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/conta_produto", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(ContaProdutoServices.get_by_id(id))

        return jsonify(ContaProdutoServices.get_all_conta_produtos()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/conta_produto/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(ContaProdutoServices.update_conta_produto(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/conta_produto/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        ContaProdutoServices.delete_conta_produto(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    