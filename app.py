import csv,hmac,html,io,textwrap
from datetime import datetime
import requests,streamlit as st

st.set_page_config(page_title="ميعاد العنزي | Miaad Alanazi",page_icon="🌸",layout="wide",initial_sidebar_state="collapsed")
PINK="#D94F8A"; SOFT="#FFF7F9"; INK="#252326"; GRAY="#777276"; LINE="#EEE9EB"

def B(x): st.markdown(textwrap.dedent(x).strip(),unsafe_allow_html=True)

B("""<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
:root{--p:#D94F8A;--s:#FFF7F9;--i:#252326;--g:#777276;--l:#EEE9EB}
html{scroll-behavior:smooth} body,.stApp{direction:rtl;text-align:right;font-family:"IBM Plex Sans Arabic","Tahoma",sans-serif!important;color:var(--i);background:#fff}
.stMarkdown,.stTextInput,.stTextArea,.stRadio,.stCheckbox,.stForm,.stTabs,.stSelectbox{direction:rtl;text-align:right}
label,p,h1,h2,h3,h4,h5,h6{direction:rtl;text-align:right}
[data-testid="stToolbar"],#MainMenu,footer{visibility:hidden}.block-container{max-width:1180px;padding-top:1rem;padding-bottom:4rem}a{text-decoration:none!important}
.nav{display:flex;align-items:center;min-height:72px;border-radius:0 0 18px 18px;margin-bottom:1.6rem;padding:0 1.4rem;background:var(--p)}
.brand{direction:ltr;font-weight:700;letter-spacing:.11em;color:#fff}.links{margin-right:auto;display:flex;gap:1.5rem;font-size:.88rem;font-weight:600}.links a{color:#fff!important}
.hero{min-height:390px;border:1px solid var(--l);border-radius:20px;margin-top:1.5rem;display:flex;align-items:center}.hc{width:100%;padding:4rem 4.2rem}.hello,.kick,.badge{color:var(--p);font-size:.8rem;font-weight:800}
.hero h1,.ch h1{color:var(--p);font-weight:700}.hero h1{font-size:clamp(3.2rem,6vw,5.4rem);margin:.4rem 0 .8rem}.roles,.copy,.meta{color:var(--g);line-height:2}.copy{max-width:850px}
.sec{padding:4.5rem 0;border-bottom:1px solid var(--l)}.title{font-size:clamp(2rem,4vw,3.4rem);margin:.25rem 0 1rem;color:var(--p);font-weight:700}
.values-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-top:1.5rem}.value-card,.course,.review,.assessment-card{border:1px solid var(--l);border-radius:16px;padding:1.2rem;background:#fff}
.value-card{min-height:150px}.value-icon{width:60px;height:60px;border-radius:16px;background:var(--s);color:var(--p);display:flex;align-items:center;justify-content:center;margin:0 0 1rem auto;font-size:1.65rem}
.fgrid{display:grid;gap:.9rem;margin-top:1.4rem}.course{display:grid;grid-template-columns:1fr auto;align-items:center;gap:1rem}.course h3{margin:0 0 .4rem;color:var(--p)}
.btn{display:inline-flex;justify-content:center;align-items:center;border:1px solid var(--p);border-radius:10px;padding:.65rem 1rem;color:var(--i)!important;background:#fff}.btn.primary{background:var(--p);color:#fff!important}
.flourish-spotlight{background:var(--p);border-radius:22px;padding:3.2rem 1.5rem;margin:2.2rem 0;text-align:center}.fl-name{font-size:clamp(2.8rem,7vw,5.2rem);font-weight:800;color:#fff!important;direction:ltr}.fl-tagline{color:#fff!important;margin-bottom:1.4rem}.fl-btn{background:#fff;color:var(--p)!important;border-radius:12px;padding:.78rem 1.25rem;font-weight:700}
.socials{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem;margin-top:1.3rem}.social{border:1px solid var(--l);border-radius:14px;padding:1rem;text-align:center;color:var(--i)!important}.social b,.social small{display:block}.social small{color:var(--g);font-size:.7rem}
.ch{padding:3rem 0;border-bottom:1px solid var(--l)}.ch h1{font-size:clamp(2.6rem,5vw,4.6rem);margin:.4rem 0 1rem}.back{color:var(--g)!important;font-size:.85rem;display:inline-block;margin:.6rem 0 1rem}
.rgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem;margin-top:1rem}.review{min-height:145px}.rtop{display:flex;justify-content:space-between}.stars{direction:ltr;color:var(--p)}.review p{color:var(--g)}.date{color:#aaa;font-size:.68rem}
.notice,.assessment-intro{border:1px solid var(--l);background:#fafafa;border-radius:12px;padding:.9rem;color:var(--g);margin-bottom:1rem}
div[data-testid="stForm"]{border:1px solid var(--l);border-radius:18px;padding:1.1rem}.stTextInput input,.stTextArea textarea{border-radius:10px!important;border:1px solid var(--l)!important}
.stButton>button,.stFormSubmitButton>button,.stDownloadButton>button{border-radius:10px!important;border:1px solid var(--p)!important;background:var(--p)!important;color:#fff!important;font-weight:700!important}
.assessment-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.5rem 0 2rem}.assessment-card{display:flex;flex-direction:column;min-height:220px}.assessment-card p{color:var(--g);line-height:1.8;flex:1}
.assessment-number{width:42px;height:42px;border-radius:12px;background:var(--s);color:var(--p);display:flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:1rem}.assessment-card h3{color:var(--i)!important}.axis-title{margin:2rem 0 .6rem;padding-bottom:.55rem;border-bottom:1px solid var(--l);color:var(--p);font-weight:700}
.foot{text-align:center;color:#999;font-size:.72rem;padding:2rem 0}
@media(max-width:850px){.links{display:none}.hc{padding:2.2rem}.values-grid{grid-template-columns:repeat(2,1fr)}.socials{grid-template-columns:repeat(2,1fr)}.rgrid,.assessment-grid{grid-template-columns:1fr}.course{grid-template-columns:1fr}}
@media(max-width:500px){.values-grid,.socials{grid-template-columns:1fr}}
</style>""")

