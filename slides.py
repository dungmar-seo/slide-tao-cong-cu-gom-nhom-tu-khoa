from slides_css import (
    setup_page, inject_css, init_state,
    render_nav, render_sidebar, TOTAL_SLIDES
)
from slides_part1 import (
    slide_1, slide_2, slide_3, slide_4,
    slide_5, slide_6, slide_7, slide_8
)
from slides_part2 import (
    slide_9, slide_10, slide_11, slide_12,
    slide_13, slide_14, slide_15, slide_16
)
import streamlit as st

# Cau hinh trang (phai goi dau tien)
setup_page()

# Inject CSS
inject_css()

# Khoi tao session state
init_state()

# Render sidebar
render_sidebar()

# Dieu huong slide
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
