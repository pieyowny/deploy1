from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import json

app = Flask(__name__)

# Load database.json content
def load_db():
    try:
        with open('database.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"pertanyaan_db": {}, "jawaban_db": {}, "progress_db": {}}

# Save to database.json
def save_db(data):
    with open('database.json', 'w') as f:
        json.dump(data, f, indent=4)

# Route for the home page
@app.route('/')
def welcome():
   return render_template('welcome.html')

# Route for the home page after login
@app.route('/home')
def home():
    return render_template('home.html')

# Route to create a new question
@app.route('/buat', methods=['GET', 'POST'])
def buat_pertanyaan():
    if request.method == 'POST':
        pertanyaan = request.form['tanyaInput'].strip()
        if not pertanyaan:
            return "Pertanyaan tidak boleh kosong!", 400

        # Generate unique ID and key for the question
        kode_pertanyaan = random.randint(10000, 99999)
        key_pertanyaan = random.randint(1000000, 9999999)

        db = load_db()
        
        # Store the question in the database
        db['pertanyaan_db'][kode_pertanyaan] = {'tanya': pertanyaan, 'jawaban': []}
        db['jawaban_db'][key_pertanyaan] = {'tanya': pertanyaan, 'jawaban': []}

        save_db(db)
        
        # Redirect to the page to share the question
        return redirect(url_for('share', kode=kode_pertanyaan))

    return render_template('buat_pertanyaan.html')

# Route to share the question link
@app.route('/share/<int:kode>')
def share(kode):
    db = load_db()
    if kode not in db['pertanyaan_db']:
        return "Pertanyaan tidak ditemukan", 404

    question = db['pertanyaan_db'][kode]
    link = f"{request.url_root}jawab/{kode}"

    return render_template('share.html', link=link)

# Route for answering a question
@app.route('/jawab/<int:kode>', methods=['GET', 'POST'])
def jawab(kode):
    db = load_db()
    if kode not in db['pertanyaan_db']:
        return "Pertanyaan tidak ditemukan", 404

    if request.method == 'POST':
        jawaban = request.form['jawabanInput'].strip()
        if not jawaban:
            return "Jawaban tidak boleh kosong!", 400

        # Add the answer to the question in the database
        db['pertanyaan_db'][kode]['jawaban'].append(jawaban)
        save_db(db)
        
        return "Jawaban terkirim!", 200

    question = db['pertanyaan_db'][kode]
    return render_template('jawab.html', question=question)

# Route to view answers to a question
@app.route('/lihatjawaban', methods=['GET', 'POST'])
def lihat_jawaban():
    if request.method == 'POST':
        key = request.form['keyJawaban'].strip()
        db = load_db()
        # Find the corresponding question by key
        question_data = db['jawaban_db'].get(int(key), None)
        if question_data is None:
            return "Key tidak ditemukan!", 404
        return render_template('lihat_jawaban.html', question_data=question_data)

    return render_template('lihat_jawaban.html')

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
