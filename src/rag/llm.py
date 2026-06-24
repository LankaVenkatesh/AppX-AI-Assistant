from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

MODEL_NAME = (
    "meta-llama/Llama-3.2-3B-Instruct"
)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto"
)

llm = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

print(
    "Llama Loaded Successfully"
)