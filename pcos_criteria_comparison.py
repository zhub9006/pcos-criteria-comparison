"""
PCOS Diagnostic Criteria Comparison Chart
==========================================
Compares the three major PCOS diagnostic criteria:
  - NIH 1990 (National Institutes of Health)
  - Rotterdam 2003 (ESHRE/ASRM consensus)
  - AES 2006 (Androgen Excess Society)

Generates a presentation-ready comparison chart saved as a PNG image.

Data sourced from:
  - Zawadzki & Dunaif, NIH 1990 working definition
  - Rotterdam ESHRE/ASRM 2003 consensus (Fertility & Sterility)
  - AE-PCOS Society 2006 position statement
  - International Evidence-Based PCOS Guideline 2023 (Teede et al.)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ──────────────────────────────────────────────
# 1. Define the three diagnostic criteria sets
# ──────────────────────────────────────────────

criteria = {
    "NIH 1990": {
        "full_name": "NIH Consensus (1990)",
        "description": "Requires BOTH features\n(excludes other disorders)",
        "Oligo-\nanovulation": "Required",
        "Hyperandro-\ngenism": "Required",
        "Polycystic\nOvaries": "Not Required",
        "Exclude Other\nDisorders": "Required",
    },
    "Rotterdam 2003": {
        "full_name": "Rotterdam / ESHRE-ASRM (2003)",
        "description": "2 of 3 features required\n(excludes other disorders)",
        "Oligo-\nanovulation": "2 of 3\nRequired",
        "Hyperandro-\ngenism": "2 of 3\nRequired",
        "Polycystic\nOvaries": "2 of 3\nRequired",
        "Exclude Other\nDisorders": "Required",
    },
    "AES 2006": {
        "full_name": "Androgen Excess Society (2006)",
        "description": "Hyperandrogenism required +\nat least 1 of the other 2\n(excludes other disorders)",
        "Oligo-\nanovulation": "1 of 2\nRequired",
        "Hyperandro-\ngenism": "Required",
        "Polycystic\nOvaries": "1 of 2\nRequired",
        "Exclude Other\nDisorders": "Required",
    },
}

features = ["Oligo-\nanovulation", "Hyperandro-\ngenism", "Polycystic\nOvaries", "Exclude Other\nDisorders"]
criteria_names = ["NIH 1990", "Rotterdam 2003", "AES 2006"]

# ──────────────────────────────────────────────
# 2. Build the chart
# ──────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor("#FAFBFE")
ax.set_facecolor("#FAFBFE")

# Color scheme — professional medical / academic
HEADER_COLOR = "#1B3A5C"
ROW_COLORS = ["#E8F0FE", "#FFFFFF"]
REQUIRED_COLOR = "#2E7D32"       # deep green
CONDITIONAL_COLOR = "#F57F17"    # amber
NOT_REQUIRED_COLOR = "#C62828"   # deep red
BORDER_COLOR = "#B0BEC5"
TEXT_COLOR = "#263238"

n_features = len(features)
n_criteria = len(criteria_names)

# Table dimensions
col_widths = [0.22] + [0.26] * n_criteria  # feature col + 3 criteria cols
row_height = 0.11
header_height = 0.13
desc_height = 0.09
start_x = 0.02
start_y = 0.92

# ── Draw header row ──
x = start_x
# Feature column header
rect = mpatches.FancyBboxPatch(
    (x, start_y - header_height), col_widths[0], header_height,
    boxstyle="round,pad=0.01", facecolor=HEADER_COLOR, edgecolor="white", linewidth=2
)
ax.add_patch(rect)
ax.text(x + col_widths[0] / 2, start_y - header_height / 2, "Diagnostic\nFeature",
        ha="center", va="center", fontsize=13, fontweight="bold", color="white")
x += col_widths[0]

for ci, cname in enumerate(criteria_names):
    rect = mpatches.FancyBboxPatch(
        (x, start_y - header_height), col_widths[ci + 1], header_height,
        boxstyle="round,pad=0.01", facecolor=HEADER_COLOR, edgecolor="white", linewidth=2
    )
    ax.add_patch(rect)
    ax.text(x + col_widths[ci + 1] / 2, start_y - header_height / 2,
            criteria[cname]["full_name"],
            ha="center", va="center", fontsize=12, fontweight="bold", color="white")
    x += col_widths[ci + 1]

# ── Draw description sub-header ──
y = start_y - header_height
x = start_x + col_widths[0]
for ci, cname in enumerate(criteria_names):
    rect = mpatches.FancyBboxPatch(
        (x, y - desc_height), col_widths[ci + 1], desc_height,
        boxstyle="round,pad=0.005", facecolor="#CFD8DC", edgecolor="white", linewidth=1.5
    )
    ax.add_patch(rect)
    ax.text(x + col_widths[ci + 1] / 2, y - desc_height / 2,
            criteria[cname]["description"],
            ha="center", va="center", fontsize=9, fontstyle="italic", color=TEXT_COLOR)
    x += col_widths[ci + 1]

# ── Draw data rows ──
y = start_y - header_height - desc_height
for fi, feat in enumerate(features):
    bg = ROW_COLORS[fi % 2]
    x = start_x

    # Feature label cell
    rect = mpatches.FancyBboxPatch(
        (x, y - row_height), col_widths[0], row_height,
        boxstyle="round,pad=0.005", facecolor=bg, edgecolor=BORDER_COLOR, linewidth=1.2
    )
    ax.add_patch(rect)
    ax.text(x + col_widths[0] / 2, y - row_height / 2, feat,
            ha="center", va="center", fontsize=11, fontweight="bold", color=TEXT_COLOR)
    x += col_widths[0]

    for ci, cname in enumerate(criteria_names):
        status = criteria[cname][feat]
        # Choose cell color
        if status == "Required":
            cell_bg = "#E8F5E9"
            text_col = REQUIRED_COLOR
            symbol = "✔  Required"
        elif status == "Not Required":
            cell_bg = "#FFEBEE"
            text_col = NOT_REQUIRED_COLOR
            symbol = "✘  Not Required"
        else:
            cell_bg = "#FFF8E1"
            text_col = CONDITIONAL_COLOR
            symbol = status

        rect = mpatches.FancyBboxPatch(
            (x, y - row_height), col_widths[ci + 1], row_height,
            boxstyle="round,pad=0.005", facecolor=cell_bg, edgecolor=BORDER_COLOR, linewidth=1.2
        )
        ax.add_patch(rect)
        ax.text(x + col_widths[ci + 1] / 2, y - row_height / 2, symbol,
                ha="center", va="center", fontsize=11, fontweight="bold", color=text_col)
        x += col_widths[ci + 1]

    y -= row_height

# ── Legend ──
legend_y = y - 0.06
legend_items = [
    (REQUIRED_COLOR, "✔ Required — mandatory for diagnosis"),
    (CONDITIONAL_COLOR, "Conditional — required in combination (2-of-3 or 1-of-2)"),
    (NOT_REQUIRED_COLOR, "✘ Not Required — not part of criteria"),
]
for li, (color, label) in enumerate(legend_items):
    ax.plot(start_x + 0.02, legend_y - li * 0.04, "s", markersize=12, color=color)
    ax.text(start_x + 0.05, legend_y - li * 0.04, label,
            va="center", fontsize=10, color=TEXT_COLOR)

# ── Key insight box ──
insight_y = legend_y - len(legend_items) * 0.04 - 0.04
insight_text = (
    "KEY INSIGHT:  NIH 1990 is the strictest (requires both HA + OA).  "
    "Rotterdam 2003 is the broadest (adds PCO-only phenotypes).  "
    "AES 2006 is intermediate (HA must always be present)."
)
rect = mpatches.FancyBboxPatch(
    (start_x, insight_y - 0.05), sum(col_widths), 0.05,
    boxstyle="round,pad=0.008", facecolor="#FFF3E0", edgecolor="#E65100", linewidth=1.5
)
ax.add_patch(rect)
ax.text(start_x + sum(col_widths) / 2, insight_y - 0.025, insight_text,
        ha="center", va="center", fontsize=9.5, fontweight="bold", color="#BF360C")

# ── Title ──
fig.suptitle("Comparison of PCOS Diagnostic Criteria",
             fontsize=22, fontweight="bold", color=HEADER_COLOR, y=0.99)
fig.text(0.5, 0.955, "NIH 1990  ·  Rotterdam 2003  ·  AES 2006",
         ha="center", fontsize=13, color="#546E7A", fontstyle="italic")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.94])

# ── Save ──
output_path = "pcos_criteria_comparison_chart.png"
fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"✅ Chart saved to: {output_path}")
