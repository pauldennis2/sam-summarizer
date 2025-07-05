# Sam Summarizer Pitch

## Introduction

### Problem

Messaging platforms like Slack and Discord are overflowing with conversation. That’s great for real-time collaboration, but also leads to information overload. Group chats move fast, topics shift, and important details get buried in the noise.

Once you fall behind, catching up isn’t easy. Even skimming can take 15–25 minutes after just a few hours away. In "internal surveys" across enterprise teams, over 40% of users reported missing key updates or action items due to message volume.

This leads to frustration, dropped threads, and users giving up on conversations altogether. When conversations get especially active, some users pull back — reading less, posting less, or avoiding the chat altogether to escape the noise.

Even with threads, tags, or search tools, users still have to dig for the information they care about. That friction adds up. And when people start ignoring chats just to keep their sanity, it breaks the very coordination these platforms are meant to support.

### Impact

Information overload doesn’t just frustrate users — it drives them away. In a recent "internal study", nearly 1 in 3 users reported muting a group channel within the first week of joining due to message fatigue. On average, users who skip conversations return 35% less frequently the following week.

Platforms that don’t help users manage high-volume conversation risk falling behind those that do. Clear, accessible information isn’t just nice to have — it’s a competitive edge.

### Solution

An automated dialogue summarization feature helps users re-engage with long group chats by highlighting the key points. Instead of scrolling through a hundred messages, users can quickly see what decisions were made, what actions were proposed, and whether they missed anything important.

This reduces the effort required to catch up and makes busy channels feel more accessible — especially for users who check in infrequently. These summaries could appear in pinned posts, thread previews, or recap notifications. For premium offerings, they could support smart highlights, daily digests, or admin-generated overviews.

While not a substitute for good communication practices, summarization fills in when structure fails. Proper use of channels, threads, and tagging is still the best way to keep conversations on track — but not everyone uses those tools appropriately. AI-powered recaps can act as a fallback.

### Defining Success

The solution will be evaluated on both qualitative and technical performance metrics. Targets include:

 - Summarization Accuracy: Achieve an average ROUGE score — which measures how well a machine-generated summary matches a human-written one — of 0.45 or higher on the SAMSum test set.
 - Technical Performance: Deliver summaries in under 1.5 seconds per conversation on standard hardware, with GPU acceleration optional but not required.
 - User Feedback: "Positive ratings" from at least 70% of surveyed users regarding usefulness, clarity, and trust in the summaries.

These criteria aim to balance model quality with system responsiveness and user adoption. We’ll refine specific thresholds based on pilot data and platform constraints.

## Process

### Outline

1. Prep the Data: Explore the SAMSum dataset, clean formatting, and split long conversations if needed. Tokenize inputs with speaker-awareness.
2. Use a BERT-based encoder-decoder setup

3. Training & Tuning: Fine-tune with a focus on ROUGE metrics. Apply learning rate scheduling, early stopping, and gradient clipping as needed.

4. Evaluate: Compare generated summaries to reference using ROUGE and a small manual check for edge cases or hallucinations.

5. "Deployment": Build a lightweight API wrapper. Enable on-demand summarization via web or app integrations. Monitor runtime, quality, and user feedback.

### Justification

A BART-based encoder-decoder model works well here because it can understand the structure of conversations and generate natural, concise summaries.

Fine-tuning a pre-trained model means we don’t have to train from scratch — saving time and compute. The model already knows general language patterns; we just adapt it to this specific task.

We will use ROUGE scores to track progress automatically, and manual checks for clarity and accuracy. Human evaluation is especially useful for spotting summaries that sound right but miss the point.

To keep training stable and efficient, we'll use standard approaches like early stopping and learning rate schedules.

### Requirements Alignment

The proposed solution meets most deliverable requirements: it uses the SAMSum dataset, applies a summarization model similar to BERT, and defines both technical and business success metrics.

It directly addresses the core need — helping users make sense of high-volume group conversations — while staying mindful of practical trade-offs like latency, model size, and integration complexity.

By fine-tuning an existing model and focusing on fast, readable summaries, the approach balances quality with speed. Outputs are short, focused, and easy to scan — making them actually useful in real-world messaging workflows.

## Timeline and Scope

### Research and Preparation

Foundational Research Phase (Estimated: 14 hours)

 * Learning transformer architectures — 3 hours. Quick review of encoder-decoder structure and attention.
 * Researching SOTA dialogue summarization — 5 hours. Reviewing recent papers and open-source implementations.
 * Understanding evaluation metrics — 2 hours. Covers ROUGE, BERTScore, and qualitative eval setups.
 * Exploring SAMSum dataset — 4 hours. Analyzing structure, speaker turns, and stylistic features.

### Implementation

Project Development Timeline (Estimated: 36 hours)

Data preprocessing and exploration — 2 hours. Includes cleaning, tokenization, and additional EDA.
Model architecture implementation — 10 hours. Setting up BART with HuggingFace; customizing if needed.
Training setup and optimization — 8 hours. Covers hyperparameter tuning, scheduling, and logging.
Evaluation and analysis — 8 hours. Automated metrics, qualitative review, and failure analysis.
Documentation and reporting — 8 hours. Writing methods, results, and preparing for presentation/demo.

### Iteration

Model refinement will be guided by early evaluation metrics and qualitative review of generated summaries, with special attention to human-sensible summaries. Feedback from project critiques will shape both architectural choices and presentation clarity. If initial results underperform, alternative approaches will be considered.

### Risk Management

Language models are very expensive to train in terms of computation time. As we are limited to one local machine and/or Google Colab, we will examine a combination of:

 - Overnight runs
 - GPU acceleration
 - Reduced sample size for training

Of course there can always be unexpected issues. The schedule proposed allows for some uexpected delays at each step and also provides a degree of "padding" before the final deadlines.

### Final Delivery

We are proposing the following final delivery schedule:

Project critique submission - 7/5/25
Final implementation completion - 7/2/25
Documentation and presentation preparation - 7/3/25
Final submission - 7/3/25