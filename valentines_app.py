import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valentine 💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 🔒 HARD RESET STREAMLIT LAYOUT (THIS IS THE KEY)
st.markdown(
    """
    <style>
    /* Remove Streamlit default spacing */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
    }

    header, footer {
        display: none !important;
    }

    html, body, [data-testid="stApp"] {
        height: 100vh !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        position: fixed !important;
    }

    iframe {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        overflow: hidden !important;
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
<meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
    -webkit-tap-highlight-color: transparent;
}

html, body {
    height: 100%;
    width: 100%;
    margin: 0;
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
    background: white;
    width: min(92vw, 420px);
    padding: 2rem;
    border-radius: 22px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.18);
    text-align: center;
    position: relative;
}

/* Icon */
.icon {
    font-size: 3.5rem;
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

/* NO */
.no {
    background: #f3f4f6;
    color: #111827;
    border: 1px solid #d1d5db;
    box-shadow: 0 10px 22px rgba(0,0,0,0.12);
    position: relative;
}

/* Helper */
.helper {
    font-size: 0.75rem;
    margin-top: 1.3rem;
    color: #6b7280;
}

/* Celebrate */
.celebrate {
    display: none;
}

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
    <div id="ask">
        <div class="icon">🐱💖</div>
        <div class="question">will you be my valentine?</div>

        <div class="buttons">
            <button class="yes" onclick="sayYes()">Yes</button>
            <button class="no" id="noBtn">No</button>
        </div>

        <div class="helper">the "No" button is feeling shy 🙈</div>
    </div>

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

function moveAway() {
    const x = Math.random() * (window.innerWidth - 140);
    const y = Math.random() * (window.innerHeight - 100);
    noBtn.style.position = "fixed";
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
}

noBtn.addEventListener("mouseenter", moveAway);
noBtn.addEventListener("mousemove", moveAway);
noBtn.addEventListener("touchstart", moveAway);

["click","mousedown","mouseup","touchend"].forEach(evt =>
    noBtn.addEventListener(evt, e => e.preventDefault())
);

function sayYes() {
    document.getElementById("ask").style.display = "none";
    document.getElementById("yay").style.display = "block";
    launchConfetti();
}

function launchConfetti() {
    const confetti = document.getElementById("confetti");
    for (let i = 0; i < 40; i++) {
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

# ⚠️ height=1 is intentional
components.html(html, height=1, scrolling=False)
