# 🐍 The Snake Game

A customizable Snake Game built with Python and Pygame.

The game supports multiple players, configurable controls, obstacles, fruits, and dynamic game settings through a JSON configuration file.

## ✨ Features

- 🐍 Snake movement and growth
- 👥 Two-player support
- 🍎 Fruit spawning
- 🧱 Obstacles and blocked cells
- 🔄 Screen wrap-around movement
- 🎮 Custom keyboard controls for each player
- ⚙️ Configurable game settings with `data/config.json`
- 🧩 Object-Oriented Programming (OOP)

## 🛠️ Technologies

- Python 3
- Pygame
- Object-Oriented Programming (OOP)
- JSON

## 📁 Project Structure

```text
the-snake-game/
│
├── data/
│   └── config.json
│
├── main.py
├── snake.py
├── game_manager.py
├── cell.py
├── consts.py
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/the-snake-game.git
```

### 2. Navigate to the project directory

```bash
cd the-snake-game
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python main.py
```

## 🎮 Controls

### Player 1

| Key | Action |
| :---: | :--- |
| `W` | Move Up |
| `S` | Move Down |
| `A` | Move Left |
| `D` | Move Right |

### Player 2

| Key | Action |
| :---: | :--- |
| `I` | Move Up |
| `K` | Move Down |
| `J` | Move Left |
| `L` | Move Right |

## ⚙️ Configuration

The game settings are stored in:

```text
data/config.json
```

You can customize:

- Cell size
- Board size
- Window dimensions
- Background color
- Snake colors
- Fruit color
- Obstacle positions
- Snake starting positions
- Snake movement directions
- Keyboard controls

Example:

```json
{
  "cell_size": 30,
  "table_size": 20,
  "fruit_color": [255, 0, 0],
  "snakes": [
    {
      "keys": {
        "w": "UP",
        "s": "DOWN",
        "a": "LEFT",
        "d": "RIGHT"
      }
    }
  ]
}
```

## 🧩 Project Architecture

The project is organized into several components:

- `main.py` — Starts and runs the game loop.
- `snake.py` — Contains the `Snake` class and movement logic.
- `game_manager.py` — Manages the game board, snakes, obstacles, turns, and fruit generation.
- `cell.py` — Represents individual cells on the game board.
- `consts.py` — Loads configuration values from `data/config.json`.
- `data/config.json` — Stores customizable game settings.

## 📝 Notes

The snakes can move through one edge of the board and appear on the opposite side.

If a snake collides with an obstacle or another occupied cell, it is removed from the game.

---

⭐ If you enjoyed this project, feel free to star the repository!
