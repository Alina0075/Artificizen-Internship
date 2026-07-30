import streamlit as st
import textwrap

from api import (
    login,
    register,
    get_rooms,
    create_room,
    get_history,
    delete_history,
    get_files,
    upload_file,
    send_chat
)

from styles import load_css


# ============================================
# HTML HELPER
# ============================================

def html_block(s: str) -> str:
    """
    Strip ALL leading/trailing whitespace on every line (not just the
    common-prefix dedent) so Streamlit's Markdown renderer treats this
    as HTML instead of a code block.

    Why: textwrap.dedent() only removes whitespace equal to the
    LEAST-indented line in the string. Nested HTML (e.g. a <div> inside
    another <div>) still ends up with 4+ leading spaces on the inner
    lines after dedent, and Streamlit's markdown parser treats any
    line indented by 4+ spaces as a code block -- even inside an
    unsafe_allow_html=True call. That's what was causing raw HTML tags
    to render as literal text. Stripping per-line avoids this entirely.

    Use this to wrap EVERY multi-line HTML string passed to
    st.markdown(..., unsafe_allow_html=True) when that string is built
    inside a function or loop (i.e. indented).
    """
    lines = s.strip("\n").split("\n")
    return "\n".join(line.strip() for line in lines)


# ============================================
# CONFIG
# ============================================

