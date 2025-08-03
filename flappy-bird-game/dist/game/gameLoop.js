"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.startGameLoop = void 0;
function startGameLoop(update, render, fps = 60) {
    const interval = 1000 / fps;
    let lastTime = performance.now();
    function loop(currentTime) {
        const deltaTime = currentTime - lastTime;
        if (deltaTime >= interval) {
            update();
            render();
            lastTime = currentTime - (deltaTime % interval);
        }
        requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
}
exports.startGameLoop = startGameLoop;
