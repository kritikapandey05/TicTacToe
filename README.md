# 🎮 AI Tic Tac Toe

An upgraded, feature-rich version of the classic Tic-Tac-Toe game — built using Python and Pygame. 
---

## 🎯 Features

- 🤖 **AI Opponents** – Choose from:
  - **Easy** (random moves)
  - **Medium** (shallow strategy)
  - **Hard** (full Minimax algorithm)

- 🎵 **Sound Effects** – Hear retro audio cues when you win, lose, or draw.

- 📊 **Score Tracker** – Tracks wins, losses, and draws across sessions using a local JSON file.

- 🎮 **Sleek UI** – Neon-style grid with pixel fonts for that old-school arcade vibe.

- 🧠 **No Repetition** – The AI gets smarter with difficulty and offers a different challenge every time.

---

## 📁 Folder Structure

```
TicTacToe/
├── main.py              # Main loop and interface
├── game.py              # Game state management and visuals
├── ai.py                # AI logic (random & minimax with depth control)
├── assets/
│   ├── PressStart2P.ttf # Pixel font for UI
│   ├── win.wav          # Sound on player win
│   ├── lose.wav         # Sound on AI win
│   ├── draw.wav         # Sound on draw
│   └── stats.json       # Auto-generated score tracker
```
## 🚀 How to Run

### 1. Install Python (3.11+ recommended)  
➡️ [Download from python.org](https://www.python.org/downloads/)

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Clone and Run the Game

```bash
git clone https://github.com/kritikapandey05/TicTacToe
cd TicTacToe
python main.py
```

---

## 🧠 How to Play

- Use your **mouse** to place your move (`X`)
- When prompted, select AI difficulty:
  - Press `1` → Easy
  - Press `2` → Medium
  - Press `3` → Hard (Minimax)
- Press `R` at any time to restart the game

---

## 🧑‍💻 Made With

- 🐍 Python 3.13  
- 🕹️ Pygame 2.6  

## 📜 License

MIT — free to use, learn from, or improve.
