VERSION: FLOURISH_DASHBOARD_2026-09-01_FINAL
import csv,hmac,html,io,textwrap
from datetime import datetime
import requests,streamlit as st
st.set_page_config(page_title="ميعاد العنزي | Miaad Alanazi",page_icon="🌸",layout="wide",initial_sidebar_state="collapsed")
PINK="#D94F8A"; SOFT="#FFF7F9"; INK="#252326"; GRAY="#777276"; LINE="#EEE9EB"; DATE_AR="16 أغسطس 2026"; DATE_DB="2026-08-16"
def B(x): st.markdown(textwrap.dedent(x).strip(),unsafe_allow_html=True)
B("""<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
:root{--p:__PINK__;--s:__SOFT__;--i:__INK__;--g:__GRAY__;--l:__LINE__}html{scroll-behavior:smooth}body,.stApp{direction:rtl;text-align:right;font-family:"IBM Plex Sans Arabic","Tahoma",sans-serif!important;color:var(--i);background:#fff}.stMarkdown,.stTextInput,.stTextArea,.stRadio,.stCheckbox,.stForm,.stTabs{direction:rtl;text-align:right}ul,ol{direction:rtl;text-align:right;padding-right:1.25rem;padding-left:0}li{margin:.38rem 0;line-height:1.9}label,p,h1,h2,h3,h4,h5,h6{direction:rtl;text-align:right}[data-testid="stHeader"]{background:#fffffff2}[data-testid="stToolbar"],#MainMenu,footer{visibility:hidden}.block-container{max-width:1180px;padding-top:1rem;padding-bottom:4rem}a{text-decoration:none!important}
.nav{display:flex;align-items:center;min-height:72px;border:0;border-radius:0 0 18px 18px;margin-bottom:1.6rem;padding:0 1.4rem;background:var(--p);box-shadow:0 8px 28px rgba(233,137,165,.14)}.brand{direction:ltr;font-weight:700;letter-spacing:.11em;color:#fff}.links{margin-right:auto;display:flex;gap:1.5rem;font-size:.88rem;font-weight:600}.links a{color:#fff!important;opacity:.92}.links a:hover{color:#fff!important;opacity:1}
.hero{min-height:390px;border:1px solid var(--l);border-radius:20px;margin-top:1.5rem;background:#fff;display:flex;align-items:center}.hc{width:100%;padding:4rem 4.2rem;display:flex;flex-direction:column;justify-content:center}.hello,.kick,.badge{color:var(--p);font-size:.8rem;font-weight:800}.hero h1{font-size:clamp(3.2rem,6vw,5.4rem);margin:.4rem 0 .8rem;line-height:1;color:var(--p);font-weight:700}.roles,.copy,.meta{color:var(--g);line-height:2}.roles{font-size:.95rem}.copy{max-width:850px;font-size:1rem}.art{position:relative;background:linear-gradient(135deg,#fff,#fdf7f8);min-height:410px}.art:before{content:"";position:absolute;width:180px;height:180px;border-radius:50%;background:#f5e8ec;left:17%;top:18%}.vase{position:absolute;width:88px;height:120px;border-radius:44% 44% 32% 32%;background:#ead6dc;left:24%;top:42%}.stem{position:absolute;width:2px;height:150px;background:#a68f96;left:31%;top:16%;transform:rotate(-8deg)}.stem2{transform:rotate(11deg);height:132px;left:30%;top:21%}.flower{position:absolute;width:11px;height:11px;border-radius:50%;background:var(--p);box-shadow:18px 8px 0 #d8a8b5,-14px 18px 0 #e6bbc6,11px 30px 0 #dca6b5;left:29%;top:15%}.book{position:absolute;height:18px;border-radius:4px;left:48%;bottom:22%;width:190px;background:#f0d9df;transform:rotate(-4deg)}.book2{width:160px;background:#fff;bottom:17%;left:51%;border:1px solid var(--l)}
.sec{padding:4.5rem 0;border-bottom:1px solid var(--l)}.title{font-size:clamp(2rem,4vw,3.4rem);margin:.25rem 0 1rem;color:var(--p);font-weight:700}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-top:1.5rem}.card,.course,.reviewentry,.review{border:1px solid var(--l);border-radius:16px;padding:1.2rem;background:#fff}.card{min-height:120px}.card i{font-style:normal;color:var(--p);font-size:1.3rem}.card b{display:block;margin:.55rem 0 .25rem;font-size:.9rem}.card span,.small{color:var(--g);font-size:.78rem;line-height:1.75}
.values-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-top:1.5rem}.value-card{border:1px solid var(--l);border-radius:16px;padding:1.35rem 1.1rem;background:#fff;text-align:center;min-height:150px;transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}.value-card:hover{transform:translateY(-3px);border-color:var(--p);box-shadow:0 10px 24px rgba(37,35,38,.05)}.value-icon{width:48px;height:48px;border-radius:50%;background:var(--s);color:var(--p);display:flex;align-items:center;justify-content:center;margin:0 auto .8rem;font-size:1.25rem;font-weight:700}.value-card h3{margin:0 0 .35rem;color:var(--i)!important;font-size:.95rem;text-align:center!important}.value-card p{margin:0;color:var(--g);font-size:.78rem;line-height:1.75;text-align:center!important}
.fgrid{display:grid;grid-template-columns:2.2fr 1fr;gap:.9rem;margin-top:1.4rem}.course{display:grid;grid-template-columns:1fr auto;align-items:center;gap:1rem}.course h3,.reviewentry h3{margin:0 0 .4rem;color:var(--p);font-weight:700}.btn{display:inline-flex;justify-content:center;align-items:center;border:1px solid var(--p);border-radius:10px;padding:.65rem 1rem;color:var(--i)!important;font-size:.82rem;background:#fff;white-space:nowrap}.btn.primary{background:var(--p);color:#fff!important}
.socials{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem;margin-top:1.3rem}.social{border:1px solid var(--l);border-radius:14px;padding:.9rem;text-align:center;color:var(--i)!important}.social strong{display:block;color:var(--p);font-size:1.1rem;direction:ltr}.social b{display:block;font-size:.78rem;margin:.3rem}.social small{display:block;color:var(--g);font-size:.65rem;direction:ltr}
.ch{padding:3rem 0;border-bottom:1px solid var(--l)}.ch h1{font-size:clamp(2.6rem,5vw,4.6rem);margin:.4rem 0 1rem;color:var(--p);font-weight:700}.back{color:var(--g)!important;font-size:.85rem;display:inline-block;margin:.6rem 0 1rem}.rgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem;margin-top:1rem}.review{min-height:145px}.rtop{display:flex;justify-content:space-between}.stars{direction:ltr;color:var(--p)}.review p{color:var(--g);line-height:1.8;font-size:.88rem}.date{color:#aaa;font-size:.68rem}
.notice{border:1px solid var(--l);background:#fafafa;border-radius:12px;padding:.9rem;color:var(--g);font-size:.83rem;line-height:1.8;margin-bottom:1rem}div[data-testid="stForm"]{border:1px solid var(--l);border-radius:18px;padding:1.1rem}.stTextInput input,.stTextArea textarea{border-radius:10px!important;border:1px solid var(--l)!important}.stButton>button,.stFormSubmitButton>button,.stDownloadButton>button{border-radius:10px!important;border:1px solid var(--p)!important;background:var(--p)!important;color:#fff!important;font-weight:700!important}div[role="radiogroup"]{direction:rtl}.foot{text-align:center;color:#999;font-size:.72rem;padding:2rem 0}
@media(max-width:850px){.links{display:none}.art{min-height:250px}.hc{padding:2.2rem}.cards,.values-grid{grid-template-columns:repeat(2,1fr)}.fgrid{grid-template-columns:1fr}.socials{grid-template-columns:repeat(2,1fr)}.rgrid{grid-template-columns:1fr}.course{grid-template-columns:1fr}}@media(max-width:500px){.cards,.values-grid,.socials{grid-template-columns:1fr}}
[data-testid="stWidgetLabel"] p{text-align:right!important;width:100%}[data-baseweb="radio"]{direction:rtl!important}.stCaption{direction:rtl!important;text-align:right!important}.stMarkdown h1,.stMarkdown h2,.stMarkdown h3{color:var(--p)!important;font-family:"IBM Plex Sans Arabic","Tahoma",sans-serif!important;font-weight:700!important}[data-testid="stHeader"]{background:transparent!important}</style>""".replace("__PINK__",PINK).replace("__SOFT__",SOFT).replace("__INK__",INK).replace("__GRAY__",GRAY).replace("__LINE__",LINE))
def secret(path,default=""):
    try:
        v=st.secrets
        for k in path.split("."): v=v[k]
        return str(v)
    except: return default
