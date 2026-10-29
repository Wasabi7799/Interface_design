"""CL Taipei — bilingual Streamlit classified-site prototype."""
from __future__ import annotations

import html
import re
from datetime import date

import streamlit as st
from catalog import CATEGORIES, DISTRICTS, MAIN_CATEGORIES, MOCK_LISTINGS

st.set_page_config(page_title="CL Taipei", page_icon="CL", layout="wide")

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
    if "DATABASE_URL" not in st.secrets:
        return []
    try:
        import psycopg
        with psycopg.connect(st.secrets["DATABASE_URL"]) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, content, created_at FROM announcements_announcement ORDER BY created_at DESC LIMIT 3")
                return cursor.fetchall()
    except Exception:
        # TODO: [後端提供公告 API、可觀測性與不洩漏技術細節的錯誤回應。]
        return []

def style():
    palette={"light":["#FFFFFF","#F7F8FA","#FFFFFF","#111827","#6B7280","#E5E7EB","#2563EB","#1D4ED8","#0F766E"],"dark":["#0F1117","#161A23","#1C2230","#E8ECF4","#9AA4B8","#2B3240","#6C8CFF","#8AA3FF","#2DD4BF"]}[st.session_state["theme"]]
    names=["bg","surface","surface-elevated","text","text-muted","border","primary","primary-hover","accent"]
    token=";".join(f"--{k}:{v}" for k,v in zip(names,palette))
    st.markdown(f"""<style>:root{{{token};--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s6:24px;--s8:32px;--button-radius:10px;--card-radius:14px;--on-primary:#FFFFFF;--shadow:0 8px 24px rgba(0,0,0,.12)}}.stApp{{background:var(--bg);color:var(--text);font-family:Inter,'Noto Sans TC',system-ui,sans-serif}}.block-container{{max-width:1200px;padding-top:var(--s8)}}h1,h2,h3,p,label,span{{color:var(--text)!important}}.muted,.meta{{color:var(--text-muted)!important}}.hero{{padding:var(--s8) 0 var(--s6)}}.hero h1{{font-size:var(--s8);margin:0}}.card,.listing{{background:var(--surface);border:1px solid var(--border);border-radius:var(--card-radius);padding:var(--s4);margin:var(--s3) 0}}.card{{min-height:118px}}.card:hover{{transform:translateY(-1px);border-color:var(--primary);box-shadow:var(--shadow)}}.price{{color:var(--accent)!important;font-weight:600}}.status{{border:1px solid var(--border);padding:var(--s1) var(--s2);border-radius:999px;font-size:12px}}.footer{{border-top:1px solid var(--border);margin-top:calc(var(--s8) + var(--s4));padding-top:var(--s6);color:var(--text-muted)}}.stButton>button,.stFormSubmitButton>button{{border-radius:var(--button-radius);background:var(--primary);border-color:var(--primary);color:var(--on-primary);font-weight:600;min-height:40px}}.stButton>button:hover,.stFormSubmitButton>button:hover{{background:var(--primary-hover);border-color:var(--primary-hover)}}.stTextInput input,.stTextArea textarea,.stSelectbox [data-baseweb='select']>div{{background:var(--surface-elevated)!important;color:var(--text)!important;border-color:var(--border)!important;border-radius:var(--button-radius)!important}}#MainMenu,footer{{display:none}}@media(max-width:640px){{.block-container{{padding-left:var(--s4);padding-right:var(--s4)}}.hero h1{{font-size:var(--s6)}}}}</style>""",unsafe_allow_html=True)

def topbar():
    c=st.columns([2,4,1,1,1,1])
    with c[0]:
        if st.button("CL Taipei",help=t("home")): route(page="home")
    with c[1]:
        with st.form("quick_search"):
            q=st.text_input(t("search"),placeholder=t("search_hint"),label_visibility="collapsed")
            if st.form_submit_button(t("search")): route(page="search",q=q.strip()[:100])
    with c[2]:
        selected=st.selectbox(t("theme"),[t("light"),t("dark")],index=0 if st.session_state["theme"]=="light" else 1,label_visibility="collapsed")
        want="light" if selected==t("light") else "dark"
        if want!=st.session_state["theme"]: st.session_state["theme"]=want; route(page=str(st.query_params.get("page","home")))
    with c[3]:
        selected=st.selectbox(t("language"),[t("chinese"),t("english")],index=0 if st.session_state["lang"]=="zh-TW" else 1,label_visibility="collapsed")
        want="zh-TW" if selected==t("chinese") else "en"
        if want!=st.session_state["lang"]: st.session_state["lang"]=want; route(page=str(st.query_params.get("page","home")))
    if st.session_state["user"]:
        with c[4]:
            if st.button(t("post")): route(page="post")
        with c[5]:
            if st.button(t("account")): route(page="me")
    else:
        with c[4]:
            if st.button(t("login")): route(page="login")
        with c[5]:
            if st.button(t("register")): route(page="register")

