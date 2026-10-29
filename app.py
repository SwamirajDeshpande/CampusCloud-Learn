
import os
import streamlit as st

st.set_page_config(
    page_title="CampusCloud Lite",
    page_icon="☁️",
    layout="wide"
)

APP_MODE = os.getenv("APP_MODE", "production")

RESOURCES = [
    {
        "title": "Python Programming Notes",
        "subject": "Programming",
        "semester": "Semester 3",
        "kind": "Notes",
        "description": "Python basics, loops, functions and examples."
    },
    {
        "title": "Database Management Systems",
        "subject": "Database",
        "semester": "Semester 3",
        "kind": "Notes",
        "description": "SQL, normalization and relational databases."
    },
    {
        "title": "Data Structures Lab Manual",
        "subject": "Programming",
        "semester": "Semester 4",
        "kind": "Lab Manual",
        "description": "Practice exercises for common data structures."
    },
    {
        "title": "Introduction to Cloud Computing",
        "subject": "Cloud",
        "semester": "Semester 4",
        "kind": "Reference",
        "description": "Learn cloud models and basic services."
    },
    {
        "title": "Machine Learning Revision",
        "subject": "AI/ML",
        "semester": "Semester 4",
        "kind": "Notes",
        "description": "Revise basic machine learning algorithms."
    },
]

if "submitted_resources" not in st.session_state:
    st.session_state.submitted_resources = []

st.title("☁️ CampusCloud Lite")
st.caption("Your campus. Your resources. One simple hub.")
st.info(f"Application environment: {APP_MODE}")

st.subheader("Discover academic resources")

all_resources = RESOURCES + st.session_state.submitted_resources

col1, col2 = st.columns(2)

with col1:
    subjects = ["All"] + sorted(
        {item["subject"] for item in all_resources}
    )
    selected_subject = st.selectbox("Filter by subject", subjects)

with col2:
    semesters = ["All"] + sorted(
        {item["semester"] for item in all_resources}
    )
    selected_semester = st.selectbox("Filter by semester", semesters)

filtered = [
    item for item in all_resources
    if (
        selected_subject == "All"
        or item["subject"] == selected_subject
    )
    and (
        selected_semester == "All"
        or item["semester"] == selected_semester
    )
]

st.write(f"**{len(filtered)} resources found**")

if filtered:
    columns = st.columns(2)

    for index, resource in enumerate(filtered):
        with columns[index % 2]:
            with st.container(border=True):
                st.subheader(resource["title"])
                st.caption(
                    f'{resource["subject"]} · '
                    f'{resource["semester"]}'
                )
                st.write(resource["description"])
                st.write(f'Type: {resource["kind"]}')
else:
    st.warning("No resources match these filters.")

st.divider()
st.subheader("Share a resource")

with st.form("resource_form", clear_on_submit=True):
    title = st.text_input("Resource title")

    subject = st.selectbox(
        "Subject",
        ["Programming", "Database", "Cloud", "AI/ML", "Other"]
    )

    semester = st.selectbox(
        "Semester",
        [
            "Semester 1", "Semester 2", "Semester 3",
            "Semester 4", "Semester 5", "Semester 6"
        ]
    )

    kind = st.selectbox(
        "Resource type",
        ["Notes", "Lab Manual", "Reference", "Other"]
    )

    description = st.text_area("Short description")
    submitted = st.form_submit_button("Submit resource")

    if submitted:
        if title.strip() and description.strip():
            st.session_state.submitted_resources.append({
                "title": title.strip(),
                "subject": subject,
                "semester": semester,
                "kind": kind,
                "description": description.strip()
            })
            st.success("Resource added to this session!")
        else:
            st.error("Please enter a title and description.")

st.divider()
st.caption(
    "Student-built prototype · Sample resources for demonstration."
)
