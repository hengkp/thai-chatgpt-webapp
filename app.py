from flask import Flask, render_template, request
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("./results")
model = GPT2LMHeadModel.from_pretrained("./results")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_text = request.form["input_text"]
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_text

if __name__ == "__main__":
    app.run(debug=True)
