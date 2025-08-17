# Circle Animation with Matplotlib

This project demonstrates how to animate a moving circle using
**Python**, **Matplotlib**, and **NumPy**.\
The animation plots the upper and lower halves of a circle, dynamically
updating them frame by frame to create smooth motion.

## 📜 Features

-   Plots a circle by calculating upper and lower semicircle points
    using the circle equation:\
    \[(x - h)\^2 + (y - k)\^2 = r\^2\]
-   Animates the circle shifting horizontally across the graph.\
-   Draws a dynamic line from the circle's edge to its center.\
-   Uses `FuncAnimation` from Matplotlib for smooth rendering.

## 📂 Project Structure

    rolling_circle_simulation.py   # Main Python script
    README.md             # Documentation

## ▶️ How to Run

1.  Install dependencies:

    ``` bash
    pip install matplotlib numpy
    ```

2.  Run the script:

    ``` bash
    python rolling_circle_simulation.py
    ```

3.  A Matplotlib window will appear showing the animated circle in
    motion.

## ⚙️ Dependencies

-   [Matplotlib](https://matplotlib.org/)
-   [NumPy](https://numpy.org/)

## 🎥 Example Behavior

-   A circle moves across the x-axis.\
-   Both upper and lower semicircle arcs are redrawn each frame.\
-   A line connects the circle's center to its circumference.\
-   The circle's center is marked with a scatter point.

## ✨ Possible Extensions

-   Add multiple moving circles.\
-   Change colors dynamically per frame.\
-   Animate circle radius instead of horizontal movement.\
-   Export animation as a `.gif` or `.mp4`.
