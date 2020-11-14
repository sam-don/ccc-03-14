from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.BookImage import BookImage
from models.Book import Book
from schemas.BookImageSchema import book_image_schema

book_images = Blueprint("book_images", __name__, url_prefix="/books/<int:book_id>/image")

@book_images.route("/", methods=["POST"])
@jwt_required
@verify_user
def book_image_create(book_id, user=None):
    pass

@book_images.route("/<int:id>", methods=["GET"])
@jwt_required
@verify_user
def book_image_show(book_id, id, user=None):
    pass

@book_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def book_image_delete(book_id, id, user=None):
    pass