URL=secret("supabase.url").rstrip("/").removesuffix("/rest/v1")
ANON=secret("supabase.anon_key")
SERVICE=secret("supabase.service_role_key")
ADMIN=secret("admin.password")
def ready(): return bool(URL and ANON)
def H(k,prefer=None):
    h={"apikey":k,"Authorization":f"Bearer {k}","Content-Type":"application/json"}
    if prefer:h["Prefer"]=prefer
    return h
def insert(d):
    r=requests.post(f"{URL}/rest/v1/tot_feedback",headers=H(ANON,"return=minimal"),json=d,timeout=15);r.raise_for_status()
def pubs():
    if not ready():return []
    r=requests.get(f"{URL}/rest/v1/tot_feedback",headers=H(ANON),params={"select":"id,name,overall,best_part,submitted_at","consent_public":"eq.true","approved_public":"eq.true","order":"submitted_at.desc"},timeout=15);r.raise_for_status();return r.json()
def alls():
    r=requests.get(f"{URL}/rest/v1/tot_feedback",headers=H(SERVICE),params={"select":"*","order":"submitted_at.desc"},timeout=15);r.raise_for_status();return r.json()
def courses():
    if not ready():return []
    r=requests.get(
        f"{URL}/rest/v1/courses",
        headers=H(ANON),
        params={
            "select":"id,slug,name_ar,name_en,course_code,course_date,description,is_active",
            "is_active":"eq.true",
            "order":"course_date.desc"
        },
        timeout=15
    )
    r.raise_for_status()
    return r.json()

