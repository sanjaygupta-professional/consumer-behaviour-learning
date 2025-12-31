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
    @import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@100;200;300;400;500;600;700;800;900&display=swap');

    :root {
        --bg-void: #000000;
        --accent-glow: #00f5ff;
        --glass-border: rgba(255, 255, 255, 0.1);
        --glass-bg: rgba(255, 255, 255, 0.05);
    }

    * { font-family: 'Inter Tight', sans-serif; -webkit-font-smoothing: antialiased; }

    .stApp {
        background: #000000;
        background-image: radial-gradient(ellipse at 20% 80%, rgba(0, 245, 255, 0.08) 0%, transparent 50%), radial-gradient(ellipse at 80% 20%, rgba(123, 104, 238, 0.08) 0%, transparent 50%);
    }

    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display: none; }

    .hero-title {
        font-size: 64px;
        font-weight: 800;
        letter-spacing: -0.04em;
        background: linear-gradient(135deg, #00f5ff 0%, #7b68ee 25%, #ff6ec7 50%, #00f5ff 75%, #7b68ee 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 8s ease infinite;
        text-align: center;
        margin-bottom: 10px;
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-subtitle {
        font-size: 18px;
        font-weight: 300;
        color: rgba(255, 255, 255, 0.6);
        letter-spacing: 0.1em;
        text-transform: uppercase;
        text-align: center;
    }

    .ice-shard {
        width: 80px;
        height: 80px;
        margin: 20px auto;
        position: relative;
        animation: shard-rotate 20s linear infinite;
    }

    .ice-shard::before {
        content: '🧊';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 48px;
        filter: drop-shadow(0 0 20px #00f5ff);
    }

    @keyframes shard-rotate {
        0% { transform: rotateY(0deg); }
        100% { transform: rotateY(360deg); }
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 24px;
        margin: 12px 0;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(0, 245, 255, 0.3);
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(0, 245, 255, 0.15);
    }

    .unit-header {
        background: linear-gradient(135deg, rgba(0,245,255,0.1) 0%, rgba(123,104,238,0.1) 100%);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin: 30px 0 20px;
        text-align: center;
    }

    .unit-title {
        font-size: 28px;
        font-weight: 700;
        color: white;
    }

    .lesson-node {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        margin: 0 auto 10px;
        transition: all 0.3s ease;
    }

    .lesson-node.available {
        background: linear-gradient(135deg, rgba(0,245,255,0.2) 0%, rgba(123,104,238,0.2) 100%);
        border: 2px solid rgba(0, 245, 255, 0.5);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
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

    .stat-pill {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 50px;
        padding: 8px 20px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin: 4px;
        color: white;
        font-weight: 600;
    }

    .progress-bar {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 10px 0;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #00f5ff, #7b68ee, #ff6ec7);
        background-size: 200% 200%;
        animation: gradient-shift 4s ease infinite;
        border-radius: 10px;
    }

    .question-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        text-align: center;
    }

    .question-text {
        font-size: 24px;
        font-weight: 600;
        color: white;
        line-height: 1.4;
    }

    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        font-family: 'Inter Tight', sans-serif !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: rgba(0, 245, 255, 0.1) !important;
        border-color: rgba(0, 245, 255, 0.3) !important;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2) !important;
    }

    .celebration-title {
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(135deg, #00f5ff, #7b68ee, #ff6ec7);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-shift 4s ease infinite;
        text-align: center;
    }

    .badge-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin: 8px;
        transition: all 0.3s ease;
    }

    .badge-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 245, 255, 0.3);
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.2);
    }

    .badge-card.unlocked {
        background: linear-gradient(135deg, rgba(0,245,255,0.1), rgba(123,104,238,0.1));
        border-color: rgba(0, 245, 255, 0.3);
    }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #000; }
    ::-webkit-scrollbar-thumb { background: rgba(0, 245, 255, 0.3); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

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
                    {"question": "Consumer Behaviour studies how people...", "options": ["Manufacture products", "Select, use, and dispose of products", "Design campaigns", "Set prices"], "correct": 1, "explanation": "Consumer Behaviour examines decisions about products and services."},
                    {"question": "Which is NOT part of consumer behaviour?", "options": ["Purchase decisions", "Product disposal", "Factory operations", "Brand selection"], "correct": 2, "explanation": "Factory operations are production, not consumer behaviour."},
                    {"question": "Understanding consumer behaviour helps with...", "options": ["Machine maintenance", "Customer needs", "Warehouse logistics", "Employee training"], "correct": 1, "explanation": "Marketers study it to understand customer needs."}
                ]
            },
            {
                "id": "1.2",
                "name": "Decision Making Process",
                "icon": "🎯",
                "xp": 20,
                "questions": [
                    {"question": "What is the FIRST stage in decision-making?", "options": ["Information Search", "Need Recognition", "Evaluation", "Purchase"], "correct": 1, "explanation": "Need Recognition is realizing there's a gap."},
                    {"question": "Phone battery dies quickly - you need new phone. This is...", "options": ["Information Search", "Need Recognition", "Post-Purchase", "Evaluation"], "correct": 1, "explanation": "Recognizing the problem is Need Recognition."},
                    {"question": "Watching YouTube reviews is which stage?", "options": ["Need Recognition", "Information Search", "Purchase", "Evaluation"], "correct": 1, "explanation": "Gathering info through reviews is Information Search."},
                    {"question": "Comparing iPhone vs Samsung is which stage?", "options": ["Information Search", "Need Recognition", "Evaluation", "Post-Purchase"], "correct": 2, "explanation": "Comparing options is Evaluation."}
                ]
            },
            {
                "id": "1.3",
                "name": "Types of Buying Behaviour",
                "icon": "🛒",
                "xp": 25,
                "questions": [
                    {"question": "Buying salt without thought is...", "options": ["Complex Buying", "Variety Seeking", "Habitual Buying", "Dissonance Reducing"], "correct": 2, "explanation": "Habitual = Low involvement + Few brand differences."},
                    {"question": "Buying a house with extensive research is...", "options": ["Habitual", "Complex Buying", "Variety Seeking", "Impulse"], "correct": 1, "explanation": "Complex = High involvement + Significant differences."},
                    {"question": "Trying different chocolates each time is...", "options": ["Complex", "Habitual", "Variety Seeking", "Dissonance Reducing"], "correct": 2, "explanation": "Variety Seeking = Low involvement, switching for novelty."},
                    {"question": "High involvement + few brand differences is...", "options": ["Complex", "Variety Seeking", "Habitual", "Dissonance-Reducing"], "correct": 3, "explanation": "Dissonance-Reducing when brands seem similar but purchase matters."}
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
                    {"question": "Segmentation means...", "options": ["Selling to everyone", "Dividing market into groups", "Setting prices", "Creating ads"], "correct": 1, "explanation": "Segmentation divides market into similar groups."},
                    {"question": "Targeting fitness enthusiasts is which type?", "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"], "correct": 2, "explanation": "Psychographic = lifestyle, values, interests."},
                    {"question": "Urban vs Rural is which segmentation?", "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"], "correct": 0, "explanation": "Geographic divides by location."}
                ]
            },
            {
                "id": "2.2",
                "name": "Targeting & Positioning",
                "icon": "🎪",
                "xp": 20,
                "questions": [
                    {"question": "What does STP stand for?", "options": ["Sales, Trade, Profit", "Segmentation, Targeting, Positioning", "Strategy, Tactics, Planning", "Supply, Transport, Production"], "correct": 1, "explanation": "STP = Segmentation, Targeting, Positioning."},
                    {"question": "Rolex focuses only on luxury buyers. This is...", "options": ["Undifferentiated", "Differentiated", "Concentrated", "Mass Marketing"], "correct": 2, "explanation": "Concentrated = focus on one segment."},
                    {"question": "Positioning is about...", "options": ["Store shelf placement", "Brand perception vs competitors", "Geographic location", "Inventory"], "correct": 1, "explanation": "Positioning = place in customers' minds."}
                ]
            },
            {
                "id": "2.3",
                "name": "Customer Retention",
                "icon": "📈",
                "xp": 25,
                "questions": [
                    {"question": "Retention Rate measures...", "options": ["New customers", "Customers kept", "Revenue", "Market share"], "correct": 1, "explanation": "Retention = % of customers kept."},
                    {"question": "1000 start, +200 new, 900 end. Retention?", "options": ["70%", "80%", "90%", "60%"], "correct": 0, "explanation": "((900-200)/1000) × 100 = 70%."},
                    {"question": "If retention is 70%, churn is...", "options": ["70%", "30%", "100%", "50%"], "correct": 1, "explanation": "Churn = 100% - Retention = 30%."}
                ]
            }
        ]
    }
}

