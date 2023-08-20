# Sokoban-by-Guillermo 
[Sokoban](https://en.wikipedia.org/wiki/Sokoban) is Japanese for warehouse keeper and a traditional video game.
The game is a transportation puzzle, where the player has to push all boxes in the room on the storage locations/ targets.
The possibility of making irreversible mistakes makes these puzzles so challenging especially for [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) algorithms, which mostly lack the ability to think ahead.
<br/>The repository implements the game Sokoban based on the rules presented [DeepMind's]() paper [Imagination Augmented Agents for Deep Reinforcement Learning](https://papers.nips.cc/paper/7152-imagination-augmented-agents-for-deep-reinforcement-learning). 
The room generation is random and therefore, will allow to train Deep Neural Networks without overfitting on a set of predefined rooms.


| Example Game 1 | Example Game 2 | Example Game 3 |
| :---: | :---: | :---: 
| ![Game 1](/img/img1.png) | ![Game 2](/img/img2.png) | ![Game 3](/img/img3.png) |


## 1 Installation

### From Repository
```bash
git https://github.com/guillsil/Sokoban-by-Guillermo.git
cd Sokoban-by-Guillermo
pip install -e .
```


## 2 Game Environment

### 2.1 Room Elements
Every room consists of five main elements: walls, floor, boxes, box targets, and a player. They might have different states whether they overlap with a box target or not. 

| Type       | State      | Graphic |
| ---        | -----      | :---: | 
| Wall       | Static     | ![Wall](/img/wall.gif "Wall") |
| Floor      | Empty      | ![Floor](/img/ground.gif "Floor") | 
| floor with goal | Empty      | ![BoxTarget](/img/goal.gif "Box Target") |
| Box        | Off Target | ![BoxOffTarget](/img/box.gif "Box") |
| Box target     | On Target  | ![BoxOnTarget](/img/box.gif "Box") |
| Player     | Off Target | ![PlayerOffTarget](/img/player.gif "Player") |
| Player with goal    | On Target  | ![PlayerOnTarget](/img/player.gif  "Player") |

### 2.2 Actions
The game provides 10 actions to interact with the environment. Push and Move actions in the Up, Down, Left and Right directions. The Hint action that shows you a move.
The action of undo and redo that modify the movements made. And the action of reset that returns the game to its initial state.
 | Action       | ID    | 
 | --------     | :---: |    
 | Move Up      |   w   |
 | Move Down    |   s   |
 | Move Left    |   a   |
 | Move Right   |   d   |
 | Reset        |   f   |
 | Undo         |   z   |
 | Redo         |   y   |
 | Hint         |   r   |
 | next level   |   e   |
 | previous level |  q   |
 