def get_course(slug):
    if not ready():return None
    r=requests.get(
        f"{URL}/rest/v1/courses",
        headers=H(ANON),
        params={
            "select":"id,slug,name_ar,name_en,course_code,course_date,description,is_active",
            "slug":f"eq.{slug}",
            "limit":"1"
        },
        timeout=15
    )
    r.raise_for_status()
    rows=r.json()
    return rows[0] if rows else None
def admin_courses():
    r=requests.get(
        f"{URL}/rest/v1/courses",
        headers=H(SERVICE),
        params={"select":"*","order":"course_date.desc"},
        timeout=15
    )
    r.raise_for_status()
    return r.json()

def add_course(d):
    r=requests.post(
        f"{URL}/rest/v1/courses",
        headers=H(SERVICE,"return=minimal"),
        json=d,
        timeout=15
    )
    r.raise_for_status()

def update_course(i,d):
    r=requests.patch(
        f"{URL}/rest/v1/courses",
        headers=H(SERVICE,"return=minimal"),
        params={"id":f"eq.{i}"},
        json=d,
        timeout=15
    )
    r.raise_for_status()

def delete_course(i):
    r=requests.delete(
        f"{URL}/rest/v1/courses",
        headers=H(SERVICE,"return=minimal"),
        params={"id":f"eq.{i}"},
        timeout=15
    )
    r.raise_for_status()

def approve(i,v):
    r=requests.patch(f"{URL}/rest/v1/tot_feedback",headers=H(SERVICE,"return=minimal"),params={"id":f"eq.{i}"},json={"approved_public":bool(v)},timeout=15);r.raise_for_status()
def nav():
    B("""<div class="nav"><div class="brand">MIAAD ALANAZI</div><div class="links"><a href="?page=home">الرئيسية</a><a href="#about">عني</a><a href="?page=flourish">FLOURISH</a><a href="#contact">تواصل معي</a></div></div>""")