def require_login(action,target):
    if st.session_state["user"]: return True
    st.session_state["pending"]=(action,target); st.info(t("login_required")); route(page="login"); return False
def favorite(listing_id,key):
    saved=listing_id in st.session_state["favorites"]
    if st.button(t("unfavorite") if saved else t("favorite"),key=key):
        if require_login("favorite",listing_id):
            st.session_state["favorites"].symmetric_difference_update({listing_id}); st.rerun()
def card(x):
    stat=t(x["status"]) if x["status"] in {"active","draft","sold","expired"} else x["status"]
    st.markdown(f"<div class='listing'><span class='status'>{html.escape(stat)}</span><h3>{html.escape(x['title'])}</h3><p class='price'>{html.escape(price(x['price']))}</p><p class='meta'>{html.escape(x['district'])} · {html.escape(x['created'])}</p></div>",unsafe_allow_html=True)
    a,b=st.columns([4,1])
    with a:
        if st.button(t("title"),key=f"open_{x['id']}"): route(page="listing",id=x["id"])
    with b: favorite(x["id"],f"fav_{x['id']}")

def home():
    st.markdown(f"<section class='hero'><h1>{html.escape(t('tagline'))}</h1><p class='muted'>{html.escape(t('intro'))}</p></section>",unsafe_allow_html=True)
    cols=st.columns(4)
    for i,(slug,en,zh,icon) in enumerate(MAIN_CATEGORIES):
        with cols[i%4]:
            main,other=(zh,en) if st.session_state["lang"]=="zh-TW" else (en,zh)
            st.markdown(f"<div class='card'><div>{icon}</div><strong>{html.escape(main)}</strong><p class='muted'>{html.escape(other)}</p><p class='meta'>{html.escape(t('count_subs',count=len(subs(slug))))}</p></div>",unsafe_allow_html=True)
            if st.button(t("browse"),key=f"cat_{slug}"): route(page="category",category=slug)
    st.header(t("latest"))
    rows=announcements()
    if not rows: st.info(t("no_announcements"))
    for title, content, created_at in rows:
        st.subheader(str(title)); st.write(str(content)); st.caption(f"{t('published')}: {created_at}")

def category_page(cat):
    if cat not in {x[0] for x in MAIN_CATEGORIES}: return not_found()
    st.caption(f"{t('home')} / {cname(cat)}"); st.header(cname(cat)); st.subheader(t("topics") if cat=="discussion-forums" else t("subcategories"))
    cols=st.columns(3)
    for i,x in enumerate(subs(cat)):
        with cols[i%3]:
            other=x["name_en"] if st.session_state["lang"]=="zh-TW" else x["name_zh"]
            st.markdown(f"<div class='card'><strong>{html.escape(cname(x['slug']))}</strong><p class='muted'>{html.escape(other)}</p></div>",unsafe_allow_html=True)
            if st.button(t("browse"),key=f"sub_{cat}_{x['slug']}"): route(page="list",category=cat,sub=x["slug"])
    if st.button(t("all_listings")): route(page="list",category=cat)

def matches(cat=None,sub=None,q="",district="",low=None,high=None):
    out=[]; needle=q.lower().strip()
    for x in all_listings():
        if cat and x["category"]!=cat or sub and x["sub"]!=sub or district and x["district"]!=district: continue
        if needle and needle not in (x["title"]+" "+x["description"]).lower(): continue
        if low is not None and (x["price"] is None or x["price"]<low): continue
        if high is not None and (x["price"] is None or x["price"]>high): continue
        out.append(x)
    return out
