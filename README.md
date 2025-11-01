# Animated Polar Equation Plotter (Butterfly)🌀

This project generates an animated visualization of a mathematical function, specifically a polar equation transformed into Cartesian coordinates and rotated. The animation displays the curve being drawn gradually, with the color changing as the animation progresses through different "loops" of the polar equation. It provides a visually engaging way to explore the behavior of this particular polar equation: `r = exp(cos(theta)) - 2 * cos(4 * theta) - sin(theta / 12)**5`.

🚀 **Key Features**

*   **Polar to Cartesian Conversion:** Transforms polar coordinates to Cartesian coordinates for plotting.
*   **Animated Plotting:** Gradually draws the curve, creating an animation effect.
*   **Color Cycling:** Changes the color of the line as the animation progresses through different loops of the equation.
*   **Customizable Appearance:** Configured with a black background and no axes for a clean visual presentation.
*   **Rotation Transformation:** Rotates the Cartesian coordinates by 90 degrees counter-clockwise.

🛠️ **Tech Stack**

*   **Programming Language:** Python
*   **Numerical Computation:** NumPy
*   **Plotting:** Matplotlib (pyplot)
*   **Animation:** Matplotlib Animation (FuncAnimation)
*   **Colormaps:** Matplotlib cm

📦 **Getting Started**

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required packages:

    ```bash
    pip install numpy matplotlib
    ```

### Running Locally

1.  Execute the `main.py` script:

    ```bash
    python main.py
    ```

    This will display the animated plot in a Matplotlib window.

📂 **Project Structure**

```
.
├── main.py      # Main script for generating the animated plot
└── README.md    # This file
```

🤝 **Contributing**

Contributions are welcome! If you have suggestions for improvements or bug fixes, please submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

📝 **License**

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.
