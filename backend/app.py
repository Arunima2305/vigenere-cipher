from flask import Flask, request, jsonify
from flask_cors import CORS
from cipher import vigenere_encrypt, vigenere_decrypt, cryptanalyse_vigenere, textstrip, substitution_encrypt, substitution_decrypt

app = Flask(__name__)
CORS(app)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = textstrip(data['text'])
    password = data.get('password', None)
    dictionary = data.get('dictionary', None)
    
    if password:
        encrypted_text = vigenere_encrypt(text, password)
    elif dictionary:
        encrypted_text = substitution_encrypt(text, dictionary)
    else:
        return jsonify({'error': 'Password or dictionary required'}), 400
    
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = textstrip(data['text'])
    password = data.get('password', None)
    dictionary = data.get('dictionary', None)
    
    if password:
        decrypted_text = vigenere_decrypt(text, password)
    elif dictionary:
        decrypted_text = substitution_decrypt(text, dictionary)
    else:
        return jsonify({'error': 'Password or dictionary required'}), 400
    
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/find_password', methods=['POST'])
def find_password():
    data = request.json
    text = textstrip(data['text'])
    password, decrypted_text = cryptanalyse_vigenere(text)
    return jsonify({'password': password, 'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
