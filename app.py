import os
import html
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
@st.cache_resource
def get_firestore_db():
    if not firebase_admin._apps:
        cred = credentials.Certificate(
            dict(st.secrets["firebase"])
        )
        firebase_admin.initialize_app(cred)

    return firestore.client()

db = get_firestore_db()

try:
    docs = db.collection("resources").stream()
    resources = [doc.to_dict() for doc in docs]

    st.success(f"Connected! Loaded {len(resources)} resources.")

    for resource in resources:
        st.write(resource["title"])

except Exception as e:
    st.error(f"Firestore error: {e}")
    
# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="CampusCloud | Learn Together",
    page_icon="D:\Python\logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_MODE = os.getenv("APP_MODE", "development")

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --ink: #17203b;
    --muted: #77819a;
    --border: #e8eaf4;
    --primary: #5b5ce2;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 85% 0%, #eeedff 0%, transparent 28%),
        linear-gradient(180deg, #f8f9ff 0%, #f5f7fc 100%);
}

[data-testid="stHeader"] { background: transparent; }

.block-container {
    width: 100%;
    max-width: 1480px;
    padding: 2rem 2rem 3rem;
    box-sizing: border-box;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--ink) !important;
    letter-spacing: -0.6px;
}
h1 { font-size: 2.45rem !important; font-weight: 700 !important; }
h2 { font-size: 1.55rem !important; font-weight: 600 !important; }
h3 { font-size: 1.1rem !important; }
p, label, input, textarea, button {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* Normal content: readable dark text */
[data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] p,
[data-testid="stAppViewContainer"] [data-testid="stMarkdownContainer"] li {
    color: #4b556f;
    line-height: 1.8;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #171d3b 0%, #22274d 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #bac3e4;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
    color: #ffffff !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 11px;
    padding: 7px 10px;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,.1);
}

