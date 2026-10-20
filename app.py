import streamlit as st
import random

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Ai Là Triệu Phú - Chủ Đề Bác Hồ",
    page_icon="🇻🇳",
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

# Danh sách 15 mức tiền thưởng
MONEY_LEVELS = [
    "200.000 VNĐ", "400.000 VNĐ", "600.000 VNĐ", "1.000.000 VNĐ", "2.000.000 VNĐ",
    "3.000.000 VNĐ", "6.000.000 VNĐ", "10.000.000 VNĐ", "14.000.000 VNĐ", "22.000.000 VNĐ",
    "30.000.000 VNĐ", "40.000.000 VNĐ", "60.000.000 VNĐ", "85.000.000 VNĐ", "150.000.000 VNĐ"
]

# Bộ 15 câu hỏi về Chủ tịch Hồ Chí Minh
QUESTIONS = [
    {
        "question": "Chủ tịch Hồ Chí Minh sinh vào ngày tháng năm nào?",
        "options": ["A: 19/05/1890", "B: 19/05/1880", "C: 02/09/1945", "D: 05/06/1911"],
        "answer": 0
    },
    {
        "question": "Quê hương của Bác Hồ thuộc tỉnh nào ngày nay?",
        "options": ["A: Hà Tĩnh", "B: Nghệ An", "C: Thanh Hóa", "D: Quảng Bình"],
        "answer": 1
    },
    {
        "question": "Bác Hồ ra đi tìm đường cứu nước vào năm nào?",
        "options": ["A: 1905", "B: 1919", "C: 1911", "D: 1930"],
        "answer": 2
    },
    {
        "question": "Bác Hồ ra đi tìm đường cứu nước từ con tàu mang tên gì?",
        "options": ["A: L'Amiral Latouche-Tréville", "B: Titanic", "C: Hải Âu", "D: Bình Thuận"],
        "answer": 0
    },
    {
        "question": "Tên khai sinh của Bác Hồ là gì?",
        "options": ["A: Nguyễn Tất Thành", "B: Nguyễn Ái Quốc", "C: Nguyễn Sinh Cung", "D: Văn Ba"],
        "answer": 2
    },
    {
        "question": "Bác Hồ đọc bản Tuyên ngôn Độc lập tại đâu?",
        "options": ["A: Bến Nhà Rồng", "B: Quảng trường Ba Đình", "C: Hang Pắc Bó", "D: Tân Trào"],
        "answer": 1
    },
    {
        "question": "Tập thơ nổi tiếng nào được Bác Hồ sáng tác trong thời gian bị giam giữ tại Trung Quốc?",
        "options": ["A: Nhật ký trong tù", "B: Viếng Lăng Bác", "C: Từ ấy", "D: Bác ơi"],
        "answer": 0
    },
    {
        "question": "Bác Hồ trở về nước trực tiếp lãnh đạo cách mạng Việt Nam vào năm nào?",
        "options": ["A: 1930", "B: 1941", "C: 1945", "D: 1954"],
        "answer": 1
    },
    {
        "question": "Tên gọi của Bác Hồ khi làm phụ bếp trên con tàu xin việc ra đi tìm đường cứu nước là gì?",
        "options": ["A: Anh Ba", "B: Văn Ba", "C: Tín Phong", "D: Thấu Chính"],
        "answer": 1
    },
    {
        "question": "Bản 'Yêu cầu của nhân dân An Nam' gửi đến Hội nghị Versailles năm 1919 do ai đứng tên?",
        "options": ["A: Nguyễn Sinh Cung", "B: Nguyễn Ái Quốc", "C: Hồ Chí Minh", "D: Lý Thụy"],
        "answer": 1
    },
    {
        "question": "Cột mốc biên giới số mấy là nơi Bác Hồ lần đầu tiên đặt chân về lại Tổ quốc sau 30 năm xa cách?",
        "options": ["A: Cột mốc 108", "B: Cột mốc 0", "C: Cột mốc 79", "D: Cột mốc 111"],
        "answer": 0
    },
    {
        "question": "Bác Hồ đã chủ trì Hội nghị thành lập Đảng Cộng sản Việt Nam vào đầu năm 1930 tại đâu?",
        "options": ["A: Hương Cảng (Hồng Kông)", "B: Quảng Châu (Trung Quốc)", "C: Paris (Pháp)", "D: Cao Bằng"],
        "answer": 0
    },
    {
        "question": "Tờ báo do Nguyễn Ái Quốc sáng lập năm 1922 tại Pháp nhằm đấu tranh cho các dân tộc bị áp bức có tên là gì?",
        "options": ["A: Thanh Niên", "B: Người Cùng Khổ (Le Paria)", "C: Cứu Quốc", "D: Nhân Dân"],
        "answer": 1
    },
    {
        "question": "Tác phẩm lý luận cách mạng quan trọng nào của Bác Hồ xuất bản năm 1927 tập hợp các bài giảng tại Quảng Châu?",
        "options": ["A: Bản án chế độ thực dân Pháp", "B: Đường Kách mệnh", "C: Cương lĩnh chính trị", "D: Lời kêu gọi toàn quốc kháng chiến"],
        "answer": 1
    },
    {
        "question": "Thành phố Sài Gòn - Gia Định chính thức được đổi tên thành Thành phố Hồ Chí Minh vào năm nào?",
        "options": ["A: 1975", "B: 1976", "C: 1980", "D: 1986"],
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
st.title("🏆 AI LÀ TRIỆU PHÚ - CHỦ ĐỀ CHỦ TỊCH HỒ CHÍ MINH")
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
        st.session_state.message