st.set_page_config(
    page_title="CyberRAG",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# ============================================
# SESSION STATE
# ============================================

defaults = {
    "token": None,
    "user": None,
    "rooms": [],
    "selected_room": None,
    "messages": [],
    "files": [],
    "page": "login",
    "auth_mode": "login"
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================
# HELPERS
# ============================================

def logout():

    st.session_state.token = None
    st.session_state.user = None
    st.session_state.rooms = []
    st.session_state.selected_room = None
    st.session_state.messages = []
    st.session_state.files = []
    st.session_state.page = "login"

    st.rerun()


def load_rooms():

    response = get_rooms(st.session_state.token)

    if response.status_code == 200:

        st.session_state.rooms = response.json()


def load_room_data(room_id):

    history_response = get_history(
        st.session_state.token,
        room_id
    )

    files_response = get_files(
        st.session_state.token,
        room_id
    )

    if history_response.status_code == 200:
        st.session_state.messages = history_response.json()

    else:
        st.session_state.messages = []

    if files_response.status_code == 200:
        st.session_state.files = files_response.json()

    else:
        st.session_state.files = []


def select_room(room):

    st.session_state.selected_room = room

    room_id = room.get("id")

    load_room_data(room_id)


# ============================================
# LOGIN / REGISTER
# ============================================

def auth_page():

    left, center, right = st.columns([1, 1.25, 1])

    with center:

        st.markdown(
            html_block("""
            <div style="
                margin-top:70px;
                text-align:center;
            ">
                <div class="login-title">
                    CyberRAG<span style="color:#1B6B47">↗</span>
                </div>

                <div class="login-subtitle" style="
                    color:#000000;
                    font-size:14px;
                    margin-top:8px;
                    margin-bottom:25px;
                ">
                    Security Intelligence &amp; Evidence Retrieval
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

        login_tab, register_tab = st.tabs(
            ["Sign in", "Create account"]
        )

        # ====================================
        # LOGIN
        # ====================================

        with login_tab:

            email = st.text_input(
                "Email",
                placeholder="analyst@soc.team",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="••••••••",
                key="login_password"
            )

            if st.button(
                "Continue →",
                use_container_width=True,
                key="login_button"
            ):

                if not email or not password:

                    st.error(
                        "Please enter email and password."
                    )

                else:

                    # Authentication uses EMAIL + PASSWORD
                    response = login(
                        email,
                        password
                    )

                    if response.status_code in [200, 201]:

                        data = response.json()

                        st.session_state.token = data[
                            "access_token"
                        ]

                        st.session_state.user = data.get(
                            "user",
                            {
                                "email": email
                            }
                        )

                        st.session_state.page = "rooms"

                        load_rooms()

                        st.rerun()

                    else:

                        try:

                            error_data = response.json()

                            error = error_data.get(
                                "detail",
                                "Invalid email or password."
                            )

                        except Exception:

                            error = "Invalid email or password."

                        st.error(
                            f"Login failed: {error}"
                        )

        # ====================================
        # REGISTER
        # ====================================

            with register_tab:

                name = st.text_input(
                    "Name",
                    placeholder="Security Analyst",
                    key="register_name"
                )

                email = st.text_input(
                    "Email",
                    placeholder="analyst@soc.team",
                    key="register_email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="••••••••",
                    key="register_password"
                )

                st.caption(
                    "Password must contain uppercase, lowercase, "
                    "number and special character."
                )

                if st.button(
                    "Create account →",
                    use_container_width=True,
                    key="register_button"
                ):

                    if not name or not email or not password:

                        st.error(
                            "All fields are required."
                        )

                    else:

                        # Registration uses NAME + EMAIL + PASSWORD
                        response = register(
                            email,
                            name,
                            password
                        )

                        if response.status_code in [200, 201]:

                            st.success(
                                "Account created. You can now sign in."
                            )

                        else:

                            try:

                                error_data = response.json()

                                error = error_data.get(
                                    "detail",
                                    "Registration failed."
                                )

                            except Exception:

                                error = "Registration failed."

                            st.error(
                                f"Registration failed: {error}"
                            )

# ============================================
# HEADER
# ============================================

def header():

    st.markdown(
        html_block("""
        <div class="cyber-header">

            <div>
                <span class="brand">
                    CyberRAG<span class="brand-accent">↗</span>
                </span>
            </div>

            <div class="model-badge">
                ● llama-3.3-70b-versatile · Groq
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


# ============================================
# ROOM LIST
# ============================================

def room_list():

    header()

    st.markdown(
        html_block("""
        <div style="
            font-size:24px;
            font-family:Georgia,serif;
            margin-bottom:4px;
        ">
        Evidence Workspaces
        </div>

        <div style="
            color:#8A8780;
            font-size:11px;
            margin-bottom:20px;
        ">
        Investigate incidents using your uploaded evidence.
        </div>
        """),
        unsafe_allow_html=True
    )

    # Dashboard statistics

    rooms = st.session_state.rooms

    total_rooms = len(rooms)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            html_block(f"""
            <div class="stat-card">
                <div class="stat-number">
                    {total_rooms}
                </div>
                <div class="stat-label">
                    WORKSPACES
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            html_block("""
            <div class="stat-card">
                <div class="stat-number">
                    <span>●</span> Online
                </div>
                <div class="stat-label">
                    RAG ENGINE
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            html_block("""
            <div class="stat-card">
                <div class="stat-number">
                    <span>JWT</span>
                </div>
                <div class="stat-label">
                    AUTHENTICATION
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    st.divider()

    # New room

    with st.expander("＋ Create new workspace"):

        room_name = st.text_input(
            "Workspace name",
            placeholder="e.g. Ransomware Investigation"
        )

        if st.button(
            "Create workspace",
            type="primary",
            key="create_room_button"
        ):

            if not room_name:

                st.warning(
                    "Enter a workspace name."
                )

            else:

                response = create_room(
                    st.session_state.token,
                    room_name
                )

                if response.status_code in [200, 201]:

                    st.success(
                        "Workspace created."
                    )

                    load_rooms()

                    st.rerun()

                else:

                    st.error(
                        response.text
                    )

    st.markdown(
        "### Your workspaces"
    )

    if not rooms:

        st.info(
            "No workspaces yet. Create your first workspace above."
        )

    else:

        for room in rooms:

            room_id = room.get("id")
            name = room.get(
                "name",
                f"Workspace {room_id}"
            )

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    html_block(f"""
                    <div class="room-card">

                        <div class="room-name">
                            ◈ {name}
                        </div>

                        <div class="room-meta">
                            ROOM ID · {room_id}
                        </div>

                    </div>
                    """),
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                    "Enter →",
                    key=f"room_{room_id}"
                ):

                    select_room(room)

                    st.session_state.page = "room"

                    st.rerun()

    st.divider()

    if st.button("Sign out"):
        key = "logout_button",
        logout()


# ============================================
# FILE SIDEBAR
# ============================================

def render_files(room_id):

    st.markdown(
        html_block("""
        <div class="card-title">
            Evidence files
        </div>
        """),
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Upload evidence",
        type=[
            "pdf",
            "docx",
            "csv",
            "txt",
            "md",
            "png",
            "jpg",
            "jpeg",
            "mp4",
            "mp3",
            "pptx"
        ],
        label_visibility="collapsed"
    )

    if uploaded:

        if st.button(
            "Upload file",
            use_container_width=True,
            key="upload_file_button"
        ):

            with st.spinner(
                "Uploading and indexing..."
            ):

                response = upload_file(
                    st.session_state.token,
                    room_id,
                    uploaded
                )

            if response.status_code in [200, 201]:

                st.success(
                    f"{uploaded.name} uploaded."
                )

                load_room_data(room_id)

                st.rerun()

            else:

                st.error(
                    response.text
                )

    st.divider()

    files = st.session_state.files

    if not files:

        st.caption(
            "No files uploaded yet."
        )

        return

    for file in files:

        filename = file.get(
                "filename",
                file.get("name", "Unknown")
        )

        status = file.get(
                "status",
                "unknown"
            ).lower()

        file_type = file.get(
                "file_type",
                filename.split(".")[-1].upper()
            )

        if status in [
                "uploaded",
                "ready",
                "completed",
                "indexed"
            ]:

                badge = "🟢 READY"

        elif status in [
                "processing",
                "indexing"
            ]:

                badge = "🟠 INDEXING"

        elif status in [
                "failed",
                "error"
            ]:

                badge = "🔴 ERROR"

        else:

                badge = "⚪ UNKNOWN"
        st.markdown(
            html_block(f"""
            <div class="card">

                <div style="
                    display:flex;
                    align-items:center;
                    gap:8px;
                ">

                    <div style="flex:1">

                        <div style="
                            font-family:monospace;
                            font-size:10px;
                            overflow:hidden;
                            text-overflow:ellipsis;
                        ">
                            {filename}
                        </div>

                        <div style="
                            font-size:9px;
                            color:#9E9B94;
                            margin-top:3px;
                        ">
                            {file_type}
                        </div>

                    </div>

                    <div style="
                        font-size:8px;
                        font-family:monospace;
                    ">
                        {badge}
                    </div>

                </div>

            </div>
            """),
            unsafe_allow_html=True
        )


# ============================================
# SOURCES
# ============================================

def render_sources(sources):

    st.markdown(
        html_block("""
        <div class="sources-title">
            Sources
        </div>
        """),
        unsafe_allow_html=True
    )

    # IMPORTANT:
    # Never hide Sources.
    # Empty list must explicitly show
    # "No sources found".

    if not sources:

        st.markdown(
            html_block("""
            <div class="source-item">
                <span style="
                    color:#9E9B94;
                    font-family:monospace;
                    font-size:10px;
                ">
                    No sources found
                </span>
            </div>
            """),
            unsafe_allow_html=True
        )

        return

    for source in sources:

        filename = source.get(
            "filename",
            "Unknown file"
        )

        file_type = source.get(
            "file_type",
            "Unknown"
        )

        chunk_index = source.get(
            "chunk_index",
            "?"
        )

        excerpt = source.get(
            "excerpt",
            ""
        )

        st.markdown(
            html_block(f"""
            <div class="source-item">

                <div class="source-file">
                    {filename}
                </div>

                <div class="source-meta">
                    TYPE: {file_type}
                    &nbsp; · &nbsp;
                    CHUNK: #{chunk_index}
                </div>

                <div class="source-excerpt">
                    {excerpt}
                </div>

            </div>
            """),
            unsafe_allow_html=True
        )


# ============================================
# CHAT MESSAGE
# ============================================

def render_message(message):

    role = message.get("role")

    content = message.get(
        "content",
        message.get(
            "message",
            message.get("answer", "")
        )
    )

    if role == "user":

        st.markdown(
            html_block(f"""
            <div class="chat-user">
                {content}
            </div>
            """),
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            html_block("""
            <div class="chat-label">
                CYBERRAG
            </div>
            """),
            unsafe_allow_html=True
        )

        st.markdown(
            html_block(f"""
            <div class="chat-ai">
                {content}
            </div>
            """),
            unsafe_allow_html=True
        )

        sources = message.get(
            "sources",
            []
        )

        with st.expander(
            f"Sources · {len(sources)}",
            expanded=False
        ):

            render_sources(sources)


# ============================================
# ROOM VIEW
# ============================================

def room_view():

    room = st.session_state.selected_room

    if not room:

        st.session_state.page = "rooms"

        st.rerun()

    room_id = room.get("id")

    room_name = room.get(
        "name",
        f"Workspace {room_id}"
    )

    header()

    # ========================================
    # ROOM HEADER
    # ========================================

    col1, col2 = st.columns([5, 1])

    with col1:

        st.markdown(
            html_block(f"""
            <div style="
                font-size:18px;
                font-weight:600;
            ">
                {room_name}
            </div>

            <div style="
                color:#9E9B94;
                font-family:monospace;
                font-size:9px;
            ">
                EVIDENCE WORKSPACE · ROOM #{room_id}
            </div>
            """),
            unsafe_allow_html=True
        )

    with col2:

        if st.button(
            "← Rooms"
        ):

            st.session_state.page = "rooms"

            st.rerun()

    st.divider()

    # ========================================
    # THREE AREA LAYOUT
    # ========================================

    left, center, right = st.columns(
        [1.1, 3.2, 1.4],
        gap="medium"
    )

    # ========================================
    # LEFT FILE PANEL
    # ========================================

    with left:

        render_files(room_id)

    # ========================================
    # CHAT PANEL
    # ========================================

    with center:

        st.markdown(
            html_block("""
            <div class="card-title">
                Investigation chat
            </div>
            """),
            unsafe_allow_html=True
        )

        messages = st.session_state.messages

        if not messages:

            st.markdown(
                html_block("""
                <div style="
                    text-align:center;
                    padding:80px 20px;
                    color:#9E9B94;
                ">

                    <div style="
                        font-size:28px;
                        margin-bottom:10px;
                    ">
                        ◈
                    </div>

                    <div style="
                        font-family:Georgia,serif;
                        font-size:20px;
                        color:#3C3B38;
                    ">
                        Ask your evidence base
                    </div>

                    <div style="
                        font-size:11px;
                        margin-top:6px;
                    ">
                        Upload files and ask questions about them.
                    </div>

                </div>
                """),
                unsafe_allow_html=True
            )

        else:

            for message in messages:

                render_message(message)

        # ====================================
        # CHAT INPUT
        # ====================================

        question = st.chat_input(
            "Ask anything about the uploaded evidence..."
        )

        if question:

            # Show user message immediately

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.spinner(
                "Searching evidence..."
            ):

                response = send_chat(
                    st.session_state.token,
                    room_id,
                    question
                )

            if response.status_code in [200, 201]:

                data = response.json()

                # Sources MUST always exist.

                sources = data.get(
                    "sources",
                    []
                )

                assistant_message = {
                    "role": "assistant",
                    "content": data.get(
                        "answer",
                        "I don't know."
                    ),
                    "sources": sources
                }

                st.session_state.messages.append(
                    assistant_message
                )

                st.rerun()

            else:

                st.error(
                    f"Chat request failed: {response.text}"
                )

    # ========================================
    # RIGHT INSPECTOR
    # ========================================

    with right:

        st.markdown(
            html_block("""
            <div class="card-title">
                Workspace overview
            </div>
            """),
            unsafe_allow_html=True
        )

        files = st.session_state.files

        ready = 0

        for f in files:

            status = f.get(
                "status",
                ""
            ).lower()

            if status in [
                "ready",
                "uploaded",
                "completed",
                "indexed"
            ]:
                ready += 1

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                html_block(f"""
                <div class="stat-card">
                    <div class="stat-number">
                        {len(files)}
                    </div>
                    <div class="stat-label">
                        FILES
                    </div>
                </div>
                """),
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                html_block(f"""
                <div class="stat-card">
                    <div class="stat-number">
                        <span>{ready}</span>
                    </div>
                    <div class="stat-label">
                        READY
                    </div>
                </div>
                """),
                unsafe_allow_html=True
            )

        st.markdown("### Recent sources")

        # Find sources from last assistant message

        latest_sources = []

        for message in reversed(
            st.session_state.messages
        ):

            if message.get("role") == "assistant":

                latest_sources = message.get(
                    "sources",
                    []
                )

                break

        if latest_sources:

            render_sources(
                latest_sources
            )

        else:

            st.caption(
                "No sources found"
            )

        st.divider()

        if st.button(
            "Refresh workspace",
            use_container_width=True,
            key="refresh_workspace_button"
        ):

            load_room_data(room_id)

            st.rerun()
            
        # ========================================
        # CHAT HISTORY CONTROLS
        # ========================================

        st.markdown("### Chat history")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "View history",
                use_container_width=True,
                key=f"view_history_{room_id}"
            ):

                response = get_history(
                    st.session_state.token,
                    room_id
                )

                if response.status_code == 200:

                    st.session_state.messages = response.json()

                    st.success("Chat history loaded.")

                    st.rerun()

                else:

                    st.error(
                        f"Failed to load history: {response.text}"
                    )


        with col2:

            if st.button(
                "Delete history",
                use_container_width=True,
                key=f"delete_history_{room_id}"
            ):

                response = delete_history(
                    st.session_state.token,
                    room_id
                )

                if response.status_code == 200:

                    st.session_state.messages = []
                    st.session_state.files = []

                    st.success(
                        "Chat history and all workspace files deleted successfully."
                    )

                    st.rerun()

                else:

                    st.error(
                        f"Failed to delete history: {response.text}"
                    )

        st.divider()

# ============================================
# ROUTER
# ============================================

if not st.session_state.token:

    auth_page()

else:

    if st.session_state.page == "rooms":

        room_list()

    elif st.session_state.page == "room":

        room_view()

    else:

        room_list()