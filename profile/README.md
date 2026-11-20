<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/hero-banner.svg" alt="MorphoNerva: neuromorphic computing for the edge. Event-driven hardware and software that work only when something changes." width="100%">
</p>

<p align="center">
  <img alt="Stage: research and development" src="https://img.shields.io/badge/stage-R%26D-4493f8?style=flat-square">
  <img alt="Focus: neuromorphic computing" src="https://img.shields.io/badge/focus-neuromorphic%20computing-bf3989?style=flat-square">
  <img alt="Approach: hardware/software co-design" src="https://img.shields.io/badge/approach-HW%2FSW%20co--design-6e7681?style=flat-square">
  <img alt="Open to collaborators" src="https://img.shields.io/badge/open%20to-collaborators-2da44e?style=flat-square">
  <img alt="Registered on SAM.gov" src="https://img.shields.io/badge/SAM.gov-registered-6e7681?style=flat-square">
</p>

<p align="center">
  <a href="#mission">Mission</a> ·
  <a href="#what-we-build">What we build</a> ·
  <a href="#why-it-matters">Why it matters</a> ·
  <a href="#current-status">Current status</a> ·
  <a href="#how-to-engage">How to engage</a>
</p>

## Mission

**MorphoNerva, Inc.** is an early-stage engineering R&D company building **neuromorphic, event-driven computing systems** for edge and scientific workloads. Our mission is to make always-on intelligence practical where power, heat and latency are the limits: put the computation next to the sensor, and spend energy only when the world changes.

We design the full stack together: spiking neural network models, the software that builds and verifies them, and the digital hardware they run on. We start with FPGA prototypes and are working toward custom silicon.

> Most sensor data is quiet most of the time. Conventional processors do the same work on every clock tick anyway. Our systems are designed to do work only when something changes.

## What we build

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/platform-dark.svg">
  <img alt="Platform flow: sensor data, spike encoding, spiking model, OmniSim, OmniSDK, FPGA prototype, future custom silicon" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/platform-light.svg" width="100%">
</picture>