def secret(path,default=""):
    try:
        v=st.secrets
        for k in path.split("."): v=v[k]
        return str(v)
    except: return default

URL=secret("supabase.url").rstrip("/").removesuffix("/rest/v1")
ANON=secret("supabase.anon_key"); SERVICE=secret("supabase.service_role_key"); ADMIN=secret("admin.password")
def ready(): return bool(URL and ANON)
def H(k,prefer=None):
    h={"apikey":k,"Authorization":f"Bearer {k}","Content-Type":"application/json"}
    if prefer:h["Prefer"]=prefer
    return h

def insert(d):
    r=requests.post(f"{URL}/rest/v1/tot_feedback",headers=H(ANON,"return=minimal"),json=d,timeout=15); r.raise_for_status()
def pubs(course_slug):
    if not ready(): return []
    r=requests.get(f"{URL}/rest/v1/tot_feedback",headers=H(ANON),params={"select":"id,name,overall,best_part,submitted_at","course_slug":f"eq.{course_slug}","consent_public":"eq.true","approved_public":"eq.true","order":"submitted_at.desc"},timeout=15); r.raise_for_status(); return r.json()
def alls():
    r=requests.get(f"{URL}/rest/v1/tot_feedback",headers=H(SERVICE),params={"select":"*","order":"submitted_at.desc"},timeout=15); r.raise_for_status(); return r.json()

def courses():
    if not ready(): return []
    r=requests.get(f"{URL}/rest/v1/courses",headers=H(ANON),params={"select":"id,slug,name_ar,name_en,course_code,course_date,description,is_active","is_active":"eq.true","order":"course_date.desc"},timeout=15); r.raise_for_status(); return r.json()
