from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
cat = pd.read_csv(ROOT / "data" / "category_performance.csv").sort_values("revenue_gbp")
reg = pd.read_csv(ROOT / "data" / "regional_performance.csv")
plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(cat["category"], cat["revenue_gbp"], color="#2563eb")
ax.set_title("Category revenue", loc="left", fontsize=18, weight="bold")
ax.set_xlabel("Revenue (£)")
ax.xaxis.set_major_formatter(lambda x, pos: f"£{x/1000:.0f}k")
for i, value in enumerate(cat["revenue_gbp"]):
    ax.text(value + 600, i, f"£{value:,.2f}", va="center", fontsize=9)
fig.tight_layout(); fig.savefig(ASSETS / "category_revenue.png", dpi=180, bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(cat["units_sold"], cat["revenue_gbp"], s=150, c=cat["revenue_gbp"], cmap="viridis", edgecolor="white", linewidth=1.2)
for _, row in cat.iterrows():
    ax.annotate(row["category"], (row["units_sold"], row["revenue_gbp"]), xytext=(6, 6), textcoords="offset points", fontsize=9)
ax.set_title("Revenue versus customer demand", loc="left", fontsize=18, weight="bold")
ax.set_xlabel("Units sold"); ax.set_ylabel("Revenue (£)")
ax.yaxis.set_major_formatter(lambda x, pos: f"£{x/1000:.0f}k")
fig.tight_layout(); fig.savefig(ASSETS / "category_performance.png", dpi=180, bbox_inches="tight"); plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(reg["region"], reg["revenue_gbp"], color="#0f766e", width=0.5)
ax.set_title("Published regional result", loc="left", fontsize=18, weight="bold")
ax.set_ylabel("Revenue (£)"); ax.yaxis.set_major_formatter(lambda x, pos: f"£{x/1000:.0f}k")
for i, row in reg.iterrows():
    ax.text(i, row["revenue_gbp"] + 1200, f"£{row['revenue_gbp']:,.2f}\n{int(row['units_sold']):,} units", ha="center", fontsize=10)
fig.tight_layout(); fig.savefig(ASSETS / "regional_performance.png", dpi=180, bbox_inches="tight"); plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
for ax, label, value in zip(axes, ["Revenue", "Recorded profit", "Margin"], ["£277,652.03", "£111,065.62", "40%"]):
    ax.set_facecolor("#eff6ff"); ax.text(0.08, 0.58, value, fontsize=19, weight="bold", color="#1d4ed8"); ax.text(0.08, 0.28, label, fontsize=11, color="#334155"); ax.axis("off")
fig.suptitle("Beyond the Shelf — published headline metrics", x=0.03, ha="left", fontsize=16, weight="bold")
fig.tight_layout(); fig.savefig(ASSETS / "kpi_snapshot.png", dpi=180, bbox_inches="tight"); plt.close(fig)
