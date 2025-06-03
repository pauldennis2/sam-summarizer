# Save this as `test_text_poc.py` in your project directory

from transformers import pipeline

print("Attempting to load a text generation pipeline...")

try:
    # Using a very small and common model for quick download and minimal footprint
    # 'distilgpt2' is good for simple text generation
    generator = pipeline('text-generation', model='distilgpt2')

    print("Pipeline loaded successfully. Generating text...")

    # Define a simple prompt
    prompt = "The quick brown fox jumps over the lazy"

    # Generate text
    # max_new_tokens controls how many new words/tokens the model will generate
    # num_return_sequences specifies how many different outputs to generate
    results = generator(prompt, max_new_tokens=10, num_return_sequences=1)

    print("\n--- Generation Successful ---")
    print(f"Input: '{prompt}'")
    print(f"Generated text: '{results[0]['generated_text']}'")
    print("\nProof of concept successful: PyTorch and Transformers are working for text generation!")

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"An error occurred during the POC test: {e}")
    print("This indicates a problem with the environment setup or library interaction.")