import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valentine's: The Sequel 🎬✨",
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
    background: linear-gradient(135deg, #f5f0eb 0%, #e8ddd5 30%, #d4c4b8 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

/* Floating hearts background */
.floating-hearts {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 1;
}

.floating-hearts span {
    position: absolute;
    font-size: 2rem;
    opacity: 0.15;
    animation: floatUp 8s ease-in infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 0;
    }
    10% { opacity: 0.4; }
    90% { opacity: 0.2; }
    100% {
        transform: translateY(-100px) rotate(360deg);
        opacity: 0;
    }
}

/* Card */
.card {
    background: linear-gradient(180deg, #ffffff 0%, #faf8f6 50%, #f5f2ef 100%);
    width: min(92vw, 760px);
    padding: 2.25rem 2.6rem;
    border-radius: 28px;
    box-shadow: 0 30px 80px rgba(139, 100, 80, 0.08), inset 0 1px 0 rgba(255,255,255,0.4);
    text-align: center;
    position: relative;
    color: #5a4a42;
    border: 1px solid rgba(212, 196, 184, 0.2);
    z-index: 2;
    animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Icon */
.icon {
    font-size: 3.8rem;
    margin-bottom: 0.6rem;
    animation: bounce 2s ease-in-out infinite;
    display: inline-block;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-15px) scale(1.1); }
}

