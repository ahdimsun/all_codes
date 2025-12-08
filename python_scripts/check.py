import matplotlib.pyplot as plt
import numpy as np

# --- 1. Create Figure with 2 Subplots ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# -------------------------------
# Graph 1: Impact of MGNREGA (Wage Floor)
# -------------------------------

# Labour quantity
L_data = np.linspace(0, 100, 200)

# Demand and Supply functions
def demand(L): return 100 - 0.8 * L
def supply(L): return 20 + 0.8 * L

# Market equilibrium
L_market = 50
W_market = demand(L_market)

# MGNREGA wage floor
W_mgnrega = 80
L_d = 25
L_s = 75

# Plot curves
ax1.plot(L_data, demand(L_data), 'b-', linewidth=2, label='Demand (Private Farms)')
ax1.plot(L_data, supply(L_data), 'g-', linewidth=2, label='Supply of Labour')

# Market equilibrium point
ax1.plot(L_market, W_market, 'ko', markersize=8)
ax1.text(L_market + 2, W_market, f'Market Equilibrium\n($W_{{market}} = {W_market}$)', va='center')

# MGNREGA wage floor line
ax1.axhline(y=W_mgnrega, color='r', linestyle='-', linewidth=3, 
            label=f'MGNREGA Wage ($W_{{MGNREGA}} = {W_mgnrega}$)')

# Q_d and Q_s points and vertical lines
ax1.plot([L_d, L_s], [W_mgnrega, W_mgnrega], 'ro', markersize=8)
ax1.plot([L_d, L_d], [0, W_mgnrega], 'r:', alpha=0.7)
ax1.plot([L_s, L_s], [0, W_mgnrega], 'r:', alpha=0.7)

# Surplus arrow and label
ax1.annotate(
    '', 
    xy=(L_d, W_mgnrega + 5), 
    xytext=(L_s, W_mgnrega + 5), 
    arrowprops=dict(arrowstyle='<->', color='black', lw=2)
)
ax1.text(
    (L_d + L_s) / 2, W_mgnrega + 8, 
    'Surplus of Labour\n(Hired by Govt.)', 
    ha='center', va='bottom', fontsize=11, color='black'
)

# Labels, title, grid
ax1.set_title('Graph 1: Impact of MGNREGA (Wage Floor)', fontsize=16)
ax1.set_xlabel('Quantity of Labour', fontsize=12)
ax1.set_ylabel('Wage Rate ($W$)', fontsize=12)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 120)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend()

# -------------------------------
# Graph 2: Impact of Skill India (Beveridge Curve)
# -------------------------------

# Unemployment rate
U = np.linspace(2, 10, 100)

# Vacancy rates
k1 = 30  # Inefficient curve
V1 = k1 / U

k2 = 15  # Efficient curve
V2 = k2 / U

ax2.plot(U, V1, 'r--', linewidth=2, label='Initial Curve ($BC_1$)\n(High Mismatch)')
ax2.plot(U, V2, 'g-', linewidth=2, label='New Curve ($BC_2$)\n(Improved Mismatch)')

# Title and labels
ax2.set_title('Graph 2: Impact of Skill India (Beveridge Curve)', fontsize=16)
ax2.set_xlabel('Unemployment Rate (%) ($U$)', fontsize=12)
ax2.set_ylabel('Job Vacancy Rate (%) ($V$)', fontsize=12)

# Annotation for inward shift
ax2.annotate(
    'Successful "Skill India" policy\nshifts the curve inwards',
    xy=(4, k2/4),  # point on new curve
    xytext=(5, 6), # text location
    arrowprops=dict(facecolor='green', shrink=0.05, width=2, headwidth=8),
    ha='center', fontsize=12, color='green', weight='bold'
)

# Arrow text (raw string to fix syntax warning)
ax2.text(5.5, 1.5, r'$\longleftarrow$ More Efficient Labour Market', fontsize=11, color='green')

# Limits, grid, legend
ax2.set_xlim(0, 11)
ax2.set_ylim(0, 11)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend()

# -------------------------------
# Finalize and Save
# -------------------------------
plt.tight_layout()
plt.savefig("1.png", dpi=300)
# plt.show()  # Uncomment if running in interactive GUI environment
