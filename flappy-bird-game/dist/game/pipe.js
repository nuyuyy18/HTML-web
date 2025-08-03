"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Pipe = void 0;
class Pipe {
    constructor(x, y, width, height, speed) {
        this.position = { x, y };
        this.width = width;
        this.height = height;
        this.speed = speed;
    }
    update() {
        this.position.x -= this.speed;
    }
    isOffScreen(screenWidth) {
        return this.position.x + this.width < 0;
    }
}
exports.Pipe = Pipe;
