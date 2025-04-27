# A* Pathfinding Visualization 🚀🗺️

A clean, interactive visualization of the A* (A-star) pathfinding algorithm built with Python and Pygame.  
Watch the A* algorithm in action as it finds the shortest path between two points on a grid!

Perfect for students, hobbyists, and anyone curious about how A* works under the hood!

---

## ✨ Features

- **Interactive Visualization**: Set start and end points, draw walls, and watch the algorithm find the shortest path.
- **Modular A* Algorithm**: `astar.py` can be imported as a module or run standalone.
- **Custom Buttons**: Easy controls to start, reset, and customize the grid.
- **Polished Visuals**: Smooth animations, custom colors, fonts, and an application icon.
- **Educational Tool**: Perfect for learning or teaching A* pathfinding.

---

## 📸 Screenshots

*(Add screenshots here if possible for a visual preview!)*

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/astar-visualizer.git
cd astar-visualizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the main GUI file:

```bash
python gui.py
```

Or run only the algorithm logic (for testing):

```bash
python astar.py
```

---

## 🎮 Controls

- **Set Start**: Right-click on a cell after pressing 1.
- **Set End**: Right-click on a cell after pressing 2.
- **Draw Walls**: Right-click on a cell after pressing 3.
- **Erase**: Right-click on a cell after pressing 4.
- **Start Algorithm**: Press the "Euclidian" / "Manhattan" button.
- **Clear Path**: Press the "Clear" button.
- **Reset Grid**: Press the "Reset Board" button.

---

## 📁 Project Structure

```
astar-visualizer/
├── astar.py          # A* algorithm implementation (standalone and importable)
├── gui.py            # Main GUI to interact with the visualizer
├── buttons.py        # Button class for GUI controls
├── colors.py         # Color definitions and utilities
├── requirements.txt  # List of required Python modules
├── fonts/            # Custom fonts used in the GUI
└── __pycache__/      # Python cache files (can be ignored)
```

---

## 📦 Dependencies

- Python 3.x  
- `pygame` (and other modules listed in `requirements.txt`)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

- **Pathfinding**: A* algorithm prioritizes paths that are cheaper to reach + closer to the goal.
- **Grid Customization**: Draw barriers and see how A* adapts in real-time.
- **Visualization**: Watch open/closed sets update as the path is calculated.

---

## 🎨 Customization

- **Colors & Fonts**: Modify `colors.py` and the `fonts/` folder to change the appearance.
- **Buttons**: Add or edit button behaviors in `buttons.py` for more features.

---


## 🙏 Acknowledgements

Created and maintained by **Suyash Abhishek Kumar**.

Explore, experiment, and learn how pathfinding works with A*!
