"""CL Taipei OpenCode edition — 設計 Token 與全域樣式。"""
from __future__ import annotations

import streamlit as st

PALETTES = {
    "light": {
        "bg": "#F4EFE4",
        "surface": "#FBF8F0",
        "surface-elevated": "#FFFDF8",
        "text": "#1C2A24",
        "text-muted": "#6F756B",
        "border": "#DCD3C2",
        "primary": "#B4432B",
        "primary-hover": "#93341F",
        "accent": "#0F6B5C",
        "on-primary": "#FFF8EF",
        "soft": "#EAE0CE",
        "glow": "rgba(180, 67, 43, 0.16)",
        "shadow": "0 26px 60px -34px rgba(46, 40, 28, 0.5)",
    },
    "dark": {
        "bg": "#111815",
        "surface": "#17211D",
        "surface-elevated": "#1E2B25",
        "text": "#F1EADB",
        "text-muted": "#A6AC9E",
        "border": "#32423A",
        "primary": "#E58A64",
        "primary-hover": "#F2A181",
        "accent": "#6BC7B4",
        "on-primary": "#23140D",
        "soft": "#22312A",
        "glow": "rgba(229, 138, 100, 0.18)",
        "shadow": "0 26px 60px -30px rgba(0, 0, 0, 0.7)",
    },
}


def inject_theme(theme: str) -> None:
    """把目前主題的 Token 與全域 CSS 注入頁面。"""
    palette = PALETTES.get(theme, PALETTES["light"])
    tokens = ";".join(f"--{key}:{value}" for key, value in palette.items())
    scheme = "dark" if theme == "dark" else "light"
    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;700&display=swap');

:root{{{tokens};
  --font-body:'Inter','Noto Sans TC',system-ui,-apple-system,sans-serif;
  --font-display:'Fraunces','Noto Serif TC',Georgia,serif;
  --radius-sm:10px;--radius-md:16px;--radius-lg:24px;--radius-xl:32px;
  color-scheme:{scheme};
}}

html,body,.stApp{{font-family:var(--font-body);}}
.stApp,[data-testid="stAppViewContainer"]{{
  background:
    radial-gradient(1100px 560px at 8% -8%,var(--glow),transparent 62%),
    radial-gradient(900px 520px at 102% 2%,color-mix(in srgb,var(--accent) 13%,transparent),transparent 58%),
    var(--bg);
  color:var(--text);
}}
[data-testid="stMain"]{{background:transparent;}}
header[data-testid="stHeader"],#MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"]{{display:none!important;}}
.block-container{{max-width:1240px;padding:1.25rem 2rem 4rem;}}
.stApp p,.stApp label,.stApp li,.stApp small{{color:var(--text);}}
h1,h2,h3,h4,h5{{font-family:var(--font-display)!important;font-weight:600!important;letter-spacing:-.02em;color:var(--text)!important;}}
a{{color:var(--primary);}}
:focus-visible{{outline:2px solid var(--primary)!important;outline-offset:2px;}}

@keyframes rise-in{{
  from{{opacity:0;transform:translateY(16px);}}
  to{{opacity:1;transform:translateY(0);}}
}}
@keyframes hero-drift{{
  0%,100%{{background-position:0% 40%;}}
  50%{{background-position:100% 60%;}}
}}
@keyframes soft-pop{{
  0%{{transform:scale(.92);opacity:0;}}
  100%{{transform:scale(1);opacity:1;}}
}}

/* ---------- Top bar ---------- */
[class*="st-key-topbar"]{{
  border-bottom:1px solid var(--border);
  padding:.45rem 0 .7rem;margin-bottom:.6rem;
}}
[class*="st-key-topbar"] [data-testid="stForm"]{{border:0;padding:0;background:transparent;}}
[class*="st-key-topbar"] [data-baseweb="select"]>div{{
  background:transparent!important;border:1px solid var(--border)!important;
  border-radius:999px!important;min-height:38px;font-size:.84rem;
}}
[class*="st-key-topbar"] [data-testid="stWidgetLabel"] p{{font-size:.68rem!important;}}
.st-key-brand_home button{{
  background:transparent!important;border:0!important;box-shadow:none!important;
  padding:0!important;min-height:0!important;color:var(--text)!important;
  font-family:var(--font-display)!important;font-size:2rem!important;
  font-weight:700!important;letter-spacing:-.05em;
  transition:transform .2s ease,color .2s ease!important;
}}
.st-key-brand_home button::before{{
  content:"CL";font-family:var(--font-body);font-size:.74rem;font-weight:700;
  letter-spacing:.06em;background:var(--primary);color:var(--on-primary);
  border-radius:10px;padding:.4rem .55rem;margin-right:.65rem;vertical-align:middle;
  transition:transform .2s ease,background .2s ease;
}}
.st-key-brand_home button:hover{{color:var(--primary)!important;transform:translateY(-1px) scale(1.02);}}
.st-key-brand_home button:hover::before{{transform:rotate(-6deg) scale(1.06);}}
.st-key-brand_home button:focus{{box-shadow:none!important;}}

