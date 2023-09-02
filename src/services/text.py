# chatbot.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf

def generate_text(prompt, max_length=256, model_name="gpt2"):

    # Load the GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Load the GPT-2 model for TensorFlow
    model = TFGPT2LMHeadModel.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id)

    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="tf")
    attention_mask = tf.ones_like(input_ids)

    # Generate text based on the input prompt
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        temperature=0.9,
        top_p=0.7,
        top_k=50,
        do_sample=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    if generated_text.startswith(prompt):
        modified_string = generated_text[len(prompt):]
    else:
        modified_string = generated_text

    return modified_string