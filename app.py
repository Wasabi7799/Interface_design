"""CL Taipei — bilingual Streamlit classified-site prototype."""
from __future__ import annotations

import html
import re
from datetime import date

import streamlit as st
from catalog import CATEGORIES, DISTRICTS, MAIN_CATEGORIES, MOCK_LISTINGS
from theme import inject_theme

st.set_page_config(page_title="CL Taipei", page_icon="CL", layout="wide")
# 隱藏上方 Header、選單以及底部的 Footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

TEXT = {
"zh-TW": {"home":"首頁","tagline":"在台北找到你需要的","intro":"探索在地的住居、服務、工作與好物。","search":"搜尋","search_hint":"搜尋貼文","login":"登入","register":"註冊","logout":"登出","post":"刊登","account":"我的帳號","theme":"主題","language":"語言","light":"明亮","dark":"黑暗","english":"English","chinese":"中文","browse":"瀏覽分類","count_subs":"{count} 個子分類","latest":"最新公告","no_announcements":"目前沒有公告","about":"關於本站","terms":"服務條款","privacy":"隱私政策","subcategories":"子分類","topics":"討論主題","all_listings":"查看全部","results":"共 {count} 筆","keyword":"關鍵字","min_price":"最低價格","max_price":"最高價格","district":"地區","all_districts":"所有地區","sort":"排序","newest":"最新","price_low":"價格低到高","price_high":"價格高到低","nearest":"距離最近","clear":"清除篩選","load_more":"載入更多","no_results":"找不到符合條件的貼文","price":"價格","negotiable":"面議","location":"地點","published":"發佈","views":"瀏覽次數","favorite":"收藏","unfavorite":"移除收藏","contact":"聯絡賣家","share":"複製連結","report":"檢舉","sold":"已售出","expired":"已過期","active":"刊登中","draft":"草稿","seller":"賣家資訊","member_since":"加入時間","description":"描述","back":"返回列表","login_required":"請先登入以繼續此操作。","email":"Email","password":"密碼","remember":"記住我","invalid_login":"Email 或密碼不正確。","display_name":"顯示名稱","confirm_password":"確認密碼","agree_terms":"我同意服務條款","password_rule":"密碼至少 8 碼，且包含英文字母與數字。","password_mismatch":"兩次密碼輸入不一致。","favorites":"我的收藏","my_listings":"我的刊登","messages":"訊息","notifications":"通知","settings":"設定","save":"儲存","edit":"編輯","mark_sold":"標記售出","delete":"刪除","empty_favorites":"尚未收藏任何貼文","empty_listings":"尚無刊登","empty_messages":"目前沒有訊息","empty_notifications":"目前沒有通知","profile":"個人中心","new_listing":"刊登新貼文","category":"分類","subcategory":"子分類","title":"標題","title_hint":"4–80 字","description_hint":"10–4000 字","negotiable_check":"面議","images":"圖片","contact_method":"聯絡方式","internal_message":"站內私訊","show_email":"顯示 Email","save_draft":"儲存草稿","publish":"發佈","published_success":"貼文已成功發佈。","draft_success":"草稿已儲存。","form_error":"請檢查欄位內容後再試一次。","image_error":"圖片必須為 jpg、png 或 webp，且每張不超過 5MB。","report_reason":"檢舉原因","report_note":"補充說明（選填）","report_sent":"已收到檢舉。","send":"送出","message_hint":"輸入訊息（1–1000 字）","message_sent":"訊息已送出。","not_found":"找不到此頁面","not_available":"此貼文已下架","login_success":"登入成功。","register_success":"註冊成功，請至信箱完成驗證。","status":"狀態","search_results":"「{query}」的搜尋結果","search_advice":"請檢查拼字、減少關鍵字，或改為瀏覽分類。","settings_saved":"偏好已儲存。","email_notification":"Email 通知","save_preferences":"儲存偏好","copyright":"CL Taipei 分類資訊平台","report_spam":"垃圾訊息","report_scam":"詐騙","report_inappropriate":"不當內容","report_category":"錯誤分類","report_other":"其他"},
"en": {"home":"Home","tagline":"Find what you need in Taipei","intro":"Explore local housing, services, jobs, and finds.","search":"Search","search_hint":"Search listings","login":"Log in","register":"Sign up","logout":"Log out","post":"Post","account":"My account","theme":"Theme","language":"Language","light":"Light","dark":"Dark","english":"English","chinese":"中文","browse":"Browse categories","count_subs":"{count} subcategories","latest":"Latest announcements","no_announcements":"No announcements at the moment","about":"About","terms":"Terms","privacy":"Privacy","subcategories":"Subcategories","topics":"Discussion topics","all_listings":"View all","results":"{count} results","keyword":"Keyword","min_price":"Minimum price","max_price":"Maximum price","district":"District","all_districts":"All districts","sort":"Sort","newest":"Newest","price_low":"Price: low to high","price_high":"Price: high to low","nearest":"Nearest","clear":"Clear filters","load_more":"Load more","no_results":"No matching listings","price":"Price","negotiable":"Negotiable","location":"Location","published":"Published","views":"Views","favorite":"Save","unfavorite":"Remove saved","contact":"Contact seller","share":"Copy link","report":"Report","sold":"Sold","expired":"Expired","active":"Active","draft":"Draft","seller":"Seller","member_since":"Member since","description":"Description","back":"Back to results","login_required":"Please log in to continue.","email":"Email","password":"Password","remember":"Remember me","invalid_login":"Email or password is incorrect.","display_name":"Display name","confirm_password":"Confirm password","agree_terms":"I agree to the Terms","password_rule":"Use at least 8 characters, including letters and numbers.","password_mismatch":"Passwords do not match.","favorites":"Saved","my_listings":"My listings","messages":"Messages","notifications":"Notifications","settings":"Settings","save":"Save","edit":"Edit","mark_sold":"Mark sold","delete":"Delete","empty_favorites":"No saved listings yet","empty_listings":"No listings yet","empty_messages":"No messages yet","empty_notifications":"No notifications yet","profile":"Profile","new_listing":"Create listing","category":"Category","subcategory":"Subcategory","title":"Title","title_hint":"4–80 characters","description_hint":"10–4000 characters","negotiable_check":"Negotiable","images":"Images","contact_method":"Contact method","internal_message":"Internal message","show_email":"Show email","save_draft":"Save draft","publish":"Publish","published_success":"Your listing is published.","draft_success":"Your draft is saved.","form_error":"Please check the fields and try again.","image_error":"Images must be jpg, png, or webp and no larger than 5MB each.","report_reason":"Report reason","report_note":"Additional information (optional)","report_sent":"Your report has been received.","send":"Send","message_hint":"Write a message (1–1000 characters)","message_sent":"Message sent.","not_found":"Page not found","not_available":"This listing is unavailable","login_success":"Logged in.","register_success":"Account created. Please verify your email.","status":"Status","search_results":"Results for “{query}”","search_advice":"Check spelling, use fewer keywords, or browse a category.","settings_saved":"Preferences saved.","email_notification":"Email notifications","save_preferences":"Save preferences","copyright":"CL Taipei classifieds","report_spam":"Spam","report_scam":"Scam","report_inappropriate":"Inappropriate content","report_category":"Wrong category","report_other":"Other"}}

