from flask import Flask, render_template_string, request

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Quiz da Fábrica de Açúcar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <div class="card shadow-lg rounded-4">
            <div class="card-body">
                <h1 class="text-center mb-4">🏭Fábrica de Açúcar</h1>

                {% if not nome %}
                    <form method="post" class="text-center">
                        <div class="mb-3">
                            <label class="form-label">Qual é o seu nome?</label>
                            <input type="text" class="form-control" name="nome" required>
                        </div>
                        <button type="submit" class="btn btn-primary btn-lg">Começar</button>
                    </form>

                {% elif not respostas %}
                    <p class="fs-5 text-center">Olá, <b>{{ nome }}</b>! Vamos ver como está seu aprendizado. 🍬</p>
                    <form method="post" class="mt-4">

                        <div class="mb-4">
                            <h5>(1) O mel rico é extraído de qual massa?</h5>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" value="A" required>
                                <label class="form-check-label">A</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" value="B">
                                <label class="form-check-label">B</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" value="C">
                                <label class="form-check-label">C</label>
                            </div>
                        </div>

                        <div class="mb-4">
                            <h5>(2) Pode-se usar mel pobre diluído na massa A?</h5>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" value="SIM" required>
                                <label class="form-check-label">SIM</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" value="NAO">
                                <label class="form-check-label">NÃO</label>
                            </div>
                        </div>

                        <div class="mb-4">
                            <h5>(3) Qual massa está mais bamba?</h5>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" value="A" required>
                                <label class="form-check-label">A = 87.3 brix</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" value="B">
                                <label class="form-check-label">B = 85.4 brix</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" value="C">
                                <label class="form-check-label">C = 89.1 brix</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" value="D">
                                <label class="form-check-label">D = 86.5 brix</label>
                            </div>
                        </div>

                        <input type="hidden" name="nome" value="{{ nome }}">
                        <div class="text-center">
                            <button type="submit" class="btn btn-success btn-lg">Enviar Respostas ✅</button>
                        </div>
                    </form>

                {% else %}
                    <h3 class="text-center mb-4">📊 Resultados para {{ nome }}</h3>
                    <ul class="list-group mb-3">
                        <li class="list-group-item">
                            (1) {{ '✅ Correto' if respostas['q1']=='A' else '❌ Errado' }}
                        </li>
                        <li class="list-group-item">
                            (2) {{ '✅ Correto' if respostas['q2']=='NAO' else '❌ Errado' }}
                        </li>
                        <li class="list-group-item">
                            (3) {{ '✅ Correto' if respostas['q3']=='B' else '❌ Errado' }}
                        </li>
                    </ul>
                    <div class="alert alert-info text-center fs-5">
                        <b>Pontuação final:</b> {{ pontos }} / 30
                    </div>
                    <div class="text-center">
                        <a href="/" class="btn btn-primary">🔄 Refazer Quiz</a>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    nome = None
    respostas = None
    pontos = 0

    if request.method == "POST":
        nome = request.form.get("nome")
        if "q1" in request.form:
            respostas = {
                "q1": request.form.get("q1"),
                "q2": request.form.get("q2"),
                "q3": request.form.get("q3"),
            }
            if respostas["q1"] == "A": pontos += 10
            if respostas["q2"] == "NAO": pontos += 10
            if respostas["q3"] == "B": pontos += 10

    return render_template_string(TEMPLATE, nome=nome, respostas=respostas, pontos=pontos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
