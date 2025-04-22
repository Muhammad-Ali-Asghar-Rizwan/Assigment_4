import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Ali Asghar | Portfolio", page_icon="💼", layout="wide")

# ---- Sidebar / Navbar ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🧠 Skills", "📂 Projects", "📬 Contact"])

# ---- Home ----
if page == "🏠 Home":
    st.title("👋 Hi, I'm Ali Asghar")
    st.subheader("💻 Web Developer | Python & JS Enthusiast")
    st.image("image/my_picture.jpg", width=100  )  # Replace with your image
    st.title("About Me")
    st.write("""
My name is Ali Asghar Muhammad Rizwan, and I am currently part of the Governor Sindh IT Initiative, specializing in
Web 3.0, Metaverse, and Artificial Intelligence. With a background in Commerce and completed Matriculation, I have
enhanced my expertise by undertaking courses in HTML, CSS, and TypeScript , Next.Js , Python , Agentic ai. I have
successfully developed and delivered multiple projects, demonstrating my ability to create dynamic and responsive web
applications. Passionate about technology and continuous learning, I am eager to apply my skills to innovative projects
and contribute to advancements in the tech industry.
    """)

# ---- Skills ----
elif page == "🧠 Skills":
    st.header("⚡ My Skills")
    st.write("""
    - 💡 Programming Languages: Python, JavaScript, TypeScript
    - 🚀 Frameworks: Next.js, Streamlit, Tailwind CSS
    - 🔧 Tools: Git, GitHub, VSCode, Figma
    """)

# ---- Projects ----
elif page == "📂 Projects":
    st.header("💼 Projects Showcase")
    col1, col2 , col3 , col4  = st.columns(4)

    with col1:
        st.image("image/Fragrance.png")  # Replace with your image
        st.subheader("Fragrance E-commerce Website")
        st.write("Built with Next.js and Tailwind CSS.")
        st.markdown("[🔗 View Live](https://figma-ui-ux-design-e-commerce.vercel.app/)")

    with col2:
        st.image("image/book.png")  # Replace with your image
        st.subheader("Personal Library Manager")
        st.write("Streamlit-based app for managing personal book collections.")
        st.markdown("[🔗 View Project](https://personal-library23.streamlit.app/)")
    with col3:
        st.image("image/e-commerce.png")  # Replace with your image
        st.subheader("E-commerce Website")
        st.write("Built with Next.js , Tailwind CSS  ,  Sanity.io , Figma UI UX.")
        st.markdown("[🔗 View Project](https://rizwan-e-commerce.vercel.app/)")
    with col4:
        st.image("image/attar.png")  # Replace with your image
        st.subheader("E-commerce Website")
        st.write("Built with Next.js , Tailwind CSS.")
        st.markdown("[🔗 View Project](https://attar-sales.vercel.app/)")
    # with col3:
    #     st.image("prt.png")  # Replace with your image
    #     st.subheader("Personal Portfolio!")
    #     st.write("Built with Next.js , Tailwind.")
    #     st.markdown("[🔗 View Project](https://giaic-q2-melisthon2-next-js-tailwind-css-port-folio.vercel.app/)")

# ---- Contact ----
elif page == "📬 Contact":
    st.header("📬 Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.success(f"Thank you {name}! I will contact you soon.")

# ---- Custom Styling ----
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f4;
    }
    .sidebar .sidebar-content {
        background: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