def init():
    p = st.query_params
    st.session_state.setdefault("lang", str(p.get("lang", "zh-TW")) if str(p.get("lang", "zh-TW")) in TEXT else "zh-TW")
    st.session_state.setdefault("theme", str(p.get("theme", "light")) if str(p.get("theme", "light")) in {"light", "dark"} else "light")
    for key, value in {"user":None,"favorites":set(),"drafts":[],"created":[],"pending":None}.items(): st.session_state.setdefault(key, value)

def t(key, **data): return (TEXT[st.session_state["lang"]].get(key) or TEXT["zh-TW"].get(key) or "").format(**data)
def route(**data):
    data = {"theme":st.session_state["theme"], "lang":st.session_state["lang"], **{k:v for k,v in data.items() if v not in (None,"")}}
    st.query_params.clear(); st.query_params.update(data); st.rerun()
def subs(parent): return [x for x in CATEGORIES if x["parent_slug"] == parent]
def cname(slug):
    field = "name_zh" if st.session_state["lang"] == "zh-TW" else "name_en"
    for x in MAIN_CATEGORIES:
        if x[0] == slug: return x[2] if field == "name_zh" else x[1]
    for x in CATEGORIES:
        if x["slug"] == slug: return x[field]
    return slug
def price(v): return t("negotiable") if v is None else f"NT${v:,.0f}"
def all_listings(): return list(MOCK_LISTINGS) + st.session_state["created"]

def announcements():
    """Read the existing announcement table when deployment settings are available."""
    try:
        database_url = st.secrets["DATABASE_URL"]
    except Exception:
        return []
    try:
        import psycopg
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, content, created_at FROM announcements_announcement ORDER BY created_at DESC LIMIT 3")
                return cursor.fetchall()
    except Exception:
        # TODO: [後端提供公告 API、可觀測性與不洩漏技術細節的錯誤回應。]
        return []


TEXT["zh-TW"].update(
    {
        "open_listing": "查看貼文",
        "filters": "篩選條件",
        "hero_eyebrow": "台北 · 城市佈告欄",
        "hero_stat_categories": "主分類",
        "post_tips": "刊登小提醒",
        "checklist": "送出前確認",
        "seller_info": "賣家資訊",
        "back_home": "回到首頁",
        "login_subtitle": "登入後即可收藏、刊登與聯絡賣家。",
        "register_subtitle": "建立帳號，開始在城市佈告欄交流。",
        "no_account": "還沒有帳號？",
        "have_account": "已經有帳號？",
    }
)
TEXT["en"].update(
    {
        "open_listing": "View listing",
        "filters": "Filters",
        "hero_eyebrow": "Taipei · City Bulletin",
        "hero_stat_categories": "main categories",
        "post_tips": "Posting tips",
        "checklist": "Before you publish",
        "seller_info": "Seller information",
        "back_home": "Back home",
        "login_subtitle": "Log in to save listings, post, and contact sellers.",
        "register_subtitle": "Create an account to join the city board.",
        "no_account": "Don't have an account?",
        "have_account": "Already have an account?",
    }
)


