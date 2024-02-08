document.addEventListener('keypress', enterListener);
function enterListener(e) {
    if (e.keyCode == 13) {
        reset();
    }
}

var collisionCount = 0
var x1 = 400
var x2 = 100
var v1 = -1
var v2 = 0
var m1 = Number(document.getElementById('weight1').value)
var m2 = Number(document.getElementById('weight2').value)
var delay = Number(document.getElementById('delay').value)
console.log(m1, m2)

var canvas = document.getElementById('canvas'),
    cw = canvas.width,
    ch = canvas.height,
    cx = null;

function reset() {
    x1 = 300
    x2 = 100
    v1 = -1
    v2 = 0
    m1 = Number(document.getElementById('weight1').value)
    m2 = Number(document.getElementById('weight2').value)
    collisionCount = 0
    delay = Number(document.getElementById('delay').value)
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


function loop() {
    let tickTime = 0
    while (1) {
        if (v2 < 0) {
            let t = Math.abs((x2 / v2))
            if (tickTime + t >= delay) {
                let delta = delay - tickTime
                x2 += v2 * delta
                x1 += v1 * delta
                break
            } else {
                collisionCount++
                tickTime += t
                x2 = 0
                x1 += v1 * t
                v2 *= -1

            }
        }

        let n = ((x2 + 100) - x1) / (v1 - v2)

        if (tickTime + n >= delay || v2 < v1) {
            let delta = delay - tickTime
            x2 += v2 * delta
            x1 += v1 * delta
            break
        } else {
            collisionCount++
            let dvv = (-2.0 * (m1) * (v1 - v2)) / (m1 + m2)
            v2 -= dvv
            v1 -= -1 * (dvv * (m2 / m1))

            x1 += v1 * n
            x2 += v2 * n
            tickTime += n
        }
    }

    cx.fillStyle = "#473f3f"
    cx.fillRect(0, 0, cw, ch)
    cx.fillStyle = "#349eeb";
    cx.fillRect(x2, 400, 100, 100);
    cx.fillStyle = "#349eeb";
    cx.fillRect(x1, 400, 100, 100);
    sleep(20)
    cx.fillStyle = "#eb9f34";
    cx.font = "30px Arial";
    cx.fillText("Счетчик столкновений: " + collisionCount, 160, 50);
    cx.fillText("Скорость m1: " + v1.toFixed(3), 160, 100);
    cx.fillText("Скорость m2: " + v2.toFixed(3), 160, 150);
}

if (typeof (canvas.getContext) !== undefined) {
    cx = canvas.getContext('2d');
    setInterval(loop, 10)
}