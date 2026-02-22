import streamlit as st

# --- 1. CẤU HÌNH GIAO DIỆN CHUYÊN NGHIỆP ---
st.set_page_config(page_title="Crisis AI Agent", page_icon="🛡️", layout="centered")

# CSS để bo tròn khung chat và làm đẹp sidebar
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; border: 1px solid #f0f2f6; margin-bottom: 10px; }
    [data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THANH BÊN (SIDEBAR) TÙY CHỈNH ---
with st.sidebar:
    st.header("⚙️ Cài đặt giả lập")
    st.divider()
    tinh_huong = st.selectbox("🎯 Loại khủng hoảng:", ["Sản phẩm lỗi", "Thái độ nhân viên", "Tin đồn xấu"])
    muc_do = st.select_slider("🔥 Mức độ giận dữ:", options=["Thấp", "Trung bình", "Cao", "Cực đoan"])
    if st.button("🔄 Làm mới kịch bản"):
        st.session_state.messages = []
        st.rerun()

# --- 3. GIAO DIỆN CHÍNH ---
st.title("🛡️ Crisis Simulation Bot")
st.caption(f"Tình huống hiện tại: {tinh_huong} | Mức độ: {muc_do}")

# Khởi tạo tin nhắn đầu tiên nếu chưa có
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "TÔI CỰC KỲ THẤT VỌNG! Các người định giải quyết chuyện này thế nào đây???"}]

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Khung nhập phản hồi
if prompt := st.chat_input("Nhập cách xử lý khéo léo của bạn..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # AI phản hồi lại (giả lập khách hàng)
    rely = "Đừng có xin lỗi suông! Tôi muốn gặp quản lý ngay lập tức!"
    st.session_state.messages.append({"role": "assistant", "content": rely})
    with st.chat_message("assistant"):
        st.write(rely)