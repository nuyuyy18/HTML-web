export function startGameLoop(update: () => void, render: () => void, fps: number = 60) {
    const interval = 1000 / fps;
    let lastTime = performance.now();

    function loop(currentTime: number) {
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