def listing_list(cat=None,sub=None,q=""):
    heading=" / ".join([cname(x) for x in (cat,sub) if x])
    if heading: st.caption(f"{t('home')} / {heading}")
    st.header(heading or t("search"))
    with st.form("filters"):
        c=st.columns(5); query=c[0].text_input(t("keyword"),value=q,max_chars=100); low=c[1].number_input(t("min_price"),0,9_999_999,0); high=c[2].number_input(t("max_price"),0,9_999_999,9_999_999); district=c[3].selectbox(t("district"),[t("all_districts"),*DISTRICTS]); order=c[4].selectbox(t("sort"),[t("newest"),t("price_low"),t("price_high"),t("nearest")]); submit=st.form_submit_button(t("search"))
    if submit: route(page="list",category=cat or "",sub=sub or "",q=query[:100])
    if st.button(t("clear"),key="clear"): route(page="list",category=cat or "",sub=sub or "")
    rows=matches(cat,sub,q,"" if district==t("all_districts") else district,int(low) if low else None,int(high) if high<9_999_999 else None)
    if order==t("price_low"): rows.sort(key=lambda x:x["price"] is None or x["price"])
    elif order==t("price_high"): rows.sort(key=lambda x:-(x["price"] or -1))
    else: rows.sort(key=lambda x:x["created"],reverse=True)
    st.subheader(t("results",count=len(rows)))
    if not rows: st.info(t("no_results")); st.caption(t("search_advice")); return
    for x in rows[:20]: card(x)
    if len(rows)>20: st.button(t("load_more"),disabled=True)

def detail(ident):
    x=next((row for row in all_listings() if row["id"]==ident),None)
    if not x or x["status"] in {"removed","expired"}: st.warning(t("not_available")); return
    st.caption(f"{t('home')} / {cname(x['category'])} / {cname(x['sub'])}"); st.title(x["title"])
    st.markdown(f"<p class='price'>{html.escape(price(x['price']))}</p><p class='meta'>{html.escape(t('location'))}: {html.escape(x['district'])} · {html.escape(t('published'))}: {html.escape(x['created'])} · {html.escape(t('views'))}: {x['views']}</p>",unsafe_allow_html=True)
    st.info("🖼️"); st.subheader(t("description")); st.write(x["description"]); st.subheader(t("seller")); st.write(x["seller"]); st.caption(f"{t('member_since')}: 2025")
    c=st.columns(4)
    with c[0]: favorite(x["id"],"detail_fav")
    with c[1]:
        if st.button(t("contact")) and require_login("contact",x["id"]): st.session_state["contact"]=x["id"]
    with c[2]:
        if st.button(t("share")): st.toast(t("share"))
    with c[3]:
        if st.button(t("report")) and require_login("report",x["id"]): st.session_state["report"]=x["id"]
    if st.session_state.get("contact")==x["id"]:
        with st.form("contact_form"):
            msg=st.text_area(t("contact"),placeholder=t("message_hint"),max_chars=1000)
            if st.form_submit_button(t("send")):
                if msg.strip():
                    # TODO: [後端建立 conversation、驗證不可私訊自己，並建立通知。]
                    st.success(t("message_sent")); st.session_state.pop("contact")
                else: st.error(t("form_error"))
    if st.session_state.get("report")==x["id"]:
        with st.form("report_form"):
            st.selectbox(t("report_reason"),[t("report_scam"),t("report_spam"),t("report_inappropriate"),t("report_category"),t("report_other")]); st.text_area(t("report_note"),max_chars=500)
            if st.form_submit_button(t("send")):
                # TODO: [後端限制同一使用者在 24 小時內只可檢舉同一貼文一次，並放入審核佇列。]
                st.success(t("report_sent")); st.session_state.pop("report")

def login():
    st.header(t("login"))
    with st.form("login_form"):
        email=st.text_input(t("email"),max_chars=254); password=st.text_input(t("password"),type="password",max_chars=128,help=t("password_rule")); st.checkbox(t("remember")); submit=st.form_submit_button(t("login"))
    if submit:
        # TODO: [後端以 Argon2id/bcrypt、rate limit、CSRF 與安全 session 驗證帳密；前端不得保存密碼。]
        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+",email.strip()) and len(password)>=8:
            st.session_state["user"]={"email":email.strip(),"name":email.split("@")[0]}; st.success(t("login_success")); pending=st.session_state.pop("pending")
            if pending:
                action,target=pending
                if action=="favorite": st.session_state["favorites"].add(target)
                if action in {"contact","report"}: st.session_state[action]=target
                route(page="listing",id=target)
            route(page="home")
        else: st.error(t("invalid_login"))
    if st.button(t("register")): route(page="register")
