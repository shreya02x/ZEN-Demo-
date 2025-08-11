# ZEN - Zero Emissions Node AI System

**Author:** Shreya Chauhan  
**Email:** shreyachauhanwork16@gmail.com  
**Location:** Delhi, India  

---

## Overview

ZEN (Zero Emissions Node) is an innovative AI inference framework designed to operate strictly within ecological boundaries by using only renewable energy inputs such as solar and wind. It challenges the conventional “always-on” AI computation model by implementing a constraint-bounded scheduler that dynamically decides when to run, pause, or offload AI tasks based on real-time clean energy availability and battery levels.

ZEN’s architecture prioritizes environmental responsibility by:

- Eliminating fallback on fossil fuels during energy shortages.
- Offloading computation to low-power fog nodes to maintain service continuity.
- Reducing e-waste through modular hardware reuse and lifecycle management.

This project presents a replicable and enforceable model for sustainable AI deployment aligned with **SDG 7 (Affordable and Clean Energy), SDG 13 (Climate Action), and SDG 15 (Life on Land).**

---

## Features

- **Renewable-Only Operation:** AI inference tasks run only when solar or wind energy exceeds thresholds.
- **Rule-Based Scheduler:** Real-time decision logic dynamically manages workloads as Light or Heavy tasks.
- **Fog Node Offloading:** Utilizes decentralized, low-power devices (e.g., Raspberry Pi) to process overflow tasks.
- **E-Waste Mitigation:** Modular upgrades and end-of-life repurposing reduce electronic waste.
- **Simulation & Visualization:** Python-based demo simulates scheduler behavior with synthetic renewable data.
- **Failover Strategies:** Battery reserves and cold-start fog nodes ensure service resilience without fossil fallback.

---

## System Architecture

- **Energy Input:** Monitored solar and wind power with LiFePO₄ battery buffering; no fossil fallback.
- **Scheduler:** Decision tree uses solar %, battery %, and task type to choose from RUN_LOCAL, OFFLOAD, or PAUSE.
- **Fog Nodes:** Low-power units with heartbeat monitoring and load balancing.
- **E-Waste Protocol:** Tracks device lifecycle and follows India’s 2023 E-Waste EPR policy for recycling.

---

## Installation & Usage

### Prerequisites

- Python 3.8 or higher
- Required Python packages:
  
```bash
pip install flask matplotlib fpdf
````

### Running the Simulation Demo

Clone this repository:

```bash
git clone https://github.com/shreya02x/ZEN-Demo-.git
cd ZEN-Demo-
```

Run the scheduler simulation and generate the report:

```bash
python zen_demo.py
```

Then generate detailed reports and visualizations:

```bash
python zen_report.py
```

### Outputs

* `zen_run.csv` — Log of scheduler decisions over simulated run.
* `zen_actions.png` — Visualization plot of solar, battery, and scheduler actions.
* `zen_report.pdf` — Automatically generated comprehensive report combining results.

---

## Results Summary

* 60% of tasks executed locally on renewable power.
* 20% offloaded to fog nodes to prevent fossil fallback.
* 10% paused due to insufficient clean energy.
* 10% deferred due to fog node unavailability.

These results confirm ZEN’s ability to enforce ecological constraints without compromising AI service continuity.

---

## Future Work

* Real-world hardware validation beyond simulations.
* Adaptive scheduler with machine learning to optimize thresholds.
* Integration with real-time weather forecasts and battery predictive models.
* Exploring alternative micro-storage technologies (compressed air, hydrogen).

---

## Impact & Use Cases

* **Rural Education & Labs:** Solar-driven AI services in off-grid areas.
* **Green Data Hubs:** Clean AI compute zones for governments and enterprises.
* **Low Network Regions:** Decentralized fog computing reduces cloud dependency.

---

## License

All Rights Reserved.
No part of this repository, its code, or associated documentation may be used, reproduced, or distributed without prior written permission from the author.

---

## Contact

Shreya Chauhan
Email: [shreyachauhanwork16@gmail.com](mailto:shreyachauhanwork16@gmail.com)

---

## References

* Strubell et al., Energy and Policy Considerations for Deep Learning in NLP, EMNLP, 2019.
* Patterson et al., Carbon Emissions and Large Neural Network Training, 2021.
* Satyanarayanan et al., VM-Based Cloudlets in Mobile Computing.
* Ministry of New and Renewable Energy, Government of India – Solar Data 2023.
* Indian E-Waste (Management) Rules, EPR Policy 2023.

```

```
