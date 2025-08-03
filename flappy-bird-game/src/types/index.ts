export interface GameObject {
    position: Vector2;
    update(): void;
    render(context: CanvasRenderingContext2D): void;
}

export interface Vector2 {
    x: number;
    y: number;
}