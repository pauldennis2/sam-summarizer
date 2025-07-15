# SAM Summarizer

This project uses a pre-trained BART model to summarize dialogs in the SAMSum dataset. The EDA is in `eda.ipynb` and the main logic is in `bart_gpu500.ipynb`.

## Project Discussion

I succeeded in using a pre-trained BART based model to create conversation summaries for the SAMSum data. My model achieved a top ROUGE-1 score of 63.5%, indicating substantial overlap with the target summaries. I spent substantial time exploring the BERT/BART option which was suggested by the course, as well as exploring T5 and BERT/gpt2. BART emerged as the best option as it is already trained to work in an encoder/decoder situation.

A substantial challenge was identifying that using a BERT encoder and a non-BERT decoder was not the right solution. This seems to be an example of "in theory it can work; in practice it's a lot of headaches for no clear gain."

My model also maintained its performance well on data it wasn't trained on (I used the validation set for this). I'm happy to have mostly avoided the overfitting problem.

Opportunities for Growth/Improvement

If I were starting this project over from scratch, the main thing I would do differently is to leverage Google Colab from the beginning. I did explore this option, but it was nearer to the end of the project, and I struggled to port my working local solution into this environment. If I were attempting a similar project for professional use, I would want to start right away on a cloud platform such as GCP/AWS in order to leverage scaling cloud resources, storage, and be able to expose an API (this would naturally support deployment).

The most significant challenge was the limitation of compute resources. Locally, I had two bad options: use CPU-only resources, leading to training that would take many hours even for a fraction of the data, or; use GPU, speeding up training but leading to substantial memory issues.

Manual review was also a struggle, so one of the biggest wins would be incorporating some kind of automated review that improves on or complements the ROUGE score. Human review does not scale well.

If I were approaching this from a fresh professional perspective, I would want to have more detailed conversations with stakeholders and users about the value this would bring. For example, does a simple "speaker/topic" breakdown cover the use case? "Speakers: Allen, Bob. Subject: Upcoming soccer match". Training a model for something like this would be less computationally expensive, and more importantly, it would avoid hallucinations and incorrect summaries that might drop important meaning.