/* ---------- Hero ---------- */
.hero{{
  position:relative;isolation:isolate;overflow:hidden;
  border:1px solid var(--border);border-radius:var(--radius-xl);
  padding:clamp(2.2rem,5vw,4.8rem);margin:1rem 0 2.4rem;
  background:
    radial-gradient(700px 340px at 88% 0%,var(--glow),transparent 62%),
    linear-gradient(135deg,var(--surface) 0%,var(--soft) 100%);
  background-size:160% 160%;
  animation:rise-in .55s cubic-bezier(.2,.7,.3,1) both,hero-drift 18s ease-in-out infinite;
}}
.hero h1,.hero-lede,.hero-chips{{animation:rise-in .6s cubic-bezier(.2,.7,.3,1) both;}}
.hero h1{{animation-delay:.06s;}}
.hero-lede{{animation-delay:.12s;}}
.hero-chips{{animation-delay:.18s;}}
.hero::before{{
  content:"";position:absolute;width:430px;height:430px;right:-130px;bottom:-200px;
  border:1px solid var(--border);border-radius:50%;opacity:.75;z-index:-1;
}}
.hero::after{{
  content:"";position:absolute;width:250px;height:250px;right:-30px;bottom:-110px;
  border:1px solid var(--border);border-radius:50%;opacity:.55;z-index:-1;
}}
.hero-eyebrow{{
  margin:0 0 .5rem;text-transform:uppercase;letter-spacing:.28em;
  font-size:.7rem;font-weight:600;color:var(--primary)!important;
}}
.hero h1{{
  font-size:clamp(2.5rem,5.2vw,4.3rem);line-height:1.05;
  margin:.2rem 0 .9rem;max-width:17ch;
}}
.hero-lede{{color:var(--text-muted)!important;font-size:1.02rem;line-height:1.75;max-width:46ch;margin:0;}}
.hero-chips{{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1.7rem;}}
.chip{{
  display:inline-flex;align-items:center;gap:.4rem;
  border:1px solid var(--border);border-radius:999px;
  background:color-mix(in srgb,var(--surface-elevated) 72%,transparent);
  padding:.42rem .85rem;font-size:.78rem;color:var(--text-muted);
}}
.chip strong{{color:var(--text);font-family:var(--font-display);font-size:.92rem;}}

/* ---------- Section headings ---------- */
.section-head{{
  display:flex;justify-content:space-between;align-items:flex-end;
  gap:1rem;margin:2.4rem 0 .9rem;
  animation:rise-in .45s ease both;
}}
.section-head h2{{font-size:clamp(1.5rem,2.6vw,2rem);margin:0;line-height:1.1;}}
.section-head .section-meta{{color:var(--text-muted)!important;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;}}
.section-head .rule{{height:1px;flex:1;background:var(--border);margin-bottom:.4rem;}}

