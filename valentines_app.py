import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valentine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

components.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">

<style>
/* ------------------ HARD STOP SCROLL ------------------ */
html, body {
    height: 100vh;
    width: 100vw;
    margin: 0;
    overflow: hidden !important;
}

/* ------------------ BACKGROUND ------------------ */
body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(
        120deg,
        #7c3aed,
        #ec4899,
        #3b82f6,
        #f97316
    );
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ------------------ CENTER CONTENT ------------------ */
.container {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card {
    background: rgba(255,255,255,0.95);
    padding: clamp(32px, 6vw, 56px);
    border-radius: 24px;
    text-align: center;
    box-shadow: 0 30px 80px rgba(0,0,0,0.25);
    width: min(90vw, 420px);
    position: relative;
}

.question {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 6vw, 40px);
    margin-bottom: 32px;
    color: #111827;
}

/* ------------------ BUTTONS ------------------ */
.buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
}

button {
    padding: 14px 32px;
    font-size: 14px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    border-radius: 999px;
    border: none;
    cursor: pointer;
    font-weight: 600;
}

/* YES BUTTON */
.yes {
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    color: white;
    box-shadow: 0 10px 25px rgba(236,72,153,0.4);
}

.yes:hover {
    transform: translateY(-2px);
}

/* NO BUTTON (VISIBLE BUT SHY) */
.no {
    background: #f3f4f6;
    color: #111827;
    border: 1px solid #d1d5db;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    position: relative;
    touch-action: manipulation;
}

/* ------------------ MODAL ------------------ */
.overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    backdrop-filter: blur(8px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 10;
}

.modal {
    background: white;
    border-radius: 22px;
    width: min(90vw, 420px);
    box-shadow: 0 30px 80px rgba(0,0,0,0.3);
    overflow: hidden;
}

.modal-bar {
    height: 6px;
    background: linear-gradient(90deg, #7c3aed, #ec4899, #3b82f6);
}

.modal-content {
    padding: 36px;
    text-align: center;
}

.modal h2 {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    margin-bottom: 10px;
}

.modal p {
    color: #4b5563;
    margin-bottom: 26px;
}

.close {
    background: #111827;
    color: white;
    padding: 12px 28px;
    border-radius: 999px;
    cursor: pointer;
}
</style>
</head>

<body>

<div class="container" id="main">
    <div class="card">
        <div class="question">will you be my valentine?</div>
        <div class="buttons">
            <button class="yes" onclick="openModal()">Yes</button>
            <button class="no" id="noBtn">No</button>
        </div>
    </div>
</div>

<!-- MODAL -->
<div class="overlay" id="overlay">
    <div class="modal">
        <div class="modal-bar"></div>
        <div class="modal-content">
            <h2>Wonderful!</h2>
            <p>I’m really happy you said yes 💖</p>
            <button class="close" onclick="closeModal()">Close</button>
        </div>
    </div>
</div>

<script>
const noBtn = document.getElementById("noBtn");

function moveAway() {
    const bw = noBtn.offsetWidth;
    const bh = noBtn.offsetHeight;

    const maxX = window.innerWidth - bw - 12;
    const maxY = window.innerHeight - bh - 12;

    const x = Math.random() * maxX;
    const y = Math.random() * maxY;

    noBtn.style.position = "fixed";
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
}

/* Pointer events = iOS safe */
noBtn.addEventListener("pointerenter", moveAway);
noBtn.addEventListener("pointerdown", (e) => {
    e.preventDefault();
    moveAway();
});
noBtn.addEventListener("click", e => e.preventDefault());

function openModal() {
    document.getElementById("overlay").style.display = "flex";
}

function closeModal() {
    document.getElementById("overlay").style.display = "none";
}
</script>

</body>
</html>
""",
    height=1000,
)