def get_course(slug):
    if not ready(): return None
    r=requests.get(f"{URL}/rest/v1/courses",headers=H(ANON),params={"select":"id,slug,name_ar,name_en,course_code,course_date,description,is_active","slug":f"eq.{slug}","limit":"1"},timeout=15); r.raise_for_status()
    rows=r.json(); return rows[0] if rows else None
def admin_courses():
    r=requests.get(f"{URL}/rest/v1/courses",headers=H(SERVICE),params={"select":"*","order":"course_date.desc"},timeout=15); r.raise_for_status(); return r.json()
def add_course(d):
    r=requests.post(f"{URL}/rest/v1/courses",headers=H(SERVICE,"return=minimal"),json=d,timeout=15); r.raise_for_status()
def update_course(i,d):
    r=requests.patch(f"{URL}/rest/v1/courses",headers=H(SERVICE,"return=minimal"),params={"id":f"eq.{i}"},json=d,timeout=15); r.raise_for_status()
def delete_course(i):
    r=requests.delete(f"{URL}/rest/v1/courses",headers=H(SERVICE,"return=minimal"),params={"id":f"eq.{i}"},timeout=15); r.raise_for_status()
def approve(i,v):
    r=requests.patch(f"{URL}/rest/v1/tot_feedback",headers=H(SERVICE,"return=minimal"),params={"id":f"eq.{i}"},json={"approved_public":bool(v)},timeout=15); r.raise_for_status()
def reassign_feedback(i,course_row):
    payload={"course_slug":str(course_row.get("slug") or ""),"course":str(course_row.get("name_ar") or course_row.get("course_code") or "برنامج تدريبي"),"course_date":str(course_row.get("course_date") or "")}
    r=requests.patch(f"{URL}/rest/v1/tot_feedback",headers=H(SERVICE,"return=minimal"),params={"id":f"eq.{i}"},json=payload,timeout=15); r.raise_for_status()

# ---------- Assessment ----------
def get_assessment_form(course_id,form_type):
    r=requests.get(f"{URL}/rest/v1/assessment_forms",headers=H(SERVICE),params={"select":"id,course_id,form_type,title,description,is_active","course_id":f"eq.{course_id}","form_type":f"eq.{form_type}","is_active":"eq.true","limit":"1"},timeout=15); r.raise_for_status()
    rows=r.json(); return rows[0] if rows else None
def get_assessment_questions(form_id):
    r=requests.get(f"{URL}/rest/v1/assessment_questions",headers=H(SERVICE),params={"select":"id,form_id,question_text,question_type,axis,options,correct_answer,points,display_order,is_required","form_id":f"eq.{form_id}","order":"display_order.asc"},timeout=15); r.raise_for_status(); return r.json()
def save_assessment_submission(course_id,form_id,participant_name,answers,questions):
    score=0; max_score=sum(float(q.get("points") or 0) for q in questions); answer_rows=[]
    qmap={int(q["id"]):q for q in questions}
    for qid,answer in answers.items():
        q=qmap[int(qid)]; pts=float(q.get("points") or 0); correct=None; earned=0; num=None; qtype=q.get("question_type")
        if qtype=="multiple_choice":
            correct=str(answer)==str(q.get("correct_answer")); earned=pts if correct else 0; score+=earned
        elif qtype=="scale_5":
            try:num=float(answer)
            except:num=None
        elif qtype=="yes_no" and q.get("correct_answer"):
            correct=str(answer)==str(q.get("correct_answer")); earned=pts if correct else 0; score+=earned
        answer_rows.append({"question_id":int(qid),"answer_text":str(answer) if answer is not None else None,"numeric_value":num,"is_correct":correct,"points_earned":earned})
    pct=(score/max_score*100) if max_score>0 else None
    payload={"course_id":int(course_id),"form_id":int(form_id),"participant_name":participant_name.strip(),"score":score if max_score>0 else None,"max_score":max_score if max_score>0 else None,"percentage":round(pct,2) if pct is not None else None}
    r=requests.post(f"{URL}/rest/v1/assessment_submissions",headers=H(SERVICE,"return=representation"),json=payload,timeout=15); r.raise_for_status()
    rows=r.json()
    if not rows: raise RuntimeError("لم يتم إنشاء سجل القياس.")
    sid=rows[0]["id"]
    for row in answer_rows: row["submission_id"]=sid
    if answer_rows:
        r=requests.post(f"{URL}/rest/v1/assessment_answers",headers=H(SERVICE,"return=minimal"),json=answer_rows,timeout=15); r.raise_for_status()
    return {"submission_id":sid,"score":score,"max_score":max_score,"percentage":pct}