def foot():B('<div class="foot">MIAAD ALANAZI · FLOURISH </div>')
def home():
    nav()
    B("""<section class="hero"><div class="hc"><div class="hello">هنا، أشارك رحلةً تنمو بالمعرفة وتزدهر بالأثر</div><h1>ميعاد العنزي</h1><div class="roles">هندسة البرمجيات • الأمن السيبراني • التدريب والتطوير المهني</div><p class="copy"></p></div></section>""")
    
    B("""<section class="sec" id="about"><div class="kick">نبذة عني</div><h2 class="title">أسعى لأن يكون لكل خطوة قيمة، ولكل تجربة أثر</h2><p class="copy">أرى مسيرتي المهنية رحلةً مستمرة من التعلّم والبناء والتطوير. أهتم بصناعة عملٍ مدروس يبدأ بفهم حقيقي، ويتشكل بوضوح، ويتطور بالتجربة والقياس. أبحث دائمًا عمّا يضيف قيمة، وأؤمن بأن أفضل النتائج هي التي لا تنتهي عند الإنجاز، بل تفتح مساحةً لما هو أفضل.</p><div class="values-grid"><div class="value-card"><div class="value-icon">✦</div><h3>الإتقان</h3><p>أن يستحق العمل أن يحمل اسمي.</p></div><div class="value-card"><div class="value-icon">◇</div><h3>التعلّم</h3><p>أن أبقى في مساحة نمو مستمر.</p></div><div class="value-card"><div class="value-icon">◎</div><h3>الأصالة</h3><p>أن يكون لما أقدمه هويته وقيمته.</p></div><div class="value-card"><div class="value-icon">↗</div><h3>الأثر</h3><p>أن يتجاوز الإنجاز لحظته ويترك قيمة.</p></div></div></section>""")
    B("""<section class="sec"><div class="kick">FLOURISH</div><h2 class="title">التطوير المهني، بهوية واضحة</h2><p class="copy"></p><p><a class="btn" href="?page=flourish">الدخول إلى FLOURISH ←</a></p></section>""")
    B("""<section class="sec" id="contact"><div class="kick">تواصل معي</div><h2 class="title">حساباتي وقنوات التواصل</h2><div class="socials"><a class="social" href="https://x.com/Mi19ad" target="_blank"><strong>𝕏</strong><b>X</b><small>@Mi19ad</small></a><a class="social" href="https://www.tiktok.com/@Mi19ad" target="_blank"><strong>♪</strong><b>TikTok</b><small>@Mi19ad</small></a><a class="social" href="https://www.linkedin.com/in/miaadalanazi" target="_blank"><strong>in</strong><b>LinkedIn</b><small>miaadalanazi</small></a><a class="social" href="https://wa.me/966508245176" target="_blank"><strong>◉</strong><b>WhatsApp</b><small>0508245176</small></a><a class="social" href="#"><strong>✉</strong><b>Email</b><small>Miaad.alhamad@gmail.com</small></a></div></section>""");foot()
def flourish():
    nav();B('<a class="back" href="?page=home">← العودة إلى الموقع</a>')
    B("""<section class="ch"><div class="badge">FLOURISH</div><h1>البرامج والتقييمات</h1><p class="copy">مساحة تجمع البرامج التدريبية المقدمة ضمن FLOURISH والتقييمات المرتبطة بها.</p></section>""")
    try:
        rows=courses()
    except requests.RequestException:
        st.warning("تعذر تحميل البرامج الآن.")
        rows=[]

    if not rows:
        st.info("لا توجد برامج متاحة حاليًا.")
    else:
        cards=[]
        for c in rows:
            slug=html.escape(str(c.get("slug") or ""))
            name=html.escape(str(c.get("name_ar") or "برنامج تدريبي"))
            name_en=html.escape(str(c.get("name_en") or ""))
            desc=html.escape(str(c.get("description") or ""))
            try:
                d=datetime.fromisoformat(str(c.get("course_date"))).strftime("%d.%m.%Y")
            except:
                d=html.escape(str(c.get("course_date") or ""))
            meta=d + (f" · {name_en}" if name_en else "")
            cards.append(
                f'<div class="course"><div><h3>{name}</h3><div class="meta">{meta}</div><p class="small">{desc}</p></div><a class="btn primary" href="?page=course&slug={slug}">فتح الدورة ←</a></div>'
            )
        B(f'<section class="sec"><div class="fgrid" style="grid-template-columns:1fr">{"".join(cards)}</div></section>')
    foot()