/* CampusCloud wordmark */
.campus-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 0 26px;
    width: 100%;
    box-sizing: border-box;
}
.campus-mark {
    display: block;
    width: 60px;
    height: 60px;
    flex: 0 0 60px;
}
.campus-wordmark { min-width: 0; }
.campus-name {
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.18rem;
    font-weight: 700;
    letter-spacing: -0.7px;
    line-height: 1.2;
    white-space: nowrap;
}
.campus-name .cloud-word { color: #8498ff !important; }
.campus-tagline {
    margin-top: 7px;
    color: #c1cbf4 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: .51rem;
    font-weight: 700;
    letter-spacing: .8px;
    white-space: nowrap;
}

/* Hero banner */
.hero {
    box-sizing: border-box;
    width: 100%;
    max-width: 100%;
    background:
        radial-gradient(circle at 90% 15%, rgba(255,255,255,.18), transparent 27%),
        linear-gradient(120deg, #292c68 0%, #5555df 55%, #8883ff 100%);
    padding: clamp(24px, 3.5vw, 40px);
    border-radius: 25px;
    margin: 5px 0 30px;
    box-shadow: 0 18px 45px rgba(73,73,190,.17);
    position: relative;
    overflow: hidden;
    isolation: isolate;
}
.hero::after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    right: -70px;
    bottom: -165px;
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 50%;
    box-shadow: 0 0 0 30px rgba(255,255,255,.06),
                0 0 0 65px rgba(255,255,255,.035);
    pointer-events: none;
    z-index: -1;
}
[data-testid="stAppViewContainer"] .hero h1,
[data-testid="stAppViewContainer"] .hero h1 *,
.hero h1 {
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: clamp(2rem, 3.3vw, 2.7rem) !important;
    line-height: 1.18 !important;
    margin: 14px 0 !important;
    overflow-wrap: anywhere;
}
[data-testid="stAppViewContainer"] .hero p,
.hero p {
    color: #eef0ff !important;
    font-size: .97rem;
    line-height: 1.8;
    max-width: 590px;
    margin-bottom: 0;
    overflow-wrap: anywhere;
}
.hero-tag {
    display: inline-block;
    color: #ffffff !important;
    background: rgba(255,255,255,.13);
    border: 1px solid rgba(255,255,255,.23);
    padding: 7px 12px;
    border-radius: 30px;
    font-size: .7rem;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Statistics cards */
.stat-card {
    background: rgba(255,255,255,.93);
    border: 1px solid #e9eafa;
    border-radius: 19px;
    padding: 20px;
    min-height: 130px;
    box-shadow: 0 6px 20px rgba(32,40,100,.035);
    transition: transform .2s ease, box-shadow .2s ease;
    box-sizing: border-box;
}
.stat-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(65,66,187,.1);
}
.stat-icon { font-size: 1.4rem; margin-bottom: 10px; }
.stat-label { color: #7b849e; font-size: .78rem; font-weight: 600; }
.stat-value {
    font-family: 'Space Grotesk', sans-serif;
    color: #272b59;
    font-size: 1.9rem;
    font-weight: 700;
    margin-top: 5px;
}

/* Resource cards */
.resource-card {
    box-sizing: border-box;
    width: 100%;
    background: linear-gradient(145deg, #ffffff, #fcfcff);
    border: 1px solid #e9eafa;
    border-radius: 19px;
    padding: 21px;
    margin-bottom: 16px;
    min-height: 225px;
    box-shadow: 0 5px 18px rgba(32,40,100,.035);
    transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.resource-card:hover {
    transform: translateY(-3px);
    border-color: #c5c6ff;
    box-shadow: 0 15px 30px rgba(65,66,187,.1);
}
.resource-icon {
    display: flex;
    width: 47px;
    height: 47px;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #eeedff, #e5e9ff);
    border: 1px solid #e0e2ff;
    border-radius: 14px;
    margin-bottom: 14px;
}
.resource-icon img { width: 28px; height: 28px; object-fit: contain; }
.resource-title {
    color: #222746;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: .98rem;
    font-weight: 800;
    line-height: 1.5;
    margin-bottom: 8px;
    overflow-wrap: anywhere;
}
.resource-desc {
    color: #7b849c;
    font-size: .82rem;
    line-height: 1.75;
    min-height: 48px;
}
.pill {
    display: inline-block;
    font-size: .68rem;
    font-weight: 700;
    color: #5556c9;
    background: #f0efff;
    border: 1px solid #e6e5ff;
    padding: 5px 9px;
    border-radius: 8px;
    margin: 0 4px 7px 0;
}
.section-note {
    color: #858da4;
    font-size: .88rem;
    margin-top: -7px;
    margin-bottom: 20px;
}

/* Inputs and buttons */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 11px;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #7778ef;
    box-shadow: 0 0 0 2px rgba(91,92,226,.12);
}
.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(110deg, #5556d9, #7372f2);
    color: #ffffff;
    border: 1px solid transparent;
    border-radius: 11px;
    padding: .65rem 1rem;
    font-weight: 700;
    box-shadow: 0 5px 13px rgba(85,86,217,.15);
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    color: #ffffff;
    box-shadow: 0 9px 20px rgba(85,86,217,.23);
    border-color: transparent;
}
div[data-testid="stForm"] {
    background: rgba(255,255,255,.95);
    padding: 25px;
    border: 1px solid #e9eafa;
    border-radius: 19px;
    box-shadow: 0 7px 24px rgba(32,40,100,.04);
}
.footer {
    border-top: 1px solid #e6e8f2;
    margin-top: 40px;
    padding-top: 22px;
    text-align: center;
    color: #929ab0;
    font-size: .78rem;
}

@media (max-width: 900px) {
    .block-container { padding: 1.3rem 1rem 2.5rem; }
    .hero { padding: 25px 22px; border-radius: 20px; }
    .hero h1 { font-size: 2rem !important; }
    .resource-card { padding: 17px; }
}

/* Fix sidebar text visibility */
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h4 {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #cbd5f1 !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #cbd5f1 !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# INLINE SVG LOGO
# Rendered with st.html, not as Markdown
# =====================================================
CAMPUSCLOUD_LOGO = """
<div class="campus-brand">
  <svg class="campus-mark" viewBox="0 0 100 85"
       xmlns="http://www.w3.org/2000/svg" role="img"
       aria-label="CampusCloud logo">
    <defs>
      <linearGradient id="campusCloudGradient" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#55C7FF"/>
        <stop offset="55%" stop-color="#3975F6"/>
        <stop offset="100%" stop-color="#7855F5"/>
      </linearGradient>
    </defs>
    <path d="M18 61 C7 61 3 51 8 42 C12 34 20 32 29 35
             C31 20 43 12 55 17 C65 20 70 28 70 37
             C83 35 93 43 91 53 C90 60 83 64 73 64 L18 64 Z"
          fill="url(#campusCloudGradient)"/>
    <path d="M20 36 L49 22 L80 36 L49 50 Z" fill="#17203B"/>
    <path d="M29 36 L49 27 L70 36 L49 45 Z" fill="#FFFFFF"/>
    <path d="M73 34 L73 48" stroke="#FFFFFF" stroke-width="2.5"
          stroke-linecap="round"/>
    <path d="M70 48 L76 48 L74 54 L72 54 Z" fill="#FFFFFF"/>
    <path d="M20 54 Q36 48 49 62 Q63 48 80 54"
          fill="none" stroke="#FFFFFF" stroke-width="3.5"
          stroke-linecap="round"/>
    <path d="M29 62 Q40 59 49 69 Q59 59 71 62"
          fill="none" stroke="#FFFFFF" stroke-width="2.7"
          stroke-linecap="round"/>
  </svg>
  <div class="campus-wordmark">
    <div class="campus-name">Campus<span class="cloud-word">Cloud</span></div>
    <div class="campus-tagline">LEARN · SHARE · GROW</div>
  </div>
</div>
"""

# =====================================================
# RESOURCE DATA
# =====================================================
DEFAULT_RESOURCES = [
    {
        "title": "Python Programming Notes",
        "subject": "Programming",
        "semester": "Semester 3",
        "kind": "Notes",
        "description": "Master Python fundamentals, loops, functions and practical examples.",
        "logo": "https://cdn.simpleicons.org/python/3776AB",
    },
    {
        "title": "Database Management Systems",
        "subject": "Database",
        "semester": "Semester 3",
        "kind": "Notes",
        "description": "Explore SQL queries, normalization and relational database design.",
        "logo": "https://cdn.simpleicons.org/mysql/4479A1",
    },
    {
        "title": "Data Structures Lab Manual",
        "subject": "Programming",
        "semester": "Semester 4",
        "kind": "Lab Manual",
        "description": "Practice arrays, linked lists, stacks, queues and algorithms.",
        "logo": "https://cdn.simpleicons.org/cplusplus/00599C",
    },
    {
        "title": "Introduction to Cloud",
        "subject": "Cloud",
        "semester": "Semester 4",
        "kind": "Reference",
        "description": "Understand cloud computing models and essential cloud services.",
        "logo": "https://cdn.simpleicons.org/googlecloud/4285F4",
    },
    {
        "title": "Machine Learning Revision",
        "subject": "AI/ML",
        "semester": "Semester 4",
        "kind": "Notes",
        "description": "Revise machine learning algorithms and model evaluation.",
        "logo": "https://cdn.simpleicons.org/scikitlearn/F7931E",
    },
    {
        "title": "Computer Networks",
        "subject": "Networking",
        "semester": "Semester 4",
        "kind": "Reference",
        "description": "Review networking layers, protocols and network fundamentals.",
        "logo": "https://cdn.simpleicons.org/cisco/049FD9",
    },
]

if "submitted_resources" not in st.session_state:
    st.session_state.submitted_resources = []


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    # st.html safely renders the inline SVG/HTML as a component.
        # CampusCloud logo image
    st.image("campuscloud_logo.png", width=100)

    # Keep the existing brand text and tagline
    st.markdown("""
    <div class="campus-wordmark">
        <div class="campus-name">
            Campus<span class="cloud-word">Cloud</span>
        </div>
        <div class="campus-tagline">
            LEARN · SHARE · GROW
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### WORKSPACE")
    page = st.radio(
        "Navigation",
        ["Dashboard", "Share a Resource", "About"],
        label_visibility="collapsed",
        key="navigation_page",
    )

    st.markdown("---")
    st.markdown("#### YOUR CAMPUS")
    st.caption("A student-powered learning space.")

    st.markdown(
        f'<div style="font-size:.78rem;color:#bac3e4;">'
        f'Environment: {html.escape(APP_MODE)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div style="margin-top:35px;padding:15px;background:#1d2944;
                border-radius:12px;font-size:.8rem;color:#cbd5e1;">
        <strong style="color:#ffffff;">Keep learning</strong><br><br>
        Every resource shared can help another student succeed.
    </div>
    """, unsafe_allow_html=True)

resources = DEFAULT_RESOURCES + st.session_state.submitted_resources


# =====================================================
# DASHBOARD
# =====================================================
if page == "Dashboard":
    st.markdown("""
    <div class="hero">
        <span class="hero-tag">✦ YOUR LEARNING WORKSPACE</span>
        <h1>Learn better, together.</h1>
        <p>
            Discover academic resources, explore new subjects,
            and share knowledge with your campus community.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Your learning overview")
    st.markdown(
        '<div class="section-note">Everything you need to get started.</div>',
        unsafe_allow_html=True,
    )

    metrics = [
        ("📚", "Available resources", len(resources)),
        ("🧠", "Subjects covered", len({r["subject"] for r in resources})),
        ("🎓", "Semesters", len({r["semester"] for r in resources})),
        ("✨", "Your contributions", len(st.session_state.submitted_resources)),
    ]

    metric_cols = st.columns(4)
    for col, (icon, label, value) in zip(metric_cols, metrics):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)
    st.markdown("## Explore resources")
    st.markdown(
        '<div class="section-note">Find the right material for your next study session.</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search resources",
        placeholder="Search by title, topic or keyword...",
    )

    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        subjects = ["All subjects"] + sorted({r["subject"] for r in resources})
        selected_subject = st.selectbox("Subject", subjects)
    with filter_col2:
        semesters = ["All semesters"] + sorted({r["semester"] for r in resources})
        selected_semester = st.selectbox("Semester", semesters)

    filtered = [
        r for r in resources
        if (selected_subject == "All subjects" or r["subject"] == selected_subject)
        and (selected_semester == "All semesters" or r["semester"] == selected_semester)
        and search.strip().lower() in (
            r["title"] + " " + r["description"] + " "
            + r["subject"] + " " + r["kind"]
        ).lower()
    ]

    st.markdown(
        f'<div style="color:#73809b;font-size:.85rem;margin:16px 0;">'
        f'Showing <strong>{len(filtered)}</strong> resources</div>',
        unsafe_allow_html=True,
    )

    if filtered:
        card_cols = st.columns(3)
        for i, resource in enumerate(filtered):
            title = html.escape(resource["title"])
            description = html.escape(resource["description"])
            subject = html.escape(resource["subject"])
            semester = html.escape(resource["semester"])
            kind = html.escape(resource["kind"])
            logo = html.escape(
                resource.get("logo", "https://cdn.simpleicons.org/book/64748B"),
                quote=True,
            )

            with card_cols[i % 3]:
                st.markdown(
                    f"""
                    <div class="resource-card">
                        <div class="resource-icon">
                            <img src="{logo}" alt="Technology logo" width="28" height="28">
                        </div>
                        <div class="resource-title">{title}</div>
                        <div class="resource-desc">{description}</div>
                        <div style="margin-top:14px;">
                            <span class="pill">{subject}</span>
                            <span class="pill">{semester}</span>
                        </div>
                        <div style="font-size:.75rem;color:#8993a9;">{kind}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        st.info("No resources found. Try another search or filter.")

    st.markdown(
        '<div class="footer">CampusCloud Lite · Built for student success</div>',
        unsafe_allow_html=True,
    )


# =====================================================
# SHARE A RESOURCE
# =====================================================
elif page == "Share a Resource":
    st.markdown("""
    <div class="hero">
        <span class="hero-tag">✦ COMMUNITY CONTRIBUTIONS</span>
        <h1>Share what you know.</h1>
        <p>
            Help fellow students learn by adding useful notes,
            references and lab materials to the resource catalogue.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Add a learning resource")
    st.markdown(
        '<div class="section-note">Fill in the details below to contribute a resource.</div>',
        unsafe_allow_html=True,
    )

    with st.form("resource_form", clear_on_submit=True):
        title = st.text_input(
            "Resource title *",
            placeholder="e.g. Introduction to Python",
        )
        col1, col2 = st.columns(2)

        with col1:
            subject = st.selectbox(
                "Subject",
                ["Programming", "Database", "Cloud", "AI/ML", "Networking", "Other"],
            )
        with col2:
            semester = st.selectbox(
                "Semester",
                [f"Semester {i}" for i in range(1, 9)],
            )

        kind = st.selectbox(
            "Resource type",
            ["Notes", "Lab Manual", "Reference", "Tutorial", "Other"],
        )
        description = st.text_area(
            "Description *",
            placeholder="What will students learn from this resource?",
        )
        submit = st.form_submit_button(
            "Publish resource →",
            use_container_width=True,
        )

        if submit:
    if title.strip() and description.strip():
        try:
            resource = {
                "title": title.strip(),
                "subject": subject,
                "semester": semester,
                "kind": kind,
                "description": description.strip(),
                "logo": "https://cdn.simpleicons.org/book/64748B",
            }

            db.collection("resources").add(resource)

            st.success("Resource saved to the cloud successfully!")
            st.rerun()

        except Exception as e:
            st.error(f"Could not save resource: {e}")
    else:
        st.error("Please complete both required fields.")

    st.caption(
        "Prototype note: submissions are stored temporarily in this session. "
        "They are not saved to a permanent shared database."
    )


# =====================================================
# ABOUT
# =====================================================
else:
    st.markdown("""
    <div class="hero">
        <span class="hero-tag">✦ ABOUT THE PROJECT</span>
        <h1>Knowledge grows when shared.</h1>
        <p>
            CampusCloud Lite is a student-built prototype that makes
            academic resources easier to discover and share.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Built with")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://cdn.simpleicons.org/python/3776AB", width=48)
        st.markdown("### Python")
        st.write("Application logic and resource handling.")

    with col2:
        st.image("https://cdn.simpleicons.org/streamlit/FF4B4B", width=48)
        st.markdown("### Streamlit")
        st.write("Interactive web interface and components.")

    with col3:
        st.image("https://cdn.simpleicons.org/github/FFFFFF", width=48)
        st.markdown("### GitHub")
        st.write("Source code management and version control.")

    st.markdown("## Project capabilities")
    st.markdown("""
    - Browse academic resources.
    - Search resources by keyword.
    - Filter by subject and semester.
    - Submit resources to the current session.
    - Read environment configuration from an environment variable.
    """)

    st.info(
        "This is a demonstration prototype. It does not yet use a permanent "
        "database, user authentication, or persistent file storage."
    )

    st.markdown(
        '<div class="footer">CampusCloud Lite · Learn · Share · Grow</div>',
        unsafe_allow_html=True,
    )
