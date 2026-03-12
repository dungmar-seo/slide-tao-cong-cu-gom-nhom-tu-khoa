import streamlit as st

TOTAL_SLIDES = 16

def setup_page():
    st.set_page_config(
        page_title="AI Tool Building",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def inject_css():
    st.markdown(
        "<style>"
        "@import url('https://fonts.googleapis.com/css2?"
        "family=Inter:wght@300;400;500;600;700;800;900"
        "&display=swap');"
        "* { font-family: 'Inter', sans-serif; }"
        ".main .block-container {"
        "  padding: 1rem 2rem 2rem 2rem;"
        "  max-width: 1100px;"
        "}"
        ".cover-slide {"
        "  background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);"
        "  padding: 3.5rem 2.5rem;"
        "  border-radius: 24px;"
        "  color: white;"
        "  text-align: center;"
        "  margin-bottom: 1.5rem;"
        "  overflow: hidden;"
        "  box-shadow: 0 20px 60px rgba(15, 12, 41, 0.4);"
        "}"
        ".cover-slide h1 {"
        "  font-size: 2.8rem;"
        "  font-weight: 900;"
        "  margin: 0 0 0.8rem 0;"
        "  line-height: 1.2;"
        "  background: linear-gradient(135deg, #fff 0%, #c7d2fe 100%);"
        "  -webkit-background-clip: text;"
        "  -webkit-text-fill-color: transparent;"
        "  background-clip: text;"
        "}"
        ".cover-slide .subtitle {"
        "  font-size: 1.2rem; opacity: 0.85; font-weight: 400;"
        "}"
        ".cover-slide .author-badge {"
        "  display: inline-block;"
        "  margin-top: 1.8rem;"
        "  padding: 0.6rem 1.5rem;"
        "  background: rgba(255,255,255,0.1);"
        "  border: 1px solid rgba(255,255,255,0.2);"
        "  border-radius: 50px;"
        "  font-weight: 600;"
        "  font-size: 1rem;"
        "}"
        ".slide-header {"
        "  background: linear-gradient(135deg, #0f0c29 0%, #302b63 100%);"
        "  padding: 1.2rem 1.8rem;"
        "  border-radius: 16px;"
        "  color: white;"
        "  margin-bottom: 1.5rem;"
        "  display: flex;"
        "  align-items: center;"
        "  gap: 1rem;"
        "  box-shadow: 0 8px 30px rgba(15, 12, 41, 0.25);"
        "}"
        ".slide-header .step-chip {"
        "  display: inline-flex;"
        "  align-items: center;"
        "  background: rgba(99, 102, 241, 0.3);"
        "  border: 1px solid rgba(99, 102, 241, 0.5);"
        "  padding: 0.3rem 0.8rem;"
        "  border-radius: 8px;"
        "  font-size: 0.8rem;"
        "  font-weight: 700;"
        "  text-transform: uppercase;"
        "  white-space: nowrap;"
        "  flex-shrink: 0;"
        "}"
        ".slide-header h2 {"
        "  margin: 0; font-size: 1.45rem;"
        "  font-weight: 800; line-height: 1.3;"
        "}"
        ".glass-card {"
        "  background: rgba(255, 255, 255, 0.95);"
        "  border: 1px solid rgba(99, 102, 241, 0.1);"
        "  border-radius: 16px;"
        "  padding: 1.5rem;"
        "  margin-bottom: 1rem;"
        "  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);"
        "}"
        ".glass-card h3 {"
        "  color: #1e1b4b; font-weight: 700;"
        "  margin: 0 0 1rem 0; font-size: 1.15rem;"
        "}"
        ".glass-card h4 {"
        "  color: #312e81; font-weight: 700;"
        "  margin: 0 0 0.8rem 0;"
        "}"
        ".neon-highlight {"
        "  background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%);"
        "  border-left: 4px solid #6366f1;"
        "  padding: 1rem 1.3rem;"
        "  border-radius: 0 14px 14px 0;"
        "  margin: 0.8rem 0;"
        "  font-size: 1rem;"
        "}"
        ".neon-warning {"
        "  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);"
        "  border-left: 4px solid #f59e0b;"
        "  padding: 1rem 1.3rem;"
        "  border-radius: 0 14px 14px 0;"
        "  margin: 0.8rem 0;"
        "  font-size: 1.05rem;"
        "  font-weight: 600;"
        "  color: #92400e;"
        "}"
        ".neon-danger {"
        "  background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);"
        "  border-left: 4px solid #ef4444;"
        "  padding: 1rem 1.3rem;"
        "  border-radius: 0 14px 14px 0;"
        "  margin: 0.8rem 0;"
        "}"
        ".neon-success {"
        "  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);"
        "  border-left: 4px solid #10b981;"
        "  padding: 1rem 1.3rem;"
        "  border-radius: 0 14px 14px 0;"
        "  margin: 0.8rem 0;"
        "}"
        ".terminal-box {"
        "  background: #0d1117;"
        "  color: #c9d1d9;"
        "  padding: 1.5rem;"
        "  border-radius: 14px;"
        "  font-family: 'Courier New', monospace;"
        "  font-size: 0.9rem;"
        "  line-height: 1.7;"
        "  margin: 0.8rem 0;"
        "  border: 1px solid #30363d;"
        "}"
        ".pipeline-flow {"
        "  display: flex;"
        "  align-items: center;"
        "  justify-content: center;"
        "  gap: 0.4rem;"
        "  flex-wrap: wrap;"
        "  margin: 1.2rem 0;"
        "}"
        ".pipeline-node {"
        "  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);"
        "  color: white;"
        "  padding: 0.7rem 1.1rem;"
        "  border-radius: 12px;"
        "  font-weight: 700;"
        "  font-size: 0.88rem;"
        "  text-align: center;"
        "  min-width: 110px;"
        "  box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);"
        "}"
        ".pipeline-node.danger {"
        "  background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);"
        "}"
        ".pipeline-node.warning {"
        "  background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);"
        "}"
        ".pipeline-node.success {"
        "  background: linear-gradient(135deg, #059669 0%, #10b981 100%);"
        "}"
        ".pipeline-arrow {"
        "  font-size: 1.4rem; color: #6366f1; font-weight: 900;"
        "}"
        ".tech-table {"
        "  width: 100%;"
        "  border-collapse: separate;"
        "  border-spacing: 0;"
        "  border-radius: 14px;"
        "  overflow: hidden;"
        "  margin: 0.8rem 0;"
        "  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);"
        "}"
        ".tech-table th {"
        "  background: linear-gradient(135deg, #0f0c29 0%, #302b63 100%);"
        "  color: white;"
        "  padding: 0.9rem 1.1rem;"
        "  font-weight: 700;"
        "  font-size: 0.88rem;"
        "  text-align: left;"
        "}"
        ".tech-table td {"
        "  padding: 0.8rem 1.1rem;"
        "  border-bottom: 1px solid #e5e7eb;"
        "  font-size: 0.9rem;"
        "  color: #1f2937;"
        "}"
        ".tech-table tr:nth-child(even) td { background: #f8fafc; }"
        ".tech-table tr:last-child td { border-bottom: none; }"
        ".metric-grid {"
        "  display: grid;"
        "  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));"
        "  gap: 1rem;"
        "  margin: 1rem 0;"
        "}"
        ".metric-item {"
        "  background: white;"
        "  border: 2px solid #e5e7eb;"
        "  border-radius: 16px;"
        "  padding: 1.3rem;"
        "  text-align: center;"
        "  transition: all 0.3s ease;"
        "}"
        ".metric-item:hover {"
        "  border-color: #6366f1;"
        "  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.15);"
        "  transform: translateY(-3px);"
        "}"
        ".metric-item .m-icon { font-size: 2.2rem; margin-bottom: 0.3rem; }"
        ".metric-item .m-value {"
        "  font-size: 1.5rem; font-weight: 900;"
        "  background: linear-gradient(135deg, #4f46e5, #7c3aed);"
        "  -webkit-background-clip: text;"
        "  -webkit-text-fill-color: transparent;"
        "  background-clip: text;"
        "}"
        ".metric-item .m-label {"
        "  font-size: 0.82rem; color: #6b7280; margin-top: 0.3rem;"
        "}"
        ".key-msg {"
        "  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);"
        "  color: white;"
        "  padding: 1.5rem 2rem;"
        "  border-radius: 16px;"
        "  text-align: center;"
        "  font-size: 1.1rem;"
        "  font-weight: 600;"
        "  margin: 1.2rem 0;"
        "  box-shadow: 0 10px 35px rgba(79, 70, 229, 0.3);"
        "}"
        ".cycle-step {"
        "  display: inline-flex;"
        "  align-items: center;"
        "  background: #eef2ff;"
        "  border: 2px solid #6366f1;"
        "  border-radius: 10px;"
        "  padding: 0.5rem 0.9rem;"
        "  margin: 0.3rem;"
        "  font-weight: 700;"
        "  font-size: 0.82rem;"
        "  color: #4338ca;"
        "}"
        ".cycle-step.success-step {"
        "  background: #d1fae5; border-color: #10b981; color: #065f46;"
        "}"
        ".cycle-step.warning-step {"
        "  background: #fef3c7; border-color: #f59e0b; color: #92400e;"
        "}"
        ".cycle-step.danger-step {"
        "  background: #fee2e2; border-color: #ef4444; color: #991b1b;"
        "}"
        ".cycle-arrow {"
        "  display: inline-block; font-size: 1.2rem;"
        "  color: #6366f1; margin: 0 0.15rem; font-weight: 900;"
        "}"
        "#MainMenu {visibility: hidden;}"
        "footer {visibility: hidden;}"
        "header {visibility: hidden;}"
        "</style>",
        unsafe_allow_html=True
    )


def init_state():
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


def render_nav():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.button(
            "⬅️ Slide trước", on_click=go_prev,
            use_container_width=True,
            disabled=(st.session_state.current_slide == 1)
        )
    with c2:
        cur = st.session_state.current_slide
        pct = int((cur / TOTAL_SLIDES) * 100)
        st.markdown(
            '<div style="text-align:center;">'
            '<div style="font-weight:700;color:#4338ca;'
            'font-size:1rem;">Slide '
            + str(cur) + ' / ' + str(TOTAL_SLIDES)
            + '</div>'
            '<div style="background:#e5e7eb;'
            'border-radius:10px;height:6px;'
            'margin-top:0.4rem;overflow:hidden;">'
            '<div style="background:linear-gradient('
            '90deg,#4f46e5,#7c3aed);height:100%;'
            'width:' + str(pct) + '%;'
            'border-radius:10px;"></div>'
            '</div></div>',
            unsafe_allow_html=True
        )
    with c3:
        st.button(
            "Slide tiếp ➡️", on_click=go_next,
            use_container_width=True,
            disabled=(
                st.session_state.current_slide == TOTAL_SLIDES
            )
        )


def render_sidebar():
    with st.sidebar:
        st.markdown(
            '<div style="text-align:center;'
            'padding:1rem 0;">'
            '<span style="font-size:2rem;">🎯</span>'
            '<br>'
            '<span style="color:#1e1b4b;'
            'font-weight:800;font-size:1.1rem;">'
            'AI Tool Building</span>'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown("---")
        names = [
            "1. Trang bìa", "2. Mục lục",
            "3. Tư duy", "4. Prompt",
            "5. Phân tích", "6. Đào sâu AI",
            "7. Thực chiến", "8. Hỏi AI",
            "9. Vòng lặp", "10. Cải tiến 1",
            "11. Cải tiến 2", "12. Nâng cấp",
            "13. Demo", "14. Mở rộng",
            "15. Tổng kết", "16. Kết thúc"
        ]
        for i, name in enumerate(names):
            if st.button(
                name, key="nav_" + str(i),
                use_container_width=True
            ):
                go_to(i + 1)
