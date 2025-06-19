from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import os
import sqlite3

load_dotenv()

app = Flask(__name__)

CORS(app)


def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS PRODUTOS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                preco FLOAT NOT NULL,
                image_url TEXT NOT NULL
            )
            """
        )


init_db()


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    try:
        data = request.get_json()

        titulo = data.get("titulo")
        descricao = data.get("descricao")
        preco = data.get("preco")
        image_url = data.get("image_url")

        if not titulo or not descricao or not preco or not image_url:
            return jsonify({"error": "Todos os campos devem ser preenchidos"}), 400

        try:
            preco = float(preco)
        except ValueError:
            return jsonify({"error": "Preço precisa ser um valor numérico"}), 400

        with sqlite3.connect("database.db") as conn:
            conn.execute("""
                    INSERT INTO PRODUTOS(titulo, descricao, preco, image_url)
                    VALUES (?, ?, ?, ?)
                    """, (titulo, descricao, preco, image_url))
            conn.commit()
            return jsonify({"message": "Seu produto foi cadastrado com sucesso!",
                            "produto": {
                                "titulo": titulo,
                                "descricao": descricao,
                                "preco": preco,
                                "image_url": image_url
                            }}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao cadastrar produto: {str(e)}"}), 500


@app.route("/", methods=["GET"])
def produtos():
    try:
        with sqlite3.connect("database.db") as conn:
            produtos = conn.execute("SELECT * FROM PRODUTOS").fetchall()

            produtos_formatado = [{"id": p[0], "titulo": p[1], "descricao": p[2],
                                "preco": p[3], "image_url": p[4]} for p in produtos]
            return jsonify(produtos_formatado), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar produtos: {str(e)}"}), 500


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