ACHIEVEMENTS = [
    {"id": "first_lesson", "name": "First Steps", "icon": "🌟", "desc": "Complete first lesson"},
    {"id": "streak_3", "name": "On Fire", "icon": "🔥", "desc": "3 day streak"},
    {"id": "perfect", "name": "Perfectionist", "icon": "💎", "desc": "No mistakes"},
    {"id": "xp_100", "name": "Century", "icon": "💯", "desc": "Earn 100 XP"},
]

# ============== SESSION STATE ==============

def init_state():
    defaults = {
        'xp': 0, 'hearts': 5, 'streak': 1, 'gems': 50,
        'daily_xp': 0, 'daily_goal': 30,
        'completed_lessons': set(), 'achievements': set(),
        'current_lesson': None, 'current_q': 0,
        'mistakes': 0, 'selected': None, 'submitted': False,
        'page': 'home'
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
    check_achievements()

def lose_heart():
    if st.session_state.hearts > 0:
        st.session_state.hearts -= 1

def check_achievements():
    if len(st.session_state.completed_lessons) >= 1:
        st.session_state.achievements.add("first_lesson")
    if st.session_state.xp >= 100:
        st.session_state.achievements.add("xp_100")

# ============== PAGES ==============

def render_home():
    # Hero
    st.markdown('<div class="ice-shard"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">ConsumerQuest</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Master Consumer Behaviour</p>', unsafe_allow_html=True)

    # Stats row using columns
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-pill">🔥 {st.session_state.streak} Streak</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-pill">⭐ Lvl {calc_level(st.session_state.xp)}</div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-pill">❤️ {st.session_state.hearts} Hearts</div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="stat-pill">💎 {st.session_state.gems} Gems</div>', unsafe_allow_html=True)

    # Daily goal
    goal_pct = min(100, int((st.session_state.daily_xp / st.session_state.daily_goal) * 100))
    st.markdown(f'<div style="text-align:center;color:rgba(255,255,255,0.6);margin-top:20px;">🎯 Daily Goal: {st.session_state.daily_xp}/{st.session_state.daily_goal} XP</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="progress-bar"><div class="progress-fill" style="width:{goal_pct}%;"></div></div>', unsafe_allow_html=True)

    # Units
    for unit_id, unit in LESSONS.items():
        st.markdown(f'<div class="unit-header"><div class="unit-title">{unit["icon"]} {unit["title"]}</div></div>', unsafe_allow_html=True)

        cols = st.columns(len(unit['lessons']))
        for idx, lesson in enumerate(unit['lessons']):
            with cols[idx]:
                completed = lesson['id'] in st.session_state.completed_lessons
                available = idx == 0 or unit['lessons'][idx-1]['id'] in st.session_state.completed_lessons

                if completed:
                    status, icon = "completed", "✅"
                elif available:
                    status, icon = "available", lesson['icon']
                else:
                    status, icon = "locked", "🔒"

                st.markdown(f'<div class="lesson-node {status}">{icon}</div>', unsafe_allow_html=True)
                st.markdown(f'<p style="color:rgba(255,255,255,0.7);text-align:center;font-size:14px;">{lesson["name"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p style="color:#00f5ff;text-align:center;font-size:12px;">+{lesson["xp"]} XP</p>', unsafe_allow_html=True)

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
    progress = int(((q_idx + 1) / len(questions)) * 100)

    # Header
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("← Exit"):
            st.session_state.page = 'home'
            st.session_state.current_lesson = None
            st.rerun()
    with col2:
        st.markdown(f'<div class="progress-bar"><div class="progress-fill" style="width:{progress}%;"></div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<p style="text-align:right;color:#ff6b6b;">{"❤️" * st.session_state.hearts}</p>', unsafe_allow_html=True)

    # Question
    st.markdown(f'<div class="question-box"><p class="question-text">{q["question"]}</p></div>', unsafe_allow_html=True)

    # Options
    for idx, opt in enumerate(q['options']):
        disabled = st.session_state.submitted
        selected = st.session_state.selected == idx

        if st.button(f"{'→ ' if selected else ''}{opt}", key=f"opt_{idx}", disabled=disabled, use_container_width=True):
            st.session_state.selected = idx
            st.rerun()

    st.write("")

    # Check or Continue
    if not st.session_state.submitted:
        if st.button("CHECK", disabled=st.session_state.selected is None, use_container_width=True):
            st.session_state.submitted = True
            if st.session_state.selected != q['correct']:
                lose_heart()
                st.session_state.mistakes += 1
            st.rerun()
    else:
        is_correct = st.session_state.selected == q['correct']
        if is_correct:
            st.success(f"✨ **Correct!** {q.get('explanation', '')}")
        else:
            st.error(f"❌ **Not quite.** {q.get('explanation', '')}")

        if st.button("CONTINUE", use_container_width=True):
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

    st.balloons()

    st.write("")
    st.write("")
    st.markdown('<p style="text-align:center;font-size:60px;">🎉</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="celebration-title">Lesson Complete!</h1>', unsafe_allow_html=True)
    st.write("")

    # Stats using Streamlit columns
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("XP Earned", f"+{xp_earned}")
    with c2:
        st.metric("Accuracy", f"{accuracy}%")
    with c3:
        st.metric("Gems", "+5")

    if st.session_state.mistakes == 0:
        st.success("🌟 PERFECT! No mistakes!")

    st.write("")
    if st.button("Continue Learning", use_container_width=True):
        st.session_state.page = 'home'
        st.session_state.current_lesson = None
        st.session_state.current_q = 0
        st.rerun()

def render_achievements():
    st.markdown('<h1 class="hero-title" style="font-size:40px;">🏆 Achievements</h1>', unsafe_allow_html=True)
    st.write("")

    cols = st.columns(4)
    for idx, ach in enumerate(ACHIEVEMENTS):
        with cols[idx % 4]:
            unlocked = ach['id'] in st.session_state.achievements
            cls = "unlocked" if unlocked else ""
            icon = ach['icon'] if unlocked else "🔒"

            st.markdown(f'''<div class="badge-card {cls}">
                <p style="font-size:40px;margin:0;">{icon}</p>
                <p style="color:white;font-weight:600;margin:8px 0 4px;">{ach["name"]}</p>
                <p style="color:rgba(255,255,255,0.5);font-size:12px;margin:0;">{ach["desc"]}</p>
            </div>''', unsafe_allow_html=True)

def render_profile():
    level = calc_level(st.session_state.xp)

    st.markdown('<div class="ice-shard"></div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-title" style="font-size:48px;">Level {level}</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Consumer Apprentice</p>', unsafe_allow_html=True)
    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total XP", st.session_state.xp)
    with c2:
        st.metric("Streak", f"🔥 {st.session_state.streak}")
    with c3:
        st.metric("Lessons", len(st.session_state.completed_lessons))
    with c4:
        st.metric("Gems", f"💎 {st.session_state.gems}")

# ============== MAIN ==============

def main():
    # Navigation
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🧊 Learn", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()
    with c2:
        if st.button("🏆 Achievements", use_container_width=True):
            st.session_state.page = 'achievements'
            st.rerun()
    with c3:
        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = 'profile'
            st.rerun()
    with c4:
        if st.button("🔄 Reset", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("---")

    # Route
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