def register():
    st.header(t("register"))
    with st.form("register_form"):
        name=st.text_input(t("display_name"),max_chars=60); email=st.text_input(t("email"),max_chars=254); password=st.text_input(t("password"),type="password",max_chars=128,help=t("password_rule")); confirm=st.text_input(t("confirm_password"),type="password",max_chars=128); terms=st.checkbox(t("agree_terms")); submit=st.form_submit_button(t("register"))
    if submit:
        secure=len(password)>=8 and bool(re.search(r"[A-Za-z]",password)) and bool(re.search(r"\d",password))
        if not(name.strip() and re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+",email.strip()) and secure and terms): st.error(t("form_error"))
        elif password!=confirm: st.error(t("password_mismatch"))
        else:
            # TODO: [後端建立 users、雜湊密碼、寄送驗證信；未驗證帳號不可刊登或私訊。]
            st.success(t("register_success")); route(page="login")

def post_page():
    if not require_login("post",""): return
    st.header(t("new_listing")); parents=[x[0] for x in MAIN_CATEGORIES]
    with st.form("post_form"):
        cat=st.selectbox(t("category"),parents,format_func=cname); sub=st.selectbox(t("subcategory"),[x["slug"] for x in subs(cat)],format_func=cname); title=st.text_input(t("title"),max_chars=80,placeholder=t("title_hint")); desc=st.text_area(t("description"),max_chars=4000,placeholder=t("description_hint")); amount=st.number_input(t("price"),0,9_999_999,0); negotiable=st.checkbox(t("negotiable_check")); district=st.selectbox(t("district"),DISTRICTS); files=st.file_uploader(t("images"),type=["jpg","jpeg","png","webp"],accept_multiple_files=True); st.radio(t("contact_method"),[t("internal_message"),t("show_email")]); terms=st.checkbox(t("agree_terms")); a,b=st.columns(2); draft=a.form_submit_button(t("save_draft")); publish=b.form_submit_button(t("publish"))
    if draft or publish:
        bad=len(files)>8 or any(f.size>5*1024*1024 for f in files); valid=4<=len(title.strip())<=80 and 10<=len(desc.strip())<=4000 and terms
        if bad: st.error(t("image_error"))
        elif not valid: st.error(t("form_error"))
        else:
            record={"id":str(2000+len(st.session_state["created"])+len(st.session_state["drafts"])),"category":cat,"sub":sub,"title":title.strip(),"description":desc.strip(),"price":None if negotiable else int(amount),"district":district,"created":str(date.today()),"status":"active" if publish else "draft","seller":st.session_state["user"]["name"],"views":0}
            # TODO: [後端驗證圖片 MIME 與檔頭、重新編碼並以隨機檔名上傳。]
            if publish: st.session_state["created"].append(record); st.success(t("published_success")); route(page="listing",id=record["id"])
            else: st.session_state["drafts"].append(record); st.success(t("draft_success"))

def profile():
    if not require_login("me",""): return
    st.header(t("profile")); tabs=st.tabs([t("favorites"),t("my_listings"),t("messages"),t("notifications"),t("settings")])
    with tabs[0]:
        rows=[x for x in all_listings() if x["id"] in st.session_state["favorites"]]
        if rows:
            for x in rows: card(x)
        else: st.info(t("empty_favorites"))
    with tabs[1]:
        rows=st.session_state["created"]+st.session_state["drafts"]
        if rows:
            for x in rows: card(x)
        else: st.info(t("empty_listings"))
    with tabs[2]: st.info(t("empty_messages"))
    with tabs[3]: st.info(t("empty_notifications"))
    with tabs[4]:
        with st.form("settings_form"):
            st.text_input(t("display_name"),value=st.session_state["user"]["name"]); st.checkbox(t("email_notification"))
            if st.form_submit_button(t("save_preferences")):
                # TODO: [後端同步使用者 locale、theme、display_name 與通知偏好。]
                st.success(t("settings_saved"))
        if st.button(t("logout")):
            # TODO: [後端撤銷 server-side session 與 refresh token。]
            st.session_state["user"]=None; route(page="home")
def not_found():
    st.header(t("not_found"));
    if st.button(t("home")): route(page="home")
def main():
    init(); style(); topbar(); page=str(st.query_params.get("page","home"))
    if page=="home": home()
    elif page=="category": category_page(str(st.query_params.get("category","")))
    elif page=="list": listing_list(str(st.query_params.get("category","")) or None,str(st.query_params.get("sub","")) or None,str(st.query_params.get("q","")))
    elif page=="listing": detail(str(st.query_params.get("id","")))
    elif page=="search": listing_list(q=str(st.query_params.get("q","")))
    elif page=="login": login()
    elif page=="register": register()
    elif page=="post": post_page()
    elif page=="me": profile()
    else: not_found()
    st.markdown(f"<div class='footer'>{html.escape(t('copyright'))} · {html.escape(t('about'))} · {html.escape(t('terms'))} · {html.escape(t('privacy'))}</div>",unsafe_allow_html=True)
if __name__=="__main__": main()
