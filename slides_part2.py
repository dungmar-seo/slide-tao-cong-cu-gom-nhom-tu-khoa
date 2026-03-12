import streamlit as st


def slide_9():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🚀 BƯỚC 3</div>'
        '<h2>🔧 Vòng lặp xây dựng công cụ</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3 style="text-align:center;">'
        '🔄 Quy trình làm việc với AI</h3>'
        '<div style="text-align:center;'
        'padding:1rem 0;">'
        '<div class="cycle-step">'
        '📝 Yêu cầu AI viết code</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step">'
        '▶️ Chạy thử trên Colab</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step danger-step">'
        '❌ Có lỗi?</div>'
        '<br><br>'
        '<div class="cycle-step">'
        '📋 Copy lỗi gửi cho AI</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step">'
        '🔧 AI sửa code</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step">'
        '🔄 Chạy lại</div>'
        '<br><br>'
        '<div class="cycle-step success-step">'
        '✅ Không lỗi → Test kết quả</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step warning-step">'
        '🤔 Kết quả ổn chưa?</div>'
        '<span class="cycle-arrow">→</span>'
        '<div class="cycle-step danger-step">'
        '📢 Chưa → Nêu vấn đề để AI cải tiến</div>'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '🔑 Không cần biết code - Chỉ cần biết '
        '<b>MÔ TẢ VẤN ĐỀ</b> cho AI! '
        'Lặp lại vòng lặp cho đến khi hoàn thiện.'
        '</div>',
        unsafe_allow_html=True
    )


def slide_10():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🔬 CẢI TIẾN</div>'
        '<h2>🔬 Cải tiến lần 1: '
        'Phát hiện từ khóa rác</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-danger">'
        '<b>😤 Vấn đề phát hiện khi test:</b><br>'
        'File từ khóa từ Ahrefs chứa '
        '<b>rất nhiều từ khóa rác</b> do cơ chế '
        'đào từ khóa của nó.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h4>Ví dụ minh họa:</h4>'
        '<table class="tech-table">'
        '<tr><th>Tìm kiếm về</th>'
        '<th>Ahrefs trả về cả</th>'
        '<th>Lý do</th></tr>'
        '<tr><td><b>"hóa đơn"</b></td>'
        '<td>🌺 "hoa mẫu đơn"</td>'
        '<td>Trùng chữ "đơn"</td></tr>'
        '<tr><td><b>"kế toán"</b></td>'
        '<td>📐 "kế hoạch toán học"</td>'
        '<td>Trùng chữ "kế" và "toán"</td></tr>'
        '</table></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-success">'
        '<b>💡 Giải pháp:</b><br>'
        'Yêu cầu AI tạo thêm <b>công cụ lọc '
        'từ khóa rác</b> trước khi gom nhóm.<br>'
        '→ Ra đời <b>Công cụ 1: Lọc & Gom từ khóa</b> '
        '(dùng AI ngữ nghĩa phân biệt từ khóa '
        'đúng ngành vs rác)'
        '</div>',
        unsafe_allow_html=True
    )


def slide_11():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🔬 CẢI TIẾN</div>'
        '<h2>🔬 Cải tiến lần 2: '
        'Gom nhóm chưa đủ sát</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-danger">'
        '<b>😤 Vấn đề tiếp theo:</b><br>'
        'Sau khi lọc rác, công cụ gom nhóm nhưng '
        '<b>phạm vi quá rộng</b> - các từ khóa '
        'trong 1 nhóm chưa đủ sát nghĩa để viết '
        'thành 1 bài.'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-success">'
        '<b>💡 Giải pháp:</b><br>'
        'Xây dựng <b>Công cụ 2: Gom từ khóa '
        'thành bài viết</b> sử dụng '
        '<b>API Google AI Studio (Gemini)</b><br>'
        '→ AI thông minh hơn, hiểu ngữ cảnh '
        'sâu hơn → Gom chính xác hơn'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h4>📊 Kết quả so sánh:</h4>'
        '<table class="tech-table">'
        '<tr><th>Hạng mục</th>'
        '<th>❌ Trước (thủ công)</th>'
        '<th>✅ Sau (công cụ AI)</th></tr>'
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
        '</table></div>',
        unsafe_allow_html=True
    )


def slide_12():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">⬆️ NÂNG CẤP</div>'
        '<h2>🌐 Từ Google Colab → '
        'Ứng dụng web dễ dùng</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-danger">'
        '<b>😤 Vấn đề với Google Colab:</b>'
        '<ul style="margin:0.5rem 0 0 1.2rem;">'
        '<li>Giao diện phức tạp, không trực quan</li>'
        '<li>Khó chia sẻ cho người khác sử dụng</li>'
        '<li>Phải biết chạy code thủ công</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="neon-success">'
        '<b>💡 Giải pháp:</b> Tiếp tục hỏi AI '
        'cách biến code thành <b>ứng dụng web</b><br>'
        '→ AI gợi ý: <b>GitHub</b> (lưu code) + '
        '<b>Streamlit</b> (tạo giao diện web)'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h4 style="text-align:center;">'
        'Hành trình nâng cấp:</h4>'
        '<div class="pipeline-flow">'
        '<div class="pipeline-node danger">'
        '😤 Google Colab<br>'
        '<small>(phức tạp)</small></div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node warning">'
        '🔧 GitHub + Streamlit<br>'
        '<small>(chuyển đổi)</small></div>'
        '<div class="pipeline-arrow">→</div>'
        '<div class="pipeline-node success">'
        '✅ Ứng dụng Web<br>'
        '<small>(ai cũng dùng được)</small></div>'
        '</div></div>',
        unsafe_allow_html=True
    )


