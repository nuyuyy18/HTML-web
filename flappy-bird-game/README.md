# Flappy Bird Game

This is a simple implementation of the classic Flappy Bird game using TypeScript. The game features a bird that the player controls by tapping the screen or pressing a key to make it flap and avoid pipes.

## Project Structure

```
flappy-bird-game
├── src
│   ├── main.ts          # Entry point of the game
│   ├── game
│   │   ├── bird.ts     # Bird class with flap and update methods
│   │   ├── pipe.ts     # Pipe class with update and isOffScreen methods
│   │   └── gameLoop.ts # Main game loop logic
│   └── types
│       └── index.ts    # Type definitions for game objects and vectors
├── package.json         # NPM configuration file
├── tsconfig.json        # TypeScript configuration file
└── README.md            # Project documentation
```

## Getting Started

To run the game, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flappy-bird-game
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Compile TypeScript**:
   ```
   npm run build
   ```

4. **Run the game**:
   ```
   npm start
   ```

## Features

- Control the bird by tapping or pressing a key.
- Avoid pipes that come towards the bird.
- Simple and engaging gameplay.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.