[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟦 Probabilistic ML (M13–M14)](4-probabilistic-ml.md) · [🔴 Frontier & Production (M18, M21–M26) →](6-frontier-production.md)

---

# 🟪 DEEP LEARNING STRATUM (Modules 15–17)

**On this page:** [M15: Deep learning foundations](#module-15) · [M16: Transformers and representations](#module-16) · [M17: Reinforcement learning](#module-17)

Choose the module on your route. Its **core outcome and project** define completion; the topic map supplies additional context. Use the [readiness pattern](../guides/readiness-checks.md#how-to-check) to explain, trace, debug and adapt the prerequisite skill before relying on it. Record one next action in the [tracker](../guides/progress-tracker.md#resume).

<details>
<summary>Optional stratum artwork</summary>

<img src="../assets/stratum-5-deep-learning.jpg" alt="Deep learning stratum, modules 15 to 17" width="100%">

</details>

> **Reading this page:** each module lists many resources — that is a menu, not a to-do list. Take **one** primary course; see the [resource defaults](../guides/how-to-read-a-module.md#pick-one). Citations like *"Video 1 (05:05)"* are resolved in [sources](../guides/sources.md#citation-key).

---

<a id="module-15"></a>
## Module 15: Deep Learning Foundations — MLPs, CNNs, Backprop

**Core outcome:** verify a NumPy backward pass, reproduce it with PyTorch autograd and train/evaluate a small MLP/CNN. Principal recommended book: Christopher M. Bishop and Hugh Bishop, **Deep Learning: Foundations and Concepts** (Springer 2024; free author-hosted web edition, paid PDF/print). Prince and fast.ai are complementary alternatives, not extra gates.

- **Do now:** Trace the shapes and derivatives through one affine layer and scalar loss, then check one smooth gradient numerically.
- **Next:** build the [M15 project](#project-15) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** distributed training, custom kernels and architecture surveys; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Derive and check a small network, then reproduce it with autograd. This exposes the connection between a loss, gradients and a working training loop before expensive experiments.

* **Strict Prerequisites:** Module 2 (chain rule), Module 3 (matrix calculus), Module 9 (SGD), Module 10 (logistic regression, cross-entropy loss).

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * Biological motivation vs artificial neuron (McCulloch-Pitts, perceptron), **Multi-Layer Perceptron (MLP)** architecture — affine transformation + activation function; **universal approximation theorem** (Cybenko 1989, Hornik 1991, with proof sketch).
  * **Backpropagation algorithm** — full derivation via chain rule as dynamic programming over the computation graph; vanishing/exploding gradients; **Xavier/Glorot initialisation**, **He initialisation** (theoretical justification for each).
  * **Momentum**, **Nesterov momentum**, **AdaGrad**, **RMSProp**, **Adam**, **AdamW** (decoupled weight decay — 2017 fix), **LAMB** (for large-batch), **Lion** ([Chen et al., 2023](https://arxiv.org/abs/2302.06675)), **Sophia** (2023), learning-rate schedules (step decay, exponential, cosine annealing, warmup, one-cycle), gradient clipping.
  * **L1/L2 penalties and decoupled weight decay**, **Dropout** (Hinton 2014 — inverted dropout, concrete dropout), **Batch Normalisation** (Ioffe-Szegedy 2015 — full derivation, internal covariate shift debate, post-hoc explanations), **Layer Normalisation**, **Group Normalisation**, **Instance Normalisation**, **RMSNorm** (a normalization option used in some LLMs), **early stopping**, **data augmentation**, **label smoothing**, **mixup**, **cutmix**.
  * **Convolutional Neural Networks** — convolution operation (discrete 2D), **kernels as learnable filters**, stride, padding (valid, same, full), pooling (max, average, global), translation equivariance vs invariance; classic architectures: **LeNet-5**, **AlexNet**, **VGG-16/19**, **GoogLeNet/Inception** (1×1 convolutions for dimensionality reduction).
  * Data augmentation for vision, dropout in CNNs, batch-norm placement debate.
  * **Effective receptive field** calculation, dilated/atrous convolutions, **ResNet** (residual connections — identity mapping, full derivation of gradient flow improvement), **DenseNet**, **SqueezeNet**, **MobileNet** (depthwise-separable convolution), **EfficientNet** (compound scaling), **ConvNeXt** (2022 — CNN catches up to ViT).
  * Gradient-based saliency, **Grad-CAM** (Selvaraju 2017), integrated gradients, **SmoothGrad**, adversarial examples (FGSM, PGD, Carlini-Wagner).
  * Second-order methods, L-BFGS, natural gradient, K-FAC.
  * **Semantic segmentation** (FCN, U-Net, DeepLab); **instance segmentation** (Mask R-CNN); **panoptic segmentation**.
  * ImageNet pretraining, **fine-tuning** vs **linear probing** vs **LoRA** (→ M18), feature extraction.
  * Vanilla AEs, denoising AEs, contractive AEs (Jacobian penalty), sparse AEs (KL penalty on activations).
  * "Features & Neural Networks I", "Neural Networks II", "Convolutional Neural Networks" — with extensive labs.
  * **Training and architectures:** SGD, backprop, autodiff, differentiable programming, CNNs, RNNs/LSTMs and a PyTorch tutorial. Read the matching *Foundations of Computer Vision* chapters on neural nets, gradient descent, backprop and CNNs at [visionbook.mit.edu](https://visionbook.mit.edu/).
  * **Optional theory:** universal approximation, Barron's theorem, depth separation, PAC learning, overparameterisation, double descent and inductive biases. These are roadmap extensions, not a claim that one archived lecture covers the entire list.
  * Neural networks in scikit-learn (MLP introduction).
  * Condensed practical treatment.

</details>

* **Courses and references:**
  * **Primary Course Link:** [MIT OCW 6.7960 Deep Learning, Fall 2024](https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/) — public lecture videos, notes, assignments and a PyTorch tutorial; instructors Phillip Isola, Sara Beery and Jeremy Bernstein. [MIT 6.S191](https://introtodeeplearning.com/) supplies a shorter free video companion. The [current 6.7960 schedule](https://deeplearning6-7960.github.io/) is a syllabus update, not a promise of public recordings for its current offering.
  * **Principal reading and further references:**
    * **_Deep Learning: Foundations and Concepts_** — Bishop & Bishop (**Springer 2024**, free online [bishopbook.com](https://www.bishopbook.com/)) — **primary text** for this module.
    * _Understanding Deep Learning_ — Simon J. D. Prince (MIT Press 2023; free online [udlbook.github.io](https://udlbook.github.io/udlbook/)) — chapters 1‑12.
    * _Dive into Deep Learning_ — Zhang, Lipton, Li, Smola — [d2l.ai](https://d2l.ai/) — PyTorch + JAX parallel implementations, continuously updated.
    * _Foundations of Computer Vision_ — Torralba, Isola, Freeman (**MIT Press 2024**, free online at [visionbook.mit.edu](https://visionbook.mit.edu/)) — the official MIT 6.7960 textbook.
    * *Hands‑On Machine Learning with Scikit‑Learn and PyTorch* — Géron (O'Reilly Oct‑Dec 2025).
    * _Deep Learning_ — Goodfellow, Bengio, Courville (2016, still relevant as historical reference).
  * **Practical Implementation:** PyTorch 2.x with a documented compatible Python/device build; CPU float32 is the required baseline. Start with a plain training loop and local JSON/CSV experiment logs. JAX, Accelerate, Lightning and hosted trackers are optional alternatives or later scaling tools.


**PyTorch training contract:** use `nn.Module`, a dataset/loader, explicit device/dtype, `optimizer.zero_grad(set_to_none=True)`, loss/backward/step and reproducible checkpoint state. Distinguish `model.train()` from `model.eval()`; evaluate under `torch.inference_mode()`. Tune and early-stop on validation data, then evaluate the held-out set once.

Implement one small `torch.autograd.Function` and check its analytical backward with [gradcheck](https://docs.pytorch.org/docs/stable/notes/gradcheck.html) in float64 at differentiable inputs; compare with native autograd. Explain why ReLU at zero is not a valid smooth finite-difference fixture. [AMP](https://docs.pytorch.org/docs/stable/amp.html) wraps the forward/loss computation; run backward outside autocast. Use `torch.amp.GradScaler` for the appropriate fp16 path; bf16 commonly needs no scaler. Keep float32 CPU as the fallback and record supported operations.

**Regularization experiment:** L2 penalization and decoupled weight decay are equivalent only for particular optimizer/update conventions; they differ for adaptive optimizers. Compare Adam with an L2 loss penalty and AdamW under matched data, steps and learning-rate budgets; document bias/norm parameter treatment. Compare one constant schedule with one warmup/decay schedule.

**Applied companion:** [fast.ai Practical Deep Learning for Coders](https://course.fast.ai/) provides free lectures and practical examples. Use it alongside the derivation/gradient checks, not as a second mandatory course. Availability of hosted GPU quotas can change; the small local fixture remains the completion route.

* **🚀 Deep Learning Systems — Training at Scale (optional depth):** Modern DL is as much a *systems* discipline as an algorithms discipline. Stanford CS336 dedicates weeks to it.
  * **JAX alongside PyTorch:** [JAX docs](https://docs.jax.dev/), [Flax NNX](https://flax.readthedocs.io/) — an optional alternative stack. Learn `jit`, `vmap`, `scan`, `shard_map`, `jax.Array` with sharding, and the [tour of JAX tutorials](https://docs.jax.dev/en/latest/tutorials.html); check current guidance before using older `pmap` examples.
  * **Mixed-Precision Training:** `torch.amp`, `bfloat16` vs `fp16` vs `fp8` (H100/B200), loss-scaling, stochastic rounding; **bf16 where supported** (wider exponent range than fp16, usually without gradient scaling; performance and operator support depend on hardware).
  * **Gradient Checkpointing:** Trade recomputation for activation memory with `torch.utils.checkpoint` or `jax.checkpoint`. Compare it with smaller batches/sequences, offloading or sharding; checkpointing alone cannot solve every model-memory limit.
  * **Fully-Sharded Data Parallel (FSDP / FSDP2):** [PyTorch FSDP API docs](https://docs.pytorch.org/docs/stable/fsdp.html) ✅ + [Getting-Started-with-FSDP2 tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) ✅. Shard parameters, gradients, and optimiser states across GPUs — an optional scaling technique, selected after measuring memory and communication costs.
  * **Distributed primitives:** DDP, FSDP/FSDP2, Tensor-Parallel (Megatron-style), Pipeline-Parallel (GPipe, PipeDream), **3D parallelism** (DP × TP × PP), ZeRO-1/2/3 (DeepSpeed).
  * **Throughput engineering:** [Triton](https://github.com/triton-lang/triton) ✅ kernels, **FlashAttention-2 / 3** (Tri Dao), **PagedAttention** (vLLM), activation recomputation strategies, `torch.compile` with `fullgraph=True`.
  * **Reading:** [*How to Scale Your Model*](https://jax-ml.github.io/scaling-book/), [PyTorch DTensor docs](https://pytorch.org/docs/stable/distributed.tensor.html), and the scaling/parallelism/systems materials listed in the selected Stanford CS336 offering; lecture numbering can change.

<a id="project-15"></a>
* **📦 Module Project (mandatory) — Backprop from scratch, then a real CNN**
  * **Deliverable:** Two halves. **(a)** A NumPy-only MLP with manual forward and backward passes for at least Linear, ReLU, and Softmax-CE layers, trained on a fixed small MNIST or local digits fixture; report held-out accuracy against a trivial baseline instead of treating a hardware-dependent target as a universal gate. **(b)** The same task in PyTorch, then a small CNN on a documented image subset with augmentation, LR scheduling and your own training loop. Full CIFAR-10 runs are optional; report actual sample count, budget and hardware.
  * **Definition of done:** (1) Compare analytic backward passes with finite differences on smooth float64 fixtures, documenting the step size and absolute/relative tolerances (`1e-5` is a starting tolerance, not a universal bound); add a tiny-batch overfit smoke test with an explicit loss target and step budget; (2) `README.md` with loss/accuracy curves for train and validation, and a confusion matrix; (3) a results memo describing a backward-pass bug you found or deliberately injected and how the check detected it.
  * **Stretch:** Add mixed-precision training and report the throughput and memory difference.
  * **Anti-goal:** Do not start from a tutorial's training loop. The point of the module is that you can write one.

---

<a id="module-16"></a>
## Module 16: Representation Learning, Transformers & Generative Models

**Core outcome:** explain tokenization and causal attention, implement a tiny decoder and evaluate a pretrained representation on a frozen task. Principal reading: Bishop and Bishop on attention/transformers; Alammar and Grootendorst, **Hands-On Large Language Models** (O’Reilly 2024, paid), is the applied book. GAN/diffusion/3D families are optional specialization depth.

- **Do now:** Draw which token positions a causal attention mask permits, then test that a later token cannot affect an earlier output.
- **Next:** build the [M16 project](#project-16) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** diffusion, GANs, 3D vision and large-scale pretraining; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Attention, learned representations and generative objectives explain how a model uses context. Build a tiny causal decoder to connect the equations with testable behavior; then compare modern architectural choices.

* **Strict Prerequisites:** Module 15 core (backprop, a working PyTorch training loop and small-network evaluation). RNNs and attention are developed here; optional M15 architecture surveys are not extra entry gates.

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * n-gram language models, perplexity, statistical LM vs neural LM.
  * RNN forward/backward through time, bidirectional RNNs.
  * LSTM full derivation, GRU comparison, vanishing-gradient resolution.
  * Contextual word embeddings, character-level convolutions, bidirectional LM.
  * **Skip-gram**, **CBOW**, negative sampling, hierarchical softmax, GloVe (global co-occurrence), FastText (subword embeddings).
  * **Encoder-decoder architecture**, **Bahdanau attention** (additive), **Luong attention** (multiplicative), content-based vs location-based attention.
  * **The Transformer** — Vaswani et al. 2017 in full. Scaled dot-product attention (Q, K, V), **multi-head attention**, **positional encoding** (sinusoidal, learned, rotary RoPE, ALiBi, YaRN), encoder stack, decoder stack with masked self-attention, layer norm placement (pre-LN vs post-LN and training trade-offs), feed-forward network (GELU → SwiGLU), residual connections.
  * **BERT** (bidirectional encoder, masked language modelling, next-sentence prediction), **RoBERTa**, **ALBERT**, **DistilBERT**, **ELECTRA** (replaced token detection), **DeBERTa** (disentangled attention).
  * Dedicated lecture on transformer architecture.
  * Three key ideas — **tokens, attention, positional codes**; Transformers as unified framework (subsuming MLPs, GNNs, CNNs); reading = *visionbook.mit.edu/transformers*.
  * **Reconstruction‑based** (autoencoders, VQ-VAE, MAE — Masked Autoencoders); **Similarity‑based / Neural Information Retrieval** — information retrieval, contrastive learning (InfoNCE, hard negatives, KL distillation), sub‑linear search & scaling trade‑offs (cross‑encoders, bi‑encoders, **late interaction / ColBERT**); **Representation Learning and Information Theory** — NN‑GP correspondence, NTK — Neural Tangent Kernel.
  * **Pre‑training** (causal LM loss, SmolLM3, OLMo 2, Marin 8B); **Scaling laws** (Kaplan 2020 + Chinchilla 2022 + Emergent Abilities debate: are emergent abilities a mirage?); **Generative models: basics → VAE & GAN → Diffusion & Flows** (Kaiming He); **Post‑training** (instruction tuning, DPO, GRPO).
  * **Generative Adversarial Networks** — minimax game formulation (Goodfellow 2014), optimal discriminator proof, **mode collapse**, **Wasserstein GAN** (earth-mover distance, Kantorovich-Rubinstein duality), **WGAN-GP** (gradient penalty), **DCGAN**, **Progressive GAN**, **StyleGAN 2/3**, **BigGAN**, **Conditional GAN**, **Pix2Pix**, **CycleGAN** (unpaired translation).
  * Evaluation metrics (IS, FID, KID, precision-recall), tricks (spectral normalisation, self-attention GAN — SAGAN).
  * * **Basics** — density models, energy-based models, Langevin samplers, **autoregressive models** (PixelRNN, PixelCNN, MADE, WaveNet), GANs.
    * **Representation-meets-generation** — **VAEs** (Kingma 2013) with full ELBO derivation, **reparameterisation trick** (ε ~ 𝒩(0,I); z = μ + σε), β-VAE for disentanglement, VQ-VAE, NVAE.
    * **Conditional models** — cGAN, cVAE, conditional diffusion, paired image-to-image (Pix2Pix), text-to-image (DALL-E, Imagen, Stable Diffusion, Midjourney), image-to-text (captioning).
  * **Diffusion Models (DDPM)** — forward noising process, reverse denoising process, **score-matching formulation** (Song & Ermon), **variational diffusion** (Ho et al. 2020), classifier-free guidance, **latent diffusion** (Stable Diffusion), **DPM-Solver / DPM-Solver++** (2022 ODE samplers), **Flow Matching** (2023), **Rectified Flow** (a generative-model family; compare objectives and sampling behavior).
  * **Adversarial robustness** (FGSM, PGD attacks, certified defences), **distribution shift** (covariate shift, label shift, concept drift), **domain adaptation** (DANN, CORAL, MMD), **foundation models** — fine-tuning, **linear probing**, **knowledge distillation**, **prompting**, **parameter-efficient fine-tuning** (PEFT: adapters, LoRA, QLoRA, IA³, prompt tuning, prefix tuning).
  * **Kaplan scaling laws** (2020), **Chinchilla scaling laws** (Hoffmann 2022 — compute-optimal N*D allocation), power-law behaviour, breaking power laws via data pruning, critical batch size.
  * Image classification, object detection (YOLO v8-v10, DETR), segmentation, video understanding, 3D vision, **NeRF** (Neural Radiance Fields), **3D Gaussian Splatting** (optional 3D representation topic).
  * Dedicated course on language modelling (see M18).

</details>

* **Courses and references:**
  * **Primary Course Link:** [MIT OCW 6.7960 Deep Learning, Fall 2024](https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/) — select transformer, representation-learning and generative-model videos. [Stanford CS336 public recordings](https://cs336.stanford.edu/) provide current architecture and language-model systems depth; its full GPU-heavy assignments are not M16 core requirements. [Harvard CS109B 2022](https://harvard-iacs.github.io/2022-CS109B/) supplies archived written materials.
  * **Principal reading and further references:**
    * **Bishop & Bishop — *Deep Learning: Foundations and Concepts*** (Springer 2024, free at [bishopbook.com](https://www.bishopbook.com/)) — chapters on attention and transformers.
    * _Understanding Deep Learning_ — Prince — Chapters 12‑18 (transformers, GANs, VAEs, diffusion).
    * **_Hands‑On Large Language Models_** — Alammar & Grootendorst (O'Reilly, Sep 2024, 428 pp.) — [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models).
    * Vaswani et al. 2017 ("Attention is All You Need") — **mandatory primary‑source reading**.
    * Ho, Jain, Abbeel 2020 ("DDPM") — for diffusion.
    * Lipman et al. 2023 ("Flow Matching") & Liu et al. 2022 ("Rectified Flow") — optional generative-model depth.
    * Radford et al. 2021 ("CLIP") — multi‑modal foundation.
    * _The Little Book of Deep Learning_ — François Fleuret — concise reference.
  * **Practical Implementation:** **Hugging Face Transformers** (pin a release compatible with the selected checkpoint and PyTorch), **Diffusers** for optional image/video work, **PEFT** for optional adapters, **xformers** / **FlashAttention**, **bitsandbytes** (4/8-bit), **`torch.compile(fullgraph=True)`** where supported (measure compile time, runtime and graph breaks; no fixed speedup), **Triton** for optional custom kernels. Pin compatible versions for the selected extension.


**Modern decoder anatomy:** start with causal multi-head attention, then study RoPE, RMSNorm, SwiGLU and [grouped-query attention (GQA)](https://arxiv.org/abs/2305.13245). GQA shares fewer key/value heads across query-head groups; explain the KV-cache trade-off and test head dimensions. These are design choices used by some model families, not requirements of every transformer. Compare one change at a time on the same budget.

**Tokenization and scaling:** implement a small byte-pair-encoding example or inspect a trained tokenizer using [tiktoken](https://github.com/openai/tiktoken). Train a learned tokenizer on training text only; document Unicode/byte behavior, special tokens and context limits. Check encoding/decoding on adversarial strings. Scaling-law fits describe measured regimes; report tokens, parameters and compute rather than extrapolating a tiny run into a frontier-model claim.

<a id="project-16"></a>
* **📦 Module Project (mandatory) — Sentiment analyser on a pretrained model, plus a transformer you built**
  * **Deliverable:** Two halves. **(a)** A sentiment (or topic) classifier built on a pretrained Hugging Face model — fine-tuned or used zero-shot, your choice, but you must justify it — with a proper eval set and error analysis. **(b)** A minimal decoder-only transformer written from scratch (tokeniser → embeddings → multi-head self-attention → residual + layer-norm → LM head) trained on a small licensed corpus with fixed train/validation partitions; compare validation cross-entropy against a unigram baseline. Keep the model tiny enough for a CPU smoke run and report sample quality without promising fluent language.
  * **Definition of done:** (1) `pytest` suite including shape checks for the attention block and a causal-mask test proving that changing any later token cannot change the output at position *t*; (2) `README.md` with the classifier's per-class metrics, a confusion matrix, up to ten inspected misclassifications (all of them if fewer), and either a live URL or exact local/container reproduction command; (3) a results memo on what your from-scratch model's failure modes taught you about the pretrained one.
  * **Stretch:** Compare your fine-tuned classifier against a well-prompted foundation model on the same eval set and report cost, latency, and accuracy — this is the exact trade-off [M21](6-frontier-production.md#module-21) formalises.
  * *Archetype source: video 1 (13:25) — "sentiment analyser on a pretrained Hugging Face model" is named as the accessible NLP portfolio project; the from-scratch half is added so the module still earns its place in the deep-learning stratum.*

---

<a id="module-17"></a>
## Module 17: Reinforcement Learning & Decision Making

**Core outcome:** formulate an MDP, verify Bellman updates, train tabular Q-learning and a tiny DQN, then explain policy gradients/PPO and the DPO distinction. Principal book: Sutton and Barto, **Reinforcement Learning: An Introduction**, second edition (2018; free author PDF and paid print).

- **Do now:** Compute one Bellman update on a two-state MDP and distinguish terminal states from time limits.
- **Next:** build the [M17 project](#project-17) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** continuous control, model-based RL, multi-agent RL and full LLM post-training; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Reinforcement learning studies decisions whose consequences unfold over time. Robotics, games and some LLM post-training methods provide different applications; the right objective and evaluation depend on the setting.

* **Strict Prerequisites:** Module 5 (Markov chains, expectation), Module 15 (can train a deep network).

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * **MDP formulation** — (S, A, P, R, γ), episodic vs continuing tasks, **Bellman equations** (value iteration, policy iteration), **optimality** (Bellman optimality operator, contraction mapping theorem proof), dynamic programming for MDPs.
  * **Model-free RL** — **Monte Carlo methods** (first-visit, every-visit), **Temporal Difference (TD)** learning, **TD(0)**, TD(λ), SARSA, **Q-learning** (off-policy TD control), **Deep Q-Networks (DQN)** (Mnih et al. 2015 — experience replay, target network, Atari), Double DQN, Dueling DQN, Rainbow DQN.
  * Optimising under model uncertainty; **explore-vs-exploit tradeoff**; **credit assignment problem**; two key timescales (state dynamics vs information dynamics) → framework table distinguishing optimisation, MDPs, RL.
  * **Reinforcement Learning 1 & 2**; Applications to **Natural Language Processing** (dialogue systems as RL, text summarisation as RL).
  * Optional RL topic branches:
    * Multi-armed bandits (ε-greedy, UCB, Thompson sampling, contextual bandits — LinUCB, Neural contextual bandits).
    * Policy gradient methods — **REINFORCE** (Williams 1992, log-likelihood trick derivation), **Actor-Critic** (A2C, A3C), **Advantage function**, **GAE** (Generalised Advantage Estimation).
    * **Trust Region methods** — TRPO (Schulman 2015), **PPO** (Schulman 2017 — clipped objective, the RLHF workhorse), **TRPO vs PPO vs ACKTR**.
    * **Deterministic Policy Gradient** (DPG), **DDPG**, **TD3**, **SAC** (Soft Actor-Critic, max-entropy RL).
    * **Model-based RL** — Dyna-Q, **MuZero**, **DreamerV3** (2024), **World models**.
    * **Inverse RL** (IRL), **Imitation Learning** (Behavioural Cloning, DAgger), **GAIL** (Generative Adversarial Imitation Learning).
    * **Offline RL** — BCQ, CQL, IQL, decision transformer.
    * **Hierarchical RL** — options framework, feudal networks, HIRO.
    * **Multi-agent RL** — self-play, fictitious play, MADDPG, AlphaZero, counterfactual regret minimisation.
  * **RLHF challenges**, reward models and **DPO** (Direct Preference Optimization, Rafailov et al., 2023) as direct optimization on preference pairs, **IPO**, **KTO**, **ORPO**, multi-turn RLHF extensions.

</details>

* **Courses and references:**
  * **Primary Course Link:** [David Silver’s free RL lectures, slides and Easy21 assignment](https://www.davidsilver.uk/teaching/). The [IITM Reinforcement Learning course description](https://study.iitm.ac.in/ds/course_pages/BSCS3003.html) is syllabus context, not a verified free lecture route.
  * **Principal reading and further references:**
    * _Reinforcement Learning: An Introduction_ (**2nd Edition, 2018**) — Sutton & Barto — [free PDF](http://incompleteideas.net/book/the-book-2nd.html) — **the canonical text**.
    * _Algorithms for Decision Making_ — Kochenderfer, Wheeler, Wray (MIT Press 2022) — [free online](https://algorithmsbook.com/).
    * _Foundations of Deep Reinforcement Learning_ — Graesser & Keng — for practitioners.
  * **Practical Implementation:** **Gymnasium** (successor to OpenAI Gym), **Stable-Baselines3 2.x**, **CleanRL** (single-file implementations — best for learning), **RLlib** (Ray, for distributed), **PettingZoo** (multi-agent), **trl** (Hugging Face — for RLHF), **DeepMind Acme**, **PufferLib** (2025, unified wrapper).


**Preference-learning bridge:** first derive REINFORCE and the PPO clipped surrogate on a small policy. Then read the [DPO paper](https://arxiv.org/abs/2305.18290): standard DPO learns from chosen/rejected pairs and a reference policy, without fitting a separate reward model or sampling online rollouts during its training loop. Distinguish this from PPO-based RLHF, which uses a learned reward signal and online sampling. Implement the tiny preference-loss calculation and test that swapping the preferred/rejected pair changes the objective as expected; full LLM post-training belongs to M18.

**RL evaluation:** separate training exploration from evaluation, use fixed episode budgets and multiple seeds, compare a random/heuristic policy, and distinguish environment termination from time-limit truncation when bootstrapping value targets. Report failures and variability; learning curves are not guaranteed to improve monotonically.

<a id="project-17"></a>
* **📦 Module Project (mandatory) — Agent that actually learns**
  * **Deliverable:** Tabular Q-learning implemented from scratch on a discrete environment (Taxi, FrozenLake, or a gridworld you define), then DQN on a continuous-observation, discrete-action environment (CartPole; LunarLander optional) with a training loop you wrote. Use at least five seeds as this lab's teaching budget, report mean/spread and held-out evaluation episodes; a single-seed result cannot establish stability across seeds.
  * **Definition of done:** (1) `pytest` suite covering the Bellman update on a hand-computable 2-state MDP, the replay buffer's sampling and eviction, and epsilon decay; (2) `README.md` with the multi-seed learning curves, the full hyperparameter table, and a recorded episode; (3) a results memo describing one instability you observed (divergence, catastrophic forgetting, reward hacking of your own reward function) and what fixed it.
  * **Stretch:** Re-run one experiment with a shaped reward and document how the agent exploited your shaping — the cheapest possible lesson in [M23](6-frontier-production.md#module-23)'s specification-gaming material.

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟦 Probabilistic ML (M13–M14)](4-probabilistic-ml.md) · [🔴 Frontier & Production (M18, M21–M26) →](6-frontier-production.md)