def slide_13():
    st.markdown(
        '<div class="slide-header">'
        '<div class="step-chip">🎉 KẾT QUẢ</div>'
        '<h2>🖥️ Demo: SEO Content '
        'Mapping Tool</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3 style="text-align:center;">'
        '🔍 SEO Content Mapping Tool</h3>'
        '<div class="metric-grid">'
        '<div class="metric-item">'
        '<div class="m-icon">🧹</div>'
        '<div class="m-value">Công cụ 1</div>'
        '<div class="m-label">Upload CSV → Lọc rác '
        '→ Gom nhóm ngữ nghĩa → Xuất Excel</div>'
        '</div>'
        '<div class="metric-item">'
        '<div class="m-icon">🤖</div>'
        '<div class="m-value">Công cụ 2</div>'
        '<div class="m-label">Nhận file từ CỤ 1 '
        'hoặc upload mới → Gemini AI gom '
        'bài viết</div></div>'
        '<div class="metric-item">'
        '<div class="m-icon">🔄</div>'
        '<div class="m-value">Pipeline</div>'
        '<div class="m-label">Chạy tự động cả 2 '
        'bước liên tiếp, không cần thao tác '
        'thủ công</div></div>'
        '</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '✅ Giao diện đẹp, ai cũng dùng được, '
        'không cần biết code! Từ 2 ngày → '
        'Vài phút!'
        '</div>',
        unsafe_allow_html=True
    )


def slide_14():
    st.markdown(
        '<div class="slide-header">'
        '<h2>💡 Với cách tư duy này, bạn có thể '
        'tạo BẤT KỲ công cụ nào!</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<h3>🛠️ Các ví dụ công cụ khác '
        'có thể tạo:</h3>'
        '<table class="tech-table">'
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
        '</table></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '🔑 Công thức chung: Vấn đề lặp lại + '
        'Tốn thời gian → Hỏi AI → Xây công cụ '
        '→ Tự động hóa'
        '</div>',
        unsafe_allow_html=True
    )


def slide_15():
    st.markdown(
        '<div class="slide-header">'
        '<h2>📋 Tổng kết: 3 bước tạo '
        'công cụ AI</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="glass-card">'
        '<table class="tech-table">'
        '<tr><th>Bước</th><th>Hành động</th>'
        '<th>Công cụ hỗ trợ</th></tr>'
        '<tr><td>🧠 <b>Bước 1</b></td>'
        '<td><b>Tư duy</b> - Nhận diện vấn đề '
        'có thể tự động hóa</td>'
        '<td>Gemini (Prompt 3 phần: '
        'Bối cảnh + Nhu cầu + Kết quả)</td></tr>'
        '<tr><td>🔍 <b>Bước 2</b></td>'
        '<td><b>Phân tích</b> - Đánh giá gợi ý, '
        'chọn hướng đi đúng</td>'
        '<td>Gemini + Tư duy phản biện '
        '(Khả thi, Hiệu quả, Đơn giản)</td></tr>'
        '<tr><td>🚀 <b>Bước 3</b></td>'
        '<td><b>Thực hiện</b> - Làm theo AI, test, '
        'phát hiện vấn đề, cải tiến liên tục</td>'
        '<td>Google Colab → GitHub + '
        'Streamlit</td></tr>'
        '</table></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="key-msg">'
        '🎯 Bạn không cần biết lập trình. '
        'Bạn chỉ cần biết <b>ĐẶT CÂU HỎI ĐÚNG</b> '
        'và <b>MÔ TẢ VẤN ĐỀ RÕ RÀNG</b> cho AI. '
        'Hãy bắt đầu từ một vấn đề nhỏ ngay hôm nay!'
        '</div>',
        unsafe_allow_html=True
    )


def slide_16():
    st.markdown(
        '<div class="cover-slide">'
        '<h1>🙏 Cảm ơn mọi người<br>'
        'đã lắng nghe!</h1>'
        '<div class="subtitle" style="'
        'font-style:italic;margin-top:1.5rem;">'
        '"Hãy bắt đầu từ một vấn đề nhỏ '
        'trong công việc hàng ngày. '
        'Hỏi AI. Thử nghiệm. Cải tiến. '
        'Bạn sẽ ngạc nhiên với những gì '
        'mình có thể tạo ra!"</div>'
        '<div class="author-badge">'
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
