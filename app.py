"""
Consumer Behaviour Learning System
Interactive study app for COBE201-1 - Units 1 & 2
Built for first-year Business Management students
"""

import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Consumer Behaviour Learning Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visuals
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #DBEAFE 0%, #EDE9FE 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .concept-card {
        background: #F8FAFC;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
    }
    .quiz-correct {
        background: #D1FAE5;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #10B981;
    }
    .quiz-incorrect {
        background: #FEE2E2;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #EF4444;
    }
    .flashcard {
        background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        cursor: pointer;
    }
    .stProgress > div > div > div > div {
        background-color: #10B981;
    }
</style>
""", unsafe_allow_html=True)

# ============== DATA DEFINITIONS ==============

# Key Definitions for Flashcards
FLASHCARDS = [
    {
        "term": "Consumer Behaviour",
        "definition": "The study of individuals, groups, or organizations and the processes they use to select, secure, use, and dispose of products, services, experiences, or ideas to satisfy their needs."
    },
    {
        "term": "Need Recognition",
        "definition": "The first stage of decision-making where the consumer identifies a gap between their current state and desired state."
    },
    {
        "term": "Complex Buying Behaviour",
        "definition": "High involvement purchase with significant differences between brands. Example: buying a car or house."
    },
    {
        "term": "Habitual Buying Behaviour",
        "definition": "Low involvement purchase with few differences between brands. Example: buying salt or sugar."
    },
    {
        "term": "Dissonance-Reducing Behaviour",
        "definition": "High involvement but few perceived differences between brands. Buyer may experience post-purchase dissonance."
    },
    {
        "term": "Variety-Seeking Behaviour",
        "definition": "Low involvement but significant brand differences. Consumer switches brands for variety, not dissatisfaction."
    },
    {
        "term": "Market Segmentation",
        "definition": "Dividing a market into distinct groups of buyers with different needs, characteristics, or behaviours."
    },
    {
        "term": "Targeting",
        "definition": "Evaluating each market segment's attractiveness and selecting one or more segments to enter."
    },
    {
        "term": "Positioning",
        "definition": "Arranging for a product to occupy a clear, distinctive, and desirable place in target consumers' minds."
    },
    {
        "term": "Customer Retention Rate",
        "definition": "The percentage of customers a company retains over a given period. Formula: ((CE-CN)/CS) x 100"
    },
    {
        "term": "Churn Rate",
        "definition": "The percentage of customers who stop using a product/service. Formula: (Lost Customers / Total Customers at Start) x 100"
    },
    {
        "term": "Perceptual Map",
        "definition": "A visual representation of how consumers perceive brands based on key attributes like price and quality."
    },
    {
        "term": "Evoked Set",
        "definition": "The set of brands that a consumer considers when making a purchase decision."
    },
    {
        "term": "Post-Purchase Behaviour",
        "definition": "Consumer actions after buying, including satisfaction evaluation, brand loyalty, or cognitive dissonance."
    },
    {
        "term": "Geographic Segmentation",
        "definition": "Dividing markets by location: nations, states, regions, cities, or neighborhoods."
    },
    {
        "term": "Psychographic Segmentation",
        "definition": "Dividing buyers based on lifestyle, personality, values, and social class."
    },
    {
        "term": "Behavioural Segmentation",
        "definition": "Dividing buyers based on knowledge, attitudes, uses, or responses to a product."
    }
]

# Quiz Questions
QUIZ_QUESTIONS = [
    {
        "question": "What is the FIRST stage in the consumer decision-making process?",
        "options": ["Information Search", "Need Recognition", "Evaluation of Alternatives", "Purchase Decision"],
        "correct": 1,
        "explanation": "Need Recognition is when the consumer realizes there's a gap between their current state and desired state."
    },
    {
        "question": "Riya is buying her first laptop for college. She researches extensively, compares brands, and reads reviews. What type of buying behaviour is this?",
        "options": ["Habitual Buying", "Variety-Seeking", "Complex Buying", "Dissonance-Reducing"],
        "correct": 2,
        "explanation": "Complex Buying Behaviour involves high involvement and significant differences between brands."
    },
    {
        "question": "Arjun buys the same brand of salt every week without much thought. This is an example of:",
        "options": ["Complex Buying Behaviour", "Dissonance-Reducing Behaviour", "Variety-Seeking Behaviour", "Habitual Buying Behaviour"],
        "correct": 3,
        "explanation": "Habitual Buying involves low involvement and few perceived differences between brands."
    },
    {
        "question": "What does STP stand for in marketing?",
        "options": ["Sales, Target, Profit", "Segmentation, Targeting, Positioning", "Strategy, Tactics, Planning", "Supply, Trade, Purchase"],
        "correct": 1,
        "explanation": "STP is the foundation of marketing strategy: Segmenting the market, Targeting segments, and Positioning the brand."
    },
    {
        "question": "A company started with 1000 customers, gained 200 new customers, and ended with 900. What is the retention rate?",
        "options": ["70%", "80%", "90%", "60%"],
        "correct": 0,
        "explanation": "Retention Rate = ((CE-CN)/CS) x 100 = ((900-200)/1000) x 100 = 70%"
    },
    {
        "question": "Priya likes trying different chocolate brands each time. Which buying behaviour is this?",
        "options": ["Complex Buying", "Habitual Buying", "Variety-Seeking", "Dissonance-Reducing"],
        "correct": 2,
        "explanation": "Variety-Seeking involves low involvement but switching brands for the sake of variety."
    },
    {
        "question": "Which segmentation type divides customers based on lifestyle and values?",
        "options": ["Geographic", "Demographic", "Psychographic", "Behavioural"],
        "correct": 2,
        "explanation": "Psychographic segmentation groups people by lifestyle, personality, values, and social class."
    },
    {
        "question": "What is the formula for Churn Rate?",
        "options": [
            "(New Customers / Total) x 100",
            "(Lost Customers / Starting Customers) x 100",
            "(Retained / Total) x 100",
            "(Profit / Revenue) x 100"
        ],
        "correct": 1,
        "explanation": "Churn Rate measures customer loss: (Lost Customers / Total Customers at Start) x 100"
    },
    {
        "question": "Rahul bought an expensive sofa but felt uncertain afterward if he made the right choice. This is called:",
        "options": ["Buyer's Remorse", "Cognitive Dissonance", "Post-Purchase Evaluation", "Brand Switching"],
        "correct": 1,
        "explanation": "Cognitive Dissonance is the discomfort felt after a high-involvement purchase when uncertain about the decision."
    },
    {
        "question": "Which is NOT a stage in the decision-making process?",
        "options": ["Need Recognition", "Brand Loyalty", "Purchase Decision", "Post-Purchase Behaviour"],
        "correct": 1,
        "explanation": "The 5 stages are: Need Recognition, Information Search, Evaluation, Purchase Decision, Post-Purchase Behaviour."
    }
]

# Case Studies
CASE_STUDIES = [
    {
        "title": "Cafe Coffee Day vs Starbucks",
        "scenario": """
        Ananya, a 22-year-old MBA student, visits coffee shops frequently. She notices:
        - CCD: Affordable, local feel, good for group studies
        - Starbucks: Premium pricing, aspirational brand, Instagram-worthy

        For daily coffee, she goes to CCD. But for special occasions or social media posts, she chooses Starbucks.
        """,
        "questions": [
            {
                "q": "What type of segmentation does Starbucks primarily use?",
                "options": ["Geographic", "Psychographic", "Demographic", "Behavioural"],
                "correct": 1,
                "explanation": "Starbucks targets based on lifestyle and aspirations (psychographic segmentation)."
            },
            {
                "q": "What buying behaviour does Ananya show for daily coffee?",
                "options": ["Complex", "Habitual", "Variety-Seeking", "Dissonance-Reducing"],
                "correct": 1,
                "explanation": "Daily coffee is low involvement with brand loyalty - habitual buying."
            }
        ]
    },
    {
        "title": "Smartphone Purchase Journey",
        "scenario": """
        Vikram wants to buy a new smartphone (budget: Rs 30,000-40,000). His journey:
        1. Old phone slowing down (realizes need)
        2. Watches YouTube reviews, asks friends (information search)
        3. Compares Samsung, OnePlus, iPhone SE (evaluation)
        4. Visits store, tests phones, buys OnePlus (purchase)
        5. Posts on social media, recommends to others (post-purchase)
        """,
        "questions": [
            {
                "q": "Which stage involves watching YouTube reviews?",
                "options": ["Need Recognition", "Information Search", "Evaluation", "Purchase Decision"],
                "correct": 1,
                "explanation": "Watching reviews and asking friends is Information Search stage."
            },
            {
                "q": "Vikram's smartphone purchase is an example of:",
                "options": ["Habitual Buying", "Variety-Seeking", "Complex Buying", "Impulse Buying"],
                "correct": 2,
                "explanation": "High involvement + significant brand differences = Complex Buying Behaviour."
            }
        ]
    },
    {
        "title": "Netflix Customer Retention",
        "scenario": """
        Netflix India data (hypothetical):
        - Start of year: 10,000 subscribers
        - New subscribers gained: 3,000
        - End of year: 11,000 subscribers
        - Subscription cost increased by 20%

        Many users share passwords. Netflix introduced cheaper mobile-only plans.
        """,
        "questions": [
            {
                "q": "What is Netflix's customer retention rate?",
                "options": ["80%", "90%", "110%", "70%"],
                "correct": 0,
                "explanation": "Retention = ((11000-3000)/10000) x 100 = 80%. They lost 2000 and gained 3000."
            },
            {
                "q": "Mobile-only plans target which segment?",
                "options": ["Premium users", "Price-sensitive users", "International users", "Business users"],
                "correct": 1,
                "explanation": "Cheaper mobile plans target price-sensitive customers (behavioural/economic segmentation)."
            }
        ]
    }
]

# Decision Making Process Steps
DECISION_PROCESS = [
    {"step": 1, "name": "Need Recognition", "icon": "💡", "description": "Consumer realizes a gap between current and desired state", "example": "Your phone battery doesn't last a full day anymore"},
    {"step": 2, "name": "Information Search", "icon": "🔍", "description": "Consumer seeks information about solutions", "example": "Reading reviews, asking friends, visiting stores"},
    {"step": 3, "name": "Evaluation of Alternatives", "icon": "⚖️", "description": "Consumer compares different options", "example": "Comparing iPhone vs Samsung vs OnePlus features"},
    {"step": 4, "name": "Purchase Decision", "icon": "🛒", "description": "Consumer decides which product to buy", "example": "Choosing OnePlus based on value for money"},
    {"step": 5, "name": "Post-Purchase Behaviour", "icon": "🔄", "description": "Consumer evaluates satisfaction after purchase", "example": "Feeling happy with choice or experiencing regret"}
]

# Buying Behaviour Types
BUYING_BEHAVIOURS = [
    {
        "type": "Complex Buying",
        "involvement": "High",
        "brand_diff": "Significant",
        "color": "#EF4444",
        "examples": ["Cars", "Houses", "Laptops", "Education"],
        "characteristics": "Extensive research, multiple evaluations, high risk"
    },
    {
        "type": "Dissonance-Reducing",
        "involvement": "High",
        "brand_diff": "Few",
        "color": "#F59E0B",
        "examples": ["Carpet", "Furniture", "Air Conditioner"],
        "characteristics": "May feel uncertainty after purchase, seeks reassurance"
    },
    {
        "type": "Variety-Seeking",
        "involvement": "Low",
        "brand_diff": "Significant",
        "color": "#10B981",
        "examples": ["Snacks", "Beverages", "Cosmetics"],
        "characteristics": "Switches brands for novelty, not dissatisfaction"
    },
    {
        "type": "Habitual Buying",
        "involvement": "Low",
        "brand_diff": "Few",
        "color": "#3B82F6",
        "examples": ["Salt", "Sugar", "Milk", "Bread"],
        "characteristics": "Automatic purchases, brand loyalty through habit"
    }
]

# ============== MAIN APPLICATION ==============

def main():
    # Sidebar Navigation
    st.sidebar.title("📚 Learning Hub")

    page = st.sidebar.radio(
        "Choose a Module:",
        ["🏠 Home", "📊 Concept Visualizations", "📝 Quiz Zone", "🎴 Flashcards", "📖 Case Studies", "🔬 Brand Analysis Tool"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Your Progress")

    # Initialize session state for progress tracking
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quizzes_attempted' not in st.session_state:
        st.session_state.quizzes_attempted = 0
    if 'flashcards_viewed' not in st.session_state:
        st.session_state.flashcards_viewed = set()

    progress = len(st.session_state.flashcards_viewed) / len(FLASHCARDS)
    st.sidebar.progress(progress)
    st.sidebar.write(f"Flashcards: {len(st.session_state.flashcards_viewed)}/{len(FLASHCARDS)}")

    if st.session_state.quizzes_attempted > 0:
        accuracy = (st.session_state.quiz_score / st.session_state.quizzes_attempted) * 100
        st.sidebar.write(f"Quiz Accuracy: {accuracy:.0f}%")

    # Route to selected page
    if page == "🏠 Home":
        show_home()
    elif page == "📊 Concept Visualizations":
        show_visualizations()
    elif page == "📝 Quiz Zone":
        show_quiz()
    elif page == "🎴 Flashcards":
        show_flashcards()
    elif page == "📖 Case Studies":
        show_case_studies()
    elif page == "🔬 Brand Analysis Tool":
        show_brand_analysis()

def show_home():
    st.markdown('<div class="main-header">Consumer Behaviour Learning Hub</div>', unsafe_allow_html=True)
    st.markdown("### Welcome to your interactive study companion for COBE201-1!")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📚 Unit 1: Fundamentals")
        st.markdown("""
        - What is Consumer Behaviour?
        - The 5-Stage Decision-Making Process
        - 4 Types of Buying Behaviour
        - Customer Types & Classifications
        """)

    with col2:
        st.markdown("#### 📈 Unit 2: Strategy")
        st.markdown("""
        - STP: Segmentation, Targeting, Positioning
        - Market Segmentation Types
        - Brand Positioning & Perceptual Maps
        - Customer Retention & Churn Rate
        """)

    st.markdown("---")
    st.markdown("### 🚀 Quick Start Guide")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("**📊 Visualizations**\nInteractive diagrams of key concepts")
    with col2:
        st.success("**📝 Quiz Zone**\nTest your understanding")
    with col3:
        st.warning("**🎴 Flashcards**\nMemorize key definitions")

def show_visualizations():
    st.markdown("## 📊 Concept Visualizations")

    viz_type = st.selectbox(
        "Choose a concept to explore:",
        ["Decision-Making Process", "Buying Behaviour Matrix", "STP Framework", "Customer Retention"]
    )

    if viz_type == "Decision-Making Process":
        st.markdown("### 🧠 The 5-Stage Decision-Making Process")
        st.markdown("*Click on each stage to learn more*")

        cols = st.columns(5)
        for i, step in enumerate(DECISION_PROCESS):
            with cols[i]:
                with st.expander(f"{step['icon']} {step['step']}"):
                    st.markdown(f"**{step['name']}**")
                    st.write(step['description'])
                    st.info(f"Example: {step['example']}")

        # Visual flow
        st.markdown("---")
        flow = " → ".join([f"{s['icon']} {s['name']}" for s in DECISION_PROCESS])
        st.markdown(f"### Flow: {flow}")

    elif viz_type == "Buying Behaviour Matrix":
        st.markdown("### 🎯 4 Types of Buying Behaviour")
        st.markdown("*Based on Involvement Level and Brand Differences*")

        # Create 2x2 matrix
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### High Involvement")
            for bb in BUYING_BEHAVIOURS:
                if bb['involvement'] == 'High':
                    st.markdown(f"""
                    <div style="background: {bb['color']}20; padding: 1rem; border-radius: 10px; border-left: 4px solid {bb['color']}; margin: 0.5rem 0;">
                        <strong>{bb['type']}</strong><br>
                        Brand Differences: {bb['brand_diff']}<br>
                        Examples: {', '.join(bb['examples'])}<br>
                        <em>{bb['characteristics']}</em>
                    </div>
                    """, unsafe_allow_html=True)

        with col2:
            st.markdown("#### Low Involvement")
            for bb in BUYING_BEHAVIOURS:
                if bb['involvement'] == 'Low':
                    st.markdown(f"""
                    <div style="background: {bb['color']}20; padding: 1rem; border-radius: 10px; border-left: 4px solid {bb['color']}; margin: 0.5rem 0;">
                        <strong>{bb['type']}</strong><br>
                        Brand Differences: {bb['brand_diff']}<br>
                        Examples: {', '.join(bb['examples'])}<br>
                        <em>{bb['characteristics']}</em>
                    </div>
                    """, unsafe_allow_html=True)

    elif viz_type == "STP Framework":
        st.markdown("### 🎯 STP: Segmentation, Targeting, Positioning")

        tab1, tab2, tab3 = st.tabs(["Segmentation", "Targeting", "Positioning"])

        with tab1:
            st.markdown("#### Market Segmentation Types")
            seg_types = {
                "Geographic": {"icon": "🌍", "bases": ["Country", "Region", "City", "Climate"], "example": "McDonald's menu varies by country"},
                "Demographic": {"icon": "👥", "bases": ["Age", "Gender", "Income", "Education"], "example": "Johnson's Baby targets parents of infants"},
                "Psychographic": {"icon": "🧠", "bases": ["Lifestyle", "Values", "Personality", "Social Class"], "example": "Harley-Davidson targets freedom-seekers"},
                "Behavioural": {"icon": "🛒", "bases": ["Usage Rate", "Loyalty", "Benefits Sought", "Occasion"], "example": "Airlines reward frequent flyers"}
            }

            for seg_name, seg_data in seg_types.items():
                with st.expander(f"{seg_data['icon']} {seg_name} Segmentation"):
                    st.write(f"**Bases:** {', '.join(seg_data['bases'])}")
                    st.info(f"Example: {seg_data['example']}")

        with tab2:
            st.markdown("#### Targeting Strategies")
            st.markdown("""
            | Strategy | Description | Example |
            |----------|-------------|---------|
            | Undifferentiated | Same offer to all | Coca-Cola (classic) |
            | Differentiated | Different offers to segments | Toyota (Corolla, Camry, Lexus) |
            | Concentrated | Focus on one segment | Rolex (luxury segment) |
            | Micromarketing | Individual customization | Nike ID (custom shoes) |
            """)

        with tab3:
            st.markdown("#### Brand Positioning")
            st.markdown("A perceptual map shows how consumers view brands:")

            st.markdown("""
            ```
                        HIGH QUALITY
                             |
                    Rolex    |    Tag Heuer
                             |
            HIGH PRICE ------+------ LOW PRICE
                             |
                    Fossil   |    Casio
                             |
                        LOW QUALITY
            ```
            """)

    elif viz_type == "Customer Retention":
        st.markdown("### 📊 Customer Retention & Churn Rate")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Retention Rate Formula")
            st.latex(r"Retention\,Rate = \frac{(CE - CN)}{CS} \times 100")
            st.markdown("""
            Where:
            - **CE** = Customers at End
            - **CN** = New Customers acquired
            - **CS** = Customers at Start
            """)

        with col2:
            st.markdown("#### Churn Rate Formula")
            st.latex(r"Churn\,Rate = \frac{Lost\,Customers}{Total\,Customers\,at\,Start} \times 100")
            st.info("Churn Rate = 100% - Retention Rate")

        st.markdown("---")
        st.markdown("### 🧮 Practice Calculator")

        col1, col2, col3 = st.columns(3)
        with col1:
            cs = st.number_input("Customers at Start (CS)", min_value=1, value=1000)
        with col2:
            cn = st.number_input("New Customers (CN)", min_value=0, value=200)
        with col3:
            ce = st.number_input("Customers at End (CE)", min_value=0, value=900)

        if st.button("Calculate Rates"):
            retention = ((ce - cn) / cs) * 100
            churn = 100 - retention

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Retention Rate", f"{retention:.1f}%")
            with col2:
                st.metric("Churn Rate", f"{churn:.1f}%")

def show_quiz():
    st.markdown("## 📝 Quiz Zone")

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    if st.button("🔄 Start New Quiz"):
        st.session_state.current_question = 0
        st.session_state.quiz_answers = {}
        st.session_state.show_results = False
        st.rerun()

    if not st.session_state.show_results:
        q_idx = st.session_state.current_question

        if q_idx < len(QUIZ_QUESTIONS):
            question = QUIZ_QUESTIONS[q_idx]

            st.progress((q_idx + 1) / len(QUIZ_QUESTIONS))
            st.markdown(f"**Question {q_idx + 1} of {len(QUIZ_QUESTIONS)}**")

            st.markdown(f"### {question['question']}")

            answer = st.radio(
                "Select your answer:",
                question['options'],
                key=f"q_{q_idx}"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Submit Answer"):
                    selected_idx = question['options'].index(answer)
                    is_correct = selected_idx == question['correct']

                    st.session_state.quiz_answers[q_idx] = {
                        'selected': selected_idx,
                        'correct': question['correct'],
                        'is_correct': is_correct
                    }

                    st.session_state.quizzes_attempted += 1
                    if is_correct:
                        st.session_state.quiz_score += 1

                    if is_correct:
                        st.markdown('<div class="quiz-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="quiz-incorrect">❌ Incorrect. The correct answer is: {question["options"][question["correct"]]}</div>', unsafe_allow_html=True)

                    st.info(f"💡 {question['explanation']}")

            with col2:
                if q_idx in st.session_state.quiz_answers:
                    if q_idx < len(QUIZ_QUESTIONS) - 1:
                        if st.button("Next Question →"):
                            st.session_state.current_question += 1
                            st.rerun()
                    else:
                        if st.button("See Results 📊"):
                            st.session_state.show_results = True
                            st.rerun()

    else:
        # Show results
        st.markdown("### 🎉 Quiz Complete!")

        correct_count = sum(1 for a in st.session_state.quiz_answers.values() if a['is_correct'])
        total = len(st.session_state.quiz_answers)
        percentage = (correct_count / total) * 100

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", f"{correct_count}/{total}")
        with col2:
            st.metric("Percentage", f"{percentage:.0f}%")
        with col3:
            if percentage >= 80:
                st.success("🌟 Excellent!")
            elif percentage >= 60:
                st.info("👍 Good job!")
            else:
                st.warning("📚 Keep studying!")

def show_flashcards():
    st.markdown("## 🎴 Flashcards")
    st.markdown("*Click 'Flip' to reveal the definition*")

    if 'current_card' not in st.session_state:
        st.session_state.current_card = 0
    if 'card_flipped' not in st.session_state:
        st.session_state.card_flipped = False

    card = FLASHCARDS[st.session_state.current_card]

    st.progress((st.session_state.current_card + 1) / len(FLASHCARDS))
    st.write(f"Card {st.session_state.current_card + 1} of {len(FLASHCARDS)}")

    # Display card
    if not st.session_state.card_flipped:
        st.markdown(f"""
        <div class="flashcard">
            <h2>{card['term']}</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="flashcard" style="background: linear-gradient(135deg, #10B981 0%, #059669 100%);">
            <div>
                <h3>{card['term']}</h3>
                <p>{card['definition']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.flashcards_viewed.add(st.session_state.current_card)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.current_card = (st.session_state.current_card - 1) % len(FLASHCARDS)
            st.session_state.card_flipped = False
            st.rerun()

    with col2:
        if st.button("🔄 Flip Card"):
            st.session_state.card_flipped = not st.session_state.card_flipped
            st.rerun()

    with col3:
        if st.button("Next ➡️"):
            st.session_state.current_card = (st.session_state.current_card + 1) % len(FLASHCARDS)
            st.session_state.card_flipped = False
            st.rerun()

    if st.button("🎲 Random Card"):
        st.session_state.current_card = random.randint(0, len(FLASHCARDS) - 1)
        st.session_state.card_flipped = False
        st.rerun()

def show_case_studies():
    st.markdown("## 📖 Case Studies")
    st.markdown("*Real-world applications of consumer behaviour concepts*")

    for i, case in enumerate(CASE_STUDIES):
        with st.expander(f"📌 Case {i+1}: {case['title']}"):
            st.markdown("#### Scenario")
            st.markdown(case['scenario'])

            st.markdown("---")
            st.markdown("#### Analysis Questions")

            for j, q in enumerate(case['questions']):
                st.markdown(f"**Q{j+1}: {q['q']}**")

                answer = st.radio(
                    f"Select answer:",
                    q['options'],
                    key=f"case_{i}_q_{j}"
                )

                if st.button(f"Check Answer", key=f"check_{i}_{j}"):
                    selected_idx = q['options'].index(answer)
                    if selected_idx == q['correct']:
                        st.success(f"✅ Correct! {q['explanation']}")
                    else:
                        st.error(f"❌ The correct answer is: {q['options'][q['correct']]}")
                        st.info(q['explanation'])

                st.markdown("---")

def show_brand_analysis():
    st.markdown("## 🔬 Brand Analysis Tool")
    st.markdown("*Analyze any brand using consumer behaviour frameworks*")

    brand_name = st.text_input("Enter a brand name to analyze:", placeholder="e.g., Nike, Apple, Zomato")

    if brand_name:
        st.markdown(f"### Analyzing: {brand_name}")

        tab1, tab2, tab3 = st.tabs(["Segmentation Analysis", "Buying Behaviour", "Positioning"])

        with tab1:
            st.markdown("#### How does this brand segment its market?")

            col1, col2 = st.columns(2)

            with col1:
                geo = st.multiselect("Geographic factors:", ["Global", "National", "Regional", "Urban", "Rural"])
                demo = st.multiselect("Demographic targets:", ["Youth (18-25)", "Adults (26-45)", "Seniors (45+)", "Families", "Singles"])

            with col2:
                psycho = st.multiselect("Psychographic appeals:", ["Aspirational", "Value-conscious", "Health-focused", "Trendy", "Traditional"])
                behav = st.multiselect("Behavioural focus:", ["Heavy users", "First-time buyers", "Brand loyalists", "Switchers"])

            if st.button("Generate Segmentation Summary"):
                st.success(f"""
                **{brand_name} Segmentation Profile:**
                - **Geographic:** {', '.join(geo) if geo else 'Not specified'}
                - **Demographic:** {', '.join(demo) if demo else 'Not specified'}
                - **Psychographic:** {', '.join(psycho) if psycho else 'Not specified'}
                - **Behavioural:** {', '.join(behav) if behav else 'Not specified'}
                """)

        with tab2:
            st.markdown("#### What type of buying behaviour applies?")

            involvement = st.slider("Customer Involvement Level", 1, 10, 5)
            brand_diff = st.slider("Brand Differentiation", 1, 10, 5)

            if involvement > 5 and brand_diff > 5:
                behaviour = "Complex Buying Behaviour"
                color = "#EF4444"
            elif involvement > 5 and brand_diff <= 5:
                behaviour = "Dissonance-Reducing Behaviour"
                color = "#F59E0B"
            elif involvement <= 5 and brand_diff > 5:
                behaviour = "Variety-Seeking Behaviour"
                color = "#10B981"
            else:
                behaviour = "Habitual Buying Behaviour"
                color = "#3B82F6"

            st.markdown(f"""
            <div style="background: {color}20; padding: 1.5rem; border-radius: 10px; border-left: 5px solid {color};">
                <h3 style="color: {color};">{behaviour}</h3>
                <p>Based on {'high' if involvement > 5 else 'low'} involvement and {'significant' if brand_diff > 5 else 'few'} brand differences.</p>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("#### Brand Positioning")

            col1, col2 = st.columns(2)

            with col1:
                price_pos = st.select_slider(
                    "Price Positioning",
                    options=["Budget", "Value", "Mid-range", "Premium", "Luxury"]
                )

            with col2:
                quality_pos = st.select_slider(
                    "Quality Positioning",
                    options=["Basic", "Standard", "Good", "Superior", "Excellence"]
                )

            differentiators = st.text_area("Key brand differentiators:", placeholder="What makes this brand unique?")

            if st.button("Create Positioning Statement"):
                st.info(f"""
                **{brand_name} Positioning Statement:**

                For customers seeking {quality_pos.lower()} quality at {price_pos.lower()} price points,
                {brand_name} is the brand that {differentiators if differentiators else 'delivers exceptional value'}.
                """)

if __name__ == "__main__":
    main()
