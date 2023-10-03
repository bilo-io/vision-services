import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

def fine_tune_gpt2():
    # Load pre-trained GPT-2 model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Load and tokenize your training dataset
    dataset = TextDataset(tokenizer=tokenizer, file_path="src/data/scribe.txt", block_size=128)

    # Prepare data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./src/models/gpt2-custom",  # Save fine-tuned model to this directory
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=8,
    )

    # Create Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    # Fine-tune the model
    trainer.train()

    # Save the fine-tuned model
    model_output_dir = "./src/models/gpt2-custom"
    model.save_pretrained(model_output_dir)
    tokenizer.save_pretrained(model_output_dir)

if __name__ == "__main__":
    fine_tune_gpt2()