def nav(): B('<div class="nav"><div class="brand">MIAAD ALANAZI</div><div class="links"><a href="?page=home">الرئيسية</a><a href="#about">عني</a><a href="?page=flourish">FLOURISH</a><a href="#contact">تواصل معي</a></div></div>')
def foot(): B('<div class="foot">MIAAD ALANAZI · FLOURISH</div>')

def home():
    nav()
    B('<section class="hero"><div class="hc"><div class="hello">هنا، أشارك رحلةً تنمو بالمعرفة وتزدهر بالأثر</div><h1>ميعاد العنزي</h1><div class="roles">هندسة البرمجيات • الأمن السيبراني • التدريب والتطوير المهني</div></div></section>')
    B('<section class="sec" id="about"><div class="kick">نبذة عني</div><h2 class="title">أسعى لأن يكون لكل خطوة قيمة، ولكل تجربة أثر</h2><p class="copy">أرى مسيرتي المهنية رحلةً مستمرة من التعلّم والبناء والتطوير. أهتم بصناعة عملٍ مدروس يبدأ بفهم حقيقي، ويتشكل بوضوح، ويتطور بالتجربة والقياس. أبحث دائمًا عمّا يضيف قيمة، وأؤمن بأن أفضل النتائج هي التي لا تنتهي عند الإنجاز، بل تفتح مساحةً لما هو أفضل.</p><div class="values-grid"><div class="value-card"><div class="value-icon">✦</div><h3>الإتقان</h3><p>أن يستحق العمل أن يحمل اسمي.</p></div><div class="value-card"><div class="value-icon">◇</div><h3>التعلّم</h3><p>أن أبقى في مساحة نمو مستمر.</p></div><div class="value-card"><div class="value-icon">◎</div><h3>الأصالة</h3><p>أن يكون لما أقدمه هويته وقيمته.</p></div><div class="value-card"><div class="value-icon">↗</div><h3>الأثر</h3><p>أن يتجاوز الإنجاز لحظته ويترك قيمة.</p></div></div></section>')
    B('<section class="flourish-spotlight"><div class="fl-name">FLOURISH</div><div class="fl-tagline">التطوير المهني، بهوية واضحة</div><a class="fl-btn" href="?page=flourish">استكشف FLOURISH ←</a></section>')
    B('<section class="sec" id="contact"><div class="kick">تواصل معي</div><h2 class="title">حساباتي وقنوات التواصل</h2><div class="socials"><a class="social" href="https://x.com/Mi19ad"><b>X</b><small>@Mi19ad</small></a><a class="social" href="https://www.tiktok.com/@Mi19ad"><b>TikTok</b><small>@Mi19ad</small></a><a class="social" href="https://www.linkedin.com/in/miaadalanazi"><b>LinkedIn</b><small>miaadalanazi</small></a><a class="social" href="https://wa.me/966508245176"><b>WhatsApp</b><small>0508245176</small></a><a class="social" href="mailto:Miaad.alhamad@gmail.com"><b>Email</b><small>Miaad.alhamad@gmail.com</small></a></div></section>')
    foot()

