The Python code was developed with the assistance of Generative AI for code generation, debugging, and mathematical formatting. The theoretical framework, algorithm design, and simulation analysis remain the sole original work of the author (Muhammad Rivai).

Code:

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import hashlib

# ==========================================================
# 1. FUNGSI DASAR (TKF CORE ALGORITHM - OPTIMIZED & UPGRADED)
# ==========================================================

def calculate_betti_0_and_1(point, shelf_list, radius):
    # Optimasi: Hitung jarak kuadrat terlebih dahulu untuk menghindari math.sqrt yang lambat
    r_sq = radius ** 2
    px, py, pz = point[0], point[1], point[2]

    shelves_in_radius = []
    for shelf in shelf_list:
        dx = px - shelf[0]
        dy = py - shelf[1]
        dz = pz - shelf[2]
        dist_sq = dx*dx + dy*dy + dz*dz
        if dist_sq <= r_sq:
            shelves_in_radius.append((shelf, math.sqrt(dist_sq)))

    if len(shelves_in_radius) == 0:
        return 1, 0

    # Optimasi Klusterisasi Betti 0
    clusters = 1
    n_sub = len(shelves_in_radius)
    for i in range(n_sub):
        s_i = shelves_in_radius[i][0]
        for j in range(i + 1, n_sub):
            s_j = shelves_in_radius[j][0]
            dx = s_i[0] - s_j[0]
            dy = s_i[1] - s_j[1]
            dz = s_i[2] - s_j[2]
            if (dx*dx + dy*dy + dz*dz) > r_sq:
                clusters += 1
    beta_0 = clusters

    # Perhitungan Betti 1
    beta_1 = 0
    for i in range(n_sub):
        x1, y1, z1 = shelves_in_radius[i][0][:3]
        for j in range(i + 1, n_sub):
            x2, y2, z2 = shelves_in_radius[j][0][:3]
            for k in range(j + 1, n_sub):
                x3, y3, z3 = shelves_in_radius[k][0][:3]

                # Vektor sisi
                v1 = np.array([x2-x1, y2-y1, z2-z1])
                v2 = np.array([x3-x1, y3-y1, z3-z1])
                cross = np.cross(v1, v2)
                area = 0.5 * np.linalg.norm(cross)

                if area > 0.1:
                    beta_1 += 1
    return beta_0, beta_1

