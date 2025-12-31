"""
Consumer Behaviour Learning Hub - Duolingo Style
Gamified interactive learning for COBE201-1
"""

import streamlit as st
import random
import json
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="ConsumerQuest - Learn Consumer Behaviour",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============== CUSTOM CSS - DUOLINGO STYLE ==============
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    * {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #235390 0%, #1a4275 100%);
        min-height: 100vh;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Top Stats Bar */
    .stats-bar {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 12px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .stat-item {
        display: flex;
        align-items: center;
        gap: 8px;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
    }

    .stat-icon {
        font-size: 1.5rem;
    }

    /* XP Bar */
    .xp-container {
        background: rgba(255,255,255,0.2);
        border-radius: 20px;
        height: 24px;
        width: 200px;
        overflow: hidden;
        position: relative;
    }

    .xp-fill {
        background: linear-gradient(90deg, #FFC800 0%, #FF9500 100%);
        height: 100%;
        border-radius: 20px;
        transition: width 0.5s ease;
    }

    .xp-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-weight: 700;
        font-size: 0.8rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    /* Hearts */
    .hearts {
        color: #FF4B4B;
        font-size: 1.5rem;
        letter-spacing: 4px;
    }

    /* Streak */
    .streak-fire {
        animation: pulse 1s infinite;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }

    /* Main Card */
    .main-card {
        background: white;
        border-radius: 24px;
        padding: 30px;
        margin: 20px auto;
        max-width: 700px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }

    /* Lesson Card */
    .lesson-card {
        background: white;
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 3px solid #E5E5E5;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .lesson-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        border-color: #58CC02;
    }

    .lesson-card.locked {
        opacity: 0.6;
        background: #F7F7F7;
    }

    .lesson-card.completed {
        border-color: #58CC02;
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
    }

    /* Progress Circle */
    .progress-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: conic-gradient(#58CC02 var(--progress), #E5E5E5 0deg);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }

    .progress-circle-inner {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
    }

    /* Question Card */
    .question-card {
        background: #F7F7F7;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        text-align: center;
    }

    .question-text {
        font-size: 1.5rem;
        font-weight: 700;
        color: #3C3C3C;
        margin-bottom: 24px;
    }

    /* Answer Options */
    .option-btn {
        background: white;
        border: 2px solid #E5E5E5;
        border-radius: 16px;
        padding: 16px 24px;
        margin: 8px 0;
        width: 100%;
        text-align: left;
        font-size: 1.1rem;
        font-weight: 600;
        color: #3C3C3C;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .option-btn:hover {
        border-color: #1CB0F6;
        background: #E8F7FF;
    }

    .option-btn.selected {
        border-color: #1CB0F6;
        background: #DDF4FF;
        border-width: 3px;
    }

    .option-btn.correct {
        border-color: #58CC02;
        background: #D7FFB8;
        border-width: 3px;
    }

    .option-btn.incorrect {
        border-color: #FF4B4B;
        background: #FFDFE0;
        border-width: 3px;
    }

    /* Check Button */
    .check-btn {
        background: linear-gradient(180deg, #58CC02 0%, #46A302 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 16px 48px;
        font-size: 1.2rem;
        font-weight: 700;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 0 #46A302;
        transition: all 0.1s ease;
        margin-top: 20px;
    }

    .check-btn:hover {
        background: linear-gradient(180deg, #62D902 0%, #50B302 100%);
    }

    .check-btn:active {
        transform: translateY(4px);
        box-shadow: none;
    }

    .check-btn:disabled {
        background: #E5E5E5;
        box-shadow: 0 4px 0 #CDCDCD;
        cursor: not-allowed;
    }

    /* Feedback Banner */
    .feedback-correct {
        background: #D7FFB8;
        border-top: 4px solid #58CC02;
        padding: 20px;
        border-radius: 0 0 16px 16px;
        margin-top: 20px;
    }

    .feedback-incorrect {
        background: #FFDFE0;
        border-top: 4px solid #FF4B4B;
        padding: 20px;
        border-radius: 0 0 16px 16px;
        margin-top: 20px;
    }

    .feedback-title {
        font-size: 1.3rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .feedback-correct .feedback-title { color: #58A700; }
    .feedback-incorrect .feedback-title { color: #EA2B2B; }

    /* Achievement Badge */
    .badge {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(135deg, #FFC800 0%, #FF9500 100%);
        border-radius: 16px;
        padding: 16px;
        margin: 8px;
        min-width: 100px;
        box-shadow: 0 4px 12px rgba(255,200,0,0.3);
    }

    .badge.locked {
        background: linear-gradient(135deg, #CDCDCD 0%, #AFAFAF 100%);
        box-shadow: none;
    }

    .badge-icon {
        font-size: 2.5rem;
        margin-bottom: 8px;
    }

    .badge-name {
        color: white;
        font-weight: 700;
        font-size: 0.9rem;
        text-align: center;
    }

    /* Celebration Confetti */
    .confetti {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }

    .confetti-piece {
        position: absolute;
        width: 10px;
        height: 10px;
        animation: confetti-fall 3s ease-out forwards;
    }

    @keyframes confetti-fall {
        0% {
            transform: translateY(-100vh) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
        }
    }

    /* Mascot */
    .mascot {
        font-size: 4rem;
        animation: bounce 2s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    /* Level Badge */
    .level-badge {
        background: linear-gradient(135deg, #CE82FF 0%, #7C3AED 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        display: inline-block;
    }

    /* Gems */
    .gems {
        color: #1CB0F6;
        font-weight: 700;
    }

    /* Unit Path */
    .unit-header {
        background: linear-gradient(135deg, #58CC02 0%, #46A302 100%);
        color: white;
        padding: 20px;
        border-radius: 16px;
        margin: 20px 0;
        text-align: center;
    }

    .unit-title {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    /* Lesson Node */
    .lesson-node {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        margin: 10px auto;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
    }

    .lesson-node.available {
        background: linear-gradient(135deg, #58CC02 0%, #46A302 100%);
        box-shadow: 0 6px 0 #3D7A02;
    }

    .lesson-node.available:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 0 #3D7A02;
    }

    .lesson-node.completed {
        background: linear-gradient(135deg, #FFC800 0%, #FF9500 100%);
        box-shadow: 0 6px 0 #CC7700;
    }

    .lesson-node.locked {
        background: #CDCDCD;
        box-shadow: 0 6px 0 #AFAFAF;
        cursor: not-allowed;
    }

    /* Crown for completed */
    .crown {
        position: absolute;
        top: -15px;
        font-size: 1.2rem;
    }

    /* Daily Goal */
    .daily-goal {
        background: linear-gradient(135deg, #FFE066 0%, #FFC800 100%);
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        margin: 16px 0;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main-card {
            margin: 10px;
            padding: 20px;
            border-radius: 16px;
        }

        .question-text {
            font-size: 1.2rem;
        }

        .stats-bar {
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }

        .xp-container {
            width: 150px;
        }
    }

    /* Matching Game */
    .match-item {
        background: white;
        border: 2px solid #E5E5E5;
        border-radius: 12px;
        padding: 12px 16px;
        margin: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        display: inline-block;
    }

    .match-item:hover {
        border-color: #1CB0F6;
    }

    .match-item.selected {
        border-color: #1CB0F6;
        background: #DDF4FF;
    }

    .match-item.matched {
        border-color: #58CC02;
        background: #D7FFB8;
        opacity: 0.6;
    }

    /* Typing exercise */
    .typing-input {
        font-size: 1.2rem;
        padding: 16px;
        border: 2px solid #E5E5E5;
        border-radius: 12px;
        width: 100%;
        text-align: center;
    }

    .typing-input:focus {
        border-color: #1CB0F6;
        outline: none;
    }
</style>
""", unsafe_allow_html=True)

# ============== DATA DEFINITIONS ==============

LESSONS = {
    "unit1": {
        "title": "Consumer Behaviour Basics",
        "icon": "🧠",
        "lessons": [
            {
                "id": "1.1",
                "name": "What is Consumer Behaviour?",
                "icon": "📚",
                "xp": 10,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Consumer Behaviour is the study of...",
                        "options": [
                            "How companies make products",
                            "How individuals select, use, and dispose of products",
                            "How to advertise products",
                            "How to set prices"
                        ],
                        "correct": 1,
                        "explanation": "Consumer Behaviour studies how people make decisions about buying and using products!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which is NOT a part of consumer behaviour study?",
                        "options": [
                            "Purchase decisions",
                            "Product disposal",
                            "Factory manufacturing",
                            "Brand selection"
                        ],
                        "correct": 2,
                        "explanation": "Factory manufacturing is about production, not consumer behaviour!"
                    },
                    {
                        "type": "fill_blank",
                        "question": "Consumer behaviour helps marketers understand customer _____ and _____.",
                        "answer": ["needs", "wants"],
                        "hint": "Think about what drives people to buy things"
                    }
                ]
            },
            {
                "id": "1.2",
                "name": "Decision Making Process",
                "icon": "🎯",
                "xp": 15,
                "questions": [
                    {
                        "type": "order",
                        "question": "Put these decision-making steps in the correct order:",
                        "items": ["Need Recognition", "Information Search", "Evaluation of Alternatives", "Purchase Decision", "Post-Purchase Behaviour"],
                        "correct_order": [0, 1, 2, 3, 4]
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Riya realizes her phone battery doesn't last all day. This is which stage?",
                        "options": ["Information Search", "Need Recognition", "Evaluation", "Purchase"],
                        "correct": 1,
                        "explanation": "Need Recognition is when you realize there's a gap between your current and desired situation!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Watching YouTube reviews before buying is which stage?",
                        "options": ["Need Recognition", "Information Search", "Post-Purchase", "Evaluation"],
                        "correct": 1,
                        "explanation": "Information Search is gathering data about possible solutions!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Comparing Samsung vs iPhone features is which stage?",
                        "options": ["Information Search", "Need Recognition", "Evaluation of Alternatives", "Purchase Decision"],
                        "correct": 2,
                        "explanation": "Evaluation is when you compare different options against each other!"
                    }
                ]
            },
            {
                "id": "1.3",
                "name": "4 Types of Buying Behaviour",
                "icon": "🛒",
                "xp": 20,
                "questions": [
                    {
                        "type": "matching",
                        "question": "Match the buying behaviour with its characteristics:",
                        "pairs": [
                            {"left": "Complex Buying", "right": "High involvement, many brand differences"},
                            {"left": "Habitual Buying", "right": "Low involvement, few brand differences"},
                            {"left": "Variety Seeking", "right": "Low involvement, many brand differences"},
                            {"left": "Dissonance Reducing", "right": "High involvement, few brand differences"}
                        ]
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Buying salt without much thought is an example of:",
                        "options": ["Complex Buying", "Variety Seeking", "Habitual Buying", "Dissonance Reducing"],
                        "correct": 2,
                        "explanation": "Habitual Buying = Low involvement + Few brand differences. You just grab what you always buy!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Buying a house involves extensive research. This is:",
                        "options": ["Habitual Buying", "Complex Buying", "Variety Seeking", "Impulse Buying"],
                        "correct": 1,
                        "explanation": "Complex Buying = High involvement + Significant brand differences. Big decisions need lots of research!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Priya tries different chocolate brands each time for fun. This is:",
                        "options": ["Complex Buying", "Habitual Buying", "Variety Seeking", "Dissonance Reducing"],
                        "correct": 2,
                        "explanation": "Variety Seeking = Low involvement but switching brands for novelty, not dissatisfaction!"
                    }
                ]
            }
        ]
    },
    "unit2": {
        "title": "Marketing Strategy - STP",
        "icon": "🎯",
        "lessons": [
            {
                "id": "2.1",
                "name": "Market Segmentation",
                "icon": "📊",
                "xp": 15,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Segmentation means:",
                        "options": [
                            "Selling to everyone",
                            "Dividing market into distinct groups",
                            "Setting prices",
                            "Creating ads"
                        ],
                        "correct": 1,
                        "explanation": "Segmentation divides the market into groups with similar needs!"
                    },
                    {
                        "type": "matching",
                        "question": "Match segmentation type with example:",
                        "pairs": [
                            {"left": "Geographic", "right": "Urban vs Rural customers"},
                            {"left": "Demographic", "right": "Age groups 18-25, 26-40"},
                            {"left": "Psychographic", "right": "Health-conscious lifestyle"},
                            {"left": "Behavioural", "right": "Frequent vs occasional buyers"}
                        ]
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Targeting fitness enthusiasts is which segmentation?",
                        "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"],
                        "correct": 2,
                        "explanation": "Psychographic segmentation is based on lifestyle, values, and interests!"
                    }
                ]
            },
            {
                "id": "2.2",
                "name": "Targeting & Positioning",
                "icon": "🎪",
                "xp": 15,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "What does STP stand for?",
                        "options": [
                            "Sales, Trade, Profit",
                            "Segmentation, Targeting, Positioning",
                            "Strategy, Tactics, Planning",
                            "Supply, Transport, Production"
                        ],
                        "correct": 1,
                        "explanation": "STP = Segmentation, Targeting, Positioning - the foundation of marketing strategy!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Rolex focuses only on luxury buyers. This targeting is:",
                        "options": ["Undifferentiated", "Differentiated", "Concentrated", "Micro"],
                        "correct": 2,
                        "explanation": "Concentrated targeting focuses on one specific segment!"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Positioning is about:",
                        "options": [
                            "Where to place products in store",
                            "How customers perceive your brand vs competitors",
                            "Geographic location",
                            "Price setting"
                        ],
                        "correct": 1,
                        "explanation": "Positioning is the place your brand occupies in customers' minds!"
                    }
                ]
            },
            {
                "id": "2.3",
                "name": "Customer Retention & Churn",
                "icon": "📈",
                "xp": 20,
                "questions": [
                    {
                        "type": "multiple_choice",
                        "question": "Customer Retention Rate measures:",
                        "options": [
                            "New customers gained",
                            "Customers kept over time",
                            "Total revenue",
                            "Market share"
                        ],
                        "correct": 1,
                        "explanation": "Retention Rate = percentage of customers you keep!"
                    },
                    {
                        "type": "calculation",
                        "question": "Company had 1000 customers at start, gained 200 new, ended with 900. What's the retention rate?",
                        "formula": "((CE-CN)/CS) × 100 = ((900-200)/1000) × 100",
                        "answer": 70,
                        "unit": "%",
                        "explanation": "Lost 300 customers (1000→900+200new=1200-300=900), so retained 700 out of 1000 = 70%"
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Churn Rate is:",
                        "options": [
                            "Same as retention rate",
                            "Opposite of retention rate",
                            "New customer rate",
                            "Growth rate"
                        ],
                        "correct": 1,
                        "explanation": "Churn Rate = 100% - Retention Rate. It measures customer loss!"
                    },
                    {
                        "type": "calculation",
                        "question": "If retention rate is 70%, what is the churn rate?",
                        "formula": "100% - 70%",
                        "answer": 30,
                        "unit": "%",
                        "explanation": "Churn = 100% - Retention = 100% - 70% = 30%"
                    }
                ]
            }
        ]
    }
}

ACHIEVEMENTS = [
    {"id": "first_lesson", "name": "First Steps", "icon": "👶", "desc": "Complete your first lesson", "xp_required": 0, "lessons_required": 1},
    {"id": "streak_3", "name": "On Fire", "icon": "🔥", "desc": "3 day streak", "streak_required": 3},
    {"id": "streak_7", "name": "Week Warrior", "icon": "⚡", "desc": "7 day streak", "streak_required": 7},
    {"id": "perfect_lesson", "name": "Perfectionist", "icon": "💎", "desc": "Complete a lesson with no mistakes", "perfect_required": True},
    {"id": "xp_100", "name": "Century", "icon": "💯", "desc": "Earn 100 XP", "xp_required": 100},
    {"id": "xp_500", "name": "Scholar", "icon": "🎓", "desc": "Earn 500 XP", "xp_required": 500},
    {"id": "unit_complete", "name": "Unit Master", "icon": "🏆", "desc": "Complete a full unit", "unit_required": True},
    {"id": "all_lessons", "name": "Consumer Expert", "icon": "👑", "desc": "Complete all lessons", "all_required": True}
]

DAILY_GOALS = [10, 20, 30, 50]  # XP targets

# ============== SESSION STATE INITIALIZATION ==============

def init_session_state():
    defaults = {
        'xp': 0,
        'level': 1,
        'hearts': 5,
        'max_hearts': 5,
        'gems': 50,
        'streak': 0,
        'last_practice_date': None,
        'completed_lessons': set(),
        'current_lesson': None,
        'current_question': 0,
        'lesson_mistakes': 0,
        'daily_xp': 0,
        'daily_goal': 20,
        'achievements_unlocked': set(),
        'show_celebration': False,
        'selected_answer': None,
        'answer_submitted': False,
        'page': 'home'
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# ============== HELPER FUNCTIONS ==============

def calculate_level(xp):
    """Calculate level based on XP (100 XP per level)"""
    return (xp // 100) + 1

def xp_for_next_level(current_xp):
    """Calculate XP needed for next level"""
    current_level = calculate_level(current_xp)
    next_level_xp = current_level * 100
    return next_level_xp - current_xp

def xp_progress_percent(current_xp):
    """Calculate progress percentage to next level"""
    level = calculate_level(current_xp)
    level_start = (level - 1) * 100
    progress = current_xp - level_start
    return (progress / 100) * 100

def check_streak():
    """Check and update streak"""
    today = datetime.now().date()

    if st.session_state.last_practice_date is None:
        st.session_state.streak = 1
        st.session_state.last_practice_date = today
    elif st.session_state.last_practice_date == today:
        pass  # Already practiced today
    elif st.session_state.last_practice_date == today - timedelta(days=1):
        st.session_state.streak += 1
        st.session_state.last_practice_date = today
    else:
        st.session_state.streak = 1  # Streak broken
        st.session_state.last_practice_date = today

def add_xp(amount):
    """Add XP and check for level up"""
    old_level = calculate_level(st.session_state.xp)
    st.session_state.xp += amount
    st.session_state.daily_xp += amount
    new_level = calculate_level(st.session_state.xp)

    if new_level > old_level:
        st.session_state.show_celebration = True
        st.session_state.gems += 10  # Bonus gems on level up

    check_achievements()

def lose_heart():
    """Lose a heart on wrong answer"""
    if st.session_state.hearts > 0:
        st.session_state.hearts -= 1

def check_achievements():
    """Check and unlock achievements"""
    for ach in ACHIEVEMENTS:
        if ach['id'] in st.session_state.achievements_unlocked:
            continue

        unlocked = False

        if 'lessons_required' in ach and len(st.session_state.completed_lessons) >= ach['lessons_required']:
            unlocked = True
        elif 'xp_required' in ach and st.session_state.xp >= ach['xp_required']:
            unlocked = True
        elif 'streak_required' in ach and st.session_state.streak >= ach['streak_required']:
            unlocked = True

        if unlocked:
            st.session_state.achievements_unlocked.add(ach['id'])
            st.session_state.gems += 5

def render_confetti():
    """Render celebration confetti"""
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
    confetti_html = '<div class="confetti">'
    for i in range(50):
        left = random.randint(0, 100)
        delay = random.random() * 2
        color = random.choice(colors)
        confetti_html += f'<div class="confetti-piece" style="left: {left}%; animation-delay: {delay}s; background: {color};"></div>'
    confetti_html += '</div>'
    st.markdown(confetti_html, unsafe_allow_html=True)

# ============== UI COMPONENTS ==============

def render_stats_bar():
    """Render top stats bar"""
    col1, col2, col3, col4, col5 = st.columns([1, 1.5, 1, 1, 1])

    with col1:
        st.markdown(f"""
        <div class="stat-item">
            <span class="streak-fire">🔥</span>
            <span>{st.session_state.streak}</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        progress = xp_progress_percent(st.session_state.xp)
        st.markdown(f"""
        <div class="stat-item">
            <span>⭐ Level {calculate_level(st.session_state.xp)}</span>
            <div class="xp-container">
                <div class="xp-fill" style="width: {progress}%;"></div>
                <span class="xp-text">{int(progress)}%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        hearts_display = "❤️" * st.session_state.hearts + "🖤" * (st.session_state.max_hearts - st.session_state.hearts)
        st.markdown(f'<div class="hearts">{hearts_display}</div>', unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="stat-item gems">
            <span>💎 {st.session_state.gems}</span>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="stat-item">
            <span>🎯 {st.session_state.daily_xp}/{st.session_state.daily_goal} XP</span>
        </div>
        """, unsafe_allow_html=True)

def render_home():
    """Render home/learning path page"""
    st.markdown('<div class="mascot">🦉</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; text-align: center;'>ConsumerQuest</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #B0C4DE; text-align: center; font-size: 1.2rem;'>Master Consumer Behaviour - One lesson at a time!</p>", unsafe_allow_html=True)

    # Daily goal progress
    goal_progress = min(100, (st.session_state.daily_xp / st.session_state.daily_goal) * 100)
    st.markdown(f"""
    <div class="daily-goal">
        <strong>🎯 Daily Goal: {st.session_state.daily_xp}/{st.session_state.daily_goal} XP</strong>
        <div class="xp-container" style="width: 100%; margin-top: 10px;">
            <div class="xp-fill" style="width: {goal_progress}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Render Units
    for unit_id, unit in LESSONS.items():
        st.markdown(f"""
        <div class="unit-header">
            <div class="unit-title">{unit['icon']} {unit['title']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Render lessons in path
        cols = st.columns(len(unit['lessons']))

        for idx, lesson in enumerate(unit['lessons']):
            with cols[idx]:
                is_completed = lesson['id'] in st.session_state.completed_lessons

                # Check if lesson is available (previous completed or first lesson)
                is_available = idx == 0 or unit['lessons'][idx-1]['id'] in st.session_state.completed_lessons

                if is_completed:
                    status_class = "completed"
                    crown = '<span class="crown">👑</span>'
                elif is_available:
                    status_class = "available"
                    crown = ""
                else:
                    status_class = "locked"
                    crown = ""

                if is_available or is_completed:
                    if st.button(f"{lesson['icon']}", key=f"lesson_{lesson['id']}", help=lesson['name']):
                        st.session_state.current_lesson = lesson
                        st.session_state.current_question = 0
                        st.session_state.lesson_mistakes = 0
                        st.session_state.selected_answer = None
                        st.session_state.answer_submitted = False
                        st.session_state.page = 'lesson'
                        st.rerun()
                else:
                    st.button(f"🔒", key=f"locked_{lesson['id']}", disabled=True, help="Complete previous lesson first")

                st.markdown(f"<p style='color: white; text-align: center; font-size: 0.9rem;'>{lesson['name']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #FFC800; text-align: center; font-size: 0.8rem;'>+{lesson['xp']} XP</p>", unsafe_allow_html=True)

def render_lesson():
    """Render lesson/quiz page"""
    lesson = st.session_state.current_lesson

    if not lesson:
        st.session_state.page = 'home'
        st.rerun()
        return

    questions = lesson.get('questions', [])
    q_idx = st.session_state.current_question

    # Check if lesson complete
    if q_idx >= len(questions):
        render_lesson_complete()
        return

    question = questions[q_idx]

    # Progress bar
    progress = (q_idx / len(questions)) * 100
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
        <button onclick="window.location.reload()" style="background: none; border: none; font-size: 1.5rem; cursor: pointer;">✕</button>
        <div class="xp-container" style="flex: 1;">
            <div class="xp-fill" style="width: {progress}%; background: linear-gradient(90deg, #58CC02 0%, #46A302 100%);"></div>
        </div>
        <span class="hearts">{"❤️" * st.session_state.hearts}</span>
    </div>
    """, unsafe_allow_html=True)

    # Back button
    if st.button("← Back", key="back_btn"):
        st.session_state.page = 'home'
        st.session_state.current_lesson = None
        st.rerun()

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    # Render question based on type
    if question['type'] == 'multiple_choice':
        render_multiple_choice(question)
    elif question['type'] == 'matching':
        render_matching(question)
    elif question['type'] == 'calculation':
        render_calculation(question)
    elif question['type'] == 'fill_blank':
        render_fill_blank(question)
    elif question['type'] == 'order':
        render_ordering(question)
    else:
        render_multiple_choice(question)  # Default

    st.markdown('</div>', unsafe_allow_html=True)

def render_multiple_choice(question):
    """Render multiple choice question"""
    st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

    for idx, option in enumerate(question['options']):
        is_selected = st.session_state.selected_answer == idx

        if st.session_state.answer_submitted:
            if idx == question['correct']:
                btn_class = "correct"
            elif is_selected:
                btn_class = "incorrect"
            else:
                btn_class = ""
        else:
            btn_class = "selected" if is_selected else ""

        if st.button(option, key=f"opt_{idx}", disabled=st.session_state.answer_submitted):
            if not st.session_state.answer_submitted:
                st.session_state.selected_answer = idx
                st.rerun()

    # Check button
    if not st.session_state.answer_submitted:
        if st.button("CHECK", key="check_btn", disabled=st.session_state.selected_answer is None):
            st.session_state.answer_submitted = True
            if st.session_state.selected_answer != question['correct']:
                lose_heart()
                st.session_state.lesson_mistakes += 1
            st.rerun()
    else:
        # Show feedback
        is_correct = st.session_state.selected_answer == question['correct']

        if is_correct:
            st.success(f"🎉 **Correct!** {question.get('explanation', '')}")
        else:
            st.error(f"❌ **Not quite!** {question.get('explanation', '')}")

        if st.button("CONTINUE", key="continue_btn"):
            st.session_state.current_question += 1
            st.session_state.selected_answer = None
            st.session_state.answer_submitted = False
            st.rerun()

def render_matching(question):
    """Render matching question"""
    st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

    pairs = question['pairs']

    # Initialize matching state
    if 'match_selections' not in st.session_state:
        st.session_state.match_selections = {}
    if 'matched_pairs' not in st.session_state:
        st.session_state.matched_pairs = set()

    # Check if all matched
    all_matched = len(st.session_state.matched_pairs) == len(pairs)

    if all_matched:
        st.success("🎉 **All matched correctly!**")
        if st.button("CONTINUE", key="continue_match"):
            st.session_state.current_question += 1
            st.session_state.match_selections = {}
            st.session_state.matched_pairs = set()
            st.rerun()
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Terms:**")
            for idx, pair in enumerate(pairs):
                if idx not in st.session_state.matched_pairs:
                    if st.button(pair['left'], key=f"left_{idx}"):
                        st.session_state.match_selections['left'] = idx
                        st.rerun()

        with col2:
            st.markdown("**Definitions:**")
            shuffled_indices = list(range(len(pairs)))
            random.seed(42)  # Consistent shuffle
            random.shuffle(shuffled_indices)

            for idx in shuffled_indices:
                pair = pairs[idx]
                if idx not in st.session_state.matched_pairs:
                    if st.button(pair['right'], key=f"right_{idx}"):
                        if 'left' in st.session_state.match_selections:
                            left_idx = st.session_state.match_selections['left']
                            if left_idx == idx:  # Correct match
                                st.session_state.matched_pairs.add(idx)
                            else:
                                lose_heart()
                                st.session_state.lesson_mistakes += 1
                            st.session_state.match_selections = {}
                            st.rerun()

def render_calculation(question):
    """Render calculation question"""
    st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

    st.info(f"💡 Formula: {question['formula']}")

    answer = st.number_input("Your answer:", key="calc_answer", step=1)

    if st.button("CHECK", key="check_calc"):
        if int(answer) == question['answer']:
            st.success(f"🎉 **Correct!** {question['answer']}{question.get('unit', '')} - {question.get('explanation', '')}")
            if st.button("CONTINUE", key="continue_calc"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            st.error(f"❌ The correct answer is {question['answer']}{question.get('unit', '')}. {question.get('explanation', '')}")
            lose_heart()
            st.session_state.lesson_mistakes += 1
            if st.button("CONTINUE", key="continue_calc_wrong"):
                st.session_state.current_question += 1
                st.rerun()

def render_fill_blank(question):
    """Render fill in the blank question"""
    st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

    if 'hint' in question:
        st.info(f"💡 Hint: {question['hint']}")

    user_answers = []
    for idx, _ in enumerate(question['answer']):
        ans = st.text_input(f"Blank {idx+1}:", key=f"blank_{idx}")
        user_answers.append(ans.lower().strip())

    if st.button("CHECK", key="check_fill"):
        correct_answers = [a.lower() for a in question['answer']]
        if user_answers == correct_answers:
            st.success("🎉 **Correct!**")
        else:
            st.error(f"❌ The correct answers are: {', '.join(question['answer'])}")
            lose_heart()
            st.session_state.lesson_mistakes += 1

        if st.button("CONTINUE", key="continue_fill"):
            st.session_state.current_question += 1
            st.rerun()

def render_ordering(question):
    """Render ordering question"""
    st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

    items = question['items']

    st.markdown("**Drag to reorder (use numbers 1-5):**")

    order = []
    for idx, item in enumerate(items):
        pos = st.selectbox(f"{item}", options=list(range(1, len(items)+1)), key=f"order_{idx}")
        order.append(pos)

    if st.button("CHECK", key="check_order"):
        # Check if order is 1,2,3,4,5
        if order == list(range(1, len(items)+1)):
            st.success("🎉 **Correct order!**")
        else:
            st.error("❌ Not quite right. The correct order is shown above.")
            lose_heart()
            st.session_state.lesson_mistakes += 1

        if st.button("CONTINUE", key="continue_order"):
            st.session_state.current_question += 1
            st.rerun()

def render_lesson_complete():
    """Render lesson completion screen"""
    lesson = st.session_state.current_lesson

    # Add XP
    xp_earned = lesson['xp']
    if st.session_state.lesson_mistakes == 0:
        xp_earned += 5  # Bonus for perfect lesson

    st.markdown('<div class="main-card" style="text-align: center;">', unsafe_allow_html=True)

    # Celebration animation
    render_confetti()

    st.markdown('<div class="mascot">🎉</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color: #58CC02;'>Lesson Complete!</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("XP Earned", f"+{xp_earned}")
    with col2:
        st.metric("Mistakes", st.session_state.lesson_mistakes)
    with col3:
        accuracy = max(0, 100 - (st.session_state.lesson_mistakes * 20))
        st.metric("Accuracy", f"{accuracy}%")

    if st.session_state.lesson_mistakes == 0:
        st.success("🌟 **PERFECT!** No mistakes!")

    # Mark lesson as complete and add XP
    if lesson['id'] not in st.session_state.completed_lessons:
        st.session_state.completed_lessons.add(lesson['id'])
        add_xp(xp_earned)
        check_streak()

    if st.button("CONTINUE", key="finish_lesson"):
        st.session_state.page = 'home'
        st.session_state.current_lesson = None
        st.session_state.current_question = 0
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def render_achievements():
    """Render achievements page"""
    st.markdown("<h1 style='color: white; text-align: center;'>🏆 Achievements</h1>", unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    cols = st.columns(4)

    for idx, ach in enumerate(ACHIEVEMENTS):
        with cols[idx % 4]:
            is_unlocked = ach['id'] in st.session_state.achievements_unlocked
            badge_class = "" if is_unlocked else "locked"

            st.markdown(f"""
            <div class="badge {badge_class}">
                <span class="badge-icon">{ach['icon'] if is_unlocked else '🔒'}</span>
                <span class="badge-name">{ach['name']}</span>
            </div>
            <p style="text-align: center; font-size: 0.8rem; color: #666;">{ach['desc']}</p>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def render_profile():
    """Render profile/stats page"""
    st.markdown("<h1 style='color: white; text-align: center;'>📊 Your Stats</h1>", unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px;">
            <div class="mascot">🦉</div>
            <h2>Level {calculate_level(st.session_state.xp)}</h2>
            <div class="level-badge">Consumer Apprentice</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.metric("Total XP", st.session_state.xp)
        st.metric("Current Streak", f"🔥 {st.session_state.streak} days")
        st.metric("Lessons Completed", len(st.session_state.completed_lessons))
        st.metric("Gems", f"💎 {st.session_state.gems}")

    # Daily goal setting
    st.markdown("---")
    st.markdown("### 🎯 Set Daily Goal")
    new_goal = st.select_slider("Daily XP Goal:", options=DAILY_GOALS, value=st.session_state.daily_goal)
    if new_goal != st.session_state.daily_goal:
        st.session_state.daily_goal = new_goal
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ============== MAIN APP ==============

def main():
    # Render stats bar
    render_stats_bar()

    # Navigation
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏠 Learn", use_container_width=True):
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

    st.markdown("---")

    # Render current page
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'lesson':
        render_lesson()
    elif st.session_state.page == 'achievements':
        render_achievements()
    elif st.session_state.page == 'profile':
        render_profile()

    # Show celebration modal
    if st.session_state.show_celebration:
        st.balloons()
        st.session_state.show_celebration = False

if __name__ == "__main__":
    main()
