import streamlit as st
import random

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Ai Là Triệu Phú",
    page_icon="💰",
    layout="wide"
)

# Tùy chỉnh giao diện CSS cho giống game show
st.markdown("""
    <style>
    .main {
        background-color: #0b112c;
        color: white;
    }
    .question-box {
        background-color: #1a237e;
        border: 2px solid #ffd700;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: white;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #ffd700;
        background-color: #0d47a1;
        color: white;
        font-size: 18px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: #1565c0;
        color: #ffd700;
        border-color: #ffffff;
    }
    .money-tree {
        background-color: #121838;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #303f9f;
    }
    </style>
""", unsafe_allow_html=True)

# Danh sách 15 câu hỏi và các mức tiền
MONEY_LEVELS = [
    "200.000 VNĐ", "400.000 VNĐ", "600.000 VNĐ", "1.000.000 VNĐ", "2.000.000 VNĐ",
    "3.000.000 VNĐ", "6.000.000 VNĐ", "10.000.000 VNĐ", "14.000.000 VNĐ", "22.000.000 VNĐ",
    "30.000.000 VNĐ", "40.000.000 VNĐ", "60.000.000 VNĐ", "85.000.000 VNĐ", "150.000.000 VNĐ"
]

QUESTIONS = [
    {
        "question": "Tháp Eiffel nằm ở thành phố nào?",
        "options": ["A: Paris", "B: Tuscany", "C: London", "D: New York City"],
        "answer": 0
    },
    {
        "question": "Thủ đô của Việt Nam là gì?",
        "options": ["A: Đà Nẵng", "B: Hà Nội", "C: TP. Hồ Chí Minh", "D: Cần Thơ"],
        "answer": 1
    },
    {
        "question": "Hành tinh nào gần Mặt Trời nhất?",
        "options": ["A: Trái Đất", "B: Sao Hỏa", "C: Sao Thủy", "D: Sao Kim"],
        "answer": 2
    },
    {
        "question": "Đơn vị tiền tệ của Nhật Bản là gì?",
        "options": ["A: Won", "B: Nhân dân tệ", "C: USD", "D: Yên"],
        "answer": 3
    },
    {
        "question": "Dòng sông nào dài nhất thế giới?",
        "options": ["A: Sông Mê Kông", "B: Sông Nile", "C: Sông Amazon", "D: Sông Hồng"],
        "answer": 1
    }
]

# Khởi tạo state
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.help_5050 = True
    st.session_state.help_audience = True
    st.session_state.help_call = True
    st.session_state.disabled_options = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.message = ""

def reset_game():
    st.session_state.current_q = 0
    st.session_state.help_5050 = True
    st.session_state.help_audience = True
    st.session_state.help_call = True
    st.session_state.disabled_options = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.message = ""

# Tiêu đề game
st.title("🏆 AI LÀ TRIỆU PHÚ")
st.write("---")

col_main, col_sidebar = st.columns([3, 1])

with col_sidebar:
    st.subheader("🛠 Quyền trợ giúp")
    c1, c2, c3 = st.columns(3)
    
    # Trợ giúp 50:50
    if c1.button("50:50", disabled=not st.session_state.help_5050 or st.session_state.game_over):
        st.session_state.help_5050 = False
        correct_idx = QUESTIONS[st.session_state.current_q]["answer"]
        wrong_indices = [i for i in range(4) if i != correct_idx]
        st.session_state.disabled_options = random.sample(wrong_indices, 2)
        st.rerun()

    # Trợ giúp Hỏi khán giả
    if c2.button("👥 Khán giả", disabled=not st.session_state.help_audience or st.session_state.game_over):
        st.session_state.help_audience = False
        correct_idx = QUESTIONS[st.session_state.current_q]["answer"]
        votes = [10, 10, 10, 10]
        votes[correct_idx] += 60
        st.session_state.message = f"📊 Khán giả bình chọn: A: {votes[0]}%, B: {votes[1]}%, C: {votes[2]}%, D: {votes[3]}%"
        st.rerun()

    # Trợ giúp Gọi điện
    if c3.button("📞 Gọi điện", disabled=not st.session_state.help_call or st.session_state.game_over):
        st.session_state.help_call = False
        correct_ans = QUESTIONS[st.session_state.current_q]["options"][QUESTIONS[st.session_state.current_q]["answer"]]
        st.session_state.message = f"📞 Chuyên gia tư vấn: 'Tôi nghĩ đáp án đúng là **{correct_ans}**!'"
        st.rerun()

    st.write("---")
    st.subheader("💰 Mức tiền thưởng")
    
    # Hiển thị cây tiền thưởng
    for i in range(len(QUESTIONS) - 1, -1, -1):
        color = "🟢" if i == st.session_state.current_q else "⚪"
        if (i + 1) % 5 == 0:
            st.markdown(f"**{color} Câu {i+1}: {MONEY_LEVELS[i]}** *(Mốc quan trọng)*")
        else:
            st.markdown(f"{color} Câu {i+1}: {MONEY_LEVELS[i]}")

with col_main:
    if st.session_state.game_over:
        if st.session_state.won:
            st.balloons()
            st.success(f"🎉 CHÚC MỪNG! Bạn đã trở thành TRIỆU PHÚ với tiền thưởng {MONEY_LEVELS[-1]}!")
        else:
            st.error("❌ Bạn đã trả lời sai hoặc dừng cuộc chơi!")
            if st.session_state.current_q > 0:
                st.info(f"💰 Số tiền bạn nhận được là: **{MONEY_LEVELS[st.session_state.current_q - 1]}**")
            else:
                st.info("💰 Số tiền bạn nhận được là: **0 VNĐ**")
        
        if st.button("Chơi lại"):
            reset_game()
            st.rerun()
            
    else:
        q_data = QUESTIONS[st.session_state.current_q]
        
        # Hiển thị câu hỏi
        st.markdown(f"<div class='question-box'>Câu {st.session_state.current_q + 1}: {q_data['question']}</div>", unsafe_allow_html=True)
        
        # Thông báo trợ giúp (nếu có)
        if st.session_state.message:
            st.info(st.session_state.message)
        
        # Hiển thị 4 đáp án dạng 2x2
        col1, col2 = st.columns(2)
        
        for idx, option in enumerate(q_data["options"]):
            target_col = col1 if idx % 2 == 0 else col2
            
            # Vô hiệu hóa đáp án bị loại bởi 50:50
            if idx in st.session_state.disabled_options:
                target_col.button(f"🚫 {option}", key=f"btn_{idx}", disabled=True)
            else:
                if target_col.button(option, key=f"btn_{idx}"):
                    if idx == q_data["answer"]:
                        st.session_state.message = ""
                        st.session_state.disabled_options = []
                        if st.session_state.current_q + 1 < len(QUESTIONS):
                            st.session_state.current_q += 1
                            st.success("Chính xác! Cùng đến với câu hỏi tiếp theo.")
                            st.rerun()
                        else:
                            st.session_state.won = True
                            st.session_state.game_over = True
                            st.rerun()
                    else:
                        st.session_state.game_over = True
                        st.rerun()

        st.write("---")
        if st.button("🛑 Dừng cuộc chơi (Bảo toàn tiền thưởng)"):
            st.session_state.game_over = True
            st.rerun()