/* ---------- Category cards ---------- */
[class*="st-key-catcard"],[class*="st-key-subcard"]{{
  position:relative;overflow:hidden;
  background:var(--surface);border:1px solid var(--border)!important;
  border-radius:var(--radius-lg);padding:1.05rem 1.1rem .7rem!important;
  min-height:212px;
  transition:transform .22s cubic-bezier(.2,.7,.3,1),border-color .22s ease,box-shadow .22s ease,background .22s ease;
  animation:rise-in .5s cubic-bezier(.2,.7,.3,1) both;
}}
[class*="st-key-catcard"]:hover,[class*="st-key-catcard"]:focus-within{{
  transform:translateY(-6px) scale(1.012);border-color:var(--primary)!important;
  box-shadow:var(--shadow);background:var(--surface-elevated);
}}
[class*="st-key-catcard"]:focus-within,[class*="st-key-subcard"]:focus-within{{
  outline:2px solid var(--primary);outline-offset:3px;
}}
[class*="st-key-catcard"] [data-testid="stVerticalBlock"]{{gap:.3rem;}}
[class*="st-key-catcard"] [class*="st-key-catbtn"],
[class*="st-key-subcard"] [class*="st-key-subbtn"]{{
  position:absolute!important;inset:0!important;z-index:8;width:100%!important;height:100%!important;margin:0!important;
}}
[class*="st-key-catcard"] .stButton,[class*="st-key-subcard"] .stButton{{
  position:absolute!important;inset:0!important;z-index:8;width:100%!important;height:100%!important;margin:0!important;
}}
[class*="st-key-catcard"] .stButton button,[class*="st-key-subcard"] .stButton button{{
  width:100%!important;height:100%!important;min-height:100%!important;
  opacity:0!important;border:0!important;background:transparent!important;box-shadow:none!important;
  outline:none!important;cursor:pointer;
}}
.cat-top{{display:flex;justify-content:space-between;align-items:center;}}
.cat-num{{font-size:.7rem;letter-spacing:.2em;color:var(--text-muted);transition:color .2s ease,transform .2s ease;}}
.cat-ico{{
  width:46px;height:46px;display:grid;place-items:center;border-radius:14px;
  background:var(--soft);font-size:1.35rem;border:1px solid var(--border);
  transition:transform .28s cubic-bezier(.2,.7,.3,1),background .22s ease,border-color .22s ease;
}}
.cat-title{{font-family:var(--font-display);font-size:1.42rem;font-weight:600;margin:.55rem 0 .05rem;letter-spacing:-.02em;transition:color .2s ease,transform .22s ease;}}
.cat-en{{text-transform:uppercase;letter-spacing:.16em;font-size:.67rem;color:var(--text-muted)!important;margin:0;}}
.cat-foot{{
  margin-top:.55rem;padding-top:.55rem;border-top:1px dashed var(--border);
  color:var(--text-muted);font-size:.76rem;
  display:flex;align-items:center;justify-content:space-between;gap:.6rem;
}}
.cat-cta{{color:var(--primary);font-weight:600;white-space:nowrap;transition:transform .2s ease,letter-spacing .2s ease;}}
[class*="st-key-catcard"]:hover .cat-ico,[class*="st-key-catcard"]:focus-within .cat-ico{{
  transform:rotate(-7deg) scale(1.08);background:var(--primary);border-color:var(--primary);
}}
[class*="st-key-catcard"]:hover .cat-title,[class*="st-key-catcard"]:focus-within .cat-title{{color:var(--primary);transform:translateX(2px);}}
[class*="st-key-catcard"]:hover .cat-cta,[class*="st-key-catcard"]:focus-within .cat-cta{{transform:translateX(4px);letter-spacing:.02em;}}
[class*="st-key-catcard"]:hover .cat-num,[class*="st-key-catcard"]:focus-within .cat-num{{color:var(--primary);transform:translateY(-1px);}}
.cat-subs{{
  position:absolute;left:0;right:0;bottom:0;z-index:3;
  padding:.7rem 1.1rem .8rem;background:var(--surface-elevated);
  border-top:1px solid var(--border);box-shadow:0 -16px 30px -24px rgba(0,0,0,.45);
  transform:translateY(112%);opacity:0;
  transition:transform .32s cubic-bezier(.2,.7,.3,1),opacity .24s ease;
}}
[class*="st-key-catcard"]:hover .cat-subs,[class*="st-key-catcard"]:focus-within .cat-subs{{
  transform:translateY(0);opacity:1;
}}
.cat-subs-title{{margin:0 0 .4rem!important;font-size:.6rem!important;letter-spacing:.18em;text-transform:uppercase;color:var(--text-muted)!important;font-weight:600;}}
.cat-subs-list{{display:flex;flex-wrap:wrap;gap:.28rem;}}
.cat-subs-list span{{
  font-size:.66rem;line-height:1.2;padding:.22rem .45rem;border-radius:999px;
  border:1px solid var(--border);background:var(--soft);color:var(--text-muted);
  white-space:nowrap;
}}
[class*="st-key-subcard"]{{
  min-height:0;padding:.85rem 1rem .55rem!important;
}}
[class*="st-key-subcard"]:hover,[class*="st-key-subcard"]:focus-within{{
  transform:translateY(-4px) scale(1.015);border-color:var(--primary)!important;
  box-shadow:var(--shadow);background:var(--surface-elevated);
}}
[class*="st-key-subcard"] .cat-title{{font-size:1.05rem;margin:.45rem 0 .05rem;}}
[class*="st-key-subcard"]:hover .cat-title,[class*="st-key-subcard"]:focus-within .cat-title{{color:var(--primary);}}
[class*="st-key-subcard"] .cat-foot{{margin-top:.4rem;padding-top:.4rem;}}
[class*="st-key-subcard"]:hover .cat-cta,[class*="st-key-subcard"]:focus-within .cat-cta{{transform:translateX(4px);}}
[class*="st-key-subcard"] .cat-num{{transition:color .2s ease;}}
[class*="st-key-subcard"]:hover .cat-num,[class*="st-key-subcard"]:focus-within .cat-num{{color:var(--primary);}}

