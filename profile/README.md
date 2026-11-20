<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/banner.svg" alt="MorphoNerva: event-driven computing, engineered for efficiency" width="100%">
</p>

<p align="center">
  <img alt="Stage: research and development" src="https://img.shields.io/badge/stage-R%26D-4493f8?style=flat-square">
  <img alt="Focus: neuromorphic computing" src="https://img.shields.io/badge/focus-neuromorphic%20computing-bf3989?style=flat-square">
  <img alt="Approach: hardware/software co-design" src="https://img.shields.io/badge/approach-HW%2FSW%20co--design-6e7681?style=flat-square">
  <img alt="Open to collaborators" src="https://img.shields.io/badge/open%20to-collaborators-2da44e?style=flat-square">
  <img alt="Registered on SAM.gov" src="https://img.shields.io/badge/SAM.gov-registered-6e7681?style=flat-square">
</p>

<p align="center">
  <a href="#why-event-driven">Why event-driven</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#the-platform">Platform</a> ·
  <a href="#evidence-not-adjectives">Evidence</a> ·
  <a href="#roadmap">Roadmap</a> ·
  <a href="#for-researchers-and-engineers">For researchers</a> ·
  <a href="#work-with-us">Work with us</a>
</p>

**MorphoNerva, Inc.** is an early-stage engineering R&D company building **event-driven, brain-inspired computing systems** for edge and scientific workloads. We design the full stack together: spiking neural network models, the software that builds and verifies them, and the digital hardware they run on. We start with FPGA prototypes and are working toward custom silicon.

> Most sensor data is quiet most of the time. Conventional processors do the same work on every clock tick anyway. Our systems are designed to do work only when something changes.

---

## Why event-driven

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/event-driven-dark.svg">
  <img alt="Illustration: a mostly quiet sensor signal; clocked processing works on every tick, event-driven processing works only when the signal changes" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/event-driven-light.svg" width="100%">
</picture>

In an event-driven system, energy and work scale with **activity**, not with the clock. That matters wherever power, heat or always-on operation is the limit.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/activity-scaling-dark.svg">
  <img alt="Idealized model: clocked work is constant; event-driven work grows with the fraction of active inputs, so sparse inputs avoid most of the work" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/activity-scaling-light.svg" width="100%">
</picture>

The first-order argument is simple. If a fraction *a* of inputs changes per step, clocked work is constant, while event-driven work is roughly *c₀ + a·c₁*. The engineering problem is keeping the fixed overhead *c₀* small and the sparsity real on real data, without giving up accuracy. That is the problem we work on.

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/spiking-neuron-dark.svg">
  <img alt="Illustration: a leaky integrate-and-fire neuron's membrane potential rising to threshold, firing a spike, and resetting" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/spiking-neuron-light.svg" width="100%">
</picture>

Spiking neurons integrate their inputs over time and communicate with sparse, discrete events (spikes). Across a network, only a small share of neurons is active at any moment:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/sparse-raster-dark.svg">
  <img alt="Synthetic spike raster of 48 neurons showing sparse activity with a burst, and the population activity curve below" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/sparse-raster-light.svg" width="100%">
</picture>

We co-design models and circuits with one goal: **the model we train is the model the hardware computes**, with no hand-off step where accuracy silently changes.

## The platform

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/platform-dark.svg">
  <img alt="Platform flow: sensor data, spike encoding, spiking model, OmniSim, OmniSDK, FPGA prototype, future custom silicon" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/platform-light.svg" width="100%">
</picture>

| | What it is | Status |
|---|---|---|
| **OmniSim** | Simulation and analysis environment for spiking models on MorphoNerva hardware | In development |
| **OmniSDK** | Developer toolkit for building and deploying spiking models on MorphoNerva hardware | In development |
| **MorphoNerva cores** | Digital event-driven neural processing cores, prototyped on FPGA first | In development |

## Evidence, not adjectives

Neuromorphic computing has a reputation for big claims. We would rather show our work. We publish only **Measured** or **Sourced** numbers, and each one says how strong the evidence behind it is:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/evidence-ladder-dark.svg">
  <img alt="Evidence ladder: Target, Estimated, Measured, Externally verified, in order of strength, with Sourced for cited results from others. Target and Estimated work is never published as a number; performance results are published from Measured upward." src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/evidence-ladder-light.svg" width="100%">
</picture>

**No performance results are published yet.** The first ones will appear here once they are measured on our own hardware, with the hardware, workload and power boundary stated.

