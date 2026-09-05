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
.values-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-top:1.5rem}.value-card{border:1px solid var(--l);border-radius:16px;padding:1.4rem 1.2rem;background:#fff;text-align:right;min-height:170px;transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}.value-card:hover{transform:translateY(-3px);border-color:var(--p);box-shadow:0 10px 24px rgba(37,35,38,.05)}.value-icon{width:60px;height:60px;border-radius:16px;background:var(--s);color:var(--p);display:flex;align-items:center;justify-content:center;margin:0 0 1rem auto;font-size:1.65rem;font-weight:700}.value-card h3{margin:0 0 .45rem;color:var(--i)!important;font-size:1.02rem;text-align:right!important}.value-card p{margin:0;color:var(--g);font-size:.82rem;line-height:1.8;text-align:right!important}
.fgrid{display:grid;grid-template-columns:2.2fr 1fr;gap:.9rem;margin-top:1.4rem}.course{display:grid;grid-template-columns:1fr auto;align-items:center;gap:1rem}.course h3,.reviewentry h3{margin:0 0 .4rem;color:var(--p);font-weight:700}.btn{display:inline-flex;justify-content:center;align-items:center;border:1px solid var(--p);border-radius:10px;padding:.65rem 1rem;color:var(--i)!important;font-size:.82rem;background:#fff;white-space:nowrap}.btn.primary{background:var(--p);color:#fff!important}
.flourish-spotlight{background:var(--p);border-radius:22px;padding:3.2rem 1.5rem;margin:2.2rem 0;text-align:center}.flourish-spotlight .fl-name{font-size:clamp(2.8rem,7vw,5.2rem);font-weight:800;letter-spacing:.08em;color:#fff!important;margin:0 0 .35rem;direction:ltr}.flourish-spotlight .fl-tagline{font-size:clamp(1rem,2vw,1.35rem);font-weight:600;color:#fff!important;margin:0 0 1.5rem}.flourish-spotlight .fl-btn{display:inline-flex;align-items:center;justify-content:center;background:#fff;color:var(--p)!important;border:1px solid #fff;border-radius:12px;padding:.78rem 1.25rem;font-size:.86rem;font-weight:700;transition:transform .2s ease,box-shadow .2s ease}.flourish-spotlight .fl-btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(37,35,38,.12)}
.socials{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem;margin-top:1.3rem}.social{border:1px solid var(--l);border-radius:14px;padding:1rem .8rem;text-align:center;color:var(--i)!important;transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}.social:hover{transform:translateY(-2px);border-color:var(--p);box-shadow:0 8px 20px rgba(37,35,38,.05)}.social-icon{width:31px;height:31px;margin:0 auto .55rem;color:var(--p);display:flex;align-items:center;justify-content:center}.social-icon svg{width:100%;height:100%;display:block;fill:currentColor}.social b{display:block;font-size:.78rem;margin:.2rem}.social small{display:block;color:var(--g);font-size:.65rem;direction:ltr}
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

def pubs(course_slug):
    if not ready():return []
    r=requests.get(
        f"{URL}/rest/v1/tot_feedback",
        headers=H(ANON),
        params={
            "select":"id,name,overall,best_part,submitted_at",
            "course_slug":f"eq.{course_slug}",
            "consent_public":"eq.true",
            "approved_public":"eq.true",
            "order":"submitted_at.desc"
        },
        timeout=15
    )
    r.raise_for_status()
    return r.json()

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

# =========================================================
# نظام القياس والتقييم - الإضافة الوحيدة
# =========================================================

def get_assessment_form(course_id,form_type):
    r=requests.get(
        f"{URL}/rest/v1/assessment_forms",
        headers=H(SERVICE),
        params={
            "select":"id,course_id,form_type,title,description,is_active",
            "course_id":f"eq.{course_id}",
            "form_type":f"eq.{form_type}",
            "is_active":"eq.true",
            "limit":"1"
        },
        timeout=15
    )
    r.raise_for_status()
    rows=r.json()
    return rows[0] if rows else None

def get_assessment_questions(form_id):
    r=requests.get(
        f"{URL}/rest/v1/assessment_questions",
        headers=H(SERVICE),
        params={
            "select":"id,form_id,question_text,question_type,axis,options,correct_answer,points,display_order,is_required",
            "form_id":f"eq.{form_id}",
            "order":"display_order.asc"
        },
        timeout=15
    )
    r.raise_for_status()
    return r.json()

def save_assessment_submission(course_id,form_id,participant_name,answers,questions):
    score=0
    max_score=sum(float(q.get("points") or 0) for q in questions)
    answer_rows=[]
    qmap={int(q["id"]):q for q in questions}

    for qid,answer in answers.items():
        q=qmap[int(qid)]
        qtype=str(q.get("question_type") or "")
        points=float(q.get("points") or 0)
        is_correct=None
        points_earned=0
        numeric_value=None

        if qtype=="multiple_choice":
            is_correct=str(answer)==str(q.get("correct_answer"))
            points_earned=points if is_correct else 0
            score+=points_earned
        elif qtype=="scale_5":
            try:numeric_value=float(answer)
            except:numeric_value=None
        elif qtype=="yes_no" and q.get("correct_answer") is not None:
            is_correct=str(answer)==str(q.get("correct_answer"))
            points_earned=points if is_correct else 0
            score+=points_earned

        answer_rows.append({
            "question_id":int(qid),
            "answer_text":str(answer) if answer is not None else None,
            "numeric_value":numeric_value,
            "is_correct":is_correct,
            "points_earned":points_earned
        })

    percentage=(score/max_score*100) if max_score>0 else None

    payload={
        "course_id":int(course_id),
        "form_id":int(form_id),
        "participant_name":participant_name.strip(),
        "score":score if max_score>0 else None,
        "max_score":max_score if max_score>0 else None,
        "percentage":round(percentage,2) if percentage is not None else None
    }

    r=requests.post(
        f"{URL}/rest/v1/assessment_submissions",
        headers=H(SERVICE,"return=representation"),
        json=payload,
        timeout=15
    )
    r.raise_for_status()
    rows=r.json()
    if not rows:
        raise RuntimeError("لم يتم إنشاء سجل القياس.")

    submission_id=rows[0]["id"]
    for row in answer_rows:
        row["submission_id"]=submission_id

    if answer_rows:
        r=requests.post(
            f"{URL}/rest/v1/assessment_answers",
            headers=H(SERVICE,"return=minimal"),
            json=answer_rows,
            timeout=15
        )
        r.raise_for_status()

    return {"submission_id":submission_id,"score":score,"max_score":max_score,"percentage":percentage}

def assessment_links(course_data):
    cid=int(course_data["id"])
    slug=html.escape(str(course_data.get("slug") or ""))
    items=[]
    specs=[
        ("pre","القياس القبلي","قياس مستوى المعرفة والمهارات قبل بدء البرنامج."),
        ("post","القياس البعدي","قياس مستوى المعرفة والمهارات بعد إتمام البرنامج."),
        ("satisfaction","تقييم تجربة البرنامج","تقييم محتوى البرنامج وتجربته التدريبية.")
    ]
    for ft,title,desc in specs:
        try:
            f=get_assessment_form(cid,ft)
        except requests.RequestException:
            f=None
        if f:
            items.append(
                f'<div class="course"><div><h3>{title}</h3><p class="small">{desc}</p></div><a class="btn primary" href="?page=assessment&slug={slug}&type={ft}">فتح النموذج ←</a></div>'
            )
    if items:
        st.markdown("### القياس والتقييم")
        B(f'<div class="fgrid" style="grid-template-columns:1fr">{"".join(items)}</div>')

def assessment_page():
    slug=st.query_params.get("slug","")
    form_type=st.query_params.get("type","")

    nav()

    if form_type not in ("pre","post","satisfaction"):
        st.error("نوع النموذج غير صحيح.")
        foot()
        return

    try:
        c=get_course(slug) if slug else None
    except requests.RequestException:
        c=None

    if not c:
        st.error("تعذر العثور على الدورة.")
        foot()
        return

    B(f'<a class="back" href="?page=course&slug={html.escape(str(slug))}">← العودة إلى الدورة</a>')

    try:
        af=get_assessment_form(int(c["id"]),form_type)
    except requests.RequestException as e:
        st.error("تعذر تحميل نموذج القياس.")
        if e.response is not None: st.code(e.response.text)
        foot()
        return

    if not af:
        st.info("هذا النموذج غير متاح حاليًا.")
        foot()
        return

    try:
        questions=get_assessment_questions(int(af["id"]))
    except requests.RequestException as e:
        st.error("تعذر تحميل أسئلة النموذج.")
        if e.response is not None: st.code(e.response.text)
        foot()
        return

    B(
        f'<section class="ch"><div class="badge">FLOURISH · القياس والتقييم</div>'
        f'<h1>{html.escape(str(af.get("title") or "القياس والتقييم"))}</h1>'
        f'<p class="copy">{html.escape(str(c.get("name_ar") or "برنامج تدريبي"))}</p></section>'
    )

    if af.get("description"):
        B(f'<div class="notice">{html.escape(str(af.get("description")))}</div>')

    if form_type=="satisfaction":
        st.caption("1 = لا أوافق بشدة · 2 = لا أوافق · 3 = محايدة · 4 = أوافق · 5 = أوافق بشدة")
    else:
        st.caption("اختاري الإجابة الأدق لكل سؤال.")

    if not questions:
        st.info("لا توجد أسئلة في هذا النموذج حتى الآن.")
        foot()
        return

    version_key=f"assessment_version_{af['id']}"
    if version_key not in st.session_state:
        st.session_state[version_key]=0
    v=st.session_state[version_key]

    with st.form(f"assessment_form_{af['id']}_{v}",clear_on_submit=False):
        participant_name=st.text_input("الاسم الكامل *",max_chars=100,key=f"assess_name_{af['id']}_{v}")
        answers={}
        last_axis=None

        for q in questions:
            qid=int(q["id"])
            qtext=str(q.get("question_text") or "")
            qtype=str(q.get("question_type") or "")
            axis=str(q.get("axis") or "")

            if axis and axis!=last_axis:
                st.markdown(f"#### {axis}")
                last_axis=axis

            key=f"assess_q_{qid}_{v}"

            if qtype=="multiple_choice":
                opts=q.get("options") or []
                if not isinstance(opts,list): opts=[]
                answers[qid]=st.radio(qtext,opts,index=None,key=key)
            elif qtype=="scale_5":
                answers[qid]=st.radio(qtext,["1","2","3","4","5"],horizontal=True,index=None,key=key)
            elif qtype=="yes_no":
                answers[qid]=st.radio(qtext,["نعم","لا"],horizontal=True,index=None,key=key)
            else:
                answers[qid]=st.text_area(qtext,max_chars=1000,key=key)

        submitted=st.form_submit_button(
            "إرسال تقييم التجربة" if form_type=="satisfaction" else "إرسال القياس",
            use_container_width=True
        )

    if submitted:
        if not participant_name or len(participant_name.strip())<2:
            st.error("الاسم الكامل إلزامي.")
        else:
            missing=[]
            for q in questions:
                if not bool(q.get("is_required")): continue
                value=answers.get(int(q["id"]))
                if value is None or (isinstance(value,str) and not value.strip()):
                    missing.append(q["id"])

            if missing:
                st.error("أكملي جميع الأسئلة المطلوبة قبل الإرسال.")
            else:
                clean_answers={
                    qid:(value.strip() if isinstance(value,str) else value)
                    for qid,value in answers.items()
                    if value is not None and not (isinstance(value,str) and not value.strip())
                }
                try:
                    save_assessment_submission(
                        int(c["id"]),
                        int(af["id"]),
                        participant_name,
                        clean_answers,
                        questions
                    )
                    st.session_state[version_key]+=1
                    st.session_state[f"assessment_saved_{af['id']}"]=True
                    st.rerun()
                except requests.RequestException as e:
                    st.error("تعذر حفظ النموذج.")
                    if e.response is not None: st.code(e.response.text)
                except Exception as e:
                    st.error(f"تعذر حفظ النموذج: {e}")

    if st.session_state.pop(f"assessment_saved_{af['id']}",False):
        st.success("تم استلام النموذج بنجاح. شكرًا لمشاركتك.")
        B(f'<div style="margin-top:1rem"><a class="btn primary" href="?page=course&slug={html.escape(str(slug))}">العودة إلى صفحة الدورة ←</a></div>')

    foot()

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

def reassign_feedback(i,course_row):
    payload={
        "course_slug":str(course_row.get("slug") or ""),
        "course":str(course_row.get("name_ar") or course_row.get("course_code") or "برنامج تدريبي"),
        "course_date":str(course_row.get("course_date") or "")
    }
    r=requests.patch(
        f"{URL}/rest/v1/tot_feedback",
        headers=H(SERVICE,"return=minimal"),
        params={"id":f"eq.{i}"},
        json=payload,
        timeout=15
    )
    r.raise_for_status()

def nav():
    B("""<div class="nav"><div class="brand">MIAAD ALANAZI</div><div class="links"><a href="?page=home">الرئيسية</a><a href="#about">عني</a><a href="?page=flourish">FLOURISH</a><a href="#contact">تواصل معي</a></div></div>""")

def foot():B('<div class="foot">MIAAD ALANAZI · FLOURISH </div>')

def home():
    nav()
    B("""<section class="hero"><div class="hc"><div class="hello">هنا، أشارك رحلةً تنمو بالمعرفة وتزدهر بالأثر</div><h1>ميعاد العنزي</h1><div class="roles">هندسة البرمجيات • الأمن السيبراني • التدريب والتطوير المهني</div><p class="copy"></p></div></section>""")

    B("""<section class="sec" id="about"><div class="kick">نبذة عني</div><h2 class="title">أسعى لأن يكون لكل خطوة قيمة، ولكل تجربة أثر</h2><p class="copy">أرى مسيرتي المهنية رحلةً مستمرة من التعلّم والبناء والتطوير. أهتم بصناعة عملٍ مدروس يبدأ بفهم حقيقي، ويتشكل بوضوح، ويتطور بالتجربة والقياس. أبحث دائمًا عمّا يضيف قيمة، وأؤمن بأن أفضل النتائج هي التي لا تنتهي عند الإنجاز، بل تفتح مساحةً لما هو أفضل.</p><div class="values-grid"><div class="value-card"><div class="value-icon">✦</div><h3>الإتقان</h3><p>أن يستحق العمل أن يحمل اسمي.</p></div><div class="value-card"><div class="value-icon">◇</div><h3>التعلّم</h3><p>أن أبقى في مساحة نمو مستمر.</p></div><div class="value-card"><div class="value-icon">◎</div><h3>الأصالة</h3><p>أن يكون لما أقدمه هويته وقيمته.</p></div><div class="value-card"><div class="value-icon">↗</div><h3>الأثر</h3><p>أن يتجاوز الإنجاز لحظته ويترك قيمة.</p></div></div></section>""")
    B("""<section class="flourish-spotlight"><div class="fl-name">FLOURISH</div><div class="fl-tagline">التطوير المهني، بهوية واضحة</div><a class="fl-btn" href="?page=flourish">استكشف FLOURISH ←</a></section>""")
    B("""<section class="sec" id="contact"><div class="kick">تواصل معي</div><h2 class="title">حساباتي وقنوات التواصل</h2><div class="socials">
<a class="social" href="https://x.com/Mi19ad" target="_blank" rel="noopener"><span class="social-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77Z"/></svg></span><b>X</b><small>@Mi19ad</small></a>
<a class="social" href="https://www.tiktok.com/@Mi19ad" target="_blank" rel="noopener"><span class="social-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.176 4.017A5.97 5.97 0 0 1 15.73.613h-3.25v14.894a3.05 3.05 0 1 1-2.09-2.893V9.31a6.286 6.286 0 1 0 5.34 6.197V8.054a9.18 9.18 0 0 0 5.37 1.72V6.55a5.97 5.97 0 0 1-3.924-2.533Z"/></svg></span><b>TikTok</b><small>@Mi19ad</small></a>
<a class="social" href="https://www.linkedin.com/in/miaadalanazi" target="_blank" rel="noopener"><span class="social-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.34 7.5H2.13V21h3.21V7.5ZM3.74 2A1.86 1.86 0 1 0 3.73 5.72 1.86 1.86 0 0 0 3.74 2ZM9.63 7.5V21h3.21v-6.69c0-1.76.33-3.47 2.52-3.47 2.15 0 2.18 2.01 2.18 3.58V21h3.21v-7.74c0-4.06-2.17-5.95-5.06-5.95-2.33 0-3.38 1.28-3.96 2.18V7.5H9.63Z"/></svg></span><b>LinkedIn</b><small>miaadalanazi</small></a>
<a class="social" href="https://wa.me/966508245176" target="_blank" rel="noopener"><span class="social-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2a9.84 9.84 0 0 0-8.38 15.01L2 22l5.12-1.6A9.96 9.96 0 1 0 12.04 2Zm0 17.95a8.1 8.1 0 0 1-4.13-1.13l-.3-.18-3.04.95.98-2.96-.2-.31a7.92 7.92 0 1 1 6.69 3.63Zm4.44-5.93c-.24-.12-1.44-.71-1.66-.79-.22-.08-.38-.12-.54.12-.16.24-.62.79-.76.95-.14.16-.28.18-.52.06-.24-.12-1.03-.38-1.96-1.21-.72-.64-1.21-1.44-1.35-1.68-.14-.24-.01-.37.11-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.54-1.3-.74-1.78-.19-.47-.39-.41-.54-.42h-.46c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32.98 2.48c.12.16 1.7 2.6 4.12 3.64.58.25 1.03.4 1.38.51.58.18 1.1.16 1.52.1.46-.07 1.44-.59 1.64-1.16.2-.57.2-1.05.14-1.16-.06-.1-.22-.16-.46-.28Z"/></svg></span><b>WhatsApp</b><small>0508245176</small></a>
<a class="social" href="mailto:Miaad.alhamad@gmail.com"><span class="social-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 5 8-5v2Z"/></svg></span><b>Email</b><small>Miaad.alhamad@gmail.com</small></a>
</div></section>""");foot()

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

def show_reviews(course_slug):
    if not ready():st.info("سيظهر هذا القسم بعد ربط قاعدة البيانات.");return
    try: rows=pubs(course_slug)
    except requests.RequestException:st.warning("تعذر تحميل التقييمات الآن.");return
    if not rows:st.info("لا توجد تقييمات منشورة لهذه الدورة حتى الآن.");return
    cards=[]
    for r in rows:
        n=html.escape(str(r.get("name") or "متدربة"));t=html.escape(str(r.get("best_part") or ""));s=max(1,min(5,int(r.get("overall") or 1)));stars="★"*s+"☆"*(5-s)
        try:d=datetime.fromisoformat(str(r.get("submitted_at") or "").replace("Z","+00:00")).strftime("%d.%m.%Y")
        except:d=""
        cards.append(f'<article class="review"><div class="rtop"><strong>{n}</strong><span class="stars">{stars}</span></div><p>{t}</p><div class="date">{d}</div></article>')
    B(f'<div class="rgrid">{"".join(cards)}</div>')

def form(course_data):
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
            d={
                "name":name.strip(),
                "course":str(course_data.get("name_ar") or course_data.get("course_code") or "برنامج تدريبي"),
                "course_slug":str(course_data.get("slug") or ""),
                "course_date":str(course_data.get("course_date") or ""),
                **{k:int(x) for k,x in zip(keys,vals)},
                "best_part":best.strip(),
                "improvement":imp.strip() if imp else None,
                "additional_notes":notes.strip() if notes else None,
                "consent_public":bool(cons),
                "approved_public":False
            }
            try:
                insert(d)
                st.session_state.form_version += 1
                st.session_state.feedback_saved_message=True
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

    saved=st.session_state.pop("feedback_saved_message",False)
    if saved:
        st.query_params["view"]="reviews"
        st.success("تم استلام تقييمك بنجاح.")

    view=st.query_params.get("view","reviews")

    if view=="feedback":
        B(f'<a class="back" href="?page=course&slug={html.escape(str(c.get("slug") or ""))}">← العودة إلى آراء المتدربات</a>')
        st.markdown("### أضيفي تقييمك")
        form(c)
    else:
        # الإضافة فقط: النماذج الثلاثة أعلى آراء المتدربات
        assessment_links(c)

        st.markdown("### آراء المتدربات")
        B(f'<div style="margin:0 0 1.2rem"><a class="btn primary" style="width:100%;font-size:.95rem;padding:.82rem 1rem" href="?page=course&slug={html.escape(str(c.get("slug") or ""))}&view=feedback">أضيفي تقييمك</a></div>')
        show_reviews(str(c.get("slug") or ""))

    foot()

def tot():
    st.query_params["page"]="course"
    st.query_params["slug"]="tot-2026-08-16"
    st.rerun()

def csvdata(rows):
    if not rows:return b""
    fields=["id","name","course","course_slug","course_date","content_quality","clarity","practical_value","activities","trainer_delivery","interaction","answers","organization","environment","materials","overall","recommend","best_part","improvement","additional_notes","consent_public","approved_public","submitted_at"];b=io.StringIO();w=csv.DictWriter(b,fieldnames=fields,extrasaction="ignore");w.writeheader();[w.writerow(r) for r in rows];return b.getvalue().encode("utf-8-sig")

def admin():
    nav();B('<section class="ch"><div class="badge">PRIVATE</div><h1>لوحة الإدارة</h1><p class="copy">إدارة الدورات والتقييمات من مكان واحد.</p></section>')
    if not ADMIN or not SERVICE:
        st.error("أضيفي كلمة مرور الإدارة وService Role Key في Streamlit Secrets.")
        return

    if "ok" not in st.session_state:
        st.session_state.ok=False

    if not st.session_state.ok:
        p=st.text_input("كلمة مرور الإدارة",type="password")
        if st.button("دخول",use_container_width=True):
            if hmac.compare_digest(p,ADMIN):
                st.session_state.ok=True
                st.rerun()
            else:
                st.error("كلمة المرور غير صحيحة.")
        return

    if st.button("تسجيل الخروج"):
        st.session_state.ok=False
        st.rerun()

    if st.session_state.pop("course_saved_message",False):
        st.success("تم حفظ الدورة بنجاح.")

    course_tab,feedback_tab=st.tabs(["إدارة الدورات","التقييمات"])

    with course_tab:
        st.markdown("### إضافة دورة جديدة")

        if "course_form_version" not in st.session_state:
            st.session_state.course_form_version=0
        fv=st.session_state.course_form_version

        with st.form(f"add_course_form_{fv}",clear_on_submit=False):
            name_ar=st.text_input("اسم الدورة بالعربي *",key=f"add_name_ar_{fv}")
            name_en=st.text_input("اسم الدورة بالإنجليزي",key=f"add_name_en_{fv}")
            code=st.text_input("رمز الدورة *",placeholder="مثال: TOT",key=f"add_code_{fv}")
            course_date=st.date_input("تاريخ الدورة *",key=f"add_date_{fv}")
            description=st.text_area("نبذة مختصرة",key=f"add_desc_{fv}")
            active=st.checkbox("إظهار الدورة في الموقع",value=True,key=f"add_active_{fv}")
            save_course=st.form_submit_button("إضافة الدورة",use_container_width=True)

        if save_course:
            clean_name=name_ar.strip()
            clean_code=code.strip()
            if not clean_name:
                st.error("اسم الدورة بالعربي إلزامي.")
            elif not clean_code:
                st.error("رمز الدورة إلزامي لإنشاء رابط الدورة تلقائيًا.")
            else:
                slug_code="".join(ch.lower() if ch.isalnum() else "-" for ch in clean_code)
                slug_code="-".join(part for part in slug_code.split("-") if part)
                clean_slug=f"{slug_code}-{course_date.isoformat()}"
                payload={
                    "slug":clean_slug,
                    "name_ar":clean_name,
                    "name_en":name_en.strip() or None,
                    "course_code":clean_code,
                    "course_date":course_date.isoformat(),
                    "description":description.strip() or None,
                    "is_active":bool(active)
                }
                try:
                    add_course(payload)
                    st.session_state.course_form_version += 1
                    st.session_state.course_saved_message=True
                    st.rerun()
                except requests.RequestException as e:
                    st.error("تعذر إضافة الدورة. بقيت جميع البيانات كما هي لتتمكني من تعديل الخطأ.")
                    if e.response is not None:
                        try:
                            err=e.response.json()
                            msg=str(err.get("message") or "")
                            if "duplicate key" in msg.lower() or "unique" in msg.lower():
                                st.info("يوجد بالفعل رابط دورة بنفس رمز الدورة والتاريخ. غيّري الرمز أو التاريخ.")
                            else:
                                st.code(e.response.text)
                        except:
                            st.code(e.response.text)

        st.caption("الرابط المختصر يُنشأ تلقائيًا من رمز الدورة + تاريخها، ولا تحتاجين إلى كتابته.")

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
            cslug=str(c.get("slug") or "")

            try:
                current_date=datetime.fromisoformat(str(c.get("course_date"))).date()
            except:
                current_date=datetime.now().date()

            with st.container(border=True):
                st.markdown(f"#### {cname}")
                meta_parts=[str(c.get("course_date") or "")]
                if c.get("course_code"):
                    meta_parts.append(str(c.get("course_code")))
                st.caption(" · ".join(x for x in meta_parts if x))
                if c.get("description"):
                    st.write(c.get("description"))

                with st.expander("تحرير الدورة"):
                    with st.form(f"edit_course_{cid}",clear_on_submit=False):
                        edit_name_ar=st.text_input(
                            "اسم الدورة بالعربي *",
                            value=str(c.get("name_ar") or ""),
                            key=f"edit_name_ar_{cid}"
                        )
                        edit_name_en=st.text_input(
                            "اسم الدورة بالإنجليزي",
                            value=str(c.get("name_en") or ""),
                            key=f"edit_name_en_{cid}"
                        )
                        edit_code=st.text_input(
                            "رمز الدورة *",
                            value=str(c.get("course_code") or ""),
                            key=f"edit_code_{cid}"
                        )
                        edit_date=st.date_input(
                            "تاريخ الدورة *",
                            value=current_date,
                            key=f"edit_date_{cid}"
                        )
                        edit_desc=st.text_area(
                            "نبذة مختصرة",
                            value=str(c.get("description") or ""),
                            key=f"edit_desc_{cid}"
                        )
                        edit_active=st.checkbox(
                            "إظهار الدورة في الموقع",
                            value=cactive,
                            key=f"edit_active_{cid}"
                        )
                        save_edit=st.form_submit_button("حفظ التعديلات",use_container_width=True)

                    if save_edit:
                        if not edit_name_ar.strip():
                            st.error("اسم الدورة بالعربي إلزامي.")
                        elif not edit_code.strip():
                            st.error("رمز الدورة إلزامي.")
                        else:
                            edit_payload={
                                "name_ar":edit_name_ar.strip(),
                                "name_en":edit_name_en.strip() or None,
                                "course_code":edit_code.strip(),
                                "course_date":edit_date.isoformat(),
                                "description":edit_desc.strip() or None,
                                "is_active":bool(edit_active)
                            }
                            try:
                                update_course(cid,edit_payload)
                                st.session_state.course_saved_message=True
                                st.rerun()
                            except requests.RequestException as e:
                                st.error("تعذر حفظ التعديلات. بقيت جميع البيانات في الخانات.")
                                if e.response is not None:
                                    st.code(e.response.text)

                    st.caption(f"الرابط الحالي: {cslug}")
                    st.caption("يبقى رابط الدورة ثابتًا عند التحرير حتى لا تتعطل الروابط السابقة.")

                col1,col2=st.columns(2)

                if col1.button(
                    "إخفاء من الموقع" if cactive else "إظهار في الموقع",
                    key=f"toggle_course_{cid}",
                    use_container_width=True
                ):
                    try:
                        update_course(cid,{"is_active":not cactive})
                        st.rerun()
                    except requests.RequestException as e:
                        st.error(f"تعذر تحديث حالة الدورة: {e}")

                if col2.button(
                    "حذف الدورة",
                    key=f"delete_course_{cid}",
                    use_container_width=True
                ):
                    st.session_state[f"confirm_delete_course_{cid}"]=True

                if st.session_state.get(f"confirm_delete_course_{cid}",False):
                    st.warning("سيتم حذف الدورة من قائمة الدورات نهائيًا. التقييمات السابقة لن تُحذف.")
                    yes,no=st.columns(2)

                    if yes.button(
                        "تأكيد الحذف",
                        key=f"yes_delete_course_{cid}",
                        use_container_width=True
                    ):
                        try:
                            delete_course(cid)
                            st.session_state.pop(f"confirm_delete_course_{cid}",None)
                            st.rerun()
                        except requests.RequestException as e:
                            st.error(f"تعذر حذف الدورة: {e}")

                    if no.button(
                        "إلغاء",
                        key=f"no_delete_course_{cid}",
                        use_container_width=True
                    ):
                        st.session_state.pop(f"confirm_delete_course_{cid}",None)
                        st.rerun()

    with feedback_tab:
        try:
            rows=alls()
            course_rows_for_feedback=admin_courses()
        except requests.RequestException as e:
            st.error(f"تعذر تحميل التقييمات: {e}")
            if e.response is not None:
                st.code(e.response.text)
            rows=[]
            course_rows_for_feedback=[]

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

            course_by_slug={str(x.get("slug") or ""):x for x in course_rows_for_feedback}
            course_labels={
                str(x.get("slug") or ""):f"{x.get('name_ar') or 'برنامج تدريبي'} · {x.get('course_date') or ''}"
                for x in course_rows_for_feedback
            }

            for r in rows:
                rid=int(r["id"])
                cons=bool(r.get("consent_public"))
                ap=bool(r.get("approved_public"))
                current_slug=str(r.get("course_slug") or "")

                with st.container(border=True):
                    st.markdown(f"### {r.get('name','')}")
                    if current_slug and current_slug in course_by_slug:
                        cc=course_by_slug[current_slug]
                        st.caption(f"{cc.get('name_ar','')} · {cc.get('course_date','')}")
                    else:
                        st.caption(f"{r.get('course','')} · {r.get('course_date','')}")
                        st.warning("هذا التقييم غير مربوط بدورة بعد.")

                    st.write(r.get("best_part") or "")
                    st.caption(f"التقييم العام: {r.get('overall','-')}/5")

                    if course_rows_for_feedback:
                        options=[""]+[str(x.get("slug") or "") for x in course_rows_for_feedback]
                        default_index=options.index(current_slug) if current_slug in options else 0
                        chosen=st.selectbox(
                            "الدورة المرتبطة بهذا التقييم",
                            options,
                            index=default_index,
                            format_func=lambda s: "— اختاري الدورة —" if not s else course_labels.get(s,s),
                            key=f"course_for_feedback_{rid}"
                        )
                        if chosen and chosen != current_slug:
                            if st.button("حفظ ربط التقييم بالدورة",key=f"save_feedback_course_{rid}",use_container_width=True):
                                try:
                                    reassign_feedback(rid,course_by_slug[chosen])
                                    st.success("تم ربط التقييم بالدورة الصحيحة.")
                                    st.rerun()
                                except requests.RequestException as e:
                                    st.error(f"تعذر ربط التقييم: {e}")

                    if cons:
                        if st.button(
                            "إلغاء النشر" if ap else "اعتماد للنشر",
                            key=f"p{rid}",
                            use_container_width=True
                        ):
                            try:
                                approve(rid,not ap)
                                st.rerun()
                            except requests.RequestException:
                                st.error("تعذر تحديث حالة النشر.")
                    else:
                        st.caption("لم توافق المتدربة على النشر.")
    foot()

page=st.query_params.get("page","home")
selected_page = {"flourish":flourish,"course":course_page,"assessment":assessment_page,"tot":tot,"admin":admin}.get(page,home)
selected_page()