def style():
    inject_theme(st.session_state["theme"])


def alt_name(slug):
    field = "name_en" if st.session_state["lang"] == "zh-TW" else "name_zh"
    for item in MAIN_CATEGORIES:
        if item[0] == slug:
            return item[1] if field == "name_en" else item[2]
    for item in CATEGORIES:
        if item["slug"] == slug:
            return item[field]
    return slug


def cat_icon(slug):
    for item in MAIN_CATEGORIES:
        if item[0] == slug:
            return item[3]
    return "•"


def status_class(value):
    return value if value in {"active", "sold", "expired", "draft"} else "active"


def reroute_same():
    data = {
        key: value
        for key, value in st.query_params.items()
        if key not in {"theme", "lang"}
    }
    data.setdefault("page", "home")
    route(**data)


def topbar():
    with st.container(key="topbar"):
        row = st.columns([2.6, 0.95, 0.95, 1.7], gap="small", vertical_alignment="center")
        with row[0]:
            if st.button("CL Taipei", key="brand_home", type="tertiary", help=t("home")):
                route(page="home")
        with row[1]:
            theme_choice = st.selectbox(
                t("theme"),
                [t("light"), t("dark")],
                index=0 if st.session_state["theme"] == "light" else 1,
                label_visibility="collapsed",
                key="theme_pick",
            )
            wanted_theme = "light" if theme_choice == t("light") else "dark"
            if wanted_theme != st.session_state["theme"]:
                st.session_state["theme"] = wanted_theme
                reroute_same()
        with row[2]:
            lang_choice = st.selectbox(
                t("language"),
                [t("chinese"), t("english")],
                index=0 if st.session_state["lang"] == "zh-TW" else 1,
                label_visibility="collapsed",
                key="lang_pick",
            )
            wanted_lang = "zh-TW" if lang_choice == t("chinese") else "en"
            if wanted_lang != st.session_state["lang"]:
                st.session_state["lang"] = wanted_lang
                reroute_same()
        with row[3]:
            actions = st.columns([1, 1], gap="small")
            with actions[0]:
                if st.session_state["user"]:
                    if st.button(t("post"), key="top_post", type="primary", width="stretch"):
                        route(page="post")
                else:
                    if st.button(t("login"), key="top_login", width="stretch"):
                        route(page="login")
            with actions[1]:
                if st.session_state["user"]:
                    if st.button(t("account"), key="top_account", width="stretch"):
                        route(page="me")
                else:
                    if st.button(t("register"), key="top_register", width="stretch"):
                        route(page="register")

        with st.form("quick_search", border=False):
            search_row = st.columns([7, 1.35], gap="small", vertical_alignment="center")
            with search_row[0]:
                query = st.text_input(
                    t("search"), placeholder=t("search_hint"), label_visibility="collapsed"
                )
            with search_row[1]:
                submitted = st.form_submit_button(
                    t("search"), type="primary", width="stretch"
                )
            if submitted:
                route(page="search", q=query.strip()[:100])


