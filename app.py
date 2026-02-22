import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyAPr01OtkLHaNMXYc3nYRRbBuePtFE03OQ")

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
        st.write(prompt
     # --- ĐOẠN DÁN MỚI TẠI ĐÂY ---
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Tạo nội dung để AI hiểu kịch bản
    noi_dung = f"""
    Bạn là khách hàng đang rất tức giận vì {tinh_huong}. 
    Mức độ giận dữ: {muc_do}/10. 
    Hãy phản hồi ngắn gọn, cực kỳ khó tính câu này của nhân viên: {prompt}
    """
    
    # AI phản hồi
    response = model.generate_content(noi_dung)
    ai_reply = response.text
    
    # Hiển thị kết quả
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
      # 1. Gọi mô hình AI Gemini
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 2. Tạo nội dung hướng dẫn cho AI (Prompt)
    huong_dan = f"""
    Bạn là một khách hàng đang rất giận dữ về vấn đề: {crisis_type}.
    Mức độ giận dữ của bạn là {anger_level}/10.
    Hãy phản hồi câu chat của nhân viên một cách đanh đá, khó tính và ngắn gọn.
    """
    
    # 3. Lấy phản hồi từ AI
    response = model.generate_content(huong_dan + prompt)
    ai_reply = response.text

    # 4. Hiển thị lên màn hình
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
              