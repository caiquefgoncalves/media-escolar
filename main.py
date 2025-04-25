from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calcular_media', methods={'POST'})
def calcular_media():
    try:
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])

        media = round((nota1+nota2+nota3)/ 3, 2)

        if media <= 5 or media == 6:
            diagnostico = "Reprovado"
        if media >= 7:
            diagnostico = "Aprovado"

        return render_template('index.html', media=media, diagnostico=diagnostico)
    except Exception as e:
        media = f'Ocorreu um erro inesperado {e}'
        diagnostico = ''
        return render_template('index.html', media=media, diagnostico=diagnostico)
if __name__ == '__main__':
    app.run(debug=True)