def flourish():
    nav(); B('<a class="back" href="?page=home">← العودة إلى الموقع</a>')
    B('<section class="ch"><div class="badge">FLOURISH</div><h1>البرامج والتقييمات</h1><p class="copy">مساحة تجمع البرامج التدريبية المقدمة ضمن FLOURISH والتقييمات المرتبطة بها.</p></section>')
    try: rows=courses()
    except requests.RequestException: rows=[]; st.warning("تعذر تحميل البرامج الآن.")
    if not rows: st.info("لا توجد برامج متاحة حاليًا.")
    else:
        cards=[]
        for c in rows:
            slug=html.escape(str(c.get("slug") or "")); name=html.escape(str(c.get("name_ar") or "برنامج تدريبي")); en=html.escape(str(c.get("name_en") or "")); desc=html.escape(str(c.get("description") or ""))
            try:d=datetime.fromisoformat(str(c.get("course_date"))).strftime("%d.%m.%Y")
            except:d=str(c.get("course_date") or "")
            cards.append(f'<div class="course"><div><h3>{name}</h3><div class="meta">{d}{(" · "+en) if en else ""}</div><p>{desc}</p></div><a class="btn primary" href="?page=course&slug={slug}">فتح الدورة ←</a></div>')
        B(f'<section class="sec"><div class="fgrid">{"".join(cards)}</div></section>')
    foot()

def show_reviews(course_slug):
    try: rows=pubs(course_slug)
    except requests.RequestException: st.warning("تعذر تحميل التقييمات الآن."); return
    if not rows: st.info("لا توجد تقييمات منشورة لهذه الدورة حتى الآن."); return
    cards=[]
    for r in rows:
        n=html.escape(str(r.get("name") or "متدربة")); t=html.escape(str(r.get("best_part") or "")); s=max(1,min(5,int(r.get("overall") or 1))); stars="★"*s+"☆"*(5-s)
        cards.append(f'<article class="review"><div class="rtop"><strong>{n}</strong><span class="stars">{stars}</span></div><p>{t}</p></article>')
    B(f'<div class="rgrid">{"".join(cards)}</div>')

def form(course_data):
    o=["1","2","3","4","5"]
    if "form_version" not in st.session_state: st.session_state.form_version=0
    v=st.session_state.form_version
    with st.form(f"f_{v}"):
        name=st.text_input("الاسم الكامل *",key=f"name_{v}")
        labels=["جودة المحتوى التدريبي *","وضوح الشرح وتسلسل الأفكار *","القيمة التطبيقية للبرنامج *","جودة الأنشطة والتطبيقات *","أسلوب المدربة في التقديم *","إدارة التفاعل والمشاركة *","التعامل مع الأسئلة والإجابات *","تنظيم البرنامج وإدارة الوقت *","ملاءمة البيئة التدريبية *","جودة المواد التدريبية *","التقييم العام للبرنامج *","مدى ترشيحك للبرنامج لغيرك *"]
        vals=[st.radio(x,o,horizontal=True,index=None,key=f"r{i}_{v}") for i,x in enumerate(labels)]
        best=st.text_area("ما أكثر شيء كان ذا قيمة بالنسبة لك؟ *",key=f"best_{v}"); imp=st.text_area("ما الذي تقترحين تحسينه؟",key=f"imp_{v}"); notes=st.text_area("ملاحظات إضافية",key=f"notes_{v}")
        cons=st.checkbox("أوافق على نشر اسمي وتقييمي ضمن آراء المتدربات.",key=f"cons_{v}")
        sub=st.form_submit_button("إرسال التقييم",use_container_width=True)
    if sub:
        if not name or len(name.strip())<2: st.error("الاسم الكامل إلزامي.")
        elif any(x is None for x in vals): st.error("أكملي جميع عناصر التقييم.")
        elif not best or len(best.strip())<3: st.error("أجيبي عن سؤال أكثر شيء كان ذا قيمة.")
        else:
            keys=["content_quality","clarity","practical_value","activities","trainer_delivery","interaction","answers","organization","environment","materials","overall","recommend"]
            d={"name":name.strip(),"course":str(course_data.get("name_ar") or "برنامج تدريبي"),"course_slug":str(course_data.get("slug") or ""),"course_date":str(course_data.get("course_date") or ""),**{k:int(x) for k,x in zip(keys,vals)},"best_part":best.strip(),"improvement":imp.strip() or None,"additional_notes":notes.strip() or None,"consent_public":bool(cons),"approved_public":False}
            try:
                insert(d); st.session_state.form_version+=1; st.session_state.feedback_saved_message=True; st.rerun()
            except requests.RequestException as e: st.error(f"تعذر حفظ التقييم: {e}")