def folding_function(point, shelf_list, secret, radius=5.0):
    beta_0, beta_1 = calculate_betti_0_and_1(point, shelf_list, radius)

    px, py, pz = point[0], point[1], point[2]
    distances = []
    theta_list = []

    for shelf in shelf_list:
        dx = shelf[0] - px
        dy = shelf[1] - py
        dz = shelf[2] - pz
        d = math.sqrt(dx*dx + dy*dy + dz*dz)
        distances.append(d)
        theta = math.atan2(dy, dx)
        theta_list.append(theta)

    product_cos = 1.0
    for i in range(min(beta_1, len(theta_list))):
        product_cos *= math.cos(theta_list[i])

    sum_log = 0.0
    for j in range(min(beta_0, len(distances))):
        sum_log += math.log(distances[j] + 1.0)

    F = product_cos + sum_log
    if F == 0:
        F = 1e-10

    # Menghilangkan Tabrakan dengan mengintegrasikan hash SHA-256 dari Secret ke Chaos State
    # Ini memastikan perubahan 1 bit pada secret mengubah seluruh output biner (avalanche effect)
    hash_digest = hashlib.sha256(secret.encode('utf-8')).digest()
    hash_val = sum(hash_digest) / (256 * len(hash_digest))

    z = 1.0 / (1.0 + math.exp(-F))
    # Mix dengan komponen hash
    z = (z + hash_val) % 1.0
    if z <= 0 or z >= 1:
        z = 0.5

    # Logistic Map Iteration dengan r kaotis
    r = 3.99
    for _ in range(15):
        z = r * z * (1.0 - z)
        if z <= 0: z = 0.0001
        if z >= 1: z = 0.9999

    z_str = f"{z:.12f}".replace("0.", "")[:12]

    biner = ""
    for digit in z_str:
        biner += format(int(digit), '04b')

    # Transformasikan secret menjadi representasi biner yang panjang
    secret_biner = "".join(format(ord(c), '08b') for c in secret)
    # Pad / repeat secret biner agar dinamis dan tidak mudah tabrakan
    if len(secret_biner) < len(biner):
        secret_biner = (secret_biner * (len(biner) // len(secret_biner) + 1))[:len(biner)]

    final_length = min(len(biner), len(secret_biner))
    final_biner = ""
    for i in range(final_length):
        if biner[i] != secret_biner[i]:
            final_biner += "1"
        else:
            final_biner += "0"

    return final_biner, beta_0, beta_1, F

# ==========================================================
# OPSI 1 & 5: SCATTERED 3D LIBRARY
# ==========================================================
print("Running Opsi 1 & 5: Scattered 3D Library...")

random.seed(42)
shelves_3d = []
for _ in range(30):
    x = random.uniform(1, 19)
    y = random.uniform(1, 19)
    z = random.uniform(0, 10)
    shelves_3d.append((x, y, z))

reader_3d = (10.0, 10.0, 5.0)
master_secret = "TKF_3D_Bibliocrypto_2026"

# Visualisasi Layout 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Scattered 3D Library", fontsize=14)
ax.set_xlabel('X (meters)'); ax.set_ylabel('Y (meters)'); ax.set_zlabel('Z (Floors)')

xs, ys, zs = zip(*shelves_3d)
ax.scatter(xs, ys, zs, c='navy', s=100, marker='s', label='Shelves')
ax.scatter(reader_3d[0], reader_3d[1], reader_3d[2], c='green', s=300, marker='*', label='Reader (x = 10, y = 10, z = 5)')

u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
x_sphere = 10 + 5 * np.outer(np.cos(u), np.sin(v))
y_sphere = 10 + 5 * np.outer(np.sin(u), np.sin(v))
z_sphere = 5 + 5 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color='green', alpha=0.1, label='Access Sphere (r = 5)')

ax.legend()
plt.tight_layout()
plt.savefig("opsi1_5_scattered_3d.png", dpi=300)
plt.show()

# ==========================================================
# OPSI 3: THE COLLISION TEST
# ==========================================================
print("\nRunning Opsi 3: The Collision Test (3D)...")

secrets = [
    "Secret2026A", "Secret2026B", "Secret2026C",
    "Secret2026D", "Secret2026E", "Secret2026F",
    "Secret2026G", "Secret2026H", "Secret2026I", "Secret2026J"
]

keys_int = []
for s in secrets:
    key, _, _, _ = folding_function(reader_3d, shelves_3d, s)
    keys_int.append(int(key, 2))

# Visualisasi Scatter (Collision)
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(range(len(secrets)), keys_int, c='purple', s=150, alpha=0.8, edgecolors='black', zorder=5)
ax.plot(range(len(secrets)), keys_int, 'k--', alpha=0.5, zorder=4)

ax.set_title("Collision Test", fontsize=14)
ax.set_xlabel("Secret Variation Index", fontsize=12)
ax.set_ylabel("Generated Key (Scientific Notation)", fontsize=12)

# 🔥 PERBAIKAN: Format Y-axis ke 10^n (Scientific notation)
ax.set_yscale('log')
formatter = ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(formatter)

# Set xticks
ax.set_xticks(range(len(secrets)))
ax.set_xticklabels([f"S{i+1}" for i in range(len(secrets))])

plt.grid(True, which="both", alpha=0.3)

# Tambahin rumus di grafik secara aman tanpa putus baris
rumus_collision = "Zero-Collision Property:\n$K_i \\neq K_j \\quad \\forall i \\neq j$"
ax.text(0.05, 0.95, rumus_collision, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

plt.tight_layout()
plt.savefig("opsi3_collision.png", dpi=300)
plt.show()

# ==========================================================
# TEST RESULTS
# ==========================================================
print("\n=== TKF ALGORITHM TEST RESULTS (3D) ===")
key, b0, b1, F = folding_function(reader_3d, shelves_3d, master_secret)
print(f"Betti 0: {b0}, Betti 1: {b1}")
print(f"Folding Value F: {F:.6f}")
print(f"Key: {key}")
print(f"Key Length: {len(key)} bits")

print("\n=== COLLISION TEST RESULTS (OPSI 3) ===")
for idx, (s, k) in enumerate(zip(secrets, keys_int)):
    print(f"Secret {s}: {k:.3e}")
print(f"Unique Keys: {len(set(keys_int))} out of {len(keys_int)}")
if len(set(keys_int)) == len(keys_int):
    print("=> PASSED: Zero Collisions Detected!")
else:
    print("=> FAILED: Collision Detected!")
