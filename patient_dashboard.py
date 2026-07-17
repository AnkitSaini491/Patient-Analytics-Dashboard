import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PATIENT DATA
# ==========================================

patient = {

    "Month":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Patients":[
        220,240,260,280,310,330,
        350,370,390,420,440,470
    ],

    "Recovered":[
        180,195,215,235,260,280,
        300,320,340,365,390,420
    ],

    "Critical":[
        18,20,22,24,23,25,
        26,28,29,30,32,35
    ],

    "Admitted":[
        45,50,55,60,65,68,
        72,75,80,85,90,95
    ],

    "Discharged":[
        160,175,190,210,230,250,
        270,290,310,335,360,390
    ],

    "Doctors":[
        15,15,16,16,17,18,
        18,19,19,20,20,21
    ],

    "Beds":[
        250,250,250,260,260,270,
        270,280,280,290,300,300
    ]
}

df = pd.DataFrame(patient)

# ==========================================
# KPI
# ==========================================

total_patients = df["Patients"].sum()

total_recovered = df["Recovered"].sum()

total_critical = df["Critical"].sum()

total_admitted = df["Admitted"].sum()

total_discharged = df["Discharged"].sum()

avg_beds = df["Beds"].mean()

# ==========================================
# DASHBOARD
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))

fig.patch.set_facecolor("#111111")

fig.suptitle(
    "PATIENT ANALYTICS DASHBOARD",
    fontsize=28,
    color="white",
    fontweight="bold"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
0.02,0.90,
f"Patients\n{total_patients}",
fontsize=14,
bbox=dict(facecolor="#3498db",boxstyle="round,pad=0.8")
)

plt.figtext(
0.18,0.90,
f"Recovered\n{total_recovered}",
fontsize=14,
bbox=dict(facecolor="#2ecc71",boxstyle="round,pad=0.8")
)

plt.figtext(
0.35,0.90,
f"Critical\n{total_critical}",
fontsize=14,
bbox=dict(facecolor="#e74c3c",boxstyle="round,pad=0.8")
)

plt.figtext(
0.52,0.90,
f"Admitted\n{total_admitted}",
fontsize=14,
bbox=dict(facecolor="#9b59b6",boxstyle="round,pad=0.8")
)

plt.figtext(
0.69,0.90,
f"Discharged\n{total_discharged}",
fontsize=14,
bbox=dict(facecolor="#f39c12",boxstyle="round,pad=0.8")
)

plt.figtext(
0.85,0.90,
f"Avg Beds\n{avg_beds:.0f}",
fontsize=14,
bbox=dict(facecolor="#16a085",boxstyle="round,pad=0.8")
)

# ==========================================
# CHART 1
# ==========================================

ax1 = plt.subplot(3,2,1)

ax1.plot(
df["Month"],
df["Patients"],
marker="o",
linewidth=3,
color="cyan"
)

ax1.fill_between(
df["Month"],
df["Patients"],
alpha=0.3,
color="cyan"
)

ax1.set_title("Monthly Patient Visits")

ax1.grid(alpha=0.3)

ax1.set_ylabel("Patients")

