import streamlit as st


def slide_1():
    st.markdown(
        '<div class="cover-slide">'
        '<h1>🎯 Cách tạo công cụ AI<br>'
        'để tự động hóa công việc</h1>'
        '<div class="subtitle">'
        'Từ ý tưởng đến sản phẩm thực tế '
        '- Không cần biết lập trình</div>'
        '<div class="author-badge">'
        '👤 Tống Công Dũng</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="metric-grid">'
        '<div class="metric-item">'
        '<div class="m-icon">🧠</div>'
        '<div class="m-value">Bước 1</div>'
        '<div class="m-label">Tư duy - Nhận diện vấn đề</div></div>'
        '<div class="metric-item">'
        '<div class="m-icon">🔍</div>'
        '<div class="m-value">Bước 2</div>'
        '<div class="m-label">Phân tích - Đánh giá & chọn hướng</div></div>'
        '<div class="metric-item">'
        '<div class="m-icon">🚀</div>'
        '<div class="m-value">Bước 3</div>'
        '<div class="m-label">Thực chiến - Xây dựng & cải tiến</div></div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '💡 Bạn không cần biết lập trình. '
        'Bạn chỉ cần biết <b>ĐẶT CÂU HỎI ĐÚNG</b> '
        'và <b>MÔ TẢ VẤN ĐỀ RÕ RÀNG</b> cho AI.'
        '</div>',
        unsafe_allow_html=True
    )


def slide_2():
    st.markdown(
        '<div class="slide-header">'
        '<h2>📌 Mục lục nội dung chia sẻ</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<table class="tech-table">'
        '<tr><th>STT</th><th>Nội dung</th>'
        '<th>Chi tiết</th></tr>'
        '<tr><td><b>01</b></td>'
        '<td>🧠 <b>Bước 1 - Tư duy</b></td>'
        '<td>Nhận diện vấn đề, công thức '
        'Prompt 3 phần</td></tr>'
        '<tr><td><b>02</b></td>'
        '<td>🔍 <b>Bước 2 - Phân tích</b></td>'
        '<td>Đánh giá gợi ý AI, chọn hướng đi '
        'đúng</td></tr>'
        '<tr><td><b>03</b></td>'
        '<td>🚀 <b>Bước 3 - Thực chiến</b></td>'
        '<td>Ví dụ: Xây dựng công cụ Gom nhóm '
        'từ khóa SEO</td></tr>'
        '<tr><td><b>04</b></td>'
        '<td>💡 <b>Tổng kết</b></td>'
        '<td>Tư duy áp dụng cho mọi bài toán '
        'công việc</td></tr>'
        '</table></div>',
        unsafe_allow_html=True
    )


def slide_3():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">⚡ BƯỚC 1</div>'
        '<h2>🧠 Tư duy: "Việc này có thể '
        'tự động hóa không?"</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3>🎯 Khi nào nên nghĩ đến tự động hóa?</h3>'
        '<p>Mỗi khi gặp công việc có '
        '<b>3 đặc điểm</b> sau:</p>'
        '<div class="metric-grid">'
        '<div class="metric-item">'
        '<div class="m-icon">🔄</div>'
        '<div class="m-value">Lặp lại</div>'
        '<div class="m-label">Công việc phải làm đi '
        'làm lại nhiều lần, hàng tuần hoặc '
        'hàng tháng</div></div>'
        '<div class="metric-item">'
        '<div class="m-icon">⏰</div>'
        '<div class="m-value">Tốn thời gian</div>'
        '<div class="m-label">Mỗi lần thực hiện '
        'mất hàng giờ hoặc hàng ngày</div></div>'
        '<div class="metric-item">'
        '<div class="m-icon">⚠️</div>'
        '<div class="m-value">Dễ sai sót</div>'
        '<div class="m-label">Làm thủ công dễ nhầm '
        'lẫn, thiếu nhất quán</div></div>'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-warning">'
        '❓ "Mình có thể nhờ AI tự động hóa '
        'việc này để sau mình nhàn hơn không?"'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-success">'
        '✅ Nếu câu trả lời là <b>CÓ THỂ</b> '
        '→ Bắt đầu hỏi AI bằng <b>Gemini</b>!'
        '</div>',
        unsafe_allow_html=True
    )


def slide_4():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">⚡ BƯỚC 1</div>'
        '<h2>💬 Công thức viết Prompt '
        'cho AI hiệu quả</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3 style="text-align:center;color:#4338ca;">'
        '📐 Công thức 3 phần</h3>'
        '<div class="pipeline-flow">'
        '<div class="pipeline-node">'
        '🔹 BỐI CẢNH<br>'
        '<small>Mình đang làm gì?</small></div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node">'
        '🔹 NHU CẦU<br>'
        '<small>Cần AI giúp gì?</small></div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node">'
        '🔹 KẾT QUẢ<br>'
        '<small>Output mong muốn?</small></div>'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h4>📝 Ví dụ Prompt thực tế:</h4>'
        '<div class="terminal-box">'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Bối cảnh:</span> '
        '"Tôi là SEO Content, hàng tuần phải gom '
        'hàng nghìn từ khóa từ Ahrefs thành '
        'các bài viết"<br><br>'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Nhu cầu:</span> '
        '"Tôi muốn tạo một công cụ tự động gom '
        'nhóm từ khóa theo ngữ nghĩa"<br><br>'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Kết quả:</span> '
        '"Output là file Excel với các nhóm bài viết, '
        'mỗi nhóm có keyword chính và keyword phụ"'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-highlight">'
        '💡 <b>Mẹo:</b> Prompt càng cụ thể, '
        'chi tiết → AI trả lời càng chính xác '
        'và hữu ích!'
        '</div>',
        unsafe_allow_html=True
    )


