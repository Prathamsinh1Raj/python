from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wedding Invitation</title>

<style>
body {
    margin: 0;
    padding: 0;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(to bottom right, #fff0f5, #ffe6f0);
    overflow: hidden;
}

.container {
    position: relative;
    top: 20vh;
    padding: 20px;
}

h1 {
    font-size: 8vw;
    color: #b30059;
    animation: glow 1.5s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #ff99cc; }
    to { text-shadow: 0 0 25px #ff1a75; }
}

.details {
    font-size: 4.5vw;
    margin-top: 20px;
    color: #800040;
}

.heart {
    position: absolute;
    color: #ff4d6d;
    animation: float 5s linear infinite;
}

@keyframes float {
    from { transform: translateY(100vh); opacity: 1; }
    to { transform: translateY(-10vh); opacity: 0; }
}

button {
    margin-top: 30px;
    padding: 12px 20px;
    font-size: 4vw;
    background: #ff1a75;
    color: white;
    border: none;
    border-radius: 30px;
}
</style>
</head>

<body>

<div class="container">
    <h1>Amirajsinh ❤️ Dishaba</h1>
    <div class="details">
        Together with their families<br><br>
        Invite you to celebrate their wedding<br><br>
        Sunday, 24th December 2026<br>
        Grand Palace Banquet Hall<br>
        7:00 PM onwards
    </div>

    <button onclick="playMusic()">🎵 Tap to Play Music</button>
</div>

<audio id="bgMusic" loop>
    <source src="/music" type="audio/mpeg">
</audio>

<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = Math.random() * 20 + 20 + "px";
    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 5000);
}

setInterval(createHeart, 500);

function playMusic() {
    document.getElementById("bgMusic").play();
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)

@app.route("/music")
def music():
    return app.send_static_file("wedding-music.mp3")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