def footer():
    st.markdown(
        f"""
        <footer class="site-footer">
          <div class="foot-brand">
            <div class="foot-mark">CL</div>
            <div>
              <strong>CL Taipei</strong>
              <p>{html.escape(t("intro"))}</p>
            </div>
          </div>
          <div class="foot-links">
            <span>{html.escape(t("about"))}</span>
            <span>{html.escape(t("terms"))}</span>
            <span>{html.escape(t("privacy"))}</span>
            <span>{html.escape(t("language"))}</span>
          </div>
          <div class="foot-meta">{html.escape(t("copyright"))}</div>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def section_head(title, meta=""):
    st.markdown(
        f"<div class='section-head'><h2>{html.escape(title)}</h2>"
        f"<div class='rule'></div><span class='section-meta'>{html.escape(meta)}</span></div>",
        unsafe_allow_html=True,
    )


def crumbs(*parts):
    nodes = []
    for index, part in enumerate(parts):
        if index:
            nodes.append("<span class='sep'>/</span>")
        label = html.escape(part)
        nodes.append(f"<strong>{label}</strong>" if index == len(parts) - 1 else f"<span>{label}</span>")
    st.markdown("<div class='crumbs'>" + "".join(nodes) + "</div>", unsafe_allow_html=True)


def page_head(title, eyebrow="", subtitle="", badge=""):
    badge_html = f"<span class='count-badge'>{html.escape(badge)}</span>" if badge else ""
    eyebrow_html = f"<p class='eyebrow'>{html.escape(eyebrow)}</p>" if eyebrow else ""
    subtitle_html = f"<p class='page-sub'>{html.escape(subtitle)}</p>" if subtitle else ""
    st.markdown(
        f"<div class='page-head'><div>{eyebrow_html}<h1>{html.escape(title)}</h1>"
        f"{subtitle_html}</div>{badge_html}</div>",
        unsafe_allow_html=True,
    )


def empty_state(message, icon="◌"):
    st.markdown(
        f"<div class='empty'><span class='empty-ico'>{html.escape(icon)}</span>"
        f"<p>{html.escape(message)}</p></div>",
        unsafe_allow_html=True,
    )


def require_login(action, target):
    if st.session_state["user"]:
        return True
    st.session_state["pending"] = (action, target)
    st.info(t("login_required"))
    route(page="login")
    return False


def favorite(listing_id, key):
    saved = listing_id in st.session_state["favorites"]
    if st.button(
        t("unfavorite") if saved else t("favorite"),
        key=key,
        type="tertiary" if saved else "secondary",
        width="stretch",
    ):
        if require_login("favorite", listing_id):
            st.session_state["favorites"].symmetric_difference_update({listing_id})
            st.rerun()


def category_card(index, item):
    slug, english, chinese, icon = item
    main, other = (chinese, english) if st.session_state["lang"] == "zh-TW" else (english, chinese)
    with st.container(border=True, key=f"catcard_{slug}"):
        st.markdown(
            f"<div class='cat-top'><span class='cat-num'>{index + 1:02d}</span>"
            f"<span class='cat-ico'>{html.escape(icon)}</span></div>"
            f"<div class='cat-title'>{html.escape(main)}</div>"
            f"<p class='cat-en'>{html.escape(other)}</p>"
            f"<div class='cat-foot'>{html.escape(t('count_subs', count=len(subs(slug))))}</div>",
            unsafe_allow_html=True,
        )
        if st.button(f"{t('browse')} →", key=f"catbtn_{slug}", type="tertiary"):
            route(page="category", category=slug)


def home():
    total_subs = sum(len(subs(item[0])) for item in MAIN_CATEGORIES)
    st.markdown(
        f"""
        <section class="hero">
          <p class="hero-eyebrow">{html.escape(t("hero_eyebrow"))}</p>
          <h1>{html.escape(t("tagline"))}</h1>
          <p class="hero-lede">{html.escape(t("intro"))}</p>
          <div class="hero-chips">
            <span class="chip"><strong>{len(MAIN_CATEGORIES)}</strong>{html.escape(t("hero_stat_categories"))}</span>
            <span class="chip"><strong>{total_subs}</strong>{html.escape(t("subcategories"))}</span>
            <span class="chip">{html.escape(t("results", count=len(all_listings())))}</span>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    section_head(t("browse"), t("count_subs", count=total_subs))
    grid = [
        st.columns([1.28, 1, 1, 1], gap="medium"),
        st.columns([1, 1, 1.28, 1], gap="medium"),
    ]
    for index, item in enumerate(MAIN_CATEGORIES):
        with grid[index // 4][index % 4]:
            category_card(index, item)

    section_head(t("latest"), t("notifications"))
    with st.container(border=True, key="notice-board"):
        rows = announcements()
        if not rows:
            st.info(t("no_announcements"))
        for title, content, created_at in rows:
            st.markdown(
                f"<div class='notice'><span class='badge'>{html.escape(str(created_at)[:10])}</span>"
                f"<div><div class='listing-title'>{html.escape(str(title))}</div>"
                f"<p class='desc-snippet'>{html.escape(str(content))}</p></div></div>",
                unsafe_allow_html=True,
            )


def category_page(cat):
    if cat not in {item[0] for item in MAIN_CATEGORIES}:
        return not_found()
    items = subs(cat)
    count = len([row for row in all_listings() if row["category"] == cat])
    crumbs(t("home"), cname(cat))
    page_head(
        cname(cat),
        eyebrow=alt_name(cat),
        subtitle=t("topics") if cat == "discussion-forums" else t("subcategories"),
        badge=t("results", count=count),
    )
    columns = st.columns(3, gap="medium")
    for index, item in enumerate(items):
        with columns[index % 3]:
            with st.container(border=True, key=f"subcard_{cat}_{item['slug']}"):
                st.markdown(
                    f"<div class='cat-top'><span class='cat-num'>{index + 1:02d}</span></div>"
                    f"<div class='cat-title'>{html.escape(cname(item['slug']))}</div>"
                    f"<p class='cat-en'>{html.escape(alt_name(item['slug']))}</p>",
                    unsafe_allow_html=True,
                )
                if st.button(
                    f"{t('browse')} →",
                    key=f"sub_{cat}_{item['slug']}",
                    type="tertiary",
                ):
                    route(page="list", category=cat, sub=item["slug"])
    if st.button(t("all_listings"), key="all_in_cat", type="primary"):
        route(page="list", category=cat)


def matches(cat=None, sub=None, q="", district="", low=None, high=None):
    out = []
    needle = q.lower().strip()
    for row in all_listings():
        if cat and row["category"] != cat or sub and row["sub"] != sub:
            continue
        if district and row["district"] != district:
            continue
        if needle and needle not in (row["title"] + " " + row["description"]).lower():
            continue
        if low is not None and (row["price"] is None or row["price"] < low):
            continue
        if high is not None and (row["price"] is None or row["price"] > high):
            continue
        out.append(row)
    return out


def listing_list(cat=None, sub=None, q=""):
    heading = " / ".join([cname(item) for item in (cat, sub) if item])
    if heading:
        crumbs(t("home"), *[cname(item) for item in (cat, sub) if item])
    params = st.query_params
    initial_q = q or str(params.get("q", ""))
    try:
        initial_low = int(str(params.get("low", "0")) or 0)
    except ValueError:
        initial_low = 0
    try:
        initial_high = int(str(params.get("high", "9999999")) or 9999999)
    except ValueError:
        initial_high = 9999999
    initial_district = str(params.get("district", ""))
    initial_sort = str(params.get("sort", "newest"))
    result_count = len(
        matches(
            cat,
            sub,
            initial_q,
            initial_district,
            initial_low or None,
            initial_high if initial_high < 9_999_999 else None,
        )
    )
    page_head(
        heading or t("search"),
        eyebrow=alt_name(sub) if sub else (alt_name(cat) if cat else t("search_hint")),
        badge=t("results", count=result_count),
    )

    left, right = st.columns([1, 2.9], gap="large")
    with left:
        with st.container(border=True, key="filter-box"):
            st.markdown(f"<p class='eyebrow'>{html.escape(t('filters'))}</p>", unsafe_allow_html=True)
            with st.form("filters", border=False):
                query = st.text_input(
                    t("keyword"), value=initial_q, max_chars=100, key=f"f_q_{cat}_{sub}"
                )
                price_cols = st.columns(2, gap="small")
                with price_cols[0]:
                    low = st.number_input(
                        t("min_price"),
                        0,
                        9_999_999,
                        initial_low,
                        key=f"f_low_{cat}_{sub}",
                    )
                with price_cols[1]:
                    high = st.number_input(
                        t("max_price"),
                        0,
                        9_999_999,
                        initial_high,
                        key=f"f_high_{cat}_{sub}",
                    )
                district = st.selectbox(
                    t("district"),
                    [t("all_districts"), *DISTRICTS],
                    index=(DISTRICTS.index(initial_district) + 1)
                    if initial_district in DISTRICTS
                    else 0,
                    key=f"f_district_{cat}_{sub}",
                )
                submitted = st.form_submit_button(
                    t("search"), type="primary", width="stretch"
                )
            if submitted:
                st.session_state["list_limit"] = 20
                route(
                    page="list",
                    category=cat or "",
                    sub=sub or "",
                    q=query.strip()[:100],
                    low=str(int(low)) if low else "",
                    high=str(int(high)) if high < 9_999_999 else "",
                    district="" if district == t("all_districts") else district,
                    sort=initial_sort,
                )
            if st.button(t("clear"), key="clear_filters", type="tertiary", width="stretch"):
                st.session_state["list_limit"] = 20
                route(page="list", category=cat or "", sub=sub or "")

    rows = matches(
        cat,
        sub,
        initial_q,
        initial_district,
        initial_low or None,
        initial_high if initial_high < 9_999_999 else None,
    )

    with right:
        top = st.columns([2, 1.15], gap="small", vertical_alignment="bottom")
        with top[0]:
            st.markdown(
                f"<p class='section-meta'>{html.escape(t('results', count=len(rows)))}</p>",
                unsafe_allow_html=True,
            )
        with top[1]:
            sort_labels = [t("newest"), t("price_low"), t("price_high"), t("nearest")]
            sort_keys = ["newest", "low", "high", "nearest"]
            order = st.selectbox(
                t("sort"),
                sort_labels,
                index=sort_keys.index(initial_sort) if initial_sort in sort_keys else 0,
                label_visibility="collapsed",
                key=f"sort_pick_{cat}_{sub}",
            )
        if order == t("price_low"):
            rows.sort(key=lambda row: row["price"] is None or row["price"])
        elif order == t("price_high"):
            rows.sort(key=lambda row: -(row["price"] or -1))
        else:
            rows.sort(key=lambda row: row["created"], reverse=True)

        signature = f"{cat}|{sub}|{initial_q}|{initial_district}|{initial_low}|{initial_high}"
        if st.session_state.get("list_sig") != signature:
            st.session_state["list_sig"] = signature
            st.session_state["list_limit"] = 20
        limit = st.session_state.setdefault("list_limit", 20)

        if not rows:
            empty_state(t("no_results"), "⌕")
            st.caption(t("search_advice"))
            if st.button(t("clear"), key="clear_empty", type="secondary"):
                st.session_state["list_limit"] = 20
                route(page="list", category=cat or "", sub=sub or "")
            return

        for row in rows[:limit]:
            card(row, ns="list")
        if len(rows) > limit:
            if st.button(t("load_more"), key="load_more", type="secondary", width="stretch"):
                st.session_state["list_limit"] = limit + 20
                st.rerun()


def card(row, ns="list"):
    stat = t(row["status"]) if row["status"] in {"active", "draft", "sold", "expired"} else row["status"]
    icon = cat_icon(row["category"])
    snippet = row["description"][:96] + ("…" if len(row["description"]) > 96 else "")
    with st.container(border=True, key=f"listing_{ns}_{row['id']}"):
        thumb, body, side = st.columns([0.75, 4.2, 1.55], gap="medium", vertical_alignment="center")
        with thumb:
            st.markdown(f"<div class='thumb'>{html.escape(icon)}</div>", unsafe_allow_html=True)
        with body:
            st.markdown(
                f"<span class='badge badge-{status_class(row['status'])}'>{html.escape(str(stat))}</span>"
                f"<div class='listing-title'>{html.escape(row['title'])}</div>"
                f"<p class='meta'>{html.escape(row['district'])} · {html.escape(str(row['created']))}</p>"
                f"<p class='desc-snippet'>{html.escape(snippet)}</p>",
                unsafe_allow_html=True,
            )
        with side:
            st.markdown(
                f"<p class='price'>{html.escape(price(row['price']))}</p>"
                f"<p class='meta'>{html.escape(t('views'))}: {row['views']}</p>",
                unsafe_allow_html=True,
            )
            if st.button(
                t("open_listing"),
                key=f"open_{ns}_{row['id']}",
                type="primary",
                width="stretch",
            ):
                route(page="listing", id=row["id"])
            favorite(row["id"], f"fav_{ns}_{row['id']}")


def detail(ident):
    row = next((item for item in all_listings() if item["id"] == ident), None)
    if not row or row["status"] in {"removed", "expired"}:
        st.warning(t("not_available"))
        if st.button(t("back_home"), key="detail_back", type="secondary"):
            route(page="home")
        return
    icon = cat_icon(row["category"])
    crumbs(t("home"), cname(row["category"]), cname(row["sub"]))
    page_head(
        row["title"],
        eyebrow=f"{cname(row['category'])} / {cname(row['sub'])}",
        subtitle=alt_name(row["sub"]),
    )

    main, aside = st.columns([2.2, 1], gap="large")
    with main:
        st.markdown(
            f"<div class='detail-hero'><span>{html.escape(icon)}</span>"
            f"<small>{html.escape(t('images'))}</small></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='meta-row'><span>{html.escape(t('location'))}: {html.escape(row['district'])}</span>"
            f"<span>{html.escape(t('published'))}: {html.escape(str(row['created']))}</span>"
            f"<span>{html.escape(t('views'))}: {row['views']}</span></div>",
            unsafe_allow_html=True,
        )
        st.markdown(f"<h2 class='block-title'>{html.escape(t('description'))}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p class='body-text'>{html.escape(row['description'])}</p>", unsafe_allow_html=True)

        if st.session_state.get("contact") == row["id"]:
            with st.container(border=True, key="contact-panel"):
                with st.form("contact_form", border=False):
                    message = st.text_area(
                        t("contact"), placeholder=t("message_hint"), max_chars=1000
                    )
                    if st.form_submit_button(t("send"), type="primary"):
                        if message.strip():
                            st.success(t("message_sent"))
                            st.session_state.pop("contact")
                        else:
                            st.error(t("form_error"))
        if st.session_state.get("report") == row["id"]:
            with st.container(border=True, key="report-panel"):
                with st.form("report_form", border=False):
                    st.selectbox(
                        t("report_reason"),
                        [
                            t("report_scam"),
                            t("report_spam"),
                            t("report_inappropriate"),
                            t("report_category"),
                            t("report_other"),
                        ],
                    )
                    st.text_area(t("report_note"), max_chars=500)
                    if st.form_submit_button(t("send"), type="primary"):
                        st.success(t("report_sent"))
                        st.session_state.pop("report")

    with aside:
        with st.container(border=True, key="detail-side"):
            st.markdown(
                f"<p class='price-lg'>{html.escape(price(row['price']))}</p>"
                f"<span class='badge badge-{status_class(row['status'])}'>{html.escape(str(t(row['status'])))}</span>",
                unsafe_allow_html=True,
            )
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            favorite(row["id"], "detail_fav")
            if st.button(t("contact"), key="contact_btn", type="primary", width="stretch"):
                if require_login("contact", row["id"]):
                    st.session_state["contact"] = row["id"]
            if st.button(t("share"), key="share_btn", width="stretch"):
                st.toast(t("share"))
            if st.button(t("report"), key="report_btn", width="stretch"):
                if require_login("report", row["id"]):
                    st.session_state["report"] = row["id"]
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            initials = (row["seller"] or "CL")[:2].upper()
            st.markdown(
                f"<p class='eyebrow'>{html.escape(t('seller_info'))}</p>"
                f"<div class='seller-row'><span class='avatar'>{html.escape(initials)}</span>"
                f"<div><p class='seller-name'>{html.escape(row['seller'])}</p>"
                f"<p class='meta'>{html.escape(t('member_since'))}: 2025</p></div></div>",
                unsafe_allow_html=True,
            )


def login():
    left, middle, right = st.columns([1, 1.35, 1], gap="large")
    with middle:
        st.markdown(
            f"<div class='auth-brand'><div class='auth-mark'>CL</div>"
            f"<h1>{html.escape(t('login'))}</h1>"
            f"<p>{html.escape(t('login_subtitle'))}</p></div>",
            unsafe_allow_html=True,
        )
        with st.container(border=True, key="auth-box"):
            with st.form("login_form", border=False):
                email = st.text_input(t("email"), max_chars=254)
                password = st.text_input(
                    t("password"),
                    type="password",
                    max_chars=128,
                    help=t("password_rule"),
                )
                st.checkbox(t("remember"))
                submitted = st.form_submit_button(
                    t("login"), type="primary", width="stretch"
                )
            if submitted:
                if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()) and len(password) >= 8:
                    st.session_state["user"] = {
                        "email": email.strip(),
                        "name": email.split("@")[0],
                    }
                    st.success(t("login_success"))
                    pending = st.session_state.pop("pending")
                    if pending:
                        action, target = pending
                        if action == "favorite":
                            st.session_state["favorites"].add(target)
                        if action in {"contact", "report"}:
                            st.session_state[action] = target
                        route(page="listing", id=target)
                    route(page="home")
                else:
                    st.error(t("invalid_login"))
            st.markdown(
                f"<p class='auth-switch'>{html.escape(t('no_account'))}</p>",
                unsafe_allow_html=True,
            )
            if st.button(t("register"), key="go_register", type="tertiary", width="stretch"):
                route(page="register")


def register():
    left, middle, right = st.columns([1, 1.35, 1], gap="large")
    with middle:
        st.markdown(
            f"<div class='auth-brand'><div class='auth-mark'>CL</div>"
            f"<h1>{html.escape(t('register'))}</h1>"
            f"<p>{html.escape(t('register_subtitle'))}</p></div>",
            unsafe_allow_html=True,
        )
        with st.container(border=True, key="auth-box"):
            with st.form("register_form", border=False):
                name = st.text_input(t("display_name"), max_chars=60)
                email = st.text_input(t("email"), max_chars=254)
                password = st.text_input(
                    t("password"),
                    type="password",
                    max_chars=128,
                    help=t("password_rule"),
                )
                confirm = st.text_input(
                    t("confirm_password"), type="password", max_chars=128
                )
                terms = st.checkbox(t("agree_terms"))
                submitted = st.form_submit_button(
                    t("register"), type="primary", width="stretch"
                )
            if submitted:
                secure = (
                    len(password) >= 8
                    and bool(re.search(r"[A-Za-z]", password))
                    and bool(re.search(r"\d", password))
                )
                if not (
                    name.strip()
                    and re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip())
                    and secure
                    and terms
                ):
                    st.error(t("form_error"))
                elif password != confirm:
                    st.error(t("password_mismatch"))
                else:
                    st.success(t("register_success"))
                    route(page="login")
            st.markdown(
                f"<p class='auth-switch'>{html.escape(t('have_account'))}</p>",
                unsafe_allow_html=True,
            )
            if st.button(t("login"), key="go_login", type="tertiary", width="stretch"):
                route(page="login")


