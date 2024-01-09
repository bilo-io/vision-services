# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

model_path = "t5-small"

def generate_code(prompt, max_length=512, model_name=model_path):
    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate code based on the prompt
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)

    # Decode the generated code
    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_code



#region OLD VERSION with LLAMA

# from transformers import CodeLlamaTokenizer, LlamaForCausalLM

# model_path = "codellama/CodeLlama-7b-Instruct-hf"

# print(f"Starting to load the model {model_path} into memory")

# # Initialize the tokenizer and model
# tokenizer = CodeLlamaTokenizer.from_pretrained(model_path)
# model = LlamaForCausalLM.from_pretrained(model_path)

# def generate_code(prompt, max_length=512, model_name=model_path):
#     # Tokenize the input prompt
#     input_ids = tokenizer.encode(prompt, return_tensors="pt")

#     # Generate code based on the prompt
#     output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)

#     # Decode the generated code
#     generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

#     return generated_code

# # Example usage:
# prompt = "Generate Python code to sort a list"
# generated_code = generate_code(prompt)
# print(generated_code)

#endregion