def assessment_cards(c):
    cid=int(c["id"]); slug=html.escape(str(c.get("slug") or "")); cards=[]
    for n,(ft,title,desc,label) in enumerate([
        ("pre","القياس القبلي","قياس مستوى المعرفة والمهارات قبل بدء البرنامج التدريبي.","بدء القياس القبلي ←"),
        ("post","القياس البعدي","قياس مستوى المعرفة والمهارات بعد إتمام البرنامج التدريبي.","بدء القياس البعدي ←"),
        ("satisfaction","تقييم تجربة البرنامج","قياس رضا المتدربات عن محتوى البرنامج وتجربته التدريبية.","تقييم التجربة ←")
    ],1):
        try:f=get_assessment_form(cid,ft)
        except requests.RequestException:f=None
        if f: cards.append(f'<div class="assessment-card"><div class="assessment-number">0{n}</div><h3>{title}</h3><p>{desc}</p><a class="btn primary" href="?page=assessment&slug={slug}&type={ft}">{label}</a></div>')
    if cards:
        st.markdown("### القياس والتقييم")
        B(f'<div class="assessment-grid">{"".join(cards)}</div>')

def assessment_page():
    slug=st.query_params.get("slug",""); ft=st.query_params.get("type","")
    nav()
    if ft not in ("pre","post","satisfaction"): st.error("نوع النموذج غير صحيح."); foot(); return
    try:c=get_course(slug)
    except requests.RequestException:c=None
    if not c: st.error("تعذر العثور على الدورة."); foot(); return
    B(f'<a class="back" href="?page=course&slug={html.escape(slug)}">← العودة إلى الدورة</a>')
    try:f=get_assessment_form(int(c["id"]),ft)
    except requests.RequestException:f=None
    if not f: st.info("هذا النموذج غير متاح حاليًا."); foot(); return
    try:qs=get_assessment_questions(int(f["id"]))
    except requests.RequestException: st.error("تعذر تحميل الأسئلة."); foot(); return
    B(f'<section class="ch"><div class="badge">FLOURISH · القياس والتقييم</div><h1>{html.escape(str(f.get("title") or ""))}</h1><p class="copy">{html.escape(str(c.get("name_ar") or ""))}</p></section>')
    if f.get("description"): B(f'<div class="assessment-intro">{html.escape(str(f["description"]))}</div>')
    if ft=="satisfaction": st.caption("1 = لا أوافق بشدة · 5 = أوافق بشدة")
    else: st.caption("اختاري الإجابة الأدق لكل سؤال.")
    verkey=f"av_{f['id']}"; st.session_state.setdefault(verkey,0); v=st.session_state[verkey]
    with st.form(f"assessment_{f['id']}_{v}"):
        name=st.text_input("الاسم الكامل *",key=f"an_{f['id']}_{v}")
        answers={}; last_axis=None
        for q in qs:
            qid=int(q["id"]); txt=str(q.get("question_text") or ""); qt=str(q.get("question_type") or ""); axis=str(q.get("axis") or "")
            if axis and axis!=last_axis and axis!="التعليقات":
                B(f'<div class="axis-title">{html.escape(axis)}</div>'); last_axis=axis
            key=f"aq_{qid}_{v}"
            if qt=="multiple_choice":
                opts=q.get("options") if isinstance(q.get("options"),list) else []
                answers[qid]=st.radio(txt,opts,index=None,key=key)
            elif qt=="scale_5":
                answers[qid]=st.radio(txt,["1","2","3","4","5"],horizontal=True,index=None,key=key)
            elif qt=="yes_no":
                answers[qid]=st.radio(txt,["نعم","لا"],horizontal=True,index=None,key=key)
            else:
                answers[qid]=st.text_area(txt,key=key)
        sub=st.form_submit_button("إرسال القياس" if ft!="satisfaction" else "إرسال تقييم التجربة",use_container_width=True)
    if sub:
        missing=[int(q["id"]) for q in qs if q.get("is_required") and (answers.get(int(q["id"])) is None or str(answers.get(int(q["id"]))).strip()=="")]
        if not name or len(name.strip())<2: st.error("الاسم الكامل إلزامي.")
        elif missing: st.error("أكملي جميع الأسئلة المطلوبة قبل الإرسال.")
        else:
            clean={k:(v.strip() if isinstance(v,str) else v) for k,v in answers.items() if v is not None and str(v).strip()!=""}
            try:
                save_assessment_submission(int(c["id"]),int(f["id"]),name,clean,qs)
                st.session_state[verkey]+=1; st.session_state[f"as_{f['id']}"]=True; st.rerun()
            except Exception as e: st.error(f"تعذر حفظ الإجابات: {e}")
    if st.session_state.pop(f"as_{f['id']}",False):
        st.success("تم استلام النموذج بنجاح. شكرًا لمشاركتك.")
        B(f'<a class="btn primary" href="?page=course&slug={html.escape(slug)}">العودة إلى صفحة الدورة ←</a>')
    foot()

