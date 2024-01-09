from flask import Flask, request, jsonify
# from transformers import pipeline
from services import generate_greeting
# AI generators
from src.services.audio import generate_audio
from src.services.video import generate_video
from src.services.text import generate_text
from src.services.image import generate_image
from src.services.code import generate_code

app = Flask(__name__)
# generator = pipeline("text-generation", model="gpt2")

# -----------------------
@app.route('/')
def hello_world():
    return 'Hello, Dudes!!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Missing parameter \'name\''}), 400
    greeting = generate_greeting(name)
    return jsonify({ 'greeting': greeting })

# -----------------------

@app.route('/generate-audio', methods=['POST'])
def generate_ai_audio():
    try:
        # Get the user's input text from the request
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({'error': 'Prompt missing in request data'}), 400

        prompt = data['prompt']
        result = generate_audio(prompt)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# -----------------------

@app.route('/generate-image', methods=['POST'])
def generate_ai_image():
    try:
        # Get the user's input text from the request
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({'error': 'Prompt missing in request data'}), 400

        prompt = data['prompt']
        result = generate_image(prompt)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# -----------------------

@app.route('/generate-text', methods=['POST'])
def generate_ai_text():
    try:
        # Get the user's input text from the request
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({'error': 'Prompt missing in request data'}), 400

        prompt = data['prompt']
        result = generate_text(prompt)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# -----------------------

@app.route('/generate-code', methods=['POST'])
def generate_ai_code():
    try:
        # Get the user's input text from the request
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({'error': 'Prompt missing in request data'}), 400

        prompt = data['prompt']
        result = generate_code(prompt)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# -----------------------

@app.route('/generate-video', methods=['POST'])
def generate_ai_video():
    try:
        # Get the user's input text from the request
        data = request.get_json()
        if 'prompt' not in data:
            return jsonify({'error': 'Prompt missing in request data'}), 400

        prompt = data['prompt']
        result = generate_video(prompt)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# -----------------------


if __name__ == '__main__':
    try:
        app.run(port=8008, debug=True)
        # app.run()
    except KeyboardInterrupt:
        # Handle a KeyboardInterrupt (Ctrl+C) gracefully
        pass