# Save this as `test_bert_poc.py` (or update your existing file)

from transformers import pipeline

print("Attempting to load a fill-mask pipeline with bert-base-uncased...")

try:
    # Use 'fill-mask' task for BERT models
    # 'bert-base-uncased' is the standard base BERT model
    unmasker = pipeline('fill-mask', model='bert-base-uncased')

    print("Pipeline loaded successfully. Unmasking text...")

    # Define a simple prompt with a mask token ([MASK])
    # BERT will try to fill in this token based on context
    results = unmasker("The capital of France is [MASK].")

    print("\n--- Unmasking Successful ---")
    print(f"Input: 'The capital of France is [MASK].'")
    print(f"Top 5 predictions for [MASK]:")
    for r in results:
        print(f"  - Token: '{r['token_str']}', Score: {r['score']:.4f}")
    print("\nProof of concept successful: BERT and Transformers are working!")

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"An error occurred during the BERT POC test: {e}")
    print("This indicates a problem with the environment setup or library interaction.")