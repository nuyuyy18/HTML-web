"use strict";
// This file is the entry point of the game. It initializes the game canvas, sets up the game loop, and handles user input for controlling the bird.
Object.defineProperty(exports, "__esModule", { value: true });
const bird_1 = require("./game/bird");
const gameLoop_1 = require("./game/gameLoop");
const canvas = document.createElement('canvas');
const context = canvas.getContext('2d');
canvas.width = 320;
canvas.height = 480;
document.body.appendChild(canvas);
const bird = new bird_1.Bird();
function handleInput(event) {
    if (event.code === 'Space') {
        bird.flap();
    }
}
window.addEventListener('keydown', handleInput);
(0, gameLoop_1.startGameLoop)(context, bird);
