import streamlit as st
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="AI Crisis Bot", page_icon="🔥")

# --- GIAO DIỆN SIDEBAR (THANH BÊN) ---
with st.sidebar:
    st.header("⚙️ Cài đặt giả lập")
    crisis_type = st.selectbox(
        "Chọn loại khủng hoảng:",
        ["Chất lượng sản phẩm", "Thái độ nhân viên", "Phốt truyền thông"]
    )
    anger_level = st.slider("Mức độ giận dữ của khách:", 1, 10, 7)
    if st.button("Làm mới cuộc hội thoại"):
        st.session_state.messages = []
        st.rerun()

# --- TIÊU ĐỀ CHÍNH ---
st.title("🔥 AI Crisis Simulation Bot")
st.markdown(f"**Tình huống:** {crisis_type} | **Độ khó:** Cấp độ {anger_level}")
st.info("Nhiệm vụ: Hãy dùng kỹ năng PR để xoa dịu khách hàng đang giận dữ.")

# --- KHỞI TẠO TIN NHẮN ĐẦU TIÊN ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    first_msg = {
        "role": "assistant", 
        "content": f"TÔI KHÔNG THỂ CHẤP NHẬN ĐƯỢC! Tại sao bên các người làm ăn tắc trách về {crisis_type.lower()} như vậy hả??? Trả lời mau!"
    }
    st.session_state.messages.append(first_msg)

# --- HIỂN THỊ LỊCH SỬ CHAT ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- XỬ LÝ PHẢN HỒI ---
if prompt := st.chat_input("Nhập phản hồi của bạn..."):
    # 1. Hiển thị tin nhắn của người dùng
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Logic giả lập phản hồi của AI (Khách hàng)
    # Trong thực tế, bạn sẽ kết nối API OpenAI/Gemini tại đây.
    # Dưới đây là phản hồi giả lập để bạn test giao diện:
    responses = [
        "Đừng có xin lỗi suông! Tôi sẽ đăng chuyện này lên hội bóc phốt!",
        "Giải quyết thế mà coi được à? Tôi muốn gặp quản lý ngay lập tức!",
        "Bên bạn định coi thường khách hàng đến bao giờ nữa?",
        "Tôi đã chụp màn hình lại hết rồi, đừng hòng chối cãi!"
    ]
    ai_reply = random.choice(responses)

    # 3. Hiển thị tin nhắn của AI
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# --- ĐÁNH GIÁ (FOOTER) ---
st.divider()
st.progress(anger_level * 10, text=f"Chỉ số khủng hoảng hiện tại: {anger_level}/10")