from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def verificar_portas(host):
    portas = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
    resultados = {}
    for porta in portas:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, porta))
            resultados[porta] = 'ABERTA' if resultado == 0 else 'Fechada'
            sock.close()
        except Exception as e:
            resultados[porta] = f"Erro: {e}"
    return resultados

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = None
    if request.method == "POST":
        host = request.form["host"]
        resultados = verificar_portas(host)
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)

