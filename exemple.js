

const CANVAS = document.getElementById("game");
const PI2 = Math.PI * 2;
const FOCAL_LENGTH = 0.8;
const KEYCODES = { 37: "left", 39: "right", 38: "forward", 40: "backward" };
const MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
];
const NO_WALL = { length2: Infinity };
const RESOLUTION = 320;
const START_QUADRANT = [1, 1];

function Bitmap(src, width, height) {
    this.image = new Image();
    this.image.src = src;
    this.width = width;
    this.height = height;
}

function attachControls(game) {
    document.addEventListener("keydown", event => {
        const direction = KEYCODES[event.keyCode];
        if (!direction) {
            return;
        }
        game.controls[direction] = true;
        event.preventDefault();
    }, false);
    document.addEventListener("keyup", event => {
        const direction = KEYCODES[event.keyCode];
        if (!direction) {
            return;
        }
        game.controls[direction] = false;
        event.preventDefault();
    }, false);
}

function baseControls() {
    return {
        left: false,
        right: false,
        forward: false,
        backward: false
    };
}

function cast(game, angle, range) {
    const point = game.player;
    const sin = Math.sin(angle);
    const cos = Math.cos(angle);
    const inspect = (step, shiftX, shiftY, distance, offset) => {
        const dx = cos < 0 ? shiftX : 0;
        const dy = sin < 0 ? shiftY : 0;
        step.height = getMapPoint(game, step.x - dx, step.y - dy);
        step.distance = distance + Math.sqrt(step.length2);
        if (shiftX) {
            step.shading = cos < 0 ? 2 : 0;
        } else {
            step.shading = sin < 0 ? 2 : 1;
        }
        step.offset = offset - Math.floor(offset);
        return step;
    };
    const ray = origin => {
        const stepX = step(sin, cos, origin.x, origin.y);
        const stepY = step(cos, sin, origin.y, origin.x, true);
        const nextStep = stepX.length2 < stepY.length2
            ? inspect(stepX, 1, 0, origin.distance, stepX.y)
            : inspect(stepY, 0, 1, origin.distance, stepY.x);
        if (nextStep.distance > range) {
            return [origin];
        }
        return [origin].concat(ray(nextStep));
    };
    const step = (rise, run, x, y, inverted) => {
        if (run === 0) {
            return NO_WALL;
        }
        const dx = run > 0 ? Math.floor(x + 1) - x : Math.ceil(x - 1) - x;
        const dy = dx * (rise / run);
        return {
            x: inverted ? y + dy : x + dx,
            y: inverted ? x + dx : y + dy,
            length2: dx * dx + dy * dy
        };
    };
    return ray({ x: point.x, y: point.y, height: 0, distance: 0 });
}

function createCamera(canvas, resolution, focalLength) {
    const width = canvas.width = window.innerWidth;
    const height = canvas.height = window.innerHeight;
    return {
        ctx: canvas.getContext("2d"),
        width,
        height,
        resolution,
        spacing: width / resolution,
        focalLength,
        range: 14,
        lightRange: 5,
        scale: width + height / 1200
    };
}

function createMap(grid) {
    return {
        grid,
        light: 0,
        wallTexture: new Bitmap("https://hotsource.dev/wp-content/uploads/2019/05/wastrel-wall.png", 512, 512),
        floorTexture: new Bitmap("https://hotsource.dev/wp-content/uploads/2019/05/wastrel-floor.jpg", 345, 345),
        skyTexture: new Bitmap("https://hotsource.dev/wp-content/uploads/2019/05/wastrel-skybox.jpg", 960, 640)
    }
}

function createPlayer() {
    return {
        x: START_QUADRANT[0] + 0.5,
        y: START_QUADRANT[1] + 0.5,
        direction: Math.PI * 0.3
    };
}

