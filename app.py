"""課程回饋表單 - Streamlit (Dark Mode)"""

import streamlit as st

st.set_page_config(page_title="課程回饋表單", page_icon="📝", layout="centered")

CSS = """
<style>
    .stApp {
        background: linear-gradient(160deg, #0f1117 0%, #161a23 55%, #12141b 100%);
    }
    .block-container {
        max-width: 720px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, label, p, span { color: #e8ecf4 !important; }
    .header-card {
        background: rgba(255, 255, 255, 0.045);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-left: 4px solid #6c8cff;
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 28px;
    }
    .header-card h1 {
        font-size: 1.9rem;
        margin: 0 0 6px 0;
        letter-spacing: 0.5px;
    }
    .header-card p {
        margin: 0;
        color: #9aa4b8 !important;
        font-size: 0.95rem;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.14) !important;
        border-radius: 10px !important;
        color: #e8ecf4 !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #6c8cff !important;
        box-shadow: 0 0 0 1px #6c8cff !important;
    }
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 16px;
        padding: 28px 26px;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #5b7cfa 0%, #8a5bfa 100%);
        border: none;
        border-radius: 10px;
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 600;
        padding: 0.65rem 1rem;
        transition: transform 0.15s ease, filter 0.15s ease;
    }
    .stButton > button:hover {
        filter: brightness(1.12);
        transform: translateY(-1px);
    }
    .thanks {
        background: rgba(46, 204, 113, 0.12);
        border: 1px solid rgba(46, 204, 113, 0.45);
        color: #6ee7a0 !important;
        border-radius: 14px;
        padding: 18px 22px;
        text-align: center;
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 22px;
    }
    footer, #MainMenu, header { visibility: hidden; }
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

st.markdown(
    """
    <div class="header-card">
        <h1>📝 課程回饋表單</h1>
        <p>請填寫下方問卷，您的寶貴意見將幫助我們持續改進課程品質。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("姓名", placeholder="請輸入您的姓名")

    dept = st.selectbox(
        "科系",
        ["資訊工程系", "電子工程系", "其他"],
        index=0,
    )

    rating = st.slider("課程滿意度", min_value=1, max_value=5, value=3)

    comment = st.text_area(
        "意見回饋",
        placeholder="請分享您對課程的建議或想法...",
        height=140,
    )

    submitted = st.form_submit_button("送出")

if submitted:
    st.markdown('<div class="thanks">✅ 感謝您的回饋!</div>', unsafe_allow_html=True)
    st.write(f"**{name}** ｜ 科系：{dept} ｜ 滿意度：{rating} / 5")
    if comment:
        st.caption("您的意見已成功送出，感謝您的支持！")