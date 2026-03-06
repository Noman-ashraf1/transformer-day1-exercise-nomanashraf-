# Transformer Day 1 Exercise – Noman Ashraf

## 1. What is Generative AI?

Generative AI refers to a class of artificial intelligence models that can generate new content such as text, images, audio, video, or code based on patterns learned from training data. Instead of simply predicting labels or making classifications like traditional machine learning models, generative models learn the underlying structure of data and produce new outputs that resemble the original data distribution.

Traditional machine learning focuses on prediction tasks such as classification or regression. For example, a model might predict whether an email is spam or not. In contrast, generative AI can create entirely new content such as writing an email, generating an image, or composing music.

Generative AI is typically built using deep learning models such as Transformers, Variational Autoencoders (VAEs), and Generative Adversarial Networks (GANs). Large Language Models (LLMs) like GPT and BERT-based architectures use the Transformer architecture to understand and generate human-like language.

### Real-world Applications

**1. Text Generation**
Tools like ChatGPT generate human-like text for writing, coding, or answering questions.

**2. Image Generation**
Models like DALL·E or Stable Diffusion generate images from text prompts.

**3. Code Generation**
AI assistants such as GitHub Copilot help developers write code automatically.

Generative AI is transforming industries including healthcare, education, software development, and media by enabling machines to create meaningful content.

---

## 2. Self-Attention Explained

Consider the sentence:

**"The cat sat on the mat."**

Self-attention allows each word in the sentence to look at every other word and determine which words are important for understanding its meaning.

### Query (Q), Key (K), and Value (V)

Each word is converted into three vectors:

**Query (Q)**  
Represents what the word is looking for.

**Key (K)**  
Represents what information the word contains.

**Value (V)**  
Represents the actual information passed forward.

The model compares the **Query of one word with the Keys of all other words** to determine relevance.

For example, when processing **"sat"**, the model might attend strongly to **"cat"** because the cat is performing the action.

---

### Why scale by √dₖ?

The dot product between Q and K can grow large when vector dimensions increase. Large values make the softmax function produce extremely small gradients.

Dividing by √dₖ stabilizes the values and keeps the training process stable.

---

### Why apply Softmax?

Softmax converts the attention scores into **probabilities** that sum to 1.

This tells the model how much attention each word should receive.

Example:

| Word | Attention Weight |
|-----|-----|
| The | 0.05 |
| cat | 0.45 |
| sat | 0.30 |
| mat | 0.20 |

---

### What problem does attention solve that RNNs struggled with?

RNNs process sequences sequentially and struggle with **long-range dependencies**. Information from earlier words may fade over time.

Self-attention allows the model to **directly connect any two words regardless of distance**, making it much better at understanding long sentences.

---

## 3. Encoder vs Decoder Comparison

| Component | Encoder | Decoder |
|----------|---------|---------|
| Input | Full input sequence | Previously generated tokens |
| Self Attention | Yes | Yes (Masked) |
| Masking | No masking | Future tokens are masked |
| Cross Attention | No | Yes |
| Purpose | Understand input representation | Generate output sequence |

### Masked Attention

Masked attention prevents the model from seeing future tokens during training.  
For example, when predicting the next word, the decoder cannot look ahead at the correct answer.

---

### Cross-Attention

Cross-attention allows the decoder to focus on relevant parts of the encoder output.

Example:
- Encoder processes the input sentence.
- Decoder attends to encoder outputs while generating translation or text.

---

### When Each is Used

**Encoder**
Used for understanding input text such as classification, embeddings, or sentiment analysis.

**Decoder**
Used for generating sequences such as text generation, translation, and summarization.

---

## 4. Vision Transformers (ViT) – High-Level Explanation

Vision Transformers apply the Transformer architecture, originally designed for language processing, to image data.

### Image Patches

Instead of processing an entire image at once, the image is divided into **small fixed-size patches** (for example 16×16 pixels). Each patch acts like a token in a sentence.

For example:

A 224×224 image with 16×16 patches produces:

196 patches (tokens)

---

### Converting Patches into Tokens

Each image patch is flattened into a vector and then passed through a **linear projection layer** to convert it into an embedding vector.

This embedding works similarly to word embeddings in language models.

---

### Positional Embeddings

Transformers do not inherently understand the order or position of tokens.

To solve this, positional embeddings are added to patch embeddings so the model understands **where each patch appears in the image**.

Without positional information, the model would treat patches as an unordered set.

---

### Difference from CNNs

Convolutional Neural Networks (CNNs) process images using convolution filters that focus on local spatial regions.

Vision Transformers differ in several ways:

| CNN | Vision Transformer |
|----|----|
| Uses convolution filters | Uses self-attention |
| Local receptive field | Global attention |
| Built-in spatial bias | Learns spatial relationships |

Transformers allow every patch to attend to every other patch, enabling **global context understanding** across the entire image.

This makes Vision Transformers powerful for many computer vision tasks including image classification, detection, and segmentation.