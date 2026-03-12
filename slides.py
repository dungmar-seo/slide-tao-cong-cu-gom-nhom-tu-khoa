import streamlit as st

# ============================================================
# CAU HINH TRANG
# ============================================================
st.set_page_config(
    page_title="AI Tool Building - Presentation",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS TOAN CUC
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Be Vietnam Pro', sans-serif; }

.main .block-container {
    padding: 1rem 2rem 2rem 2rem;
    max-width: 1100px;
}

/* Slide header */
.slide-cover {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem 2rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.35);
}
.slide-cover h1 {
    font-size: 2.6rem;
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    line-height: 1.3;
}
.slide-cover p {
    font-size: 1.2rem;
    opacity: 0.92;
    margin: 0;
}
.slide-cover .author {
    margin-top: 1.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    opacity: 0.95;
}

/* Slide title bar */
.slide-title {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem 1.5rem;
    border-radius: 14px;
    color: white;
    margin-bottom: 1.2rem;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.25);
}
.slide-title h2 {
    margin: 0;
    font-size: 1.5rem;
    font-weight: 700;
}
.slide-title .step-badge {
    display: inline-block;
    background: rgba(255,255,255,0.25);
    padding: 0.2rem 0.7rem;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.4rem;
}

/* Content card */
.content-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}

/* Highlight box */
.highlight-box {
    background: linear-gradient(135deg, #f0f4ff 0%, #faf0ff 100%);
    border-left: 4px solid #667eea;
    padding: 1rem 1.2rem;
    border-radius: 0 12px 12px 0;
    margin: 0.8rem 0;
    font-size: 1.05rem;
}

/* Question box */
.question-box {
    background: linear-gradient(135deg, #fff7ed 0%, #fffbeb 100%);
    border-left: 4px solid #f59e0b;
    padding: 1rem 1.2rem;
    border-radius: 0 12px 12px 0;
    margin: 0.8rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #92400e;
}

/* Problem box */
.problem-box {
    background: linear-gradient(135deg, #fef2f2 0%, #fff1f2 100%);
    border-left: 4px solid #ef4444;
    padding: 1rem 1.2rem;
    border-radius: 0 12px 12px 0;
    margin: 0.8rem 0;
}

/* Solution box */
.solution-box {
    background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
    border-left: 4px solid #10b981;
    padding: 1rem 1.2rem;
    border-radius: 0 12px 12px 0;
    margin: 0.8rem 0;
}

/* Prompt box */
.prompt-box {
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 1.2rem;
    border-radius: 12px;
    font-family: 'Courier New', monospace;
    font-size: 0.92rem;
    line-height: 1.6;
    margin: 0.8rem 0;
    border: 1px solid #313244;
}
.prompt-box .label {
    color: #89b4fa;
    font-weight: 700;
}

/* Flow step */
.flow-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin: 1rem 0;
}
.flow-step {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.6rem 1rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.9rem;
    text-align: center;
    min-width: 120px;
}
.flow-arrow {
    font-size: 1.5rem;
    color: #667eea;
    font-weight: 700;
}

/* Metric card */
.metric-row {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
}
.metric-card {
    flex: 1;
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
}
.metric-card .icon { font-size: 2rem; }
.metric-card .value {
    font-size: 1.6rem;
    font-weight: 800;
    color: #667eea;
    margin: 0.3rem 0;
}
.metric-card .label {
    font-size: 0.85rem;
    color: #64748b;
}

/* Nav buttons */
.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 2px solid #e2e8f0;
}
.slide-counter {
    font-size: 1rem;
    font-weight: 600;
    color: #64748b;
}

/* Table styling */
.styled-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 12px;
    overflow: hidden;
    margin: 0.8rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.styled-table th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.8rem 1rem;
    font-weight: 600;
    font-size: 0.9rem;
    text-align: left;
}
.styled-table td {
    padding: 0.7rem 1rem;
    border-bottom: 1px solid #e2e8f0;
    font-size: 0.9rem;
}
.styled-table tr:nth-child(even) td {
    background: #f8fafc;
}
.styled-table tr:last-child td {
    border-bottom: none;
}