def course_page():
    slug=st.query_params.get("slug","")
    try:c=get_course(slug)
    except requests.RequestException:c=None
    if not c:
        nav(); st.error("تعذر العثور على الدورة."); foot(); return
    name=str(c.get("name_ar") or "برنامج تدريبي"); en=str(c.get("name_en") or ""); code=str(c.get("course_code") or ""); date=str(c.get("course_date") or "")
    try:d=datetime.fromisoformat(date).strftime("%d.%m.%Y")
    except:d=date
    nav(); B('<a class="back" href="?page=flourish">← العودة إلى FLOURISH</a>')
    badge="FLOURISH"+(f" · {html.escape(code)}" if code else ""); desc=html.escape(str(c.get("description") or ""))
    B(f'<section class="ch"><div class="badge">{badge}</div><h1>{html.escape(name)}</h1><p class="copy">{html.escape(d)}{(" · "+html.escape(en)) if en else ""}</p>{f"<p class=copy>{desc}</p>" if desc else ""}</section>')
    if st.session_state.pop("feedback_saved_message",False): st.success("تم استلام تقييمك بنجاح.")
    view=st.query_params.get("view","reviews")
    if view=="feedback":
        B(f'<a class="back" href="?page=course&slug={html.escape(slug)}">← العودة إلى آراء المتدربات</a>'); st.markdown("### أضيفي تقييمك"); form(c)
    else:
        assessment_cards(c)
        st.markdown("### آراء المتدربات")
        B(f'<div style="margin:0 0 1.2rem"><a class="btn primary" style="width:100%" href="?page=course&slug={html.escape(slug)}&view=feedback">أضيفي تقييمك</a></div>')
        show_reviews(slug)
    foot()

def tot():
    st.query_params["page"]="course"; st.query_params["slug"]="tot-2026-08-16"; st.rerun()

def csvdata(rows):
    if not rows:return b""
    fields=["id","name","course","course_slug","course_date","content_quality","clarity","practical_value","activities","trainer_delivery","interaction","answers","organization","environment","materials","overall","recommend","best_part","improvement","additional_notes","consent_public","approved_public","submitted_at"]
    b=io.StringIO(); w=csv.DictWriter(b,fieldnames=fields,extrasaction="ignore"); w.writeheader()
    for r in rows:w.writerow(r)
    return b.getvalue().encode("utf-8-sig")

