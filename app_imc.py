from flask import Flask, render_template #Importando o Flask

app_imc = Flask(__name__)

@app_imc.route("/")
def home():
    return render_template("imc.html")

if __name__ == "__main__":
    app_imc.run(debug=True)
