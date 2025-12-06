from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    data = request.get_json()
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))
    op = data.get("op")

    # Logika dari kalkulator.py
    if op == "1":
        hasil = a + b
    elif op == "2":
        hasil = a - b
    elif op == "3":
        hasil = a * b
    elif op == "4":
        if b == 0:
            return jsonify({"error": "Tidak bisa membagi dengan nol!"})
        hasil = a / b
    else:
        return jsonify({"error": "Operator tidak valid!"})

    return jsonify({"hasil": hasil})

if __name__ == '__main__':
    app.run(debug=True)
