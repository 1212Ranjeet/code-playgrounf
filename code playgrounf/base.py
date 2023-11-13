from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_website', methods=['POST'])
def generate_website():
    prompt = request.form['prompt']

    # Use OpenAI GPT-3 to generate content based on the user prompt
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose an appropriate GPT-3 engine
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )

    generated_content = response['choices'][0]['text']

    return render_template('result.html', generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)