def post_page():
    if not require_login("post", ""):
        return
    page_head(t("new_listing"), eyebrow=t("post"), subtitle=t("latest"))
    main, aside = st.columns([2.15, 1], gap="large")
    with main:
        with st.container(border=True, key="post-form-box"):
            parents = [item[0] for item in MAIN_CATEGORIES]
            select_cols = st.columns(2, gap="medium")
            with select_cols[0]:
                cat = st.selectbox(t("category"), parents, format_func=cname, key="post_cat")
            with select_cols[1]:
                sub = st.selectbox(
                    t("subcategory"),
                    [item["slug"] for item in subs(cat)],
                    format_func=cname,
                    key=f"post_sub_{cat}",
                )
            with st.form("post_form", border=False):
                title = st.text_input(
                    t("title"), max_chars=80, placeholder=t("title_hint")
                )
                desc = st.text_area(
                    t("description"),
                    max_chars=4000,
                    placeholder=t("description_hint"),
                )
                money = st.columns(2, gap="medium")
                with money[0]:
                    amount = st.number_input(t("price"), 0, 9_999_999, 0)
                with money[1]:
                    negotiable = st.checkbox(t("negotiable_check"))
                district = st.selectbox(t("district"), DISTRICTS)
                files = st.file_uploader(
                    t("images"),
                    type=["jpg", "jpeg", "png", "webp"],
                    accept_multiple_files=True,
                )
                st.radio(
                    t("contact_method"),
                    [t("internal_message"), t("show_email")],
                )
                terms = st.checkbox(t("agree_terms"))
                buttons = st.columns(2, gap="medium")
                with buttons[0]:
                    draft = st.form_submit_button(t("save_draft"), width="stretch")
                with buttons[1]:
                    publish = st.form_submit_button(
                        t("publish"), type="primary", width="stretch"
                    )
            if draft or publish:
                too_big = len(files) > 8 or any(
                    item.size > 5 * 1024 * 1024 for item in files
                )
                valid = 4 <= len(title.strip()) <= 80 and 10 <= len(desc.strip()) <= 4000 and terms
                if too_big:
                    st.error(t("image_error"))
                elif not valid:
                    st.error(t("form_error"))
                else:
                    record = {
                        "id": str(
                            2000
                            + len(st.session_state["created"])
                            + len(st.session_state["drafts"])
                        ),
                        "category": cat,
                        "sub": sub,
                        "title": title.strip(),
                        "description": desc.strip(),
                        "price": None if negotiable else int(amount),
                        "district": district,
                        "created": str(date.today()),
                        "status": "active" if publish else "draft",
                        "seller": st.session_state["user"]["name"],
                        "views": 0,
                    }
                    if publish:
                        st.session_state["created"].append(record)
                        st.success(t("published_success"))
                        route(page="listing", id=record["id"])
                    else:
                        st.session_state["drafts"].append(record)
                        st.success(t("draft_success"))
    with aside:
        with st.container(border=True, key="post-tips"):
            st.markdown(
                f"<p class='eyebrow'>{html.escape(t('post_tips'))}</p>"
                f"<h3>{html.escape(t('checklist'))}</h3>"
                f"<ul class='tips'>"
                f"<li>{html.escape(t('title_hint'))}</li>"
                f"<li>{html.escape(t('description_hint'))}</li>"
                f"<li>{html.escape(t('image_error'))}</li>"
                f"</ul>",
                unsafe_allow_html=True,
            )


