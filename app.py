from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# ===== Persistencia en memoria =====

libros = [
    {"id": 1, "titulo": "Harry Potter y la Piedra Filosofal", "precio": 119000},
    {"id": 2, "titulo": "EL SEÑOR de LOS ANILLOS I - LA COMUNIDAD DEL ANILLO", "precio": 43000},
    {"id": 3, "titulo": "Percy Jackson - El Ladrón Del Rayo", "precio": 39000},
    {"id": 4, "titulo": "Libro Las Crónicas De Narnia", "precio": 59000},
    {"id": 5, "titulo": "It", "precio": 47500},
]

carrito = []

# ===== Endpoints =====
#Listar libros disponibles
@app.route('/api/libros', methods=['GET'])
def listar_libros():
    """
    Listar libros disponibles
    ---
    responses:
      200:
        description: Lista de libros
    """
    return jsonify(libros), 200

#Ver carrito
@app.route('/api/carrito', methods=['GET'])
def ver_carrito():
    """
    Ver carrito
    ---
    responses:
      200:
        description: Lista de productos en el carrito
    """
    return jsonify(carrito), 200
    
#Agregar libro al carrito
@app.route('/api/carrito', methods=['POST'])
def agregar_al_carrito():
    """
    Agregar libro al carrito
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
    responses:
      201:
        description: Libro agregado al carrito
      400:
        description: JSON inválido
      404:
        description: Libro no encontrado
    """
    data = request.get_json()

    if not data or "id" not in data:
        return jsonify({"error": "Debes enviar un JSON con 'id'"}), 400

    libro_id = data["id"]
    libro = next((l for l in libros if l["id"] == libro_id), None)

    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    item = next((i for i in carrito if i["id"] == libro_id), None)

    if item:
        item["cantidad"] += 1
    else:
        carrito.append({
            "id": libro["id"],
            "titulo": libro["titulo"],
            "precio": libro["precio"],
            "cantidad": 1
        })

    return jsonify({"mensaje": "Libro agregado", "carrito": carrito}), 201


#Eliminar una unidad del libro del carrito
@app.route('/api/carrito/<int:id>', methods=['DELETE'])
def eliminar_del_carrito(id):
    """
    Eliminar una unidad del libro del carrito
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del libro a eliminar una unidad
    responses:
      200:
        description: Se redujo la cantidad o se eliminó el libro
      404:
        description: Libro no encontrado en el carrito
    """
    item = next((i for i in carrito if i["id"] == id), None)

    if item is None:
        return jsonify({"error": "El libro no está en el carrito"}), 404

    if item["cantidad"] > 1:
        item["cantidad"] -= 1
        mensaje = "Se eliminó una unidad del libro"
    else:
        carrito.remove(item)
        mensaje = "Se eliminó el libro del carrito"

    return jsonify({
        "mensaje": mensaje,
        "carrito": carrito
    }), 200

#Calcular total del carrito
@app.route('/api/carrito/total', methods=['GET'])
def calcular_total():
    """
    Calcular total del carrito
    ---
    responses:
      200:
        description: Total de la compra
    """
    total = sum(i["precio"] * i["cantidad"] for i in carrito)
    return jsonify({"total": total}), 200

if __name__ == '__main__':
    app.run(debug=True)