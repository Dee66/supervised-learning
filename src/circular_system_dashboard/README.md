# Circular System Dashboard

## Overview
The Circular System Dashboard project provides an interactive visualization tool for understanding the dynamics of machine learning systems through a circular system map. This project integrates a circular system map with dashboard-style overlays and animated failure propagation, allowing users to explore the feedback loops and operational metrics of a production ML system.

## Features
- **Interactive Circular System Map**: Visualize the stages of a machine learning system and their interconnections.
- **Dashboard Overlays**: Display relevant metrics and insights dynamically as users interact with the system map.
- **Animated Failure Propagation**: Observe how failures propagate through the system, enhancing understanding of potential risks and impacts.

## Project Structure
```
circular-system-dashboard
├── notebooks
│   └── 01_circular_system_dashboard.ipynb
├── src
│   ├── circular_map.py
│   ├── dashboard_overlays.py
│   └── animation_utils.py
├── requirements.txt
└── README.md
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd circular-system-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Launch the Jupyter notebook:
   ```
   jupyter notebook notebooks/01_circular_system_dashboard.ipynb
   ```

2. Interact with the circular system map to explore different stages of the machine learning process.

3. Use the dashboard overlays to view metrics and insights relevant to the current stage.

4. Observe the animated failure propagation to understand how issues can affect the system.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.