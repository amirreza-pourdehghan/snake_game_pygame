# 🐍 Snake Game

A simple Snake game made with **Python** and **Pygame**.

## Features

* Classic Snake gameplay
* Simple and modular code
* Configurable settings using `config.json`
* Keyboard controls

## Installation

```bash
git clone https://github.com/amirreza-pourdehghan/snake_game_pygame.git
cd snake_game_pygame
pip install pygame
```

Run the game:

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