| | What it is | Who it is for | Status |
|---|---|---|---|
| **Neuromorphic edge accelerator** | A digital, event-driven neural processing core for always-on sensing, prototyped on FPGA first, with custom silicon as the long-term goal | Product teams building battery-powered, embedded or remote sensing systems | In development |
| **OmniSim** | Simulation and analysis environment for spiking models, built so that what you simulate is what the hardware computes | Researchers and model developers | In development |
| **OmniSDK** | Developer toolkit to import, build and deploy spiking models on MorphoNerva hardware, starting from the open [NIR](https://github.com/neuromorphs/NIR) model format | Application and embedded engineers | In development |

We co-design models and circuits with one goal: **the model we train is the model the hardware computes**, with no hand-off step where accuracy silently changes.

<details>
<summary><b>How spiking neural networks work (a two-minute primer)</b></summary>

<br>

Our designs borrow one idea from biology. A neuron collects inputs from many others, and only when enough arrive does it send a short pulse (a spike) to the next cells. Between spikes it does almost nothing.

<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/photos/neuron-blausen.jpg" alt="Labelled illustration of a biological neuron: dendrites, cell body, axon and synaptic terminals" width="60%">
  <br><sub>A biological neuron. Inputs arrive on the dendrites; the output spike travels down the axon. Illustration: BruceBlaus, <a href="https://commons.wikimedia.org/wiki/File:Blausen_0657_MultipolarNeuron.png">Wikimedia Commons</a>, CC BY 3.0 (resized).</sub>
</p>

Spiking neural networks keep that behaviour in a simplified, digital form. Each model neuron integrates its inputs over time and fires when it crosses a threshold:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/spiking-neuron-dark.svg">
  <img alt="Illustration: a leaky integrate-and-fire neuron's membrane potential rising to threshold, firing a spike, and resetting" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/spiking-neuron-light.svg" width="100%">
</picture>

Across a network, only a small share of neurons is active at any moment. That sparsity is what event-driven hardware is built to exploit:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/sparse-raster-dark.svg">
  <img alt="Synthetic spike raster of 48 neurons showing sparse activity with a burst, and the population activity curve below" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/sparse-raster-light.svg" width="100%">
</picture>

<sub>Both figures are textbook illustrations drawn from synthetic data, not measurements.</sub>

</details>

## Why it matters

Sensors are moving to the edge: on machines, in vehicles, on robots and in remote instruments. Many of them must listen or watch all the time, on a small power budget, far from a data centre.

**Event sensors already work this way.** A conventional camera sends every pixel of every frame. An event camera reports only the pixels that change, as a sparse stream of events:

<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/photos/event-camera-comparison.jpg" alt="Top: conventional video frames of a running cheetah. Bottom: the sparse stream of events an event camera produces for the same scene over time." width="100%">
  <br><sub>Same scene, two sensors: conventional frames (top) and event-camera output (bottom). Image: TimoStoffregen, <a href="https://commons.wikimedia.org/wiki/File:Event_camera_comparison.jpg">Wikimedia Commons</a>, CC BY-SA 4.0 (resized).</sub>
</p>

Clocked processors turn that sparse signal back into dense work. In an event-driven system, energy and work scale with **activity**, not with the clock:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/event-driven-dark.svg">
  <img alt="Illustration: a mostly quiet sensor signal; clocked processing works on every tick, event-driven processing works only when the signal changes" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/event-driven-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/activity-scaling-dark.svg">
  <img alt="Idealized model: clocked work is constant; event-driven work grows with the fraction of active inputs, so sparse inputs avoid most of the work" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/activity-scaling-light.svg" width="100%">
</picture>

The first-order argument is simple. If a fraction *a* of inputs changes per step, clocked work is constant, while event-driven work is roughly *c₀ + a·c₁*. The engineering problem is keeping the fixed overhead *c₀* small and the sparsity real on real data, without giving up accuracy. That is the problem we work on.

### Where it applies

<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/photos/wind-farm-power-county.jpg" alt="Aerial view of wind turbines spread across open farmland with mountains behind" width="80%">
  <br><sub>Remote, always-on assets are a natural fit for low-power monitoring at the sensor. Photo: U.S. Department of Energy, <a href="https://commons.wikimedia.org/wiki/File:Power_County_Wind_Farm_002.jpg">Wikimedia Commons</a>, public domain (resized).</sub>
</p>

| Domain | Example problem |
|---|---|
| 🏭 **Industrial monitoring** | Always-on sound and vibration analysis for machine health |
| 🎙️ **Audio sensing** | Keyword and acoustic event detection on a small power budget |
| 🤖 **Event cameras and robotics** | Reacting to motion with low latency |
| 🔬 **Scientific and harsh-environment sensing** | Instruments where power, heat or bandwidth is constrained |

<details>
<summary><b>Neuromorphic hardware is an established research field</b></summary>

<br>

Brain-inspired chips have been built and studied for years by government, academic and industry programmes. Our work builds on that public research. We focus on making it practical for edge products, with verification and honest benchmarking at the centre.

<p align="center">
  <img src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/photos/darpa-synapse-board.jpg" alt="A research circuit board carrying a four-by-four array of brain-inspired chips" width="65%">
  <br><sub>A 16-chip brain-inspired computing board from DARPA's SyNAPSE programme (2014). Not MorphoNerva hardware. Photo: DARPA, <a href="https://commons.wikimedia.org/wiki/File:DARPA_SyNAPSE_16_Chip_Board.jpg">Wikimedia Commons</a>, public domain (resized).</sub>
</p>

</details>

## Current status

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/roadmap-dark.svg">
  <img alt="Roadmap: research (done), Prototype 0 digital core in design and simulation (now), Prototype 1 measured on FPGA, pilots with design partners, custom silicon" src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/roadmap-light.svg" width="100%">
</picture>

We are building **Prototype 0**: the first digital core, designed and checked in simulation before it goes onto FPGA hardware.

**No performance results are published yet.** Neuromorphic computing has a reputation for big claims, and we would rather show our work. We publish only **Measured** or **Sourced** numbers, and each one says how strong the evidence behind it is:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/evidence-ladder-dark.svg">
  <img alt="Evidence ladder: Target, Estimated, Measured, Externally verified, in order of strength, with Sourced for cited results from others. Target and Estimated work is never published as a number; performance results are published from Measured upward." src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/evidence-ladder-light.svg" width="100%">
</picture>

The first results will appear here once they are measured on our own hardware, with the hardware, workload and power boundary stated.

<details>
<summary><b>How we check our work: from model to board</b></summary>

<br>

Before anything counts, it is checked against a reference model at every step:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/verification-flow-dark.svg">
  <img alt="Verification flow: reference model, hardware design, simulation in two independent tools, gate-level check, formal proofs, FPGA build, board measurement. Every step is compared with the reference model, and a mismatch stops the line." src="https://raw.githubusercontent.com/MorphoNerva-Inc/.github/main/profile/assets/verification-flow-light.svg" width="100%">
</picture>

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
<summary><b>How we report results: evidence labels</b></summary>

<br>

We publish only **Measured** or **Sourced** numbers. The other two labels describe work in progress and never come with a number:

| Label | Meaning |
|---|---|
| **Measured** | Run by us on stated hardware, with workload and power boundary given |
| **Sourced** | Someone else's published result, cited |
| **Estimated** | From a model or simulation; used internally, not published as a number |
| **Target** | A goal, not a result; stated without numbers |

</details>

## How to engage

We are building a small, rigorous team and network. We especially want to hear from:

- **Pilot partners** with an always-on sensing problem where power or latency is the bottleneck
- **Research collaborators** in neuromorphic computing, low-power signal processing, digital design and verification
- **Engineers and students** interested in SNN training, RTL design and verification, FPGA implementation, compilers and runtime software, or power measurement

👉 **[Tell us about your interest](https://github.com/MorphoNerva-Inc/.github/issues/new?template=collaboration.yml)** (a short public form; please don't include confidential details). A company contact address is coming soon.

Our engineering repositories are private while the technology is under development. Public tools, benchmarks and papers will be released here as they reach validation and IP-review milestones. Follow the organization to be notified.

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
<summary><b>New to neuromorphic computing? Good public starting points</b></summary>

<br>

- [*Neuronal Dynamics*](https://neuronaldynamics.epfl.ch/online/index.html), Gerstner, Kistler, Naud and Paninski: a free online textbook on spiking neuron models
- Roy, Jaiswal and Panda, [*Towards spike-based machine intelligence with neuromorphic computing*](https://doi.org/10.1038/s41586-019-1677-2), Nature (2019): an overview of the field
- Eshraghian et al., [*Training Spiking Neural Networks Using Lessons From Deep Learning*](https://arxiv.org/abs/2109.12894): a practical tutorial on training SNNs
- [NIR](https://github.com/neuromorphs/NIR), the Neuromorphic Intermediate Representation: an open format for exchanging spiking models between frameworks and hardware
- [Open Neuromorphic](https://open-neuromorphic.org): a community hub for open neuromorphic research and tools

</details>

---

<sub>© 2026 MorphoNerva, Inc. All rights reserved. Registered US small business (SAM.gov). MorphoNerva figures on this page are diagrams or illustrations based on textbook models and synthetic data, not measured results. Photographs and third-party illustrations are used under their licences; credits are in each caption and in <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/profile/assets/SOURCES.md">image sources</a>. See <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/CONTRIBUTING.md">contributing</a>, <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/CODE_OF_CONDUCT.md">code of conduct</a> and <a href="https://github.com/MorphoNerva-Inc/.github/blob/main/SECURITY.md">security</a>.</sub>
