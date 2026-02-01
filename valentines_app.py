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

    html {
        height: 100vh !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        overscroll-behavior: none !important;
        -webkit-overflow-scrolling: none !important;
        touch-action: none !important;
    }

    body, [data-testid="stApp"] {
        height: 100vh !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        overscroll-behavior: none !important;
        -webkit-overflow-scrolling: none !important;
        touch-action: none !important;
    }

    iframe {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        overflow: hidden !important;
        overscroll-behavior: none !important;
        scrolling: no !important;
    }
    
    /* Lock iframe content */
    iframe[data-testid="stIframe"] {
        overflow: hidden !important;
        scrolling: no !important;
    }

    /* Prevent all scrolling on EVERY element */
    *, *::before, *::after {
        overscroll-behavior: none !important;
        -webkit-overflow-scrolling: none !important;
        touch-action: none !important;
    }

    /* Lock all containers */
    .main, .block-container, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        position: fixed !important;
        height: 100vh !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }

    /* Hide scrollbars everywhere */
    ::-webkit-scrollbar {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
        background: transparent !important;
    }

    * {
        -ms-overflow-style: none !important;
        scrollbar-width: none !important;
    }

    /* Prevent any element from being scrollable */
    div, section, article, main, aside, header, footer {
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
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, viewport-fit=cover" />

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
    -webkit-tap-highlight-color: transparent;
}

html {
    height: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    overscroll-behavior: none !important;
    -webkit-overflow-scrolling: none !important;
    touch-action: none !important;
    -ms-touch-action: none !important;
}

body {
    height: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    background: linear-gradient(135deg, #fbd3e9, #fcefee);
    display: flex;
    align-items: center;
    justify-content: center;
    overscroll-behavior: none !important;
    -webkit-overflow-scrolling: none !important;
    touch-action: none !important;
    -ms-touch-action: none !important;
}

/* Hide scrollbars */
::-webkit-scrollbar {
    display: none;
    width: 0;
    height: 0;
}

* {
    overscroll-behavior: none;
    -webkit-overflow-scrolling: none;
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
(function() {
    'use strict';
    
    // Store original scroll positions
    let scrollX = 0;
    let scrollY = 0;
    
    // ULTRA AGGRESSIVE SCROLL LOCK - Multiple methods
    function ultraLockScroll() {
        // Method 1: Force scroll to 0
        if (window.scrollX !== 0 || window.scrollY !== 0) {
            window.scrollTo(0, 0);
            window.scroll(0, 0);
        }
        
        // Method 2: Lock document elements
        if (document.documentElement.scrollTop !== 0 || document.documentElement.scrollLeft !== 0) {
            document.documentElement.scrollTop = 0;
            document.documentElement.scrollLeft = 0;
        }
        
        // Method 3: Lock body
        if (document.body.scrollTop !== 0 || document.body.scrollLeft !== 0) {
            document.body.scrollTop = 0;
            document.body.scrollLeft = 0;
        }
        
        // Method 4: Force styles
        document.documentElement.style.setProperty('overflow', 'hidden', 'important');
        document.documentElement.style.setProperty('position', 'fixed', 'important');
        document.documentElement.style.setProperty('top', '0', 'important');
        document.documentElement.style.setProperty('left', '0', 'important');
        document.documentElement.style.setProperty('width', '100%', 'important');
        document.documentElement.style.setProperty('height', '100%', 'important');
        
        document.body.style.setProperty('overflow', 'hidden', 'important');
        document.body.style.setProperty('position', 'fixed', 'important');
        document.body.style.setProperty('top', '0', 'important');
        document.body.style.setProperty('left', '0', 'important');
        document.body.style.setProperty('width', '100%', 'important');
        document.body.style.setProperty('height', '100%', 'important');
        
        // Method 5: Lock all scrollable elements
        const allElements = document.querySelectorAll('*');
        allElements.forEach(el => {
            if (el.scrollTop !== 0 || el.scrollLeft !== 0) {
                el.scrollTop = 0;
                el.scrollLeft = 0;
            }
            el.style.setProperty('overflow', 'hidden', 'important');
        });
        
        // Continue locking
        requestAnimationFrame(ultraLockScroll);
    }
    
    // Start immediately
    ultraLockScroll();
    
    // Also use setInterval as backup
    setInterval(function() {
        window.scrollTo(0, 0);
        document.documentElement.scrollTop = 0;
        document.documentElement.scrollLeft = 0;
        document.body.scrollTop = 0;
        document.body.scrollLeft = 0;
    }, 10);
    
    // Prevent ALL scroll events - Ultra aggressive
    const killScroll = function(e) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        window.scrollTo(0, 0);
        return false;
    };
    
    // Block every possible scroll event
    const scrollEvents = [
        'scroll', 'wheel', 'mousewheel', 'DOMMouseScroll', 'MozMousePixelScroll',
        'touchstart', 'touchmove', 'touchend', 'touchcancel',
        'gesturestart', 'gesturechange', 'gestureend',
        'keydown', 'keyup'
    ];
    
    scrollEvents.forEach(event => {
        // Add to document
        document.addEventListener(event, killScroll, { passive: false, capture: true });
        // Add to documentElement
        document.documentElement.addEventListener(event, killScroll, { passive: false, capture: true });
        // Add to body
        document.body.addEventListener(event, killScroll, { passive: false, capture: true });
        // Add to window
        window.addEventListener(event, killScroll, { passive: false, capture: true });
    });
    
    // Prevent keyboard scrolling
    document.addEventListener('keydown', function(e) {
        if ([32, 33, 34, 35, 36, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
            e.preventDefault();
            return false;
        }
    }, { passive: false, capture: true });
    
    // Prevent touch scrolling completely
    let lastTouchY = 0;
    document.addEventListener('touchstart', function(e) {
        lastTouchY = e.touches[0].clientY;
        e.preventDefault();
    }, { passive: false, capture: true });
    
    document.addEventListener('touchmove', function(e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    }, { passive: false, capture: true });
    
    // Lock on any event
    ['resize', 'orientationchange', 'load', 'DOMContentLoaded'].forEach(event => {
        window.addEventListener(event, function() {
            setTimeout(function() {
                window.scrollTo(0, 0);
                document.documentElement.scrollTop = 0;
                document.body.scrollTop = 0;
            }, 0);
        });
    });
    
    // MutationObserver to watch for style changes
    const observer = new MutationObserver(function() {
        window.scrollTo(0, 0);
        document.documentElement.scrollTop = 0;
        document.body.scrollTop = 0;
    });
    
    observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['style', 'class'],
        childList: true,
        subtree: true
    });
    
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['style', 'class'],
        childList: true,
        subtree: true
    });
})();

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

# ⚠️ height=1 is intentional - prevents iframe scrolling
components.html(html, height=1, scrolling=False)