Before anything counts, it is checked against a reference model at every step, from the first model to the board:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/verification-flow-dark.svg">
  <img alt="Verification flow: reference model, hardware design, simulation in two independent tools, gate-level check, formal proofs, FPGA build, board measurement. Every step is compared with the reference model, and a mismatch stops the line." src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/verification-flow-light.svg" width="100%">
</picture>

## Roadmap

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/roadmap-dark.svg">
  <img alt="Roadmap: research (done), Prototype 0 digital core in design and simulation (now), Prototype 1 measured on FPGA, pilots with design partners, custom silicon" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/roadmap-light.svg" width="100%">
</picture>

## Where it applies

| Domain | Example problem |
|---|---|
| 🏭 **Industrial monitoring** | Always-on sound and vibration analysis for machine health |
| 🎙️ **Audio sensing** | Keyword and acoustic event detection at very low power |
| 🤖 **Event cameras and robotics** | Reacting to motion with low latency |
| 🔬 **Scientific and harsh-environment sensing** | Instruments where power, heat or bandwidth is constrained |

## For researchers and engineers

<details>
<summary><b>Research questions we care about</b></summary>

<br>

- How much activity sparsity survives on real sensor data, not just benchmarks, and what does it cost in accuracy?
- Which ways of turning continuous signals into events (encodings) work best for which signals?
- How should training account for the exact arithmetic of low-precision digital hardware?
- How do you verify a neural processor so that simulation and silicon agree on every step?
- When does event-driven hardware beat a well-optimized conventional baseline, and when does it not?

</details>

<details>
<summary><b>How we work: engineering standards</b></summary>

<br>

| Standard | What it means |
|---|---|
| **Pre-registered experiments** | Hypothesis, comparison arms, ≥ 3 random seeds and a kill criterion are written down before a run |
| **Strong baselines** | Every result is compared with a well-tuned conventional model at matched size, not a weak straw man |
| **Model = hardware** | Hardware is verified step by step against a reference model before it counts |
| **Negative results kept** | An experiment that fails is recorded with its reason, and revisited when conditions change |
| **Clean provenance** | Every dataset, dependency and design decision has a recorded source and licence |

</details>

<details>
<summary><b>How we report results</b></summary>

<br>

We publish only **Measured** or **Sourced** numbers. The other two labels describe work in progress and never come with a number:

| Label | Meaning |
|---|---|
| **Measured** | Run by us on stated hardware, with workload and power boundary given |
| **Sourced** | Someone else's published result, cited |
| **Estimated** | From a model or simulation; used internally, not published as a number |
| **Target** | A goal, not a result; stated without numbers |

We publish performance results once they are measured on our own hardware, not before.

</details>

<details>
<summary><b>New to neuromorphic computing? Good public starting points</b></summary>

<br>

- [*Neuronal Dynamics*](https://neuronaldynamics.epfl.ch/online/index.html), Gerstner, Kistler, Naud and Paninski: a free online textbook on spiking neuron models
- Roy, Jaiswal and Panda, [*Towards spike-based machine intelligence with neuromorphic computing*](https://doi.org/10.1038/s41586-019-1677-2), Nature (2019): an overview of the field
- Eshraghian et al., [*Training Spiking Neural Networks Using Lessons From Deep Learning*](https://arxiv.org/abs/2109.12894): a practical tutorial on training SNNs
- [Open Neuromorphic](https://open-neuromorphic.org): a community hub for open neuromorphic research and tools

</details>

## Work with us

We are building a small, rigorous team and network. We especially want to hear from:

- **Pilot partners** with an always-on sensing problem where power or latency is the bottleneck
- **Research collaborators** in neuromorphic computing, low-power signal processing, digital design and verification
- **Engineers and students** interested in SNN training, RTL design and verification, FPGA implementation, compilers and runtime software, or power measurement

👉 **[Tell us about your interest](https://github.com/MorphoNerva-Inc/.github/issues/new?template=collaboration.yml)** (a short public form; please don't include confidential details). A company contact address is coming soon.

Our engineering repositories are private while the technology is under development. Public tools, benchmarks and papers will be released here as they reach validation and IP-review milestones. Follow the organization to be notified.

---

<sub>© 2026 MorphoNerva, Inc. All rights reserved. Registered US small business (SAM.gov). Figures on this page are diagrams or illustrations based on textbook models and synthetic data, not measured results. See <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/CONTRIBUTING.md">contributing</a>, <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/CODE_OF_CONDUCT.md">code of conduct</a> and <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/SECURITY.md">security</a>.</sub>