/* ---------- Generic bordered containers ---------- */
[data-testid="stVerticalBlockBorderWrapper"]{{
  background:var(--surface);border:1px solid var(--border)!important;
  border-radius:var(--radius-lg);box-shadow:none;
}}
[class*="st-key-listing"]{{
  padding:.95rem 1.05rem!important;border-radius:var(--radius-md)!important;
  transition:transform .22s cubic-bezier(.2,.7,.3,1),border-color .22s ease,box-shadow .22s ease;
  animation:rise-in .42s cubic-bezier(.2,.7,.3,1) both;
}}
[class*="st-key-listing"]:hover{{transform:translateY(-3px);border-color:var(--primary)!important;box-shadow:var(--shadow);}}
[class*="st-key-listing"] [data-testid="stVerticalBlock"]{{gap:.3rem;}}

/* ---------- Listing cards ---------- */
.thumb{{
  width:78px;height:78px;display:grid;place-items:center;border-radius:18px;
  background:var(--soft);border:1px solid var(--border);font-size:1.75rem;
  transition:transform .28s cubic-bezier(.2,.7,.3,1),background .22s ease,border-color .22s ease;
}}
[class*="st-key-listing"]:hover .thumb{{transform:scale(1.06) rotate(-3deg);background:var(--surface-elevated);border-color:var(--primary);}}
.card-topline{{display:flex;align-items:center;justify-content:space-between;gap:.6rem;margin-bottom:.05rem;}}
.views-pill{{
  display:inline-flex;align-items:center;gap:.28rem;flex:none;
  border:1px solid var(--border);border-radius:999px;background:var(--surface-elevated);
  padding:.16rem .5rem;color:var(--text-muted);font-size:.66rem;letter-spacing:.03em;
  transition:border-color .2s ease,color .2s ease,background .2s ease;
}}
.views-pill strong{{font-family:var(--font-display);font-size:.8rem;color:var(--text);line-height:1;}}
[class*="st-key-listing"]:hover .views-pill{{border-color:var(--primary);color:var(--primary);}}
[class*="st-key-listing"]:hover .views-pill strong{{color:var(--primary);}}
.listing-title{{font-family:var(--font-display);font-size:1.12rem;font-weight:600;line-height:1.35;margin:.18rem 0 .12rem;transition:color .2s ease;}}
[class*="st-key-listing"]:hover .listing-title{{color:var(--primary);}}
.price{{font-family:var(--font-display);color:var(--primary)!important;font-weight:600;font-size:1.18rem;margin:0;}}
.price-lg{{font-family:var(--font-display);color:var(--primary)!important;font-weight:600;font-size:2.05rem;line-height:1.1;margin:0;}}
.meta,.muted{{color:var(--text-muted)!important;font-size:.79rem;margin:.18rem 0;}}
.desc-snippet{{color:var(--text-muted)!important;font-size:.84rem;line-height:1.55;margin:.3rem 0 0;}}
.body-text{{line-height:1.8;font-size:.95rem;white-space:pre-wrap;}}
.badge{{
  display:inline-flex;align-items:center;gap:.35rem;border-radius:999px;
  padding:.18rem .6rem;font-size:.68rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;
  background:var(--soft);color:var(--text-muted);border:1px solid var(--border);
}}
.badge-active{{background:color-mix(in srgb,var(--accent) 14%,transparent);color:var(--accent);border-color:color-mix(in srgb,var(--accent) 35%,transparent);}}
.badge-sold,.badge-expired{{background:color-mix(in srgb,var(--primary) 13%,transparent);color:var(--primary);border-color:color-mix(in srgb,var(--primary) 32%,transparent);}}
.badge-draft{{background:var(--soft);color:var(--text-muted);}}

