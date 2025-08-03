// This file is the entry point of the game. It initializes the game canvas, sets up the game loop, and handles user input for controlling the bird.

import { Bird } from './game/bird';
import { startGameLoop } from './game/gameLoop';

const canvas = document.createElement('canvas');
const context = canvas.getContext('2d');
canvas.width = 320;
canvas.height = 480;
document.body.appendChild(canvas);

const bird = new Bird();

function handleInput(event: KeyboardEvent) {
    if (event.code === 'Space') {
        bird.flap();
    }
}

window.addEventListener('keydown', handleInput);

startGameLoop(context, bird);