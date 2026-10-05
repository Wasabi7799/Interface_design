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

    /* 深色輸入框 */
    .stTextInput input,
    .stTextArea textarea {
        background-color: #0b0e14 !important;
        border: 1px solid #2b3240 !important;
        border-radius: 10px !important;
        color: #f2f5fa !important;
        caret-color: #f2f5fa !important;
    }
    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #7f8a9e !important;
        opacity: 1 !important;
    }
    .stTextInput input:focus,
    .stTextArea textarea:focus {
        background-color: #10141c !important;
        border-color: #6c8cff !important;
        box-shadow: 0 0 0 1px #6c8cff !important;
    }

    /* 深色下拉選單 */
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #0b0e14 !important;
        border: 1px solid #2b3240 !important;
        border-radius: 10px !important;
    }
    .stSelectbox div[data-baseweb="select"] > div:hover {
        border-color: #3d4759 !important;
    }
    .stSelectbox div[data-baseweb="select"] * {
        color: #f2f5fa !important;
    }
    .stSelectbox div[role="listbox"],
    .stSelectbox ul[role="listbox"] {
        background-color: #0b0e14 !important;
        border: 1px solid #2b3240 !important;
    }
    .stSelectbox li,
    .stSelectbox div[role="option"] {
        background-color: #0b0e14 !important;
        color: #f2f5fa !important;
    }
    .stSelectbox li:hover,
    .stSelectbox div[role="option"]:hover {
        background-color: #1b2130 !important;
        color: #ffffff !important;
    }
    .stSelectbox svg { fill: #f2f5fa !important; }

    /* 表單容器 */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 16px;
        padding: 28px 26px;
    }

    /* 深色送出按鈕 */
    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2f3c74 0%, #43307a 100%);
        border: 1px solid #4d5da3;
        border-radius: 10px;
        color: #f2f5fa !important;
        font-size: 1.05rem;
        font-weight: 600;
        padding: 0.65rem 1rem;
        box-shadow: none;
        transition: filter 0.15s ease, transform 0.15s ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: linear-gradient(135deg, #3a4a8c 0%, #523b91 100%);
        border-color: #6c8cff;
        color: #ffffff !important;
        filter: none;
        transform: translateY(-1px);
    }
    .stButton > button:active,
    .stFormSubmitButton > button:active {
        transform: translateY(0);
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

st.session_state.setdefault("form_version", 0)
st.session_state.setdefault("last_submission", None)

version = st.session_state["form_version"]

st.markdown(
    """
    <div class="header-card">
        <h1>📝 課程回饋表單</h1>
        <p>請填寫下方問卷，您的寶貴意見將幫助我們持續改進課程品質。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

name = st.text_input("姓名", key=f"name_{version}", placeholder="請輸入您的姓名")

dept = st.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"],
    key=f"dept_{version}",
)

other_dept = ""
if dept == "其他":
    other_dept = st.text_input(
        "請輸入您的科系名稱",
        key=f"other_dept_{version}",
        placeholder="例如：機械工程系",
    )

rating = st.slider("課程滿意度", min_value=1, max_value=5, value=3, key=f"rating_{version}")

comment = st.text_area(
    "意見回饋",
    key=f"comment_{version}",
    placeholder="請分享您對課程的建議或想法...",
    height=140,
)

submitted = st.button("送出")

if submitted:
    final_dept = other_dept.strip() if dept == "其他" else dept
    final_name = name.strip()

    if not final_name:
        st.warning("請填寫姓名。")
    elif dept == "其他" and not final_dept:
        st.warning("請輸入您的科系名稱。")
    else:
        st.session_state["last_submission"] = {
            "name": final_name,
            "dept": final_dept,
            "rating": rating,
            "has_comment": bool(comment.strip()),
        }
        st.session_state["form_version"] = version + 1
        st.rerun()

if st.session_state["last_submission"]:
    record = st.session_state["last_submission"]
    st.markdown('<div class="thanks">✅ 感謝您的回饋!</div>', unsafe_allow_html=True)
    st.write(
        f"**{record['name']}** ｜ 科系：{record['dept']} ｜ 滿意度：{record['rating']} / 5"
    )
    if record["has_comment"]:
        st.caption("您的意見已成功送出，感謝您的支持！")