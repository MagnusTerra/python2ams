from flask import Flask, request, jsonify
from funcs.lex import *
from translate import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/translate", methods=['POST'])
def translate():
    data = request.get_json()
    code = data.get('code')
    code_type = data.get('code_type')

    if not code and not code_type:
        return jsonify({
            'error': 'Both atributte are necessary code and code_type'
        }), 400

    result_lex = detect_language(code, code_type)

    if result_lex["status"] :
        try:
            asm_code = tranlate_to_asm(code)
            
            return jsonify({
                'status' : True,
                'code' : asm_code
            }), 200
            
        except Exception as e:
            return jsonify({
                'error' : f"An Error have ocurred: {e}"
            }), 400
    
    else :
        return jsonify({
            'error' : result_lex['content']
        })

if __name__ == "__main__":
    app.run(debug=True, port=3000)