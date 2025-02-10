# controller.py
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.products_service import ProductService

product_blueprint = Blueprint('products', __name__)

@product_blueprint.route('/products', methods=['POST', 'PUT'])  # Add PUT to allowed methods
def handle_product():
    if request.method == 'PUT' or request.form.get('_method') == 'PUT':
        data = request.form
        name = data.get('name')
        description = data.get('description')
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
            
        result = ProductService.update_product(name, description)
        if result is None:
            return jsonify({'error': 'Product not found'}), 404
            
        return redirect(url_for('products.index'))
    
    elif request.method == 'POST':
        data = request.form
        name = data.get('name')
        description = data.get('description')
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
            
        ProductService.create_product(name, description)
        return redirect(url_for('products.index'))

@product_blueprint.route('/')
def index():
    return render_template('index.html')