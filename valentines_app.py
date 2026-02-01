import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Valentine 💖")

# Kill Streamlit scroll completely
st.markdown(
    """
    <style>
    html, body, [data-testid="stApp"] {
        height: 100vh;
        overflow: hidden !important;
    }
    iframe {
        height: 100vh !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
}

html, body {
    margin: 0;
    height: 100%;
    overflow: hidden;
}

body {
    background: linear-gradient(135deg, #fbd3e9, #fcefee);
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Card */
.card {
    background: #ffffff;
    width: min(92%, 420px);
    padding: 2rem;
    border-radius: 22px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.18);
    text-align: center;
    position: relative;
}

/* Icon */
.icon {
    font-size: 3.6rem;
    margin-bottom: 1rem;
}

/* Question */
.question {
    font-size: 1.35rem;
    font-weight: 500;
    margin-bottom: 2rem;
    color: #111827;
}

/* Buttons */
.buttons {
    display: flex;
    justify-content: center;
    gap: 1.6rem;
}

button {
    border: none;
    padding: 0.75rem 2.2rem;
    border-radius: 999px;
    font-size: 0.9rem;
    cursor: pointer;
}

/* YES */
.yes {
    background: #ec4899;
    color: white;
    box-shadow: 0 12px 30px rgba(236,72,153,0.45);
}

.yes:hover {
    transform: translateY(-1px);
}

/* NO (visible but shy) */
.no {
    background: #f3f4f6;
    color: #111827;
    border: 1px solid #d1d5db;
    box-shadow: 0 10px 22px rgba(0,0,0,0.12);
    position: relative;
}

/* Helper text */
.helper {
    font-size: 0.75rem;
    margin-top: 1.3rem;
    color: #6b7280;
}

/* Celebration state */
.celebrate {
    display: none;
}

.celebrate h2 {
    margin: 1rem 0;
}

/* Confetti */
.confetti {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.confetti span {
    position: absolute;
    width: 8px;
    height: 8px;
    background: #ec4899;
    animation: fall 2s linear infinite;
}

@keyframes fall {
    to { transform: translateY(100vh); }
}
</style>
</head>

<body>

<div class="card">
    <!-- ASK STATE -->
    <div id="ask">
        <div class="icon">🐱💖</div>
        <div class="question">will you be my valentine?</div>

        <div class="buttons">
            <button class="yes" onclick="sayYes()">Yes</button>
            <button class="no" id="noBtn">No</button>
        </div>

        <div class="helper">the "No" button is feeling shy 🙈</div>
    </div>

    <!-- YES STATE -->
    <div class="celebrate" id="yay">
        <div class="icon">🎉</div>
        <h2>YAY!</h2>
        <img
            src="https://media.giphy.com/media/26xBs99iqmmSLYGqY/giphy.gif"
            style="width:100%; border-radius:14px;"
        />
    </div>

    <div class="confetti" id="confetti"></div>
</div>

<script>
const noBtn = document.getElementById("noBtn");

// Evade cursor
noBtn.addEventListener("mouseenter", moveAway);
noBtn.addEventListener("mousemove", moveAway);

// Block all clicks
["click","mousedown","mouseup"].forEach(evt =>
    noBtn.addEventListener(evt, e => e.preventDefault())
);

function moveAway() {
    const x = Math.random() * (window.innerWidth - 140);
    const y = Math.random() * (window.innerHeight - 80);
    noBtn.style.position = "fixed";
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
}

function sayYes() {
    document.getElementById("ask").style.display = "none";
    document.getElementById("yay").style.display = "block";
    launchConfetti();
}

function launchConfetti() {
    const confetti = document.getElementById("confetti");
    for (let i = 0; i < 45; i++) {
        const piece = document.createElement("span");
        piece.style.left = Math.random() * 100 + "%";
        piece.style.animationDuration = (1 + Math.random() * 2) + "s";
        confetti.appendChild(piece);
    }
}
</script>

</body>
</html>
"""

components.html(html, height=1, scrolling=False)