def show_reviews():
    if not ready():st.info("سيظهر هذا القسم بعد ربط قاعدة البيانات.");return
    try: rows=pubs()
    except requests.RequestException:st.warning("تعذر تحميل التقييمات الآن.");return
    if not rows:st.info("لا توجد تقييمات منشورة حتى الآن.");return
    cards=[]
    for r in rows:
        n=html.escape(str(r.get("name") or "متدربة"));t=html.escape(str(r.get("best_part") or ""));s=max(1,min(5,int(r.get("overall") or 1)));stars="★"*s+"☆"*(5-s)
        try:d=datetime.fromisoformat(str(r.get("submitted_at") or "").replace("Z","+00:00")).strftime("%d.%m.%Y")
        except:d=""
        cards.append(f'<article class="review"><div class="rtop"><strong>{n}</strong><span class="stars">{stars}</span></div><p>{t}</p><div class="date">{d}</div></article>')
    B(f'<div class="rgrid">{"".join(cards)}</div>')
def form():
    B('<div class="notice">الاسم الكامل إلزامي</div>')
    o=["1","2","3","4","5"]

    if "form_version" not in st.session_state:
        st.session_state.form_version=0
    v=st.session_state.form_version

    with st.form(f"f_{v}",clear_on_submit=False):
        name=st.text_input("الاسم الكامل *",max_chars=100,key=f"name_{v}")
        st.caption("1 = يحتاج تحسينًا كبيرًا · 5 = ممتاز")

        labels=["جودة المحتوى التدريبي *","وضوح الشرح وتسلسل الأفكار *","القيمة التطبيقية للبرنامج *","جودة الأنشطة والتطبيقات *","أسلوب المدربة في التقديم *","إدارة التفاعل والمشاركة *","التعامل مع الأسئلة والإجابات *","تنظيم البرنامج وإدارة الوقت *","ملاءمة البيئة التدريبية *","جودة المواد التدريبية *","التقييم العام للبرنامج *","مدى ترشيحك للبرنامج لغيرك *"]
        vals=[st.radio(x,o,horizontal=True,index=None,key=f"r{i}_{v}") for i,x in enumerate(labels)]

        best=st.text_area("ما أكثر شيء كان ذا قيمة بالنسبة لك؟ *",max_chars=700,key=f"best_{v}")
        imp=st.text_area("ما الذي تقترحين تحسينه؟",max_chars=700,key=f"imp_{v}")
        notes=st.text_area("ملاحظات إضافية",max_chars=700,key=f"notes_{v}")
        cons=st.checkbox("أوافق على نشر اسمي وتقييمي ضمن آراء المتدربات.",key=f"cons_{v}")
        sub=st.form_submit_button("إرسال التقييم",use_container_width=True)

    if sub:
        if not name or len(name.strip())<2:
            st.error("الاسم الكامل إلزامي.")
        elif any(x is None for x in vals):
            st.error("أكملي جميع عناصر التقييم.")
        elif not best or len(best.strip())<3:
            st.error("أجيبي عن سؤال أكثر شيء كان ذا قيمة.")
        elif not ready():
            st.error("قاعدة البيانات غير مربوطة بعد.")
        else:
            keys=["content_quality","clarity","practical_value","activities","trainer_delivery","interaction","answers","organization","environment","materials","overall","recommend"]
            d={"name":name.strip(),"course":"TOT","course_date":DATE_DB,**{k:int(x) for k,x in zip(keys,vals)},"best_part":best.strip(),"improvement":imp.strip(),"additional_notes":notes.strip() if notes else None,"consent_public":bool(cons),"approved_public":False}
            try:
                insert(d)
                st.session_state.form_version += 1
                st.success("تم استلام تقييمك بنجاح.")
                st.rerun()
            except requests.RequestException as e:
                st.error(f"تعذر حفظ التقييم: {e}")
                if e.response is not None:
                    st.code(e.response.text)