/* ---------- Breadcrumbs & page heads ---------- */
.crumbs{{display:flex;flex-wrap:wrap;align-items:center;gap:.45rem;color:var(--text-muted);font-size:.78rem;letter-spacing:.04em;margin:.4rem 0 1.1rem;}}
.crumbs .sep{{opacity:.45;}}
.crumbs strong{{color:var(--text);font-weight:600;}}
.st-key-crumbs{{margin:.4rem 0 1.1rem;animation:rise-in .4s ease both;}}
.st-key-crumbs [data-testid="stHorizontalBlock"]{{align-items:center!important;gap:.12rem!important;}}
.st-key-crumbs [data-testid="stMarkdownContainer"] p{{margin:0!important;}}
.st-key-crumbs .stButton button{{
  background:transparent!important;border:0!important;box-shadow:none!important;
  min-height:26px!important;padding:.1rem .38rem!important;border-radius:8px!important;
  color:var(--text-muted)!important;font-size:.78rem!important;font-weight:500;
  transition:background .16s ease,color .16s ease,transform .16s ease;
}}
.st-key-crumbs .stButton button:hover{{background:var(--soft)!important;color:var(--primary)!important;transform:translateY(-1px);}}
.st-key-crumbs .stButton:last-child button{{color:var(--text)!important;font-weight:600;}}
.st-key-crumbs .stButton:last-child button:hover{{color:var(--primary)!important;}}
.crumb-sep{{color:var(--text-muted);opacity:.45;font-size:.78rem;padding:0 .1rem;}}
.crumb-current{{color:var(--text);font-weight:600;font-size:.78rem;padding:.1rem .38rem;}}
.page-head{{display:flex;justify-content:space-between;align-items:flex-end;gap:1rem;margin-bottom:1.4rem;animation:rise-in .45s cubic-bezier(.2,.7,.3,1) both;}}
.page-head h1{{font-size:clamp(2rem,4vw,3.1rem);line-height:1.05;margin:0;}}
.page-sub{{color:var(--text-muted)!important;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;margin:.45rem 0 0;}}
.eyebrow{{text-transform:uppercase;letter-spacing:.24em;font-size:.7rem;font-weight:600;color:var(--primary)!important;margin:0 0 .35rem;}}
.count-badge{{border:1px solid var(--border);border-radius:999px;padding:.5rem .9rem;font-size:.78rem;color:var(--text-muted);white-space:nowrap;}}

/* ---------- Detail ---------- */
.detail-hero{{
  height:300px;border-radius:var(--radius-lg);border:1px solid var(--border);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.55rem;
  background:radial-gradient(420px 200px at 50% 20%,var(--glow),transparent 70%),linear-gradient(140deg,var(--surface),var(--soft));
  margin-bottom:1.3rem;animation:soft-pop .5s cubic-bezier(.2,.7,.3,1) both;
}}
.detail-hero span{{font-size:4rem;line-height:1;}}
.detail-hero small{{text-transform:uppercase;letter-spacing:.24em;font-size:.66rem;color:var(--text-muted);}}
.block-title{{font-size:1.35rem;margin:1.6rem 0 .5rem;}}
.meta-row{{display:flex;flex-wrap:wrap;gap:.55rem 1.1rem;color:var(--text-muted);font-size:.8rem;margin:.4rem 0 0;}}
.seller-row{{display:flex;align-items:center;gap:.75rem;margin:.9rem 0 .3rem;}}
.avatar{{
  width:44px;height:44px;border-radius:50%;display:grid;place-items:center;
  background:var(--primary);color:var(--on-primary);font-weight:700;font-size:.8rem;letter-spacing:.04em;flex:none;
}}
.seller-name{{font-weight:600;font-size:.9rem;margin:0;}}
.divider{{height:1px;background:var(--border);margin:.9rem 0;}}

/* ---------- Auth ---------- */
.auth-brand{{text-align:center;margin:.8rem 0 1.3rem;}}
.auth-brand .auth-mark{{
  display:inline-grid;place-items:center;width:52px;height:52px;border-radius:16px;
  background:var(--primary);color:var(--on-primary);font-weight:700;font-size:.85rem;
  letter-spacing:.05em;margin-bottom:.75rem;
}}
.auth-brand h1{{font-size:2rem;margin:0;}}
.auth-brand p{{color:var(--text-muted)!important;font-size:.85rem;margin:.35rem 0 0;}}
[class*="st-key-auth-box"]{{padding:1.3rem 1.4rem 1rem!important;}}