function drawColumns(game) {
    const { ctx } = game.camera;
    const { floorTexture, wallTexture } = game.map;
    ctx.save();
    const drawColumn = (column, ray, angle) => {
        // const texture = wallTexture;
        const left = Math.floor(column * game.camera.spacing);
        const width = Math.ceil(game.camera.spacing);
        let hit = -1;
        while (++hit < ray.length && ray[hit].height <= 0);
        for (let s = ray.length - 1; s >= 0; s--) {
            const step = ray[s];
            // var rainDrops = Math.pow(Math.random(), 3) * s;
            // var rain = (rainDrops > 0) && project(0.1, angle, step.distance);
            if (s === hit) {
                const wallTextureX = Math.floor(wallTexture.width * step.offset);
                const floorTextureX = Math.floor(floorTexture.width * step.offset);
                const wall = project(step.height, angle, step.distance);
                ctx.globalAlpha = 1;
                // Walls:
                ctx.drawImage(wallTexture.image, wallTextureX, 0, 1, wallTexture.height, left, wall.top, width, wall.height);
                // Floor:
                ctx.fillStyle = "#000";
                ctx.fillRect(left, wall.top + wall.height, width, game.camera.height);
                // ctx.drawImage(floorTexture.image,
                //     floorTextureX, 0,
                //     1, floorTexture.height,
                //     left, wall.height * 2,
                //     width, 1000);
                ctx.fillStyle = "#000000";
                ctx.globalAlpha = Math.max((step.distance + step.shading) / game.camera.lightRange - game.map.light, 0);
                ctx.fillRect(left, wall.top, width, wall.height); // darkness
            }
            ctx.fillStyle = "#ffffff";
            ctx.globalAlpha = 0.15;
            // while (--rainDrops > 0) ctx.fillRect(left, Math.random() * rain.top, 1, rain.height);
        }
    };
    const project = (height, angle, distance) => {
        const z = distance * Math.cos(angle);
        const wallHeight = game.camera.height * height / z;
        const bottom = game.camera.height / 2 * (1 + 1 / z);
        return {
            top: bottom - wallHeight,
            height: wallHeight
        }; 
    };
    for (let column = 0; column < game.camera.resolution; column++) {
        const x = column / game.camera.resolution - 0.5;
        const angle = Math.atan2(x, game.camera.focalLength);
        const ray = cast(game, game.player.direction + angle, game.camera.range);
        drawColumn(column, ray, angle);
    }
    ctx.restore();
}

function drawSky(game) {
    const { light: ambient, skyTexture } = game.map;
    const { ctx } = game.camera;
    const { direction } = game.player;
    const width = skyTexture.width * (game.camera.height / skyTexture.height) * 2;
    const left = (direction / PI2) * -width;
    ctx.save();
    ctx.drawImage(skyTexture.image, left, 0, width, game.camera.height);
    if (left < width - game.camera.width) {
        ctx.drawImage(skyTexture.image, left + width, 0, width, game.camera.height);
    }
    if (ambient > 0) {
        ctx.fillStyle = "#ffffff";
        ctx.globalAlpha = ambient * 0.1;
        ctx.fillRect(0, game.camera.height * 0.5, game.camera.width, game.camera.height * 0.5);
    }
    ctx.restore();
}

function getMapPoint(game, x, y) {
    const gameWidth = game.map.grid[0].length;
    const gameHeight = game.map.grid.length;
    const rx = Math.floor(x);
    const ry = Math.floor(y);
    if (rx < 0 || rx > gameWidth - 1 || ry < 0 || ry > gameHeight - 1) {
        return -1;
    }
    return game.map.grid[ry][rx];
}

function loop(callback) {
    let lastTime = 0;
    const handleFrame = time => {
        const seconds = (time - lastTime) / 1000;
        lastTime = time;
        if (seconds < 0.2) {
            callback(seconds);
        }
        requestAnimationFrame(handleFrame);
    };
    requestAnimationFrame(handleFrame);
}

function newGame() {
    const game = {
        camera: createCamera(CANVAS, RESOLUTION, FOCAL_LENGTH),
        map: createMap(MAP),
        player: createPlayer(),
        controls: baseControls()
    };
    attachControls(game);
    return game;
}

function play(game) {
    loop(seconds => {
        updateMap(game, seconds);
        updatePlayer(game, seconds);
        render(game);
    });
}

function render(game) {
    drawSky(game);
    drawColumns(game);
}

function rotatePlayer(game, angle) {
    game.player.direction = (game.player.direction + angle + PI2) % PI2;
}

function updateMap(game, seconds) {
    if (game.map.light > 0) {
        game.map.light = Math.max(game.map.light - 10 * seconds, 0);
    } else if (Math.random() * 5 < seconds) {
        game.map.light = 2;
    }
}

function updatePlayer(game, seconds) {
    const { controls } = game;
    if (controls.left) {
        rotatePlayer(game, -Math.PI * seconds);
    }
    if (controls.right) {
        rotatePlayer(game, Math.PI * seconds);
    }
    if (controls.forward) {
        walkPlayer(game, 3 * seconds);
    }
    if (controls.backward) {
        walkPlayer(game, -3 * seconds);
    }
}

function walkPlayer(game, distance) {
    const dx = Math.cos(game.player.direction) * distance;
    const dy = Math.sin(game.player.direction) * distance;
    if (getMapPoint(game, game.player.x + dx, game.player.y) <= 0) {
        game.player.x += dx;
    }
    if (getMapPoint(game, game.player.x, game.player.y + dy) <= 0) {
        game.player.y += dy;
    }
}

// Start
play(newGame());
