![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Theis Drawdown Curve Calculator
 
*For hydrogeologists and groundwater engineers: enter aquifer and pumping parameters to predict drawdown over time at a single observation well and export the curve.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Hydrogeology / Groundwater
 
The user provides five physical inputs and one display setting. Inputs: transmissivity T in m^2/day (positive, default 100), storativity S dimensionless (default 0.0001, allowed 1e-6 to 1e-1), pumping rate Q in m^3/day (positive, default 500), radial distance from pumping well to observation point r in meters (positive, default 50), maximum pumping time t_max in days (positive, default 1), and number of curve points N via an integer slider from 20 to 200 (default 80). The app generates N logarithmically spaced time values from max(1e-4, t_max/1000) to t_max. For each time t, it computes the auxiliary variable u = (r^2 * S) / (4 * T * t). It then evaluates the Theis well function W(u) using scipy.special.exp1(u), which gives the exact exponential integral for this non-negative argument. If SciPy is unavailable, it falls back to the series approximation W(u) = -0.5772 - ln(u) + u - u^2/(2*2!) + u^3/(3*3!) - ... until terms are smaller than 1e-9. Drawdown s in meters is calculated as s = (Q / (4 * pi * T)) * W(u). The Gradio interface uses a single column with clearly labeled numeric inputs for T, S, Q, r, and t_max, a slider for N, and a Calculate button. Outputs are: a Plotly line chart with log-scale x-axis for time in days and y-axis drawdown in meters; a data table showing time, u, W(u), and drawdown; and a downloadable CSV file with the same columns. If any input is invalid or r equals zero, an error message appears instead of the outputs. There is no ML component; this is a deterministic analytical well hydraulics model implemented as a clean engineering calculator.
 
## Run it
 
```bash
docker build -t theis-drawdown-curve-calculator .
docker run -p 7860:7860 theis-drawdown-curve-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-18.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