/* ---------- Empty state ---------- */
.empty{{
  text-align:center;padding:3rem 1.2rem;border:1px dashed var(--border);
  border-radius:var(--radius-lg);background:var(--surface);
}}
.empty .empty-ico{{font-size:2.1rem;display:block;margin-bottom:.5rem;}}
.empty h3{{margin:.2rem 0 .35rem;font-size:1.25rem;}}
.empty p{{color:var(--text-muted);font-size:.86rem;margin:0;}}

/* ---------- Footer ---------- */
.site-footer{{
  margin-top:4rem;border-top:1px solid var(--border);padding:2.2rem 0 1rem;
  display:grid;grid-template-columns:1.6fr 1fr;gap:1.6rem;
}}
.foot-brand{{display:flex;gap:.8rem;align-items:flex-start;}}
.foot-mark{{
  width:42px;height:42px;border-radius:12px;display:grid;place-items:center;
  background:var(--primary);color:var(--on-primary);font-size:.7rem;font-weight:700;letter-spacing:.05em;flex:none;
}}
.foot-brand strong{{font-family:var(--font-display);font-size:1.1rem;display:block;}}
.foot-brand p{{color:var(--text-muted)!important;font-size:.8rem;margin:.3rem 0 0;max-width:38ch;line-height:1.6;}}
.foot-links{{display:flex;flex-wrap:wrap;gap:.6rem 1.1rem;justify-content:flex-end;align-content:flex-start;}}
.foot-links span{{color:var(--text-muted);font-size:.8rem;}}
.foot-meta{{grid-column:1/-1;color:var(--text-muted);font-size:.75rem;border-top:1px dashed var(--border);padding-top:1rem;margin-top:.4rem;}}

/* ---------- Widgets ---------- */
.stButton button,.stFormSubmitButton button{{
  border-radius:999px;min-height:40px;font-weight:600;font-size:.85rem;
  background:var(--surface-elevated);color:var(--text);
  border:1px solid var(--border);box-shadow:none;
  transition:background .15s ease,color .15s ease,border-color .15s ease,transform .15s ease;
}}
.stButton button:hover,.stFormSubmitButton button:hover{{
  border-color:var(--primary);color:var(--primary);background:var(--surface-elevated);transform:translateY(-1px);
}}
.stButton button:active,.stFormSubmitButton button:active{{transform:translateY(0) scale(.97);}}
[data-testid="stBaseButton-primary"],.stButton button[kind="primary"],.stFormSubmitButton button[kind="primary"]{{
  background:var(--primary)!important;border-color:var(--primary)!important;color:var(--on-primary)!important;
}}
[data-testid="stBaseButton-primary"]:hover,.stButton button[kind="primary"]:hover,.stFormSubmitButton button[kind="primary"]:hover{{
  background:var(--primary-hover)!important;border-color:var(--primary-hover)!important;color:var(--on-primary)!important;
}}
[data-testid="stBaseButton-tertiary"],.stButton button[kind="tertiary"]{{
  background:transparent!important;border-color:transparent!important;color:var(--text-muted)!important;
  min-height:36px;padding:.2rem .4rem!important;
}}
[data-testid="stBaseButton-tertiary"]:hover,.stButton button[kind="tertiary"]:hover{{
  color:var(--primary)!important;background:var(--soft)!important;transform:none;
}}
.stTextInput input,.stNumberInput input,.stTextArea textarea{{
  background:var(--surface-elevated)!important;color:var(--text)!important;
  border:1px solid var(--border)!important;border-radius:12px!important;
  min-height:42px;font-size:.9rem;
}}
.stTextArea textarea{{min-height:96px;}}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="base-input"]{{
  background:transparent!important;border:0!important;
}}
[data-baseweb="select"]>div{{
  background:var(--surface-elevated)!important;color:var(--text)!important;
  border:1px solid var(--border)!important;border-radius:12px!important;min-height:42px;
}}
[data-baseweb="select"] svg{{fill:var(--text-muted)!important;}}
[data-baseweb="popover"] [data-baseweb="menu"],[data-baseweb="popover"] ul{{
  background:var(--surface-elevated)!important;border:1px solid var(--border)!important;border-radius:14px!important;
}}
[data-baseweb="popover"] li{{color:var(--text)!important;background:transparent!important;}}
[data-baseweb="popover"] li:hover{{background:var(--soft)!important;}}
[data-testid="stWidgetLabel"] p{{font-size:.77rem!important;letter-spacing:.05em;color:var(--text-muted)!important;font-weight:600;}}
[data-testid="stCheckbox"] label p,[data-testid="stRadio"] label p{{color:var(--text)!important;font-size:.86rem!important;}}
[data-testid="stFileUploaderDropzone"]{{
  background:var(--surface)!important;border:1px dashed var(--border)!important;border-radius:16px!important;
}}
[data-testid="stFileUploaderDropzone"] button{{
  background:var(--surface-elevated)!important;color:var(--text)!important;border:1px solid var(--border)!important;
}}
[data-testid="stForm"]{{background:transparent;border:0;padding:0;}}
[data-testid="stAlert"]{{border-radius:var(--radius-md);border:1px solid var(--border);background:var(--surface)!important;}}
[data-testid="stAlert"] p{{color:var(--text)!important;}}
[data-testid="stNumberInput"] button{{background:var(--surface)!important;color:var(--text)!important;border-color:var(--border)!important;}}
[data-testid="stSlider"]{{padding-top:.15rem;}}
[data-testid="stSlider"] [role="slider"]{{
  background:var(--primary)!important;border-color:var(--primary)!important;
  box-shadow:0 0 0 4px color-mix(in srgb,var(--primary) 18%,transparent);
  transition:transform .16s ease,box-shadow .16s ease;
}}
[data-testid="stSlider"] [role="slider"]:hover,[data-testid="stSlider"] [role="slider"]:focus{{
  transform:scale(1.12);box-shadow:0 0 0 6px color-mix(in srgb,var(--primary) 24%,transparent);
}}
[data-testid="stSlider"] [data-testid="stThumbValue"]{{color:var(--primary)!important;font-weight:600;}}
[data-testid="stSlider"] [data-testid="stSliderTickBarMin"],[data-testid="stSlider"] [data-testid="stSliderTickBarMax"]{{color:var(--text-muted)!important;}}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"]{{
  background:var(--surface);border:1px solid var(--border);border-radius:999px;
  padding:.3rem;gap:.2rem;
}}
.stTabs [data-baseweb="tab"]{{
  border-radius:999px;padding:.45rem .95rem;color:var(--text-muted);
  font-weight:600;font-size:.83rem;
}}
.stTabs [aria-selected="true"]{{background:var(--text)!important;color:var(--bg)!important;}}
.stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"]{{display:none;}}

