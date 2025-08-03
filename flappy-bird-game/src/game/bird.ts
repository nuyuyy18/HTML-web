class Bird {
    position: { x: number; y: number };
    velocity: { x: number; y: number };
    gravity: number;
    lift: number;

    constructor(x: number, y: number) {
        this.position = { x: x, y: y };
        this.velocity = { x: 0, y: 0 };
        this.gravity = 0.6;
        this.lift = -15;
    }

    flap() {
        this.velocity.y += this.lift;
    }

    update() {
        this.velocity.y += this.gravity;
        this.position.y += this.velocity.y;

        // Prevent the bird from falling off the bottom of the screen
        if (this.position.y > window.innerHeight) {
            this.position.y = window.innerHeight;
            this.velocity.y = 0;
        }

        // Prevent the bird from flying off the top of the screen
        if (this.position.y < 0) {
            this.position.y = 0;
            this.velocity.y = 0;
        }
    }
}