# Topological Key Folding (TKF) Algorithm

This repository contains the Python implementation of the **Topological Key Folding (TKF)** algorithm, a core component of the **Spatio-temporal Bibliocryptography** framework.

## 📌 Overview
Unlike conventional cryptographic key derivation functions (KDFs) that rely solely on static secrets, TKF derives cryptographic keys based on the physical and topological configuration of a spatial environment (e.g., a library or data center). 

The code simulates a 3D environment, computes persistent homology (Betti numbers) to extract intrinsic topological features, and mixes them with a SHA-256 hash and a Logistic Chaos Map to ensure zero-collision resistance.

## ✨ Features
- **3D Scattered Library Layout Simulation**: Visualizes shelves and access radius in a 3D space.
- **Ground-Up Betti Numbers Computation**: Calculates Betti-0 (connected components) and Betti-1 (cycles/holes).
- **Topological Key Folding Algorithm**: Derives cryptographic keys based on spatial topology.
- **Avalanche Effect & Collision Testing**: Validates the cryptographic strength against secret variations.

## ⚙️ Requirements
- Python 3.8+
- `numpy`
- `matplotlib`
- `hashlib` (built-in)
- `math` (built-in)

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/muhrivai654-bit/Python-code-for-Topological-Key-Folding-TKF-in-spatio-temporal-cryptography.git

   
The Python code was developed with the assistance of Generative AI for code generation, debugging, and mathematical formatting. The theoretical framework, algorithm design, and simulation analysis remain the sole original work of the author (Muhammad Rivai).  