/* ---------- Notices, tips & misc ---------- */
.notice{{display:flex;gap:1rem;align-items:flex-start;padding:.85rem 0;border-bottom:1px dashed var(--border);}}
.notice:last-child{{border-bottom:0;}}
.notice .badge{{flex:none;margin-top:.2rem;}}
.notice .listing-title{{font-size:1.02rem;margin:0 0 .2rem;}}
ul.tips{{margin:.5rem 0 0;padding-left:1.1rem;color:var(--text-muted)!important;font-size:.84rem;line-height:1.7;}}
ul.tips li{{color:var(--text-muted)!important;margin-bottom:.35rem;}}
.auth-switch{{text-align:center;color:var(--text-muted)!important;font-size:.82rem;margin:.9rem 0 .2rem;}}
.avatar-lg{{width:56px;height:56px;font-size:1rem;}}
.stButton button p,.stFormSubmitButton button p,[data-testid^="stBaseButton"] p{{color:inherit!important;}}
.stTabs [data-baseweb="tab"] p{{color:inherit!important;}}
[class*="st-key-notice-board"]{{padding:1rem 1.3rem!important;}}
[class*="st-key-post-tips"]{{padding:1.2rem 1.3rem!important;}}
[class*="st-key-filter-box"]{{padding:1.1rem 1.15rem!important;}}
[class*="st-key-detail-side"]{{padding:1.2rem 1.2rem .9rem!important;}}
[class*="st-key-profile-card"]{{padding:1rem 1.2rem!important;}}
[class*="st-key-post-form-box"]{{padding:1.2rem 1.3rem!important;}}
[class*="st-key-settings-box"]{{padding:1.1rem 1.2rem .8rem!important;}}
[class*="st-key-contact-panel"],[class*="st-key-report-panel"]{{padding:1rem 1.2rem .6rem!important;margin-top:1rem;}}
[class*="st-key-auth-box"],[class*="st-key-filter-box"],[class*="st-key-detail-side"],[class*="st-key-post-form-box"]{{
  animation:rise-in .5s cubic-bezier(.2,.7,.3,1) both;
}}

