export class Pipe {
    position: { x: number; y: number };
    width: number;
    height: number;
    speed: number;

    constructor(x: number, y: number, width: number, height: number, speed: number) {
        this.position = { x, y };
        this.width = width;
        this.height = height;
        this.speed = speed;
    }

    update() {
        this.position.x -= this.speed;
    }

    isOffScreen(screenWidth: number) {
        return this.position.x + this.width < 0;
    }
}