/* Cycle diagram */
.cycle-box {
    background: white;
    border: 2px solid #667eea;
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    margin: 0.8rem 0;
}
.cycle-box .cycle-step {
    display: inline-block;
    background: #f0f4ff;
    border: 2px solid #667eea;
    border-radius: 10px;
    padding: 0.5rem 0.8rem;
    margin: 0.3rem;
    font-weight: 600;
    font-size: 0.85rem;
    color: #4338ca;
}
.cycle-box .cycle-arrow {
    display: inline-block;
    font-size: 1.2rem;
    color: #667eea;
    margin: 0 0.2rem;
}

/* Key message */
.key-message {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 14px;
    text-align: center;
    font-size: 1.15rem;
    font-weight: 600;
    margin: 1rem 0;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

/* Hide streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================
TOTAL_SLIDES = 16

if "current_slide" not in st.session_state:
    st.session_state.current_slide = 1


def go_next():
    if st.session_state.current_slide < TOTAL_SLIDES:
        st.session_state.current_slide += 1


def go_prev():
    if st.session_state.current_slide > 1:
        st.session_state.current_slide -= 1


def go_to(n):
    st.session_state.current_slide = n


# ============================================================
# NAVIGATION
# ============================================================
def render_nav():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.button(
            "⬅️ Trước",
            on_click=go_prev,
            use_container_width=True,
            disabled=(st.session_state.current_slide == 1)
        )
    with c2:
        st.markdown(
            '<div style="text-align:center;padding:0.5rem 0;'
            'font-weight:600;color:#64748b;">'
            'Slide ' + str(st.session_state.current_slide)
            + ' / ' + str(TOTAL_SLIDES)
            + '</div>',
            unsafe_allow_html=True
        )
    with c3:
        st.button(
            "Tiếp ➡️",
            on_click=go_next,
            use_container_width=True,
            disabled=(
                st.session_state.current_slide == TOTAL_SLIDES
            )
        )


# ============================================================
# SIDEBAR: Quick nav
# ============================================================
with st.sidebar:
    st.markdown("## 📑 Danh sách Slide")
    slide_names = [
        "1. Trang bìa",
        "2. Mục lục",
        "3. Bước 1 - Tư duy",
        "4. Công thức Prompt",
        "5. Bước 2 - Phân tích",
        "6. Đào sâu với AI",
        "7. Bước 3 - Mở đầu",
        "8. Hỏi AI & Nhận gợi ý",
        "9. Vòng lặp xây dựng",
        "10. Cải tiến lần 1",
        "11. Cải tiến lần 2",
        "12. Nâng cấp thành App",
        "13. Demo công cụ",
        "14. Tư duy mở rộng",
        "15. Tổng kết 3 bước",
        "16. Kết thúc"
    ]
    for i, name in enumerate(slide_names):
        is_current = (i + 1 == st.session_state.current_slide)
        label = ("👉 " if is_current else "") + name
        if st.button(
            label,
            key="nav_" + str(i),
            use_container_width=True
        ):
            go_to(i + 1)


# ============================================================
# SLIDE 1: TRANG BIA
# ============================================================
def slide_1():
    st.markdown(
        '<div class="slide-cover">'
        '<h1>🎯 Cách tạo công cụ AI<br>'
        'để tự động hóa công việc</h1>'
        '<p>Từ ý tưởng đến sản phẩm '
        '- Ai cũng làm được!</p>'
        '<div class="author">'
        '👤 Tống Công Dũng</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '💡 Bạn không cần biết lập trình. '
        'Bạn chỉ cần biết ĐẶT CÂU HỎI ĐÚNG '
        'và MÔ TẢ VẤN ĐỀ RÕ RÀNG cho AI.'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 2: MUC LUC
# ============================================================
def slide_2():
    st.markdown(
        '<div class="slide-title">'
        '<h2>📌 Mục lục nội dung</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<table class="styled-table">'
        '<tr><th>STT</th><th>Nội dung</th>'
        '<th>Mô tả</th></tr>'
        '<tr><td><b>1</b></td>'
        '<td>🧠 <b>Bước 1 - Tư duy</b></td>'
        '<td>Đặt câu hỏi đúng cho AI</td></tr>'
        '<tr><td><b>2</b></td>'
        '<td>🔍 <b>Bước 2 - Phân tích</b></td>'
        '<td>Đánh giá gợi ý và chọn hướng đi</td></tr>'
        '<tr><td><b>3</b></td>'
        '<td>🚀 <b>Bước 3 - Thực chiến</b></td>'
        '<td>Ví dụ: Công cụ Gom nhóm từ khóa SEO</td></tr>'
        '<tr><td><b>4</b></td>'
        '<td>💡 <b>Tổng kết</b></td>'
        '<td>Ứng dụng mở rộng & Kết luận</td></tr>'
        '</table>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 3: BUOC 1 - TU DUY
# ============================================================
def slide_3():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 1</div>'
        '<h2>🧠 Tư duy: '
        '"Việc này có thể tự động hóa không?"</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<p style="font-size:1.05rem;">'
        'Mỗi khi gặp một công việc '
        '<b>lặp đi lặp lại</b>, '
        '<b>tốn nhiều thời gian</b>, '
        'hoặc <b>dễ sai sót</b> '
        '→ Hãy tự hỏi:</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="question-box">'
        '❓ "Mình có thể nhờ AI tự động hóa '
        'việc này để sau mình nhàn hơn không?"'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="solution-box">'
        '✅ Nếu câu trả lời là <b>CÓ THỂ</b> '
        '→ Bắt đầu hỏi AI bằng <b>Gemini</b>!'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="highlight-box">'
        '🔑 <b>Công cụ sử dụng:</b> '
        'Google Gemini (miễn phí, mạnh mẽ, '
        'hiểu tiếng Việt tốt)'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 4: CONG THUC PROMPT
# ============================================================
def slide_4():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 1</div>'
        '<h2>💬 Công thức viết Prompt '
        'cho AI hiệu quả</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h3 style="text-align:center;color:#4338ca;">'
        '📐 Công thức 3 phần</h3>'
        '<div class="flow-container">'
        '<div class="flow-step">'
        '🔹 BỐI CẢNH<br>'
        '<small>Mình đang làm gì?</small></div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step">'
        '🔹 NHU CẦU<br>'
        '<small>Cần AI giúp gì?</small></div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step">'
        '🔹 KẾT QUẢ<br>'
        '<small>Output mong muốn?</small></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="prompt-box">'
        '<span class="label">🔹 Bối cảnh:</span> '
        '"Tôi là SEO Content, hàng tuần phải gom '
        'hàng nghìn từ khóa từ Ahrefs thành '
        'các bài viết"<br><br>'
        '<span class="label">🔹 Nhu cầu:</span> '
        '"Tôi muốn tạo một công cụ tự động gom nhóm '
        'từ khóa theo ngữ nghĩa"<br><br>'
        '<span class="label">🔹 Kết quả:</span> '
        '"Output là file Excel với các nhóm bài viết, '
        'mỗi nhóm có keyword chính và keyword phụ"'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 5: BUOC 2 - PHAN TICH
# ============================================================
def slide_5():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 2</div>'
        '<h2>🔍 Phân tích: '
        'Đánh giá gợi ý từ AI</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="problem-box">'
        '⚠️ Khi AI đưa ra các gợi ý triển khai '
        '→ <b>Không vội làm ngay!</b>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h3>🎯 3 tiêu chí đánh giá</h3>'
        '<table class="styled-table">'
        '<tr><th>Tiêu chí</th>'
        '<th>Câu hỏi cần trả lời</th></tr>'
        '<tr><td>✅ <b>Khả thi</b></td>'
        '<td>Mình có thể tự làm được không? '
        '(không cần biết code chuyên sâu)</td></tr>'
        '<tr><td>✅ <b>Hiệu quả</b></td>'
        '<td>Giải pháp có thực sự giải quyết '
        'đúng vấn đề không?</td></tr>'
        '<tr><td>✅ <b>Đơn giản</b></td>'
        '<td>Có cách nào đơn giản hơn không?</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="flow-container">'
        '<div class="flow-step">'
        'AI đưa gợi ý</div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step">'
        'Cân nhắc ưu/nhược</div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step">'
        'Chọn cách phù hợp</div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step">'
        'Đào sâu chi tiết</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 6: DAO SAU VOI AI
# ============================================================
def slide_6():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 2</div>'
        '<h2>🔎 Sau khi chọn hướng đi '
        '- Đào sâu chi tiết</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h3>📋 Nguyên tắc làm việc với AI</h3>'
        '<div class="highlight-box">'
        '🔄 <b>Làm theo</b> → <b>Gặp lỗi</b> '
        '→ <b>Báo lại cho AI</b> → <b>AI sửa</b> '
        '→ <b>Tiếp tục</b>'
        '</div>'
        '<div class="highlight-box">'
        '📋 <b>Copy lỗi chính xác</b> gửi cho AI '
        'để AI hiểu đúng vấn đề'
        '</div>'
        '<div class="highlight-box">'
        '🎯 <b>Không cần hiểu hết code</b>, '
        'chỉ cần hiểu logic và biết cách '
        'mô tả vấn đề'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '💡 AI là trợ lý của bạn - '
        'Bạn chỉ cần biết MÔ TẢ VẤN ĐỀ, '
        'AI sẽ lo phần KỸ THUẬT!'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 7: BUOC 3 - MO DAU
# ============================================================
def slide_7():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - THỰC CHIẾN</div>'
        '<h2>🚀 Ví dụ: Công cụ Gom nhóm '
        'từ khóa SEO</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="problem-box">'
        '<h3>😩 Vấn đề thực tế</h3>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<table class="styled-table">'
        '<tr><th>Hạng mục</th><th>Chi tiết</th></tr>'
        '<tr><td>📋 <b>Công việc</b></td>'
        '<td>Gom ~1.000 từ khóa đầu vào '
        'thành các bài viết cụ thể</td></tr>'
        '<tr><td>⏰ <b>Thời gian thủ công</b></td>'
        '<td><b style="color:#ef4444;">'
        '1.5 - 2 ngày</b> làm việc liên tục</td></tr>'
        '<tr><td>🔄 <b>Tần suất</b></td>'
        '<td>Lặp đi lặp lại thường xuyên, '
        'liên tục</td></tr>'
        '<tr><td>😫 <b>Cảm giác</b></td>'
        '<td>Tốn thời gian, nhàm chán, '
        'dễ sai sót</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="question-box">'
        '💡 "Mình có thể tạo công cụ gom nhóm '
        'tự động được không?" → Quyết định: HỎI AI!'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 8: HOI AI VA NHAN GOI Y
# ============================================================
def slide_8():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - THỰC CHIẾN</div>'
        '<h2>💬 Hỏi Gemini và nhận gợi ý</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="prompt-box">'
        '<span class="label">🔹 Bối cảnh:</span> '
        'Tôi là SEO Content, thường xuyên phải gom '
        'hàng nghìn từ khóa từ file Ahrefs thành '
        'các nhóm bài viết.<br><br>'
        '<span class="label">🔹 Nhu cầu:</span> '
        'Tôi muốn tạo một công cụ tự động để gom '
        'nhóm từ khóa theo ngữ nghĩa, thay vì '
        'làm thủ công.<br><br>'
        '<span class="label">🔹 Kết quả:</span> '
        'Output là file Excel, mỗi nhóm có keyword '
        'chính và các keyword phụ liên quan.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="solution-box">'
        '🤖 <b>AI gợi ý:</b> Có thể sử dụng '
        '<b>Google Colab</b> + Python để xử lý tự động'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="highlight-box">'
        '✅ <b>Đánh giá:</b> Google Colab miễn phí, '
        'không cần cài đặt, chạy trên trình duyệt '
        '→ <b>Phù hợp!</b>'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SLIDE 9: VONG LAP XAY DUNG
# ============================================================
def slide_9():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - THỰC CHIẾN</div>'
        '<h2>🔧 Vòng lặp xây dựng công cụ</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<div class="cycle-box">'
        '<div class="cycle-step">'
        '📝 Yêu cầu AI viết code</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step">'
        '▶️ Chạy thử trên Colab</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step">'
        '❌ Có lỗi?</div>'
        '<br><br>'
        '<div class="cycle-step">'
        '📋 Gửi lỗi cho AI</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step">'
        '🔧 AI sửa code</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step">'
        '🔄 Quay lại chạy thử</div>'
        '<br><br>'
        '<div class="cycle-step" '
        'style="background:#ecfdf5;color:#065f46;'
        'border-color:#10b981;">'
        '✅ Không lỗi → Test kết quả</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step" '
        'style="background:#fff7ed;color:#92400e;'
        'border-color:#f59e0b;">'
        '🤔 Đã ổn chưa?</div>'
        '<div class="cycle-arrow">→</div>'
        '<div class="cycle-step" '
        'style="background:#fef2f2;color:#991b1b;'
        'border-color:#ef4444;">'
        '📢 Chưa → Nêu vấn đề cho AI cải tiến</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '🔑 Không cần biết code - Chỉ cần biết '
        'MÔ TẢ VẤN ĐỀ cho AI!'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 10: CAI TIEN LAN 1
# ============================================================
def slide_10():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - CẢI TIẾN</div>'
        '<h2>🔬 Cải tiến lần 1: '
        'Phát hiện từ khóa rác</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="problem-box">'
        '<h4>😤 Vấn đề phát hiện khi test:</h4>'
        '<p>File từ khóa từ Ahrefs chứa '
        '<b>rất nhiều từ khóa rác</b> do cơ chế '
        'đào từ khóa của nó.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h4>Ví dụ minh họa:</h4>'
        '<table class="styled-table">'
        '<tr><th>Tìm kiếm về</th>'
        '<th>Ahrefs trả về cả</th>'
        '<th>Lý do</th></tr>'
        '<tr><td><b>"hóa đơn"</b></td>'
        '<td>🌺 "hoa mẫu đơn"</td>'
        '<td>Trùng chữ "đơn"</td></tr>'
        '<tr><td><b>"kế toán"</b></td>'
        '<td>📐 "kế hoạch toán học"</td>'
        '<td>Trùng chữ "kế" và "toán"</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="solution-box">'
        '<h4>💡 Giải pháp:</h4>'
        '<p>Nghiên cứu và yêu cầu AI tạo thêm '
        '<b>công cụ lọc từ khóa rác</b> trước khi '
        'gom nhóm</p>'
        '<p>→ Ra đời <b>Công cụ 1: Lọc & Gom từ khóa</b> '
        '(dùng AI ngữ nghĩa để phân biệt từ khóa '
        'đúng ngành vs rác)</p>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 11: CAI TIEN LAN 2
# ============================================================
def slide_11():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - CẢI TIẾN</div>'
        '<h2>🔬 Cải tiến lần 2: '
        'Gom nhóm chưa đủ sát</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="problem-box">'
        '<h4>😤 Vấn đề tiếp theo:</h4>'
        '<p>Sau khi lọc rác, công cụ gom nhóm nhưng '
        '<b>phạm vi quá rộng</b> - các từ khóa trong '
        '1 nhóm chưa đủ sát nghĩa để viết thành '
        '1 bài.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="solution-box">'
        '<h4>💡 Giải pháp:</h4>'
        '<p>Xây dựng <b>Công cụ 2: Gom từ khóa '
        'thành bài viết</b> sử dụng '
        '<b>API Google AI Studio (Gemini)</b></p>'
        '<p>→ AI thông minh hơn, hiểu ngữ cảnh '
        'sâu hơn → Gom chính xác hơn</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h4>📊 Kết quả so sánh:</h4>'
        '<table class="styled-table">'
        '<tr><th>Hạng mục</th>'
        '<th>❌ Trước</th>'
        '<th>✅ Sau</th></tr>'
        '<tr><td><b>Thời gian</b></td>'
        '<td style="color:#ef4444;">'
        '1.5 - 2 ngày</td>'
        '<td style="color:#10b981;font-weight:700;">'
        'Vài phút ⚡</td></tr>'
        '<tr><td><b>Độ chính xác</b></td>'
        '<td>Phụ thuộc người làm</td>'
        '<td style="color:#10b981;font-weight:700;">'
        'AI + kiểm tra lại</td></tr>'
        '<tr><td><b>Khả năng lặp lại</b></td>'
        '<td>Mệt mỏi, nhàm chán</td>'
        '<td style="color:#10b981;font-weight:700;">'
        'Tự động, nhất quán</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 12: NANG CAP THANH APP
# ============================================================
def slide_12():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">BƯỚC 3 - NÂNG CẤP</div>'
        '<h2>🌐 Từ Google Colab → '
        'Ứng dụng web dễ dùng</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="problem-box">'
        '<h4>😤 Vấn đề với Google Colab:</h4>'
        '<ul>'
        '<li>Giao diện phức tạp, không trực quan</li>'
        '<li>Khó chia sẻ cho người khác sử dụng</li>'
        '<li>Phải biết chạy code thủ công</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="solution-box">'
        '<h4>💡 Giải pháp:</h4>'
        '<p>Tiếp tục hỏi AI cách biến code thành '
        '<b>ứng dụng web</b></p>'
        '<p>→ AI gợi ý: <b>GitHub</b> (lưu code) + '
        '<b>Streamlit</b> (tạo giao diện web)</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<div class="flow-container">'
        '<div class="flow-step" '
        'style="background:#ef4444;">'
        '😤 Google Colab<br>'
        '<small>(phức tạp)</small></div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step" '
        'style="background:#f59e0b;">'
        '🔧 GitHub + Streamlit<br>'
        '<small>(chuyển đổi)</small></div>'
        '<div class="flow-arrow">→</div>'
        '<div class="flow-step" '
        'style="background:#10b981;">'
        '✅ Ứng dụng Web<br>'
        '<small>(ai cũng dùng được)</small></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 13: DEMO CONG CU
# ============================================================
def slide_13():
    st.markdown(
        '<div class="slide-title">'
        '<div class="step-badge">KẾT QUẢ</div>'
        '<h2>🖥️ Demo: SEO Content Mapping Tool</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<h3 style="text-align:center;">'
        '🔍 SEO Content Mapping Tool</h3>'
        '<div class="metric-row">'
        '<div class="metric-card">'
        '<div class="icon">🧹</div>'
        '<div class="value">Công cụ 1</div>'
        '<div class="label">Upload CSV → Lọc rác '
        '→ Gom nhóm ngữ nghĩa → Xuất Excel</div>'
        '</div>'
        '<div class="metric-card">'
        '<div class="icon">🤖</div>'
        '<div class="value">Công cụ 2</div>'
        '<div class="label">Nhận file từ CỤ 1 '
        'hoặc upload mới → Gemini AI gom bài viết</div>'
        '</div>'
        '<div class="metric-card">'
        '<div class="icon">🔄</div>'
        '<div class="value">Pipeline</div>'
        '<div class="label">Chạy tự động cả 2 bước '
        'liên tiếp</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '✅ Giao diện đẹp, ai cũng dùng được, '
        'không cần biết code!'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 14: TU DUY MO RONG
# ============================================================
def slide_14():
    st.markdown(
        '<div class="slide-title">'
        '<h2>💡 Với cách tư duy này, '
        'bạn có thể tạo BẤT KỲ công cụ nào!</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<table class="styled-table">'
        '<tr><th>Công cụ</th>'
        '<th>Vấn đề giải quyết</th>'
        '<th>Độ khó</th></tr>'
        '<tr><td>🏷️ <b>Tạo mã Schema</b></td>'
        '<td>Tự động tạo structured data '
        'từ file thông tin</td>'
        '<td>⭐⭐</td></tr>'
        '<tr><td>🔤 <b>Chuyển tiếng Việt '
        'có dấu → không dấu</b></td>'
        '<td>Đặt tên file ảnh chuẩn SEO '
        'hàng loạt</td>'
        '<td>⭐</td></tr>'
        '<tr><td>✍️ <b>Tạo Prompt nhanh</b></td>'
        '<td>Sinh prompt tối ưu để tạo ảnh/'
        'viết bài AI</td>'
        '<td>⭐⭐</td></tr>'
        '<tr><td>📊 <b>Phân tích đối thủ</b></td>'
        '<td>Tự động so sánh content '
        'với đối thủ</td>'
        '<td>⭐⭐⭐</td></tr>'
        '<tr><td>📝 <b>Tạo outline bài viết</b></td>'
        '<td>Từ keyword → dàn bài chi tiết '
        'tự động</td>'
        '<td>⭐⭐</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '🔑 Vấn đề lặp lại + Tốn thời gian '
        '→ Hỏi AI → Xây công cụ → Tự động hóa'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 15: TONG KET
# ============================================================
def slide_15():
    st.markdown(
        '<div class="slide-title">'
        '<h2>📋 Tổng kết: 3 bước tạo công cụ AI</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="content-card">'
        '<table class="styled-table">'
        '<tr><th>Bước</th><th>Hành động</th>'
        '<th>Công cụ hỗ trợ</th></tr>'
        '<tr><td>🧠 <b>Bước 1</b></td>'
        '<td><b>Tư duy</b> - Nhận diện vấn đề '
        'có thể tự động hóa</td>'
        '<td>Gemini (Prompt 3 phần)</td></tr>'
        '<tr><td>🔍 <b>Bước 2</b></td>'
        '<td><b>Phân tích</b> - Đánh giá gợi ý, '
        'chọn hướng đi đúng</td>'
        '<td>Gemini + Tư duy phản biện</td></tr>'
        '<tr><td>🚀 <b>Bước 3</b></td>'
        '<td><b>Thực hiện</b> - Làm theo AI, test, '
        'cải tiến liên tục</td>'
        '<td>Google Colab → GitHub + Streamlit</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-message">'
        '🎯 Bạn không cần biết lập trình. '
        'Bạn chỉ cần biết ĐẶT CÂU HỎI ĐÚNG '
        'và MÔ TẢ VẤN ĐỀ RÕ RÀNG cho AI.'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SLIDE 16: KET THUC
# ============================================================
def slide_16():
    st.markdown(
        '<div class="slide-cover">'
        '<h1>🙏 Cảm ơn mọi người<br>'
        'đã lắng nghe!</h1>'
        '<p style="font-size:1.1rem;'
        'margin-top:1.5rem;font-style:italic;">'
        '"Hãy bắt đầu từ một vấn đề nhỏ '
        'trong công việc hàng ngày của bạn. '
        'Hỏi AI. Thử nghiệm. Cải tiến. '
        'Bạn sẽ ngạc nhiên với những gì '
        'mình có thể tạo ra!"</p>'
        '<div class="author" style="margin-top:2rem;">'
        '👤 Tống Công Dũng</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="text-align:center;'
        'margin-top:2rem;">'
        '<h2>🎤 Q&A - Hỏi đáp</h2>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# DIEU HUONG SLIDE
# ============================================================
slide = st.session_state.current_slide

if slide == 1:
    slide_1()
elif slide == 2:
    slide_2()
elif slide == 3:
    slide_3()
elif slide == 4:
    slide_4()
elif slide == 5:
    slide_5()
elif slide == 6:
    slide_6()
elif slide == 7:
    slide_7()
elif slide == 8:
    slide_8()
elif slide == 9:
    slide_9()
elif slide == 10:
    slide_10()
elif slide == 11:
    slide_11()
elif slide == 12:
    slide_12()
elif slide == 13:
    slide_13()
elif slide == 14:
    slide_14()
elif slide == 15:
    slide_15()
elif slide == 16:
    slide_16()

# Render navigation
st.markdown("---")
render_nav()

# === KET THUC FILE slides.py ===