def slide_5():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">⚡ BƯỚC 2</div>'
        '<h2>🔍 Phân tích: Đánh giá '
        'gợi ý từ AI</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-danger">'
        '⚠️ Khi AI đưa ra các gợi ý triển khai '
        '→ <b>Không vội làm ngay!</b> '
        'Hãy cân nhắc kỹ.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3>🎯 3 tiêu chí đánh giá</h3>'
        '<table class="tech-table">'
        '<tr><th>Tiêu chí</th>'
        '<th>Câu hỏi cần trả lời</th></tr>'
        '<tr><td>✅ <b>Khả thi</b></td>'
        '<td>Mình có thể tự làm được không? '
        '(không cần biết code chuyên sâu)</td></tr>'
        '<tr><td>✅ <b>Hiệu quả</b></td>'
        '<td>Giải pháp có thực sự giải quyết '
        'đúng vấn đề không?</td></tr>'
        '<tr><td>✅ <b>Đơn giản</b></td>'
        '<td>Có cách nào đơn giản hơn, '
        'dễ triển khai hơn không?</td></tr>'
        '</table></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="pipeline-flow">'
        '<div class="pipeline-node">'
        'AI đưa gợi ý</div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node warning">'
        'Cân nhắc ưu/nhược</div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node success">'
        'Chọn cách phù hợp</div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node">'
        'Đào sâu chi tiết</div>'
        '</div>',
        unsafe_allow_html=True
    )


def slide_6():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">⚡ BƯỚC 2</div>'
        '<h2>🔎 Đào sâu chi tiết với AI</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3>📋 Nguyên tắc làm việc với AI</h3>'
        '<div class="neon-highlight">'
        '🔄 <b>Làm theo hướng dẫn AI</b> → '
        '<b>Gặp lỗi</b> → '
        '<b>Copy lỗi gửi lại cho AI</b> → '
        '<b>AI sửa</b> → '
        '<b>Tiếp tục</b></div>'
        '<div class="neon-highlight">'
        '📋 <b>Copy lỗi chính xác</b> gửi cho AI '
        'để AI hiểu đúng vấn đề cần sửa</div>'
        '<div class="neon-highlight">'
        '🎯 <b>Không cần hiểu hết code</b>, '
        'chỉ cần hiểu logic và biết cách '
        'mô tả vấn đề rõ ràng</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '💡 AI là trợ lý của bạn - '
        'Bạn chỉ cần biết MÔ TẢ VẤN ĐỀ, '
        'AI sẽ lo phần KỸ THUẬT!'
        '</div>',
        unsafe_allow_html=True
    )


def slide_7():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🚀 BƯỚC 3</div>'
        '<h2>🚀 Ví dụ thực tế: Công cụ '
        'Gom nhóm từ khóa SEO</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-danger">'
        '<b>😩 Vấn đề thực tế gặp phải:</b>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<table class="tech-table">'
        '<tr><th>Hạng mục</th>'
        '<th>Chi tiết</th></tr>'
        '<tr><td>📋 <b>Công việc</b></td>'
        '<td>Gom ~1.000 từ khóa đầu vào thành '
        'các bài viết cụ thể</td></tr>'
        '<tr><td>⏰ <b>Thời gian thủ công</b></td>'
        '<td><b style="color:#ef4444;">'
        '1.5 - 2 ngày</b> làm việc liên tục</td></tr>'
        '<tr><td>🔄 <b>Tần suất</b></td>'
        '<td>Lặp đi lặp lại thường xuyên, '
        'liên tục hàng tuần</td></tr>'
        '<tr><td>😫 <b>Cảm giác</b></td>'
        '<td>Tốn thời gian, nhàm chán, '
        'dễ sai sót khi mệt</td></tr>'
        '</table></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-warning">'
        '💡 "Mình có thể tạo công cụ gom nhóm '
        'tự động được không?" → Quyết định: '
        '<b>HỎI AI!</b>'
        '</div>',
        unsafe_allow_html=True
    )


def slide_8():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🚀 BƯỚC 3</div>'
        '<h2>💬 Hỏi Gemini và nhận gợi ý</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h4>📝 Prompt gửi cho Gemini:</h4>'
        '<div class="terminal-box">'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Bối cảnh:</span> '
        'Tôi là SEO Content, thường xuyên phải gom '
        'hàng nghìn từ khóa từ file Ahrefs thành '
        'các nhóm bài viết.<br><br>'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Nhu cầu:</span> '
        'Tôi muốn tạo một công cụ tự động để gom '
        'nhóm từ khóa theo ngữ nghĩa, thay vì '
        'làm thủ công.<br><br>'
        '<span style="color:#79c0ff;font-weight:700;">'
        '🔹 Kết quả:</span> '
        'Output là file Excel, mỗi nhóm có keyword '
        'chính và các keyword phụ liên quan.'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-success">'
        '🤖 <b>AI gợi ý:</b> Có thể sử dụng '
        '<b>Google Colab</b> + Python để xử lý '
        'tự động</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-highlight">'
        '✅ <b>Đánh giá:</b> Google Colab miễn phí, '
        'không cần cài đặt, chạy trên trình duyệt '
        '→ <b>Phù hợp!</b></div>',
        unsafe_allow_html=True
    )