def course_page():
    slug=st.query_params.get("slug","")
    try:
        c=get_course(slug) if slug else None
    except requests.RequestException:
        c=None

    if not c:
        nav()
        B('<a class="back" href="?page=flourish">← العودة إلى FLOURISH</a>')
        st.error("تعذر العثور على الدورة.")
        foot()
        return

    name=str(c.get("name_ar") or "برنامج تدريبي")
    name_en=str(c.get("name_en") or "")
    course_code=str(c.get("course_code") or "")
    course_date=str(c.get("course_date") or "")

    try:
        date_ar=datetime.fromisoformat(course_date).strftime("%d.%m.%Y")
    except:
        date_ar=course_date

    nav()
    B('<a class="back" href="?page=flourish">← العودة إلى FLOURISH</a>')
    badge="FLOURISH" + (f" · {html.escape(course_code)}" if course_code else "")
    subtitle=html.escape(date_ar) + (f" · {html.escape(name_en)}" if name_en else "")
    desc=html.escape(str(c.get("description") or ""))
    description_html=f'<p class="copy">{desc}</p>' if desc else ""
    B(f'<section class="ch"><div class="badge">{badge}</div><h1>{html.escape(name)}</h1><p class="copy">{subtitle}</p>{description_html}</section>')

    reviews_first=st.query_params.get("tab","")=="reviews"
    labels=["آراء المتدربات","التقييم"] if reviews_first else ["التقييم","آراء المتدربات"]
    tabs=st.tabs(labels)
    for label,tab in zip(labels,tabs):
        with tab:
            st.markdown(f"### {label}")
            if label=="آراء المتدربات":
                show_reviews()
            else:
                form()
    foot()

def tot():
    nav();B('<a class="back" href="?page=flourish">← العودة إلى FLOURISH</a>');B(f'<section class="ch"><div class="badge">FLOURISH · TOT</div><h1>برنامج إعداد المدربين (TOT)</h1><p class="copy">{DATE_AR} · صفحة التقييم وآراء المتدربات.</p></section>')
    reviews_first=st.query_params.get("tab","")=="reviews";labels=["آراء المتدربات","التقييم"] if reviews_first else ["التقييم","آراء المتدربات"]
    tabs=st.tabs(labels)
    for label,tab in zip(labels,tabs):
        with tab:
            st.markdown(f"### {label}")
            if label=="آراء المتدربات":
                show_reviews()
            else:
                form()
    foot()
def csvdata(rows):
    if not rows:return b""
    fields=["id","name","course","course_date","content_quality","clarity","practical_value","activities","trainer_delivery","interaction","answers","organization","environment","materials","overall","recommend","best_part","improvement","additional_notes","consent_public","approved_public","submitted_at"];b=io.StringIO();w=csv.DictWriter(b,fieldnames=fields,extrasaction="ignore");w.writeheader();[w.writerow(r) for r in rows];return b.getvalue().encode("utf-8-sig")
