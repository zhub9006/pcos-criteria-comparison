"""
PCOS Diagnostic Criteria Comparison Chart Generator
====================================================
Compares the three main PCOS diagnostic criteria sets:
  - NIH 1990 (Zawadzki & Dunaif)
  - Rotterdam 2003 (ESHRE/ASRM)
  - AE-PCOS 2006 (Androgen Excess Society)

Saves a presentation-ready comparison chart as PNG.

Data sourced from:
  - Rotterdam 2003 consensus (Fertility & Sterility)
  - AE-PCOS 2006 position statement
  - NIH 1990 working definition
  - 2023 International Evidence-Based PCOS Guideline (Teede et al.)
  - GitHub: rrmadmin/rrm-academy-cf  src/data/pcos.json
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Criteria definitions ──────────────────────────────────────────────

criteria = {
    "NIH 1990": {
        "subtitle": "Zawadzki & Dunaif",
        "oligo_anovulation": "Required",
        "hyperandrogenism": "Required",
        "polycystic_ovaries": "Not considered",
        "rule": "Both features required",
        "prevalence": "~6–10%",
        "phenotypes_captured": "A, B",
        "key_stance": "Narrowest definition; captures\nmetabolically-loaded classic\nphenotype only"
    },
    "Rotterdam 2003": {
        "subtitle": "ESHRE / ASRM",
        "oligo_anovulation": "One of three",
        "hyperandrogenism": "One of three",
        "polycystic_ovaries": "One of three",
        "rule": "2 of 3 required",
        "prevalence": "~10–15%",
        "phenotypes_captured": "A, B, C, D",
        "key_stance": "Most widely used; broadest\nphenotype capture; source of\nthe four-phenotype classification"
    },
    "AE-PCOS 2006": {
        "subtitle": "Androgen Excess Society",
        "oligo_anovulation": "Optional (if HA present)",
        "hyperandrogenism": "Required",
        "polycystic_ovaries": "Optional (if HA present)",
        "rule": "HA required + either OD or PCO",
        "prevalence": "~8–12%",
        "phenotypes_captured": "A, B, C",
        "key_stance": "Frames PCOS as fundamentally\nhyperandrogenic; excludes\nnormo-androgenic Phenotype D"
    }
}

features = ["Oligo-/Anovulation", "Hyperandrogenism\n(clinical/biochemical)", "Polycystic Ovaries\n(ultrasound)"]
criteria_names = list(criteria.keys())

# ── Build the feature requirement matrix ──────────────────────────────

# Color coding:
#   Required       → dark teal
#   One of three   → medium blue
#   Optional       → light amber
#   Not considered → light grey

color_map = {
    "Required":       "#1a6b5a",   # dark teal
    "One of three":   "#3b82c4",   # medium blue
    "Optional (if HA present)": "#d4a843",  # amber
    "Not considered": "#d1d5db",   # light grey
}

matrix = []
for c in criteria_names:
    row = [
        criteria[c]["oligo_anovulation"],
        criteria[c]["hyperandrogenism"],
        criteria[c]["polycystic_ovaries"],
    ]
    matrix.append(row)

# ── Figure layout ──────────────────────────────────────────────────────

fig = plt.figure(figsize=(18, 11), facecolor="#f8f9fa")

# Main grid: top area for chart, bottom area for summary boxes
gs = fig.add_gridspec(2, 1, height_ratios=[3, 1.6], hspace=0.18)

ax_chart = fig.add_subplot(gs[0])
ax_summary = fig.add_subplot(gs[1])

# ── Chart (top) ────────────────────────────────────────────────────────

ax_chart.set_facecolor("#f8f9fa")
ax_chart.set_xlim(-0.5, len(features) - 0.5)
ax_chart.set_ylim(-0.8, len(criteria_names) - 0.2)

cell_w = 0.92
cell_h = 0.72

for i, c in enumerate(criteria_names):
    y = len(criteria_names) - 1 - i
    for j, feat in enumerate(features):
        val = matrix[i][j]
        clr = color_map.get(val, "#cccccc")

        rect = mpatches.FancyBboxPatch(
            (j - cell_w/2, y - cell_h/2), cell_w, cell_h,
            boxstyle="round,pad=0.04",
            facecolor=clr, edgecolor="#444444", linewidth=1.4,
            zorder=3
        )
        ax_chart.add_patch(rect)

        # Determine text colour for readability
        txt_clr = "white" if clr in [color_map["Required"], color_map["One of three"]] else "#222222"
        ax_chart.text(j, y, val, ha='center', va='center',
                      fontsize=11.5, fontweight='bold', color=txt_clr, zorder=4)

    # Criteria label on the left
    ax_chart.text(-1.6, y + 0.12, c, ha='center', va='center',
                  fontsize=14, fontweight='bold', color="#222222")
    ax_chart.text(-1.6, y - 0.22, criteria[c]["subtitle"], ha='center', va='center',
                  fontsize=9.5, color="#666666", style='italic')

# Feature labels on top
for j, feat in enumerate(features):
    ax_chart.text(j, len(criteria_names) + 0.15, feat,
                  ha='center', va='bottom', fontsize=12.5, fontweight='bold', color="#222222")

ax_chart.text(-1.6, len(criteria_names) + 0.15, "Criteria",
              ha='center', va='bottom', fontsize=13, fontweight='bold', color="#222222")

# Title
ax_chart.text(len(features)/2 - 0.5, len(criteria_names) + 0.65,
              "PCOS Diagnostic Criteria — Feature Requirement Comparison",
              ha='center', va='center', fontsize=19, fontweight='bold', color="#1a1a2e")

ax_chart.text(len(features)/2 - 0.5, len(criteria_names) + 0.42,
              "NIH 1990  ·  Rotterdam 2003  ·  AE-PCOS 2006",
              ha='center', va='center', fontsize=12, color="#555555")

ax_chart.axis('off')

# ── Legend ──────────────────────────────────────────────────────────────

legend_items = [
    mpatches.Patch(facecolor=color_map["Required"], edgecolor="#444", label="Required"),
    mpatches.Patch(facecolor=color_map["One of three"], edgecolor="#444", label="One of three (2-of-3 rule)"),
    mpatches.Patch(facecolor=color_map["Optional (if HA present)"], edgecolor="#444", label="Optional (conditional)"),
    mpatches.Patch(facecolor=color_map["Not considered"], edgecolor="#444", label="Not considered"),
]
ax_chart.legend(handles=legend_items, loc='lower center', ncol=4,
                fontsize=10.5, frameon=True, fancybox=True,
                edgecolor="#aaaaaa", facecolor="#f0f0f0",
                bbox_to_anchor=(0.5, -0.08))

# ── Summary boxes (bottom) ────────────────────────────────────────────

ax_summary.set_facecolor("#f8f9fa")
ax_summary.set_xlim(0, 3)
ax_summary.set_ylim(0, 1)
ax_summary.axis('off')

box_colors = ["#1a6b5a", "#3b82c4", "#d4a843"]
box_x_positions = [0.08, 1.08, 2.08]

for idx, c in enumerate(criteria_names):
    bx = box_x_positions[idx]
    # Box background
    rect = mpatches.FancyBboxPatch(
        (bx, 0.05), 0.84, 0.88,
        boxstyle="round,pad=0.06",
        facecolor=box_colors[idx], edgecolor="#333333", linewidth=1.5, alpha=0.15,
        zorder=2
    )
    ax_summary.add_patch(rect)

    # Header bar
    hdr = mpatches.FancyBboxPatch(
        (bx, 0.73), 0.84, 0.20,
        boxstyle="round,pad=0.03",
        facecolor=box_colors[idx], edgecolor="#333333", linewidth=1.2, alpha=0.85,
        zorder=3
    )
    ax_summary.add_patch(hdr)

    ax_summary.text(bx + 0.42, 0.87, c, ha='center', va='center',
                    fontsize=13, fontweight='bold', color="white", zorder=4)
    ax_summary.text(bx + 0.42, 0.78, criteria[c]["rule"], ha='center', va='center',
                    fontsize=10, color="white", zorder=4)

    # Details
    details = [
        f"Prevalence yield: {criteria[c]['prevalence']}",
        f"Phenotypes captured: {criteria[c]['phenotypes_captured']}",
    ]
    for k, line in enumerate(details):
        ax_summary.text(bx + 0.42, 0.60 - k * 0.12, line,
                        ha='center', va='center', fontsize=10, color="#333333", zorder=4)

    # Stance (smaller text)
    ax_summary.text(bx + 0.42, 0.28, criteria[c]["key_stance"],
                    ha='center', va='center', fontsize=8.5, color="#555555",
                    style='italic', zorder=4, linespacing=1.4)

# ── Footer ──────────────────────────────────────────────────────────────

fig.text(0.5, 0.01,
         "Sources: Zawadzki & Dunaif 1990 · Rotterdam ESHRE/ASRM 2003 · AE-PCOS Society 2006 · "
         "International Guideline 2023 (Teede et al.)  |  "
         "Data: github.com/rrmadmin/rrm-academy-cf",
         ha='center', fontsize=8, color="#999999")

# ── Save ────────────────────────────────────────────────────────────────

output_path = "pcos_criteria_comparison.png"
fig.savefig(output_path, dpi=200, bbox_inches='tight', facecolor="#f8f9fa")
print(f"✅ Chart saved to {output_path}")
plt.close(fig)
