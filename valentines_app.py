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

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
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

/* Floating background */
.floating-bg {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 1;
}

.floating-bg span {
    position: absolute;
    font-size: 2rem;
    opacity: 0.12;
    animation: floatUp 8s ease-in infinite;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.15; }
    90% { opacity: 0.08; }
    100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
}

/* Main card */
.card {
    background: linear-gradient(180deg, #ffffff 0%, #faf8f6 50%, #f5f2ef 100%);
    width: min(92vw, 760px);
    padding: 2.25rem 2rem;
    border-radius: 28px;
    box-shadow: 0 30px 80px rgba(139, 100, 80, 0.08), inset 0 1px 0 rgba(255,255,255,0.4);
    text-align: center;
    position: relative;
    color: #5a4a42;
    border: 1px solid rgba(212, 196, 184, 0.2);
    z-index: 2;
}

/* Stage containers */
.stage {
    display: none;
    animation: fadeIn 0.6s ease;
}

.stage.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ===== STAGE 1: INTRO ===== */
.intro-icon {
    font-size: 5rem;
    margin-bottom: 1rem;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.intro-subtitle {
    font-size: 0.8rem;
    font-weight: 500;
    color: #c9a68e;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.intro-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #5a4a42;
    margin-bottom: 1.5rem;
    line-height: 1.4;
}

.tap-hint {
    font-size: 0.85rem;
    color: #c9a68e;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

/* ===== STAGE 2: CARDS ===== */
.cards-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #5a4a42;
    margin-bottom: 1.2rem;
}

.cards-row {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
}

.flip-card {
    width: 100px;
    height: 140px;
    perspective: 600px;
    cursor: pointer;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
}

.flip-card.flipped .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 14px;
    backface-visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    font-weight: 600;
    padding: 0.6rem;
}

.flip-card-front {
    background: linear-gradient(135deg, #b8856a, #c9a68e);
    color: white;
    font-size: 2rem;
    box-shadow: 0 8px 25px rgba(184, 133, 106, 0.2);
}

.flip-card-back {
    background: linear-gradient(180deg, #fff, #faf8f6);
    color: #5a4a42;
    transform: rotateY(180deg);
    border: 2px solid rgba(184, 133, 106, 0.15);
    font-size: 0.78rem;
    line-height: 1.4;
    text-align: center;
}

.cards-progress {
    font-size: 0.8rem;
    color: #c9a68e;
    margin-top: 0.5rem;
}

/* ===== STAGE 3: COMPATIBILITY ===== */
.compat-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #5a4a42;
    margin-bottom: 1.5rem;
}

.meter-container {
    background: #f0ebe5;
    border-radius: 999px;
    height: 28px;
    width: 85%;
    margin: 0 auto 1rem;
    overflow: hidden;
    position: relative;
}

.meter-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #c9a68e, #b8856a, #a06b4a);
    border-radius: 999px;
    transition: width 0.3s ease;
}

.meter-percent {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(90deg, #b8856a, #c9a68e, #b8856a);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 2s linear infinite;
    margin-bottom: 0.5rem;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.meter-status {
    font-size: 1rem;
    font-weight: 600;
    color: #9d7961;
    min-height: 1.5rem;
}

/* ===== STAGE 4: THE QUESTION ===== */
.question-icon {
    font-size: 3rem;
    margin-bottom: 0.6rem;
}

.question-subtitle {
    font-size: 0.85rem;
    font-weight: 500;
    color: #c9a68e;
    margin-bottom: 0.8rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.question-text {
    font-size: 1.7rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
    background: linear-gradient(90deg, #b8856a, #c9a68e, #b8856a);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    line-height: 1.3;
}

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

.yes {
    background: linear-gradient(90deg, #b8856a, #c9a68e);
    color: white;
    box-shadow: 0 18px 50px rgba(184, 133, 106, 0.15), 0 6px 18px rgba(0,0,0,0.1);
    font-weight: 800;
    width: 13rem;
    padding: 1rem 2.8rem;
    font-size: 1.05rem;
    border-radius: 999px;
    animation: btnPulse 2s ease-in-out infinite;
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

@keyframes btnPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

@keyframes glow {
    0%, 100% { opacity: 0; }
    50% { opacity: 0.6; }
}

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
}

/* ===== STAGE 5: CELEBRATE ===== */
.celebrate {
    display: none;
}

.celebrate h2 {
    font-size: 1.5rem;
    color: #5a4a42;
    margin-bottom: 0.5rem;
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
    0%, 100% { opacity: 0; transform: scale(0); }
    50% { opacity: 1; transform: scale(1); }
}

</style>
</head>

<body>

<div class="floating-bg" id="floatingBg"></div>

<div class="card">
    <div class="sparkles" id="sparkles"></div>

    <!-- STAGE 1: INTRO -->
    <div class="stage active" id="stage1" onclick="goToStage(2)">
        <div class="intro-icon">✨</div>
        <div class="intro-subtitle">Valentine's: The Sequel 🎬</div>
        <div class="intro-title">Hey Malavika...<br>I made something for you 😊</div>
        <div class="tap-hint">tap to see what's up 👀</div>
    </div>

    <!-- STAGE 2: CARD PICK -->
    <div class="stage" id="stage2">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🃏</div>
        <div class="cards-title">Pick your cards</div>
        <div class="cards-row">
            <div class="flip-card" onclick="flipCard(this, 0)">
                <div class="flip-card-inner">
                    <div class="flip-card-front">?</div>
                    <div class="flip-card-back">First date? Nailed it. ✅</div>
                </div>
            </div>
            <div class="flip-card" onclick="flipCard(this, 1)">
                <div class="flip-card-inner">
                    <div class="flip-card-front">?</div>
                    <div class="flip-card-back">Vibe check? Off the charts 📊</div>
                </div>
            </div>
            <div class="flip-card" onclick="flipCard(this, 2)">
                <div class="flip-card-inner">
                    <div class="flip-card-front">?</div>
                    <div class="flip-card-back">The universe says... keep reading 🔮</div>
                </div>
            </div>
        </div>
        <div class="cards-progress" id="cardsProgress">Tap each card to reveal 👆</div>
    </div>

    <!-- STAGE 3: COMPATIBILITY METER -->
    <div class="stage" id="stage3">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
        <div class="compat-title">Running compatibility check...</div>
        <div class="meter-percent" id="meterPercent">0%</div>
        <div class="meter-container">
            <div class="meter-fill" id="meterFill"></div>
        </div>
        <div class="meter-status" id="meterStatus"></div>
    </div>

    <!-- STAGE 4: THE QUESTION -->
    <div class="stage" id="stage4">
        <div class="question-icon">😊🌟✨</div>
        <div class="question-subtitle">Valentine's: The Sequel 🎬</div>
        <div class="question-text">So Malavika... second date on Valentine's?<br>Perfect timing right? 😏✨</div>

        <div class="buttons">
            <button class="yes" id="yesBtn" onclick="sayYes()">Yes! 😊</button>
            <button class="no" id="noBtn">No 😅</button>
        </div>

        <div class="helper">No pressure, just good vibes ✨</div>
    </div>

    <!-- STAGE 5: CELEBRATION -->
    <div class="stage" id="stage5">
        <div style="font-size: 3.5rem; margin-bottom: 0.5rem; animation: float 2s ease-in-out infinite;">🎉😊</div>
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

<script>
// ===== STAGE MANAGEMENT =====
function goToStage(num) {
    document.querySelectorAll('.stage').forEach(s => s.classList.remove('active'));
    const stage = document.getElementById('stage' + num);
    stage.classList.add('active');
    stage.style.animation = 'none';
    stage.offsetHeight; // trigger reflow
    stage.style.animation = 'fadeIn 0.6s ease';

    if (num === 3) startCompatibility();
}

// ===== STAGE 2: CARD FLIP =====
let cardsFlipped = 0;

function flipCard(el, idx) {
    if (el.classList.contains('flipped')) return;
    el.classList.add('flipped');
    cardsFlipped++;

    const progress = document.getElementById('cardsProgress');
    if (cardsFlipped === 1) progress.textContent = '1 of 3 revealed... keep going! 🔥';
    if (cardsFlipped === 2) progress.textContent = '2 of 3... one more! 👀';
    if (cardsFlipped === 3) {
        progress.textContent = 'All cards revealed! ✨';
        setTimeout(() => goToStage(3), 1200);
    }
}

// ===== STAGE 3: COMPATIBILITY METER =====
function startCompatibility() {
    const fill = document.getElementById('meterFill');
    const percent = document.getElementById('meterPercent');
    const status = document.getElementById('meterStatus');
    let current = 0;
    const target = 110;

    const messages = [
        { at: 0, text: 'Initializing... 🔄' },
        { at: 15, text: 'Analyzing vibes... 🎵' },
        { at: 35, text: 'Checking humor compatibility... 😂' },
        { at: 55, text: 'Looking good... 👀' },
        { at: 75, text: 'Oh wow... 🫣' },
        { at: 90, text: 'Wait... is this right?! 😳' },
        { at: 105, text: 'COMPATIBILITY OVERLOAD 🔥' }
    ];

    const interval = setInterval(() => {
        current++;
        const displayPercent = Math.min(current, target);
        const fillWidth = Math.min((current / target) * 100, 100);
        fill.style.width = fillWidth + '%';
        percent.textContent = displayPercent + '%';

        // Update status message
        for (let i = messages.length - 1; i >= 0; i--) {
            if (current >= messages[i].at) {
                status.textContent = messages[i].text;
                break;
            }
        }

        if (current >= target) {
            clearInterval(interval);
            setTimeout(() => goToStage(4), 1500);
        }
    }, 30);
}

// ===== STAGE 4: YES/NO BUTTONS =====
const noBtn = document.getElementById('noBtn');
const yesBtn = document.getElementById('yesBtn');
let noClickCount = 0;

function handleNoClick(e) {
    e.stopPropagation();
    noClickCount = Math.min(noClickCount + 1, 100);

    const grow = 1 + Math.min(noClickCount * 0.08, 1.5);
    const shrink = Math.max(1 - Math.min(noClickCount * 0.06, 0.7), 0.35);
    yesBtn.style.transform = 'scale(' + grow + ')';
    noBtn.style.transform = 'scale(' + shrink + ')';
    noBtn.style.opacity = '' + Math.max(0.35, shrink);

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

noBtn.addEventListener('mouseenter', moveAwayShort);
noBtn.addEventListener('mousemove', moveAwayShort);
noBtn.addEventListener('touchstart', moveAwayShort);
noBtn.addEventListener('click', handleNoClick);
noBtn.addEventListener('touchstart', function(e) { e.preventDefault(); handleNoClick(e); });

// ===== STAGE 5: CELEBRATION =====
function sayYes() {
    goToStage(5);
    launchConfetti();
}

function launchConfetti() {
    const confetti = document.getElementById('confetti');
    for (let i = 0; i < 80; i++) {
        const piece = document.createElement('span');
        piece.style.left = Math.random() * 100 + '%';
        piece.style.background = ['#b8856a','#c9a68e','#d4c4b8','#d4a574','#e8c9a0'][Math.floor(Math.random()*5)];
        piece.style.width = (6 + Math.random() * 10) + 'px';
        piece.style.height = piece.style.width;
        piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
        piece.style.animationDuration = (1 + Math.random() * 2.5) + 's';
        piece.style.top = (-20 - Math.random() * 40) + 'px';
        confetti.appendChild(piece);
        setTimeout(() => piece.remove(), 4000);
    }
}

// ===== BACKGROUND FLOATING ELEMENTS =====
function createFloatingElements() {
    const container = document.getElementById('floatingBg');
    const items = ['🤍', '🤎', '✨', '🌟', '💫', '⭐'];

    setInterval(() => {
        const el = document.createElement('span');
        el.textContent = items[Math.floor(Math.random() * items.length)];
        el.style.left = Math.random() * 100 + '%';
        el.style.fontSize = (1 + Math.random() * 1.5) + 'rem';
        el.style.animationDuration = (6 + Math.random() * 4) + 's';
        el.style.animationDelay = Math.random() * 2 + 's';
        container.appendChild(el);
        setTimeout(() => el.remove(), 10000);
    }, 1000);
}

function createSparkles() {
    const container = document.getElementById('sparkles');
    const positions = [
        { top: '10%', left: '5%' }, { top: '20%', right: '8%' },
        { top: '50%', left: '2%' }, { top: '70%', right: '5%' },
        { top: '85%', left: '10%' }, { top: '15%', right: '15%' },
        { bottom: '15%', left: '12%' }, { bottom: '25%', right: '10%' }
    ];

    positions.forEach((pos, i) => {
        const sparkle = document.createElement('span');
        Object.assign(sparkle.style, pos);
        sparkle.style.animationDelay = (i * 0.3) + 's';
        container.appendChild(sparkle);
    });
}

createFloatingElements();
createSparkles();
</script>

</body>
</html>
"""

# ⚠️ height=1 is intentional
components.html(html, height=1, scrolling=False)
