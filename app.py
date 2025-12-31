"""
Consumer Behaviour Learning Hub - Igloo.inc Style
Immersive dark theme with 3D effects and iridescent gradients
"""

import streamlit as st
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="ConsumerQuest | Learn Consumer Behaviour",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============== IGLOO.INC STYLE CSS ==============
st.markdown("""
<style>
    /* Import Inter Tight Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@100;200;300;400;500;600;700;800;900&display=swap');

    /* Root Variables */
    :root {
        --bg-void: #000000;
        --bg-card: rgba(255, 255, 255, 0.03);
        --bg-card-hover: rgba(255, 255, 255, 0.08);
        --text-primary: #ffffff;
        --text-secondary: rgba(255, 255, 255, 0.6);
        --text-tertiary: rgba(255, 255, 255, 0.4);
        --accent-ice: linear-gradient(135deg, #00f5ff 0%, #7b68ee 25%, #ff6ec7 50%, #00f5ff 75%, #7b68ee 100%);
        --accent-glow: #00f5ff;
        --glass-border: rgba(255, 255, 255, 0.1);
        --glass-bg: rgba(255, 255, 255, 0.05);
    }

    /* Global Styles */
    * {
        font-family: 'Inter Tight', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .stApp {
        background: var(--bg-void);
        background-image:
            radial-gradient(ellipse at 20% 80%, rgba(0, 245, 255, 0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 20%, rgba(123, 104, 238, 0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(255, 110, 199, 0.05) 0%, transparent 70%);
        min-height: 100vh;
    }

    /* Hide Streamlit Defaults */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Floating Particles Background */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: var(--accent-glow);
        border-radius: 50%;
        opacity: 0.3;
        animation: float-particle 20s infinite ease-in-out;
        box-shadow: 0 0 10px var(--accent-glow), 0 0 20px var(--accent-glow);
    }

    @keyframes float-particle {
        0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 0.3; }
        90% { opacity: 0.3; }
        100% { transform: translateY(-100vh) rotate(720deg); opacity: 0; }
    }

    /* Iridescent Text */
    .iridescent-text {
        background: var(--accent-ice);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 8s ease infinite;
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 80px 20px 60px;
        position: relative;
        z-index: 1;
    }

    .hero-title {
        font-size: clamp(48px, 10vw, 120px);
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1;
        margin-bottom: 24px;
        background: var(--accent-ice);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 8s ease infinite;
    }

    .hero-subtitle {
        font-size: clamp(16px, 2vw, 24px);
        font-weight: 300;
        color: var(--text-secondary);
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    .hero-description {
        font-size: clamp(14px, 1.5vw, 18px);
        color: var(--text-tertiary);
        max-width: 600px;
        margin: 0 auto 40px;
        line-height: 1.6;
    }

    /* 3D Ice Shard Logo */
    .ice-shard {
        width: 120px;
        height: 120px;
        margin: 0 auto 40px;
        position: relative;
        transform-style: preserve-3d;
        animation: shard-rotate 20s linear infinite;
    }

    .ice-shard::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0,245,255,0.3) 0%, rgba(123,104,238,0.3) 50%, rgba(255,110,199,0.3) 100%);
        clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        animation: shard-pulse 4s ease-in-out infinite;
    }

    .ice-shard::after {
        content: '🧊';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 48px;
        filter: drop-shadow(0 0 20px var(--accent-glow));
    }

    @keyframes shard-rotate {
        0% { transform: rotateY(0deg) rotateX(10deg); }
        100% { transform: rotateY(360deg) rotateX(10deg); }
    }

    @keyframes shard-pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
    }

    /* Glass Cards */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 24px;
        padding: 32px;
        margin: 16px 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.6s ease;
    }

    .glass-card:hover::before {
        left: 100%;
    }

    .glass-card:hover {
        background: var(--bg-card-hover);
        border-color: rgba(0, 245, 255, 0.3);
        transform: translateY(-8px) scale(1.02);
        box-shadow:
            0 20px 60px rgba(0, 245, 255, 0.15),
            0 0 40px rgba(123, 104, 238, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }

    /* Unit Headers */
    .unit-header {
        background: linear-gradient(135deg, rgba(0,245,255,0.1) 0%, rgba(123,104,238,0.1) 100%);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 24px 32px;
        margin: 40px 0 24px;
        position: relative;
        overflow: hidden;
    }

    .unit-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0,245,255,0.1), transparent);
        animation: rotate-glow 10s linear infinite;
    }

    @keyframes rotate-glow {
        100% { transform: rotate(360deg); }
    }

    .unit-title {
        font-size: clamp(24px, 4vw, 36px);
        font-weight: 700;
        color: var(--text-primary);
        position: relative;
        z-index: 1;
    }

    /* Lesson Nodes - 3D Style */
    .lesson-node-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
    }

    .lesson-node {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        cursor: pointer;
        position: relative;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        transform-style: preserve-3d;
    }

    .lesson-node.available {
        background: linear-gradient(135deg, rgba(0,245,255,0.2) 0%, rgba(123,104,238,0.2) 100%);
        border: 2px solid rgba(0, 245, 255, 0.5);
        box-shadow:
            0 0 30px rgba(0, 245, 255, 0.3),
            inset 0 0 20px rgba(0, 245, 255, 0.1);
    }

    .lesson-node.available:hover {
        transform: translateY(-10px) rotateX(10deg) scale(1.1);
        box-shadow:
            0 20px 40px rgba(0, 245, 255, 0.4),
            0 0 60px rgba(123, 104, 238, 0.3),
            inset 0 0 30px rgba(0, 245, 255, 0.2);
    }

    .lesson-node.completed {
        background: linear-gradient(135deg, rgba(0,245,255,0.4) 0%, rgba(123,104,238,0.4) 100%);
        border: 2px solid rgba(0, 245, 255, 0.8);
    }

    .lesson-node.locked {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(255, 255, 255, 0.1);
        opacity: 0.5;
    }

    .lesson-name {
        color: var(--text-secondary);
        font-size: 14px;
        font-weight: 500;
        text-align: center;
        max-width: 120px;
    }

    .lesson-xp {
        color: var(--accent-glow);
        font-size: 12px;
        font-weight: 600;
    }

    /* Stats Bar */
    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 32px;
        padding: 20px;
        flex-wrap: wrap;
    }

    .stat-item {
        display: flex;
        align-items: center;
        gap: 12px;
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        padding: 12px 24px;
        border-radius: 100px;
        border: 1px solid var(--glass-border);
        transition: all 0.3s ease;
    }

    .stat-item:hover {
        border-color: rgba(0, 245, 255, 0.3);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2);
    }

    .stat-icon {
        font-size: 24px;
    }

    .stat-value {
        font-size: 18px;
        font-weight: 700;
        color: var(--text-primary);
    }

    .stat-label {
        font-size: 12px;
        color: var(--text-tertiary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Progress Ring */
    .progress-ring {
        position: relative;
        width: 60px;
        height: 60px;
    }

    .progress-ring svg {
        transform: rotate(-90deg);
    }

    .progress-ring circle {
        fill: none;
        stroke-width: 4;
    }

    .progress-ring .bg {
        stroke: rgba(255, 255, 255, 0.1);
    }

    .progress-ring .progress {
        stroke: url(#gradient);
        stroke-linecap: round;
        transition: stroke-dashoffset 0.5s ease;
    }

    /* Question Card */
    .question-card {
        background: var(--glass-bg);
        backdrop-filter: blur(30px);
        border: 1px solid var(--glass-border);
        border-radius: 32px;
        padding: 48px;
        max-width: 800px;
        margin: 40px auto;
        position: relative;
    }

    .question-text {
        font-size: clamp(20px, 3vw, 32px);
        font-weight: 600;
        color: var(--text-primary);
        text-align: center;
        margin-bottom: 40px;
        line-height: 1.4;
    }

    /* Answer Options - Holographic Style */
    .option-btn {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px 28px;
        margin: 12px 0;
        color: var(--text-primary);
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .option-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: var(--accent-ice);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .option-btn:hover {
        border-color: rgba(0, 245, 255, 0.5);
        transform: translateX(8px);
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.2);
    }

    .option-btn:hover::before {
        opacity: 0.05;
    }

    .option-btn.selected {
        border-color: var(--accent-glow);
        background: rgba(0, 245, 255, 0.1);
        box-shadow: 0 0 40px rgba(0, 245, 255, 0.3);
    }

    .option-btn.correct {
        border-color: #00ff88;
        background: rgba(0, 255, 136, 0.1);
        box-shadow: 0 0 40px rgba(0, 255, 136, 0.3);
    }

    .option-btn.incorrect {
        border-color: #ff4d6d;
        background: rgba(255, 77, 109, 0.1);
        box-shadow: 0 0 40px rgba(255, 77, 109, 0.3);
    }

    /* Check Button - Iridescent */
    .check-btn {
        background: var(--accent-ice);
        background-size: 200% 200%;
        border: none;
        border-radius: 100px;
        padding: 18px 48px;
        color: #000;
        font-size: 16px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        cursor: pointer;
        transition: all 0.3s ease;
        animation: gradient-shift 4s ease infinite;
        margin-top: 32px;
    }

    .check-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 40px rgba(0, 245, 255, 0.4);
    }

    /* Feedback */
    .feedback-correct {
        background: linear-gradient(135deg, rgba(0,255,136,0.1) 0%, rgba(0,245,255,0.1) 100%);
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin-top: 24px;
        color: #00ff88;
    }

    .feedback-incorrect {
        background: linear-gradient(135deg, rgba(255,77,109,0.1) 0%, rgba(255,110,199,0.1) 100%);
        border: 1px solid rgba(255, 77, 109, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin-top: 24px;
        color: #ff4d6d;
    }

    /* Achievement Badges */
    .badge {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 24px;
        margin: 12px;
        min-width: 120px;
        transition: all 0.3s ease;
    }

    .badge:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 245, 255, 0.3);
        box-shadow: 0 20px 40px rgba(0, 245, 255, 0.2);
    }

    .badge.unlocked {
        background: linear-gradient(135deg, rgba(0,245,255,0.1) 0%, rgba(123,104,238,0.1) 100%);
        border-color: rgba(0, 245, 255, 0.3);
    }

    .badge-icon {
        font-size: 48px;
        margin-bottom: 12px;
        filter: drop-shadow(0 0 10px var(--accent-glow));
    }

    .badge.locked .badge-icon {
        filter: grayscale(1) opacity(0.3);
    }

    .badge-name {
        color: var(--text-primary);
        font-weight: 600;
        font-size: 14px;
        text-align: center;
    }

    /* Navigation */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin: 24px 0;
        flex-wrap: wrap;
    }

    .nav-btn {
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 100px;
        padding: 12px 24px;
        color: var(--text-secondary);
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .nav-btn:hover, .nav-btn.active {
        background: rgba(0, 245, 255, 0.1);
        border-color: rgba(0, 245, 255, 0.3);
        color: var(--text-primary);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2);
    }

    /* Daily Goal */
    .daily-goal {
        background: linear-gradient(135deg, rgba(0,245,255,0.05) 0%, rgba(123,104,238,0.05) 100%);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 16px;
        padding: 20px 32px;
        text-align: center;
        margin: 24px auto;
        max-width: 400px;
    }

    .goal-text {
        color: var(--text-secondary);
        font-size: 14px;
        margin-bottom: 12px;
    }

    .goal-progress {
        height: 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 100px;
        overflow: hidden;
    }

    .goal-fill {
        height: 100%;
        background: var(--accent-ice);
        background-size: 200% 200%;
        animation: gradient-shift 4s ease infinite;
        border-radius: 100px;
        transition: width 0.5s ease;
    }

    /* Lesson Complete Celebration */
    .celebration {
        text-align: center;
        padding: 60px 20px;
    }

    .celebration-icon {
        font-size: 100px;
        animation: celebrate-bounce 0.6s ease infinite;
        filter: drop-shadow(0 0 30px var(--accent-glow));
    }

    @keyframes celebrate-bounce {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-20px) scale(1.1); }
    }

    .celebration-title {
        font-size: clamp(32px, 6vw, 56px);
        font-weight: 800;
        background: var(--accent-ice);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-shift 4s ease infinite;
        margin: 24px 0;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero { padding: 40px 16px 30px; }
        .glass-card { padding: 20px; margin: 8px 0; }
        .question-card { padding: 24px; margin: 20px 8px; }
        .stats-bar { gap: 12px; }
        .stat-item { padding: 8px 16px; }
        .ice-shard { width: 80px; height: 80px; }
    }

    /* Streamlit Button Overrides */
    .stButton > button {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border) !important;
        border-radius: 16px !important;
        color: var(--text-primary) !important;
        font-family: 'Inter Tight', sans-serif !important;
        font-weight: 600 !important;
        padding: 16px 32px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: rgba(0, 245, 255, 0.1) !important;
        border-color: rgba(0, 245, 255, 0.3) !important;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.2) !important;
        transform: translateY(-2px);
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-void);
    }

    ::-webkit-scrollbar-thumb {
        background: rgba(0, 245, 255, 0.3);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 245, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Floating particles background - rendered via CSS only (no dynamic HTML)
def render_particles():
    # Use CSS-only particles to avoid HTML rendering issues
    particle_css = '<style>.particles-bg{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;}'
    for i in range(20):
        left = random.randint(0, 100)
        delay = round(random.random() * 15, 1)
        duration = round(15 + random.random() * 10, 1)
        particle_css += f'.p{i}{{position:absolute;left:{left}%;width:4px;height:4px;background:#00f5ff;border-radius:50%;opacity:0.4;box-shadow:0 0 10px #00f5ff;animation:float-p {duration}s {delay}s infinite linear;}}'
    particle_css += '@keyframes float-p{0%{transform:translateY(100vh);opacity:0;}10%{opacity:0.4;}90%{opacity:0.4;}100%{transform:translateY(-100vh);opacity:0;}}</style>'
    particle_divs = '<div class="particles-bg">' + ''.join([f'<div class="p{i}"></div>' for i in range(20)]) + '</div>'
    st.markdown(particle_css + particle_divs, unsafe_allow_html=True)

# ============== DATA ==============

LESSONS = {
    "unit1": {
        "title": "Consumer Behaviour Fundamentals",
        "icon": "🧠",
        "lessons": [
            {
                "id": "1.1",
                "name": "What is Consumer Behaviour?",
                "icon": "📚",
                "xp": 15,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Consumer Behaviour studies how people...",
                        "options": [
                            "Manufacture products in factories",
                            "Select, use, and dispose of products",
                            "Design marketing campaigns",
                            "Set product prices"
                        ],
                        "correct": 1,
                        "explanation": "Consumer Behaviour examines the entire journey of how people make decisions about products and services."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which is NOT part of consumer behaviour study?",
                        "options": ["Purchase decisions", "Product disposal", "Factory operations", "Brand selection"],
                        "correct": 2,
                        "explanation": "Factory operations are part of production management, not consumer behaviour."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Understanding consumer behaviour helps marketers with...",
                        "options": ["Machine maintenance", "Customer needs and wants", "Warehouse logistics", "Employee training"],
                        "correct": 1,
                        "explanation": "Marketers study consumer behaviour to better understand and serve customer needs."
                    }
                ]
            },
            {
                "id": "1.2",
                "name": "Decision Making Process",
                "icon": "🎯",
                "xp": 20,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the FIRST stage in consumer decision-making?",
                        "options": ["Information Search", "Need Recognition", "Evaluation", "Purchase"],
                        "correct": 1,
                        "explanation": "Need Recognition occurs when you realize there's a gap between your current and desired state."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Riya's phone battery dies quickly. She realizes she needs a new phone. This is...",
                        "options": ["Information Search", "Need Recognition", "Post-Purchase", "Evaluation"],
                        "correct": 1,
                        "explanation": "Recognizing the problem with her current phone is Need Recognition."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Watching YouTube reviews before buying is which stage?",
                        "options": ["Need Recognition", "Information Search", "Purchase Decision", "Evaluation"],
                        "correct": 1,
                        "explanation": "Gathering information through reviews is the Information Search stage."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Comparing iPhone vs Samsung features is which stage?",
                        "options": ["Information Search", "Need Recognition", "Evaluation of Alternatives", "Post-Purchase"],
                        "correct": 2,
                        "explanation": "Comparing options against each other is the Evaluation stage."
                    }
                ]
            },
            {
                "id": "1.3",
                "name": "Types of Buying Behaviour",
                "icon": "🛒",
                "xp": 25,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Buying salt without much thought is an example of...",
                        "options": ["Complex Buying", "Variety Seeking", "Habitual Buying", "Dissonance Reducing"],
                        "correct": 2,
                        "explanation": "Habitual Buying = Low involvement + Few brand differences."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Buying a house involves extensive research. This is...",
                        "options": ["Habitual Buying", "Complex Buying", "Variety Seeking", "Impulse Buying"],
                        "correct": 1,
                        "explanation": "Complex Buying = High involvement + Significant brand differences."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Priya tries different chocolate brands each time. This is...",
                        "options": ["Complex Buying", "Habitual Buying", "Variety Seeking", "Dissonance Reducing"],
                        "correct": 2,
                        "explanation": "Variety Seeking = Low involvement but switching for novelty."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "High involvement + few brand differences equals...",
                        "options": ["Complex Buying", "Variety Seeking", "Habitual Buying", "Dissonance-Reducing"],
                        "correct": 3,
                        "explanation": "Dissonance-Reducing behaviour occurs when brands seem similar but the purchase matters."
                    }
                ]
            }
        ]
    },
    "unit2": {
        "title": "STP Marketing Strategy",
        "icon": "🎯",
        "lessons": [
            {
                "id": "2.1",
                "name": "Market Segmentation",
                "icon": "📊",
                "xp": 20,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Segmentation means...",
                        "options": ["Selling to everyone", "Dividing market into distinct groups", "Setting prices", "Creating ads"],
                        "correct": 1,
                        "explanation": "Segmentation divides the market into groups with similar needs."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Targeting fitness enthusiasts is which segmentation?",
                        "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"],
                        "correct": 2,
                        "explanation": "Psychographic segmentation is based on lifestyle, values, and interests."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Urban vs Rural is which segmentation type?",
                        "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"],
                        "correct": 0,
                        "explanation": "Geographic segmentation divides by location."
                    }
                ]
            },
            {
                "id": "2.2",
                "name": "Targeting & Positioning",
                "icon": "🎪",
                "xp": 20,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "What does STP stand for?",
                        "options": ["Sales, Trade, Profit", "Segmentation, Targeting, Positioning", "Strategy, Tactics, Planning", "Supply, Transport, Production"],
                        "correct": 1,
                        "explanation": "STP = Segmentation, Targeting, Positioning - the foundation of marketing."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Rolex focuses only on luxury buyers. This targeting is...",
                        "options": ["Undifferentiated", "Differentiated", "Concentrated", "Mass Marketing"],
                        "correct": 2,
                        "explanation": "Concentrated targeting focuses on one specific segment."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Positioning is about...",
                        "options": ["Store shelf placement", "How customers perceive your brand", "Geographic location", "Inventory position"],
                        "correct": 1,
                        "explanation": "Positioning is the place your brand occupies in customers' minds."
                    }
                ]
            },
            {
                "id": "2.3",
                "name": "Customer Retention",
                "icon": "📈",
                "xp": 25,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Retention Rate measures...",
                        "options": ["New customers gained", "Customers kept over time", "Total revenue", "Market share"],
                        "correct": 1,
                        "explanation": "Retention Rate = percentage of customers you keep."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Company: 1000 start, +200 new, 900 end. Retention rate?",
                        "options": ["70%", "80%", "90%", "60%"],
                        "correct": 0,
                        "explanation": "((900-200)/1000) × 100 = 70% retention."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "If retention is 70%, churn rate is...",
                        "options": ["70%", "30%", "100%", "50%"],
                        "correct": 1,
                        "explanation": "Churn = 100% - Retention = 100% - 70% = 30%."
                    }
                ]
            }
        ]
    }
}

ACHIEVEMENTS = [
    {"id": "first_lesson", "name": "First Steps", "icon": "🌟", "desc": "Complete first lesson"},
    {"id": "streak_3", "name": "On Fire", "icon": "🔥", "desc": "3 day streak"},
    {"id": "streak_7", "name": "Week Warrior", "icon": "⚡", "desc": "7 day streak"},
    {"id": "perfect", "name": "Perfectionist", "icon": "💎", "desc": "No mistakes in a lesson"},
    {"id": "xp_100", "name": "Century", "icon": "💯", "desc": "Earn 100 XP"},
    {"id": "unit_done", "name": "Unit Master", "icon": "🏆", "desc": "Complete a unit"},
]

# ============== SESSION STATE ==============

def init_state():
    defaults = {
        'xp': 0, 'level': 1, 'hearts': 5, 'streak': 0,
        'gems': 50, 'daily_xp': 0, 'daily_goal': 30,
        'completed_lessons': set(), 'achievements': set(),
        'current_lesson': None, 'current_q': 0,
        'mistakes': 0, 'selected': None, 'submitted': False,
        'page': 'home', 'last_date': None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ============== HELPERS ==============

def calc_level(xp):
    return (xp // 100) + 1

def add_xp(amount):
    st.session_state.xp += amount
    st.session_state.daily_xp += amount
    st.session_state.level = calc_level(st.session_state.xp)
    check_achievements()

def lose_heart():
    if st.session_state.hearts > 0:
        st.session_state.hearts -= 1

def check_achievements():
    if len(st.session_state.completed_lessons) >= 1:
        st.session_state.achievements.add("first_lesson")
    if st.session_state.xp >= 100:
        st.session_state.achievements.add("xp_100")
    if st.session_state.streak >= 3:
        st.session_state.achievements.add("streak_3")
    if st.session_state.streak >= 7:
        st.session_state.achievements.add("streak_7")

# ============== RENDER FUNCTIONS ==============

def render_hero():
    st.markdown("""
    <div class="hero">
        <div class="ice-shard"></div>
        <h1 class="hero-title">ConsumerQuest</h1>
        <p class="hero-subtitle">Master Consumer Behaviour</p>
        <p class="hero-description">
            An immersive learning experience. Master the psychology of consumer decisions
            through bite-sized lessons and interactive challenges.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_stats():
    level = calc_level(st.session_state.xp)
    xp_progress = (st.session_state.xp % 100)

    st.markdown(f"""
    <div class="stats-bar">
        <div class="stat-item">
            <span class="stat-icon">🔥</span>
            <div>
                <div class="stat-value">{st.session_state.streak}</div>
                <div class="stat-label">Streak</div>
            </div>
        </div>
        <div class="stat-item">
            <span class="stat-icon">⭐</span>
            <div>
                <div class="stat-value">Lvl {level}</div>
                <div class="stat-label">{xp_progress}/100 XP</div>
            </div>
        </div>
        <div class="stat-item">
            <span class="stat-icon">❤️</span>
            <div>
                <div class="stat-value">{st.session_state.hearts}</div>
                <div class="stat-label">Hearts</div>
            </div>
        </div>
        <div class="stat-item">
            <span class="stat-icon">💎</span>
            <div>
                <div class="stat-value">{st.session_state.gems}</div>
                <div class="stat-label">Gems</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Daily goal
    goal_pct = min(100, (st.session_state.daily_xp / st.session_state.daily_goal) * 100)
    st.markdown(f"""
    <div class="daily-goal">
        <div class="goal-text">🎯 Daily Goal: {st.session_state.daily_xp}/{st.session_state.daily_goal} XP</div>
        <div class="goal-progress">
            <div class="goal-fill" style="width: {goal_pct}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_home():
    render_hero()
    render_stats()

    # Units and lessons
    for unit_id, unit in LESSONS.items():
        st.markdown(f"""
        <div class="unit-header">
            <div class="unit-title">{unit['icon']} {unit['title']}</div>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(len(unit['lessons']))

        for idx, lesson in enumerate(unit['lessons']):
            with cols[idx]:
                completed = lesson['id'] in st.session_state.completed_lessons
                available = idx == 0 or unit['lessons'][idx-1]['id'] in st.session_state.completed_lessons

                if completed:
                    status = "completed"
                    icon = "✅"
                elif available:
                    status = "available"
                    icon = lesson['icon']
                else:
                    status = "locked"
                    icon = "🔒"

                st.markdown(f"""
                <div class="lesson-node-container">
                    <div class="lesson-node {status}">{icon}</div>
                    <div class="lesson-name">{lesson['name']}</div>
                    <div class="lesson-xp">+{lesson['xp']} XP</div>
                </div>
                """, unsafe_allow_html=True)

                if available or completed:
                    if st.button("Start", key=f"btn_{lesson['id']}", use_container_width=True):
                        st.session_state.current_lesson = lesson
                        st.session_state.current_q = 0
                        st.session_state.mistakes = 0
                        st.session_state.selected = None
                        st.session_state.submitted = False
                        st.session_state.page = 'lesson'
                        st.rerun()

def render_lesson():
    lesson = st.session_state.current_lesson
    if not lesson:
        st.session_state.page = 'home'
        st.rerun()
        return

    questions = lesson['questions']
    q_idx = st.session_state.current_q

    if q_idx >= len(questions):
        render_complete()
        return

    q = questions[q_idx]
    progress = ((q_idx + 1) / len(questions)) * 100

    # Header
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("← Exit"):
            st.session_state.page = 'home'
            st.session_state.current_lesson = None
            st.rerun()
    with col2:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.1); border-radius: 100px; height: 8px; overflow: hidden;">
            <div style="width: {progress}%; height: 100%; background: var(--accent-ice); background-size: 200% 200%; animation: gradient-shift 4s ease infinite;"></div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align: right; color: #ff6b6b;'>{'❤️' * st.session_state.hearts}</div>", unsafe_allow_html=True)

    # Question
    st.markdown(f"""
    <div class="question-card">
        <div class="question-text">{q['question']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Options
    for idx, opt in enumerate(q['options']):
        selected = st.session_state.selected == idx

        if st.session_state.submitted:
            if idx == q['correct']:
                cls = "correct"
            elif selected:
                cls = "incorrect"
            else:
                cls = ""
        else:
            cls = "selected" if selected else ""

        if st.button(opt, key=f"opt_{idx}", disabled=st.session_state.submitted, use_container_width=True):
            st.session_state.selected = idx
            st.rerun()

    # Check/Continue button
    if not st.session_state.submitted:
        if st.button("CHECK", key="check", disabled=st.session_state.selected is None, use_container_width=True):
            st.session_state.submitted = True
            if st.session_state.selected != q['correct']:
                lose_heart()
                st.session_state.mistakes += 1
            st.rerun()
    else:
        is_correct = st.session_state.selected == q['correct']
        if is_correct:
            st.markdown(f"""
            <div class="feedback-correct">
                <strong>✨ Correct!</strong><br>{q.get('explanation', '')}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-incorrect">
                <strong>❌ Not quite!</strong><br>{q.get('explanation', '')}
            </div>
            """, unsafe_allow_html=True)

        if st.button("CONTINUE", key="continue", use_container_width=True):
            st.session_state.current_q += 1
            st.session_state.selected = None
            st.session_state.submitted = False
            st.rerun()

def render_complete():
    lesson = st.session_state.current_lesson
    xp_earned = lesson['xp']
    if st.session_state.mistakes == 0:
        xp_earned += 10
        st.session_state.achievements.add("perfect")

    if lesson['id'] not in st.session_state.completed_lessons:
        st.session_state.completed_lessons.add(lesson['id'])
        add_xp(xp_earned)
        st.session_state.gems += 5

    accuracy = max(0, 100 - (st.session_state.mistakes * 20))

    st.markdown(f"""
    <div class="celebration">
        <div class="celebration-icon">🎉</div>
        <h1 class="celebration-title">Lesson Complete!</h1>

        <div class="stats-bar" style="justify-content: center; margin-top: 40px;">
            <div class="stat-item">
                <span class="stat-icon">⭐</span>
                <div>
                    <div class="stat-value">+{xp_earned}</div>
                    <div class="stat-label">XP Earned</div>
                </div>
            </div>
            <div class="stat-item">
                <span class="stat-icon">🎯</span>
                <div>
                    <div class="stat-value">{accuracy}%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
            </div>
            <div class="stat-item">
                <span class="stat-icon">💎</span>
                <div>
                    <div class="stat-value">+5</div>
                    <div class="stat-label">Gems</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.mistakes == 0:
        st.markdown("<p style='text-align: center; color: #00f5ff; font-size: 18px;'>🌟 PERFECT! No mistakes!</p>", unsafe_allow_html=True)

    st.balloons()

    if st.button("Continue Learning", use_container_width=True):
        st.session_state.page = 'home'
        st.session_state.current_lesson = None
        st.session_state.current_q = 0
        st.rerun()

def render_achievements():
    st.markdown("""
    <div class="hero" style="padding: 40px 20px;">
        <h1 class="hero-title" style="font-size: 48px;">🏆 Achievements</h1>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, ach in enumerate(ACHIEVEMENTS):
        with cols[idx % 3]:
            unlocked = ach['id'] in st.session_state.achievements
            cls = "unlocked" if unlocked else "locked"

            st.markdown(f"""
            <div class="badge {cls}">
                <div class="badge-icon">{ach['icon'] if unlocked else '🔒'}</div>
                <div class="badge-name">{ach['name']}</div>
                <div style="color: rgba(255,255,255,0.5); font-size: 12px; margin-top: 8px;">{ach['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_profile():
    level = calc_level(st.session_state.xp)

    st.markdown(f"""
    <div class="hero" style="padding: 40px 20px;">
        <div class="ice-shard" style="width: 80px; height: 80px;"></div>
        <h1 class="hero-title" style="font-size: 48px;">Level {level}</h1>
        <p class="hero-subtitle">Consumer Apprentice</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px;">⭐</div>
            <div style="font-size: 24px; font-weight: 700; color: white;">{st.session_state.xp}</div>
            <div style="color: rgba(255,255,255,0.5);">Total XP</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px;">🔥</div>
            <div style="font-size: 24px; font-weight: 700; color: white;">{st.session_state.streak}</div>
            <div style="color: rgba(255,255,255,0.5);">Day Streak</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px;">📚</div>
            <div style="font-size: 24px; font-weight: 700; color: white;">{len(st.session_state.completed_lessons)}</div>
            <div style="color: rgba(255,255,255,0.5);">Lessons Done</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px;">🏆</div>
            <div style="font-size: 24px; font-weight: 700; color: white;">{len(st.session_state.achievements)}</div>
            <div style="color: rgba(255,255,255,0.5);">Achievements</div>
        </div>
        """, unsafe_allow_html=True)

# ============== MAIN ==============

def main():
    render_particles()

    # Navigation
    st.markdown("""
    <div class="nav-container">
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🧊 Learn", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()
    with col2:
        if st.button("🏆 Achievements", use_container_width=True):
            st.session_state.page = 'achievements'
            st.rerun()
    with col3:
        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = 'profile'
            st.rerun()
    with col4:
        if st.button("🔄 Reset", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Page routing
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'lesson':
        render_lesson()
    elif st.session_state.page == 'achievements':
        render_achievements()
    elif st.session_state.page == 'profile':
        render_profile()

if __name__ == "__main__":
    main()