/* Subtitle */
.subtitle {
    font-size: 0.85rem;
    font-weight: 500;
    color: #c9a68e;
    margin-bottom: 0.8rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

/* Question */
.question {
    font-size: 1.9rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
    background: linear-gradient(90deg, #b8856a, #c9a68e, #b8856a);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

/* Buttons */
.buttons {
    display: flex;
    justify-content: center;
    gap: 1.4rem;
    align-items: center;
}

button {
    border: none;
    padding: 0.9rem 2.6rem;
    border-radius: 999px;
    font-size: 1rem;
    cursor: pointer;
    transition: transform 280ms cubic-bezier(.2,.9,.2,1), width 280ms ease, opacity 220ms ease;
}

/* YES */
.yes {
    background: linear-gradient(90deg, #b8856a, #c9a68e);
    color: white;
    box-shadow: 0 18px 50px rgba(184, 133, 106, 0.15), 0 6px 18px rgba(0,0,0,0.1);
    font-weight: 800;
    width: 13rem;
    padding: 1rem 2.8rem;
    font-size: 1.05rem;
    border-radius: 999px;
    animation: pulse 2s ease-in-out infinite;
    position: relative;
}

.yes::before {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 999px;
    background: linear-gradient(90deg, #b8856a, #c9a68e);
    opacity: 0;
    animation: glow 2s ease-in-out infinite;
    z-index: -1;
    filter: blur(12px);
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

@keyframes glow {
    0%, 100% { opacity: 0; }
    50% { opacity: 0.6; }
}

/* NO */
.no {
    background: linear-gradient(180deg, #faf8f6, #f0ebe5);
    color: #8b6450;
    border: 2px solid rgba(184, 133, 106, 0.15);
    box-shadow: 0 10px 30px rgba(139, 100, 80, 0.05);
    position: relative;
    width: 7.2rem;
    padding: 0.9rem 1.2rem;
    font-weight: 600;
}

.helper {
    font-size: 0.95rem;
    margin-top: 0.8rem;
    color: #9d7961;
    animation: shake 3s ease-in-out infinite;
    display: inline-block;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-3px); }
    75% { transform: translateX(3px); }
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
    background: #b8856a;
    animation: fall 2s linear infinite;
}

@keyframes fall {
    to { transform: translateY(100vh); }
}

/* Popup - Hidden */
.popup {
    display: none !important;
}

.small-note {
    font-size: 0.78rem;
    color: #c9a68e;
    margin-top: 0.6rem;
    animation: fadeInOut 3s ease-in-out infinite;
}

@keyframes fadeInOut {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
}

/* Sparkles */
.sparkles {
    position: absolute;
    inset: -50px;
    pointer-events: none;
}

.sparkles span {
    position: absolute;
    width: 4px;
    height: 4px;
    background: #d4a574;
    border-radius: 50%;
    animation: sparkle 3s ease-in-out infinite;
    box-shadow: 0 0 10px #d4a574;
}

@keyframes sparkle {
    0%, 100% {
        opacity: 0;
        transform: scale(0);
    }
    50% {
        opacity: 1;
        transform: scale(1);
    }
}

</style>
</head>

<body>

<div class="floating-hearts" id="floatingHearts"></div>

<div class="card">
    <div class="sparkles" id="sparkles"></div>
    <div id="ask">
        <div class="icon">
            <span style="display: inline-block; animation: bounce 2s ease-in-out infinite;">😊</span>
            <span style="display: inline-block; animation: bounce 2s ease-in-out 0.2s infinite;">🌟</span>
            <span style="display: inline-block; animation: bounce 2s ease-in-out 0.4s infinite;">✨</span>
        </div>
        <div class="subtitle">Valentine's: The Sequel 🎬</div>
        <div class="question">So Malavika... second date on Valentine's?
I know, perfect timing right? 😏✨</div>

        <div class="buttons">
            <button class="yes" id="yesBtn" onclick="sayYes()">Yes! 😊</button>
            <button class="no" id="noBtn">No 😅</button>
        </div>

        <div class="helper">No pressure, just good vibes ✨</div>
    </div>

    <div class="celebrate" id="yay">
        <div class="icon">🎉😊</div>
        <h2>Awesome! Date #2 locked in! ✨</h2>
        <p style="font-size: 1.3rem; font-weight: 600; color: #5a4a42; margin: 1rem 0;">
            14th Feb @ 8:30 PM<br>
            I'll pick you up! 🚗💨<br>
            <span style="font-size: 1.1rem; color: #b8856a;">P.S. - Location's a surprise 😏🎁</span>
        </p>
        <img
            src="https://media.giphy.com/media/g9582DNuQppxC/giphy.gif"
            style="width:100%; border-radius:14px; margin-top:8px;"
        />
    </div>

    <div class="confetti" id="confetti"></div>
</div>

<div class="popup" id="popup">
    <img id="popupGif" src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" />
    <div class="txt" id="popupTxt">aww, come on! 😿</div>
</div>

<script>
const noBtn = document.getElementById("noBtn");
const yesBtn = document.getElementById("yesBtn");
const popup = document.getElementById("popup");
const popupTxt = document.getElementById("popupTxt");
const popupGif = document.getElementById("popupGif");

let noClickCount = 0;

const messages = [
    { txt: "aww, don't be shy! 😿", gif: "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" },
    { txt: "I baked cookies 🍪 just for you!", gif: "https://media.giphy.com/media/3o6ZsY7Zb9k6k8fQ2A/giphy.gif" },
    { txt: "We can watch silly cat vids 🐱🎬", gif: "https://media.giphy.com/media/26u4nJPf0JtQPdStq/giphy.gif" },
    { txt: "Pretty please? 🌸✨", gif: "https://media.giphy.com/media/xUPGcyi3G2v6j1V0kY/giphy.gif" },
    { txt: "You're too cute to refuse 😽💖", gif: "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" },
    { txt: "Ok last one — wink wink 😉", gif: "https://media.giphy.com/media/l0MYKzNQ2w5zQk1y0/giphy.gif" },
    { txt: "Fine... I'm turning up the charm! 💫", gif: "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" }
];

function showPopup(msgObj) {
    popupTxt.textContent = msgObj.txt;
    popupGif.src = msgObj.gif;
    popup.classList.add('show');
    clearTimeout(popup._hideTimeout);
    popup._hideTimeout = setTimeout(() => popup.classList.remove('show'), 2500);
}

function handleNoClick(e) {
    e.stopPropagation();
    noClickCount = Math.min(noClickCount + 1, 100);

    // Gradually make YES bigger and NO smaller
    const grow = 1 + Math.min(noClickCount * 0.08, 1.5); // up to ~2.5x
    const shrink = Math.max(1 - Math.min(noClickCount * 0.06, 0.7), 0.35);
    yesBtn.style.transform = `scale(${grow})`;
    noBtn.style.transform = `scale(${shrink})`;
    noBtn.style.opacity = `${Math.max(0.35, shrink)}`;

    // Move button on every click
    moveAwayShort();
}

function moveAwayShort() {
    const margin = 120;
    const x = Math.random() * (window.innerWidth - margin);
    const y = Math.random() * (window.innerHeight - margin);
    noBtn.style.position = 'fixed';
    noBtn.style.left = x + 'px';
    noBtn.style.top = y + 'px';
}

// re-enable hover movement: moves away when hovered or touched
noBtn.addEventListener('mouseenter', moveAwayShort);
noBtn.addEventListener('mousemove', moveAwayShort);
noBtn.addEventListener('touchstart', moveAwayShort);

noBtn.addEventListener('click', handleNoClick);
noBtn.addEventListener('touchstart', function(e){ e.preventDefault(); handleNoClick(e); });

function sayYes() {
    document.getElementById("ask").style.display = "none";
    document.getElementById("yay").style.display = "block";
    launchConfetti();
}

function launchConfetti() {
    const confetti = document.getElementById("confetti");
    for (let i = 0; i < 60; i++) {
        const piece = document.createElement("span");
        piece.style.left = Math.random() * 100 + "%";
        piece.style.background = ['#b8856a','#c9a68e','#d4c4b8','#d4a574'][Math.floor(Math.random()*4)];
        piece.style.width = (6+Math.random()*10) + 'px';
        piece.style.height = piece.style.width;
        piece.style.animationDuration = (1 + Math.random() * 2.5) + "s";
        piece.style.top = (-20 - Math.random()*40) + 'px';
        confetti.appendChild(piece);
        setTimeout(()=> piece.remove(), 4000);
    }
}

// Create floating hearts
function createFloatingHearts() {
    const container = document.getElementById("floatingHearts");
    const hearts = ['🤍', '🤎', '✨', '🌟', '💫', '⭐', '💛'];

    setInterval(() => {
        const heart = document.createElement("span");
        heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
        heart.style.left = Math.random() * 100 + "%";
        heart.style.fontSize = (1 + Math.random() * 1.5) + "rem";
        heart.style.animationDuration = (6 + Math.random() * 4) + "s";
        heart.style.animationDelay = Math.random() * 2 + "s";
        container.appendChild(heart);

        setTimeout(() => heart.remove(), 10000);
    }, 800);
}

// Create sparkles around card
function createSparkles() {
    const container = document.getElementById("sparkles");
    const positions = [
        { top: '10%', left: '5%' },
        { top: '20%', right: '8%' },
        { top: '50%', left: '2%' },
        { top: '70%', right: '5%' },
        { top: '85%', left: '10%' },
        { top: '15%', right: '15%' },
        { bottom: '15%', left: '12%' },
        { bottom: '25%', right: '10%' }
    ];

    positions.forEach((pos, i) => {
        const sparkle = document.createElement("span");
        Object.assign(sparkle.style, pos);
        sparkle.style.animationDelay = (i * 0.3) + "s";
        container.appendChild(sparkle);
    });
}

// Initialize animations
createFloatingHearts();
createSparkles();
</script>

</body>
</html>
"""

# ⚠️ height=1 is intentional
components.html(html, height=1, scrolling=False)