/* ---------- Cascade guards for Streamlit markdown ---------- */
html,body{{background:var(--bg)!important;color:var(--text)!important;}}
.hero-eyebrow{{font-size:.7rem!important;font-family:var(--font-body)!important;}}
.hero-lede{{font-size:1.02rem!important;}}
.cat-en{{font-size:.67rem!important;}}
.meta,.muted{{font-size:.79rem!important;}}
.desc-snippet{{font-size:.84rem!important;}}
.page-sub{{font-size:.82rem!important;}}
.section-head .section-meta{{font-size:.78rem!important;}}
.badge{{font-size:.68rem!important;}}
.chip{{font-size:.78rem!important;}}
.chip strong{{font-size:.92rem!important;}}
.cat-num{{font-size:.7rem!important;}}
.cat-foot{{font-size:.76rem!important;}}
.crumbs{{font-size:.78rem!important;}}
.count-badge{{font-size:.78rem!important;}}
.views-pill{{font-size:.66rem!important;}}
.views-pill strong{{font-size:.8rem!important;}}
.cat-subs-title{{font-size:.6rem!important;}}
.cat-subs-list span{{font-size:.66rem!important;}}
.st-key-crumbs .stButton button{{font-size:.78rem!important;}}
.crumb-sep,.crumb-current{{font-size:.78rem!important;}}
.auth-switch{{font-size:.82rem!important;}}
.foot-brand p{{font-size:.8rem!important;}}
.foot-links span{{font-size:.8rem!important;}}
.foot-meta{{font-size:.75rem!important;}}
.body-text{{font-size:.95rem!important;}}
.price{{font-size:1.18rem!important;}}
.price-lg{{font-size:2.05rem!important;}}
.empty p{{font-size:.86rem!important;}}
ul.tips{{font-size:.84rem!important;}}
.st-key-brand_home button,.st-key-brand_home button[data-testid="stBaseButton-tertiary"],.st-key-brand_home [data-testid="stBaseButton-tertiary"]{{color:var(--text)!important;}}
.st-key-brand_home button:hover,.st-key-brand_home [data-testid="stBaseButton-tertiary"]:hover{{color:var(--primary)!important;background:transparent!important;}}

/* ---------- Responsive ---------- */
@media (max-width:900px){{
  .block-container{{padding:1rem 1rem 3rem;}}
  .hero{{padding:2rem 1.35rem;border-radius:24px;}}
  .hero h1{{font-size:2.2rem;}}
  .page-head{{flex-direction:column;align-items:flex-start;}}
  .section-head{{flex-direction:column;align-items:flex-start;}}
  .site-footer{{grid-template-columns:1fr;}}
  .foot-links{{justify-content:flex-start;}}
  [class*="st-key-catcard"]{{min-height:0;}}
  [class*="st-key-topbar"] [data-testid="stHorizontalBlock"]{{flex-wrap:nowrap!important;gap:.35rem!important;}}
  [class*="st-key-topbar"] [data-testid="column"]{{min-width:0!important;width:auto!important;flex:1 1 0!important;}}
  [class*="st-key-topbar"] [data-baseweb="select"]>div{{min-height:34px!important;padding-left:.4rem!important;padding-right:.15rem!important;font-size:.75rem!important;}}
  [class*="st-key-topbar"] button{{min-height:34px!important;font-size:.76rem!important;padding:.2rem .35rem!important;}}
  .st-key-brand_home button{{font-size:1.32rem!important;}}
  .st-key-brand_home button::before{{font-size:.6rem;padding:.28rem .38rem;margin-right:.35rem;}}
  .stTextInput input{{min-height:38px!important;font-size:.82rem!important;}}
  .cat-subs{{padding:.6rem .9rem .7rem;}}
  .cat-subs-list span{{font-size:.62rem;}}
  .st-key-crumbs{{margin:.3rem 0 .8rem;}}
  [class*="st-key-catcard"]:hover,[class*="st-key-catcard"]:focus-within,
  [class*="st-key-subcard"]:hover,[class*="st-key-subcard"]:focus-within{{transform:none;}}
}}
@media (prefers-reduced-motion:reduce){{
  *{{transition:none!important;animation:none!important;}}
}}
</style>
""",
        unsafe_allow_html=True,
    )