def admin():
    nav(); B('<section class="ch"><div class="badge">PRIVATE</div><h1>لوحة الإدارة</h1><p class="copy">إدارة الدورات والتقييمات من مكان واحد.</p></section>')
    if not ADMIN or not SERVICE: st.error("أضيفي كلمة مرور الإدارة وService Role Key في Streamlit Secrets."); return
    st.session_state.setdefault("ok",False)
    if not st.session_state.ok:
        p=st.text_input("كلمة مرور الإدارة",type="password")
        if st.button("دخول",use_container_width=True):
            if hmac.compare_digest(p,ADMIN): st.session_state.ok=True; st.rerun()
            else: st.error("كلمة المرور غير صحيحة.")
        return
    if st.button("تسجيل الخروج"): st.session_state.ok=False; st.rerun()
    course_tab,feedback_tab=st.tabs(["إدارة الدورات","التقييمات"])
    with course_tab:
        st.markdown("### إضافة دورة جديدة")
        st.session_state.setdefault("course_form_version",0); fv=st.session_state.course_form_version
        with st.form(f"add_course_{fv}"):
            na=st.text_input("اسم الدورة بالعربي *"); ne=st.text_input("اسم الدورة بالإنجليزي"); code=st.text_input("رمز الدورة *"); dt=st.date_input("تاريخ الدورة *"); desc=st.text_area("نبذة مختصرة"); active=st.checkbox("إظهار الدورة في الموقع",value=True); save=st.form_submit_button("إضافة الدورة",use_container_width=True)
        if save:
            if not na.strip() or not code.strip(): st.error("اسم الدورة ورمزها إلزاميان.")
            else:
                sc="-".join(p for p in "".join(ch.lower() if ch.isalnum() else "-" for ch in code.strip()).split("-") if p); payload={"slug":f"{sc}-{dt.isoformat()}","name_ar":na.strip(),"name_en":ne.strip() or None,"course_code":code.strip(),"course_date":dt.isoformat(),"description":desc.strip() or None,"is_active":active}
                try:add_course(payload); st.success("تمت إضافة الدورة."); st.rerun()
                except requests.RequestException as e: st.error(f"تعذر إضافة الدورة: {e}")
        st.markdown("### الدورات الحالية")
        try:cr=admin_courses()
        except requests.RequestException:cr=[]
        for c in cr:
            cid=int(c["id"])
            with st.container(border=True):
                st.markdown(f"#### {c.get('name_ar','')}"); st.caption(f"{c.get('course_date','')} · {c.get('course_code','')}")
                if c.get("description"):st.write(c["description"])
                a,b=st.columns(2)
                if a.button("إخفاء من الموقع" if c.get("is_active") else "إظهار في الموقع",key=f"t{cid}",use_container_width=True):
                    update_course(cid,{"is_active":not bool(c.get("is_active"))}); st.rerun()
                if b.button("حذف الدورة",key=f"d{cid}",use_container_width=True):
                    delete_course(cid); st.rerun()
    with feedback_tab:
        try:rows=alls()
        except requests.RequestException:rows=[]
        if not rows: st.info("لا توجد تقييمات.")
        else:
            n=len(rows); pub=sum(bool(r.get("consent_public")) and bool(r.get("approved_public")) for r in rows); avg=sum(int(r.get("overall") or 0) for r in rows)/n
            a,b,c=st.columns(3); a.metric("التقييمات",n); b.metric("المنشورة",pub); c.metric("المتوسط",f"{avg:.1f}/5")
            st.download_button("تنزيل CSV",csvdata(rows),"feedback.csv","text/csv",use_container_width=True)
            for r in rows:
                rid=int(r["id"])
                with st.container(border=True):
                    st.markdown(f"### {r.get('name','')}"); st.write(r.get("best_part") or ""); st.caption(f"التقييم العام: {r.get('overall','-')}/5")
                    if r.get("consent_public"):
                        if st.button("إلغاء النشر" if r.get("approved_public") else "اعتماد للنشر",key=f"p{rid}",use_container_width=True):
                            approve(rid,not bool(r.get("approved_public"))); st.rerun()
                    else: st.caption("لم توافق المتدربة على النشر.")
    foot()

page=st.query_params.get("page","home")
{"flourish":flourish,"course":course_page,"assessment":assessment_page,"tot":tot,"admin":admin}.get(page,home)()