def profile():
    if not require_login("me", ""):
        return
    user = st.session_state["user"]
    initials = (user["name"] or "CL")[:2].upper()
    page_head(t("profile"), eyebrow=t("account"), subtitle=user["email"])
    with st.container(border=True, key="profile-card"):
        head = st.columns([0.6, 3.6, 1.2], gap="medium", vertical_alignment="center")
        with head[0]:
            st.markdown(
                f"<span class='avatar avatar-lg'>{html.escape(initials)}</span>",
                unsafe_allow_html=True,
            )
        with head[1]:
            st.markdown(
                f"<p class='seller-name'>{html.escape(user['name'])}</p>"
                f"<p class='meta'>{html.escape(user['email'])}</p>",
                unsafe_allow_html=True,
            )
        with head[2]:
            if st.button(t("logout"), key="logout_top", type="secondary", width="stretch"):
                st.session_state["user"] = None
                route(page="home")

    tabs = st.tabs(
        [
            t("favorites"),
            t("my_listings"),
            t("messages"),
            t("notifications"),
            t("settings"),
        ]
    )
    with tabs[0]:
        rows = [row for row in all_listings() if row["id"] in st.session_state["favorites"]]
        if rows:
            for row in rows:
                card(row, ns="fav")
        else:
            empty_state(t("empty_favorites"), "♡")
    with tabs[1]:
        rows = st.session_state["created"] + st.session_state["drafts"]
        if rows:
            for row in rows:
                card(row, ns="mine")
        else:
            empty_state(t("empty_listings"), "▤")
    with tabs[2]:
        empty_state(t("empty_messages"), "✉")
    with tabs[3]:
        empty_state(t("empty_notifications"), "◔")
    with tabs[4]:
        with st.container(border=True, key="settings-box"):
            with st.form("settings_form", border=False):
                st.text_input(t("display_name"), value=user["name"])
                st.checkbox(t("email_notification"))
                if st.form_submit_button(t("save_preferences"), type="primary"):
                    st.success(t("settings_saved"))


def not_found():
    st.markdown(
        f"<div class='empty' style='margin-top:2rem'>"
        f"<span class='empty-ico'>🧭</span>"
        f"<h3>{html.escape(t('not_found'))}</h3>"
        f"<p>{html.escape(t('search_advice'))}</p></div>",
        unsafe_allow_html=True,
    )
    if st.button(t("back_home"), key="not_found_home", type="primary"):
        route(page="home")


def main():
    init()
    style()
    topbar()
    page = str(st.query_params.get("page", "home"))
    if page == "home":
        home()
    elif page == "category":
        category_page(str(st.query_params.get("category", "")))
    elif page == "list":
        listing_list(
            str(st.query_params.get("category", "")) or None,
            str(st.query_params.get("sub", "")) or None,
            str(st.query_params.get("q", "")),
        )
    elif page == "listing":
        detail(str(st.query_params.get("id", "")))
    elif page == "search":
        listing_list(q=str(st.query_params.get("q", "")))
    elif page == "login":
        login()
    elif page == "register":
        register()
    elif page == "post":
        post_page()
    elif page == "me":
        profile()
    else:
        not_found()
    footer()


if __name__ == "__main__":
    main()