def admin():
    nav();B('<section class="ch"><div class="badge">PRIVATE</div><h1>لوحة الإدارة</h1><p class="copy">إدارة الدورات والتقييمات من مكان واحد.</p></section>')
    if not ADMIN or not SERVICE:st.error("أضيفي كلمة مرور الإدارة وService Role Key في Streamlit Secrets.");return
    if "ok" not in st.session_state:st.session_state.ok=False
    if not st.session_state.ok:
        p=st.text_input("كلمة مرور الإدارة",type="password")
        if st.button("دخول",use_container_width=True):
            if hmac.compare_digest(p,ADMIN):st.session_state.ok=True;st.rerun()
            else:st.error("كلمة المرور غير صحيحة.")
        return

    if st.button("تسجيل الخروج"):st.session_state.ok=False;st.rerun()

    course_tab,feedback_tab=st.tabs(["إدارة الدورات","التقييمات"])

    with course_tab:
        st.markdown("### إضافة دورة جديدة")
        with st.form("add_course_form",clear_on_submit=True):
            name_ar=st.text_input("اسم الدورة بالعربي *")
            name_en=st.text_input("اسم الدورة بالإنجليزي")
            code=st.text_input("رمز الدورة",placeholder="مثال: TOT")
            slug=st.text_input("الرابط المختصر *",placeholder="مثال: public-speaking-2026")
            course_date=st.date_input("تاريخ الدورة")
            description=st.text_area("وصف مختصر")
            active=st.checkbox("إظهار الدورة في الموقع",value=True)
            save_course=st.form_submit_button("إضافة الدورة",use_container_width=True)

        if save_course:
            clean_slug=slug.strip().lower().replace(" ","-")
            if not name_ar.strip():
                st.error("اسم الدورة بالعربي إلزامي.")
            elif not clean_slug:
                st.error("الرابط المختصر إلزامي.")
            else:
                payload={
                    "slug":clean_slug,
                    "name_ar":name_ar.strip(),
                    "name_en":name_en.strip() or None,
                    "course_code":code.strip() or None,
                    "course_date":course_date.isoformat(),
                    "description":description.strip() or None,
                    "is_active":bool(active)
                }
                try:
                    add_course(payload)
                    st.success("تمت إضافة الدورة بنجاح.")
                    st.rerun()
                except requests.RequestException as e:
                    st.error(f"تعذر إضافة الدورة: {e}")
                    if e.response is not None:st.code(e.response.text)

        st.markdown("### الدورات الحالية")
        try:
            course_rows=admin_courses()
        except requests.RequestException as e:
            st.error(f"تعذر تحميل الدورات: {e}")
            course_rows=[]

        if not course_rows:
            st.info("لا توجد دورات.")
        for c in course_rows:
            cid=int(c["id"])
            cname=str(c.get("name_ar") or "")
            cactive=bool(c.get("is_active"))
            with st.container(border=True):
                st.markdown(f"#### {cname}")
                st.caption(f"{c.get('course_date','')} · {c.get('course_code') or ''} · {c.get('slug','')}")
                if c.get("description"):st.write(c.get("description"))

                col1,col2=st.columns(2)
                if col1.button("إخفاء من الموقع" if cactive else "إظهار في الموقع",key=f"toggle_course_{cid}",use_container_width=True):
                    try:
                        update_course(cid,{"is_active":not cactive})
                        st.rerun()
                    except requests.RequestException as e:
                        st.error(f"تعذر تحديث الدورة: {e}")

                if col2.button("حذف الدورة",key=f"delete_course_{cid}",use_container_width=True):
                    st.session_state[f"confirm_delete_course_{cid}"]=True

                if st.session_state.get(f"confirm_delete_course_{cid}",False):
                    st.warning("سيتم حذف الدورة من قائمة الدورات نهائيًا. التقييمات السابقة لن تُحذف.")
                    yes,no=st.columns(2)
                    if yes.button("تأكيد الحذف",key=f"yes_delete_course_{cid}",use_container_width=True):
                        try:
                            delete_course(cid)
                            st.session_state.pop(f"confirm_delete_course_{cid}",None)
                            st.rerun()
                        except requests.RequestException as e:
                            st.error(f"تعذر حذف الدورة: {e}")
                    if no.button("إلغاء",key=f"no_delete_course_{cid}",use_container_width=True):
                        st.session_state.pop(f"confirm_delete_course_{cid}",None)
                        st.rerun()

    with feedback_tab:
        try:
            rows=alls()
        except requests.RequestException as e:
            st.error(f"تعذر تحميل التقييمات: {e}")
            if e.response is not None:
                st.code(e.response.text)
            rows=[]

        if not rows:
            st.info("لا توجد تقييمات.")
        else:
            n=len(rows)
            pub=sum(bool(r.get("consent_public")) and bool(r.get("approved_public")) for r in rows)
            avg=sum(int(r.get("overall") or 0) for r in rows)/n
            a,b,c=st.columns(3)
            a.metric("التقييمات",n)
            b.metric("المنشورة",pub)
            c.metric("المتوسط",f"{avg:.1f}/5")
            st.download_button("تنزيل CSV",csvdata(rows),"feedback.csv","text/csv",use_container_width=True)

            for r in rows:
                rid=int(r["id"]);cons=bool(r.get("consent_public"));ap=bool(r.get("approved_public"))
                with st.container(border=True):
                    st.markdown(f"### {r.get('name','')}")
                    st.caption(f"{r.get('course','')} · {r.get('course_date','')}")
                    st.write(r.get("best_part") or "")
                    st.caption(f"التقييم العام: {r.get('overall','-')}/5")
                    if cons:
                        if st.button("إلغاء النشر" if ap else "اعتماد للنشر",key=f"p{rid}",use_container_width=True):
                            try:approve(rid,not ap);st.rerun()
                            except requests.RequestException:st.error("تعذر تحديث حالة النشر.")
                    else:
                        st.caption("لم توافق المتدربة على النشر.")
    foot()
page=st.query_params.get("page","home")
selected_page = {"flourish":flourish,"course":course_page,"tot":tot,"admin":admin}.get(page,home)
selected_page()
