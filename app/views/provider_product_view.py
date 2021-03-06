from app.custom_errors.fk_not_found import FkNotFoundError
from ..services import ProviderProductServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_provider_product', __name__, url_prefix='/api')


@bp.route("/provider_product", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProviderProductServices.create_provider_product(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except FkNotFoundError as e:
        return e.message


@bp.route("/provider_product", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(ProviderProductServices.get_by_id(id))

        return jsonify(ProviderProductServices.get_all_provider_products()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/provider_product/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProviderProductServices.update_provider_product(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except FkNotFoundError as e:
        return e.message


@bp.route("/provider_product/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        ProviderProductServices.delete_provider_product(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
