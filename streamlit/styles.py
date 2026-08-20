import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* ==============================
           GLOBAL
        ============================== */

        .stApp {
            background: #F7F6F2;
            color: #111110;
        }

        header[data-testid="stHeader"] {
            background: #FFFFFF;
        }

        footer {
            visibility: hidden;
        }

        #MainMenu {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 100%;
        }


        /* ==============================
           TOP HEADER
        ============================== */

        .cyber-header {
            background: #FFFFFF;
            border-bottom: 1px solid #E2DED7;
            padding: 10px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .brand {
            font-family: Georgia, serif;
            font-style: italic;
            font-size: 22px;
            font-weight: 600;
        }

        .brand-accent {
            color: #1B6B47;
        }

        .model-badge {
            background: #F2F0EC;
            border: 1px solid #E2DED7;
            border-radius: 6px;
            padding: 6px 10px;
            font-family: monospace;
            font-size: 11px;
            color: #6B6860;
        }


        /* ==============================
           CARDS
        ============================== */

        .card {
            background: #FFFFFF;
            border: 1px solid #E2DED7;
            border-radius: 10px;
            padding: 14px;
            margin-bottom: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,.04);
        }

        .card-title {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: .08em;
            color: #8A8780;
            font-weight: 600;
            margin-bottom: 8px;
        }


        /* ==============================
           ROOM CARD
        ============================== */

        .room-card {
            background: #FFFFFF;
            border: 1px solid #E2DED7;
            border-radius: 9px;
            padding: 13px;
            margin-bottom: 7px;
        }

        .room-name {
            font-size: 13px;
            font-weight: 600;
        }

        .room-meta {
            color: #8A8780;
            font-size: 10px;
            font-family: monospace;
            margin-top: 4px;
        }


        /* ==============================
           STATUS
        ============================== */

        .status-ready {
            color: #1B6B47;
            background: #E6F2EC;
            border: 1px solid #B8D9C6;
            border-radius: 5px;
            padding: 3px 7px;
            font-size: 9px;
            font-family: monospace;
        }

        .status-processing {
            color: #A05C1A;
            background: #FEF4E8;
            border: 1px solid #E6C99D;
            border-radius: 5px;
            padding: 3px 7px;
            font-size: 9px;
            font-family: monospace;
        }

        .status-error {
            color: #B93737;
            background: #FAEAEA;
            border: 1px solid #E7B6B6;
            border-radius: 5px;
            padding: 3px 7px;
            font-size: 9px;
            font-family: monospace;
        }


        /* ==============================
           CHAT
        ============================== */

        .chat-user {
            background: #111110;
            color: white;
            padding: 11px 14px;
            border-radius: 12px 12px 3px 12px;
            margin: 7px 0;
            margin-left: 20%;
            font-size: 13px;
            line-height: 1.6;
        }

        .chat-ai {
            background: #F8F7F4;
            border: 1px solid #E2DED7;
            padding: 12px 14px;
            border-radius: 3px 12px 12px 12px;
            margin: 7px 0;
            margin-right: 5%;
            font-size: 13px;
            line-height: 1.7;
        }

        .chat-label {
            color: #1B6B47;
            font-family: monospace;
            font-size: 9px;
            font-weight: 600;
            margin-bottom: 4px;
        }


        /* ==============================
           SOURCES
        ============================== */

        .sources-box {
            border-left: 2px solid #1B6B47;
            background: #FFFFFF;
            border-top: 1px solid #E2DED7;
            border-right: 1px solid #E2DED7;
            border-bottom: 1px solid #E2DED7;
            border-radius: 0 7px 7px 0;
            padding: 10px;
            margin: 5px 0 14px 0;
        }

        .sources-title {
            color: #8A8780;
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: .1em;
            font-weight: 600;
            margin-bottom: 7px;
        }

        .source-item {
            background: #F8F7F4;
            border: 1px solid #E2DED7;
            border-radius: 6px;
            padding: 8px;
            margin-top: 5px;
        }

        .source-file {
            font-family: monospace;
            font-size: 10px;
            font-weight: 500;
        }

        .source-meta {
            color: #8A8780;
            font-family: monospace;
            font-size: 9px;
            margin-top: 3px;
        }

        .source-excerpt {
            color: #6B6860;
            font-family: monospace;
            font-size: 9px;
            line-height: 1.5;
            margin-top: 6px;
            border-top: 1px solid #E2DED7;
            padding-top: 6px;
        }


        /* ==============================
   LOGIN / REGISTER — PRODUCT AUTH
============================== */

.login-shell {
    width: min(440px, 94vw);
    margin: 5vh auto 0 auto;
}

.login-brand {
    text-align: center;
    margin-bottom: 26px;
}

.login-brand-mark {
    width: 46px;
    height: 46px;
    margin: 0 auto 14px auto;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #111110;
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.04em;
    box-shadow: 0 8px 24px rgba(17,17,16,.12);
}

.login-brand-name {
    color: #111110;
    font-size: 25px;
    font-weight: 700;
    letter-spacing: -0.04em;
}

.login-brand-name span {
    color: #1B6B47;
}

.login-title {
    color: #111110 !important;
    font-size: 29px !important;
    font-weight: 700 !important;
    letter-spacing: -0.035em !important;
    text-align: center !important;
    margin: 0 0 7px 0 !important;
}

.login-subtitle {
    color: #77736B !important;
    font-size: 13px !important;
    line-height: 1.55 !important;
    text-align: center !important;
    margin: 0 0 24px 0 !important;
}

.login-card {
    background: #FFFFFF;
    border: 1px solid #E3DFD8;
    border-radius: 16px;
    padding: 30px 30px 26px 30px;
    box-shadow:
        0 18px 45px rgba(17,17,16,.07),
        0 2px 8px rgba(17,17,16,.03);
}

.login-label {
    color: #292824 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    margin: 0 0 6px 0 !important;
}

.login-link {
    color: #1B6B47 !important;
    font-weight: 600 !important;
    cursor: pointer;
}

.auth-divider {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #A09B92;
    font-size: 10px;
    margin: 20px 0;
}

.auth-divider::before,
.auth-divider::after {
    content: "";
    flex: 1;
    height: 1px;
    background: #E8E4DD;
}

.auth-security {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    color: #8A8780;
    font-size: 10px;
    margin-top: 17px;
}

.auth-security-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #1B6B47;
}

.auth-footer {
    text-align: center;
    color: #8A8780;
    font-size: 10px;
    line-height: 1.5;
    margin-top: 18px;
}

.auth-footer strong {
    color: #6B6860;
    font-weight: 600;
}

.error-message {
    color: #B93737 !important;
    background: #FFF5F4 !important;
    border: 1px solid #EBC4C1 !important;
    border-radius: 8px !important;
    padding: 10px 12px !important;
    font-size: 12px !important;
    line-height: 1.45 !important;
}

.success-message {
    color: #1B6B47 !important;
    background: #F1F8F4 !important;
    border: 1px solid #C6DFD0 !important;
    border-radius: 8px !important;
    padding: 10px 12px !important;
    font-size: 12px !important;
    line-height: 1.45 !important;
}


/* ==============================
   STAT CARDS
        ============================== */

        .stat-card {
            background: white;
            border: 1px solid #E2DED7;
            border-radius: 8px;
            padding: 12px;
        }

        .stat-number {
            font-size: 21px;
            font-weight: 600;
        }

        .stat-number span {
            color: #1B6B47;
        }

        .stat-label {
            color: #8A8780;
            font-size: 9px;
            font-family: monospace;
        }


        /* ==============================
           BUTTONS
        ============================== */

        .stButton > button {
            background: #FFFFFF;
            color: #111110;
            border-radius: 6px;
            border: 1px solid #D2CEC7;
            font-size: 11px;
            min-height: 34px;
        }

        .stButton > button:hover {
            border-color: #1B6B47;
            color: #1B6B47;
        }

        .stButton > button p {
            color: inherit;
        }


        /* ==============================
           INPUTS / LABELS / WIDGETS
           (Streamlit's default theme was
           bleeding through on these,
           making labels & fields hard
           to read against the light UI)
        ============================== */

        input,
        textarea {
            border-radius: 6px !important;
            caret-color: #111110 !important;
        }

        .stTextInput label,
        .stFileUploader label,
        .stSelectbox label,
        .stTextArea label {
            color: #6B6860 !important;
            font-size: 12px !important;
            font-weight: 600 !important;
        }

        .stTextInput > div > div > input,
        .stTextArea textarea {
            background: #FFFFFF !important;
            color: #111110 !important;
            border: 1px solid #D2CEC7 !important;
            caret-color: #111110 !important;
        }

        .stTextInput > div > div > input::placeholder,
        .stTextArea textarea::placeholder {
            color: #ADA99F !important;
        }

        /* ==============================
           AUTH INPUTS
        ============================== */

        .login-card .stTextInput {
            margin-bottom: 13px;
        }

        .login-card .stTextInput label {
            color: #292824 !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            margin-bottom: 5px !important;
        }

        .login-card .stTextInput > div > div > input {
            min-height: 44px !important;
            background: #FFFFFF !important;
            color: #111110 !important;
            border: 1px solid #D8D3CB !important;
            border-radius: 9px !important;
            padding: 0 12px !important;
            font-size: 13px !important;
            box-shadow: 0 1px 2px rgba(17,17,16,.02) !important;
            transition: border-color .15s ease, box-shadow .15s ease !important;
        }

        .login-card .stTextInput > div > div > input:focus {
            border-color: #1B6B47 !important;
            box-shadow: 0 0 0 3px rgba(27,107,71,.10) !important;
        }

        .login-card .stTextInput > div > div > input::placeholder {
            color: #AAA59C !important;
        }

        /* Primary authentication button */
        .login-card .stButton > button {
            width: 100% !important;
            min-height: 44px !important;
            margin-top: 7px !important;
            background: #111110 !important;
            color: #FFFFFF !important;
            border: 1px solid #111110 !important;
            border-radius: 9px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            letter-spacing: -.01em !important;
            box-shadow: 0 5px 14px rgba(17,17,16,.12) !important;
            transition: all .15s ease !important;
        }

        .login-card .stButton > button p {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }

        .login-card .stButton > button:hover {
            background: #1B6B47 !important;
            border-color: #1B6B47 !important;
            color: #FFFFFF !important;
            transform: translateY(-1px);
            box-shadow: 0 7px 18px rgba(27,107,71,.18) !important;
        }

        .login-card .stButton > button:active {
            transform: translateY(0);
        }

        /* ==============================
        AUTH TABS — CLEAN FIX
        ============================== */

        .login-card .stTabs {
            width: 100%;
        }

        /* Tab container */
        .login-card .stTabs [data-baseweb="tab-list"] {
            width: 100% !important;
            background: #F5F3EF !important;
            border-radius: 9px !important;
            padding: 4px !important;
            gap: 3px !important;
            margin-bottom: 23px !important;
        }

        /* Individual tabs */
        .login-card .stTabs [data-baseweb="tab"] {
            flex: 1 !important;
            justify-content: center !important;
            border-radius: 7px !important;
            height: 34px !important;

            background: transparent !important;

            color: #55524C !important;
            opacity: 1 !important;

            font-size: 12px !important;
            font-weight: 600 !important;
        }

        /* The actual tab text */
        .login-card .stTabs [data-baseweb="tab"] p {
            color: #55524C !important;
            opacity: 1 !important;
            font-size: 12px !important;
            font-weight: 600 !important;
        }

        /* Active tab */
        .login-card .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: #FFFFFF !important;
            color: #111110 !important;
            opacity: 1 !important;
            box-shadow: 0 1px 4px rgba(17,17,16,.08) !important;
        }

        .login-card .stTabs [data-baseweb="tab"][aria-selected="true"] p {
            color: #111110 !important;
            opacity: 1 !important;
        }

        /* Hover */
        .login-card .stTabs [data-baseweb="tab"]:hover {
            color: #1B6B47 !important;
        }

        .login-card .stTabs [data-baseweb="tab"]:hover p {
            color: #1B6B47 !important;
        }

        /* Active indicator */
        .login-card .stTabs [data-baseweb="tab-highlight"] {
            background: #1B6B47 !important;
        }

        /* File uploader dropzone */

        [data-testid="stFileUploaderDropzone"] {
            background: #FFFFFF !important;
            border: 1px dashed #D2CEC7 !important;
        }

        [data-testid="stFileUploaderDropzone"] * {
            color: #6B6860 !important;
        }

        /* "Browse files" button inside the dropzone was inheriting the
           dark OS/browser theme: dark button + dark text = unreadable.
           Force it to a legible, on-brand look. Target every element
           inside it explicitly (span, p, div, svg) since Streamlit
           wraps the label in nested elements that can each carry
           their own inherited color. */

        div[data-testid="stFileUploaderDropzone"] button,
        button[data-testid="stBaseButton-secondary"],
        div[data-testid="stFileUploader"] button {
            background-color: #111110 !important;
            border: 1px solid #111110 !important;
            border-radius: 6px !important;
        }

        div[data-testid="stFileUploaderDropzone"] button,
        div[data-testid="stFileUploaderDropzone"] button span,
        div[data-testid="stFileUploaderDropzone"] button p,
        div[data-testid="stFileUploaderDropzone"] button div,
        button[data-testid="stBaseButton-secondary"],
        button[data-testid="stBaseButton-secondary"] span,
        button[data-testid="stBaseButton-secondary"] p,
        button[data-testid="stBaseButton-secondary"] div,
        div[data-testid="stFileUploader"] button,
        div[data-testid="stFileUploader"] button span,
        div[data-testid="stFileUploader"] button p {
            color: #FFFFFF !important;
            fill: #FFFFFF !important;
            opacity: 1 !important;
        }

        div[data-testid="stFileUploaderDropzone"] button:hover,
        button[data-testid="stBaseButton-secondary"]:hover,
        div[data-testid="stFileUploader"] button:hover {
            background-color: #1B6B47 !important;
            border-color: #1B6B47 !important;
        }

        /* Uploaded file row + its remove ("x") button. The remove
           button is an icon-only button that was rendering as a
           solid black square with a black icon on top — invisible.
           Give it a visible background and a white icon. */

        [data-testid="stFileUploaderFile"] {
            background: #FFFFFF !important;
            border: 1px solid #E2DED7 !important;
            border-radius: 8px !important;
        }

        [data-testid="stFileUploaderFile"] * {
            color: #111110 !important;
        }

        [data-testid="stFileUploaderFileName"] {
            color: #111110 !important;
        }

        [data-testid="stFileUploaderFileErrorMessage"] {
            color: #B93737 !important;
        }

        [data-testid="stFileUploaderDeleteBtn"],
        [data-testid="stFileUploaderFile"] button {
            background: #111110 !important;
            border-radius: 6px !important;
        }

        [data-testid="stFileUploaderDeleteBtn"] svg,
        [data-testid="stFileUploaderFile"] button svg {
            fill: #FFFFFF !important;
            color: #FFFFFF !important;
        }

        [data-testid="stFileUploaderDeleteBtn"]:hover,
        [data-testid="stFileUploaderFile"] button:hover {
            background: #B93737 !important;
        }

        /* Expander headers (e.g. "+ Create new workspace", Sources) */

        .streamlit-expanderHeader,
        [data-testid="stExpander"] summary {
            background: #FFFFFF !important;
            color: #111110 !important;
        }

        /* Chat input box at bottom of chat panel */

        [data-testid="stChatInput"] textarea {
            background: #FFFFFF !important;
            color: #111110 !important;
            caret-color: #111110 !important;
        }

        /* ==============================
           NATIVE ALERTS
           (st.error / st.warning / st.success / st.info)
           These pick up the browser/OS dark-mode text color by
           default, which made the text nearly invisible against
           the light alert backgrounds. Force explicit colors.
        ============================== */

        [data-testid="stAlert"] p,
        [data-testid="stAlert"] span,
        [data-testid="stAlert"] div {
            color: inherit !important;
        }

        [data-testid="stAlertContentError"] {
            color: #B93737 !important;
        }

        [data-testid="stAlertContentWarning"] {
            color: #A05C1A !important;
        }

        [data-testid="stAlertContentSuccess"] {
            color: #1B6B47 !important;
        }

        [data-testid="stAlertContentInfo"] {
            color: #2B5F8A !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
        <style>

        .login-title {
            color: #111110 !important;
            font-size: 32px !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
        }

        .login-subtitle {
            color: #6B6860 !important;
            font-size: 13px !important;
            margin-bottom: 25px !important;
        }

        .login-label {
            color: #111110 !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            margin-bottom: 5px !important;
        }

        .login-link {
            color: #1B6B47 !important;
            font-weight: 600 !important;
            cursor: pointer;
        }

        .error-message {
            color: #B93737 !important;
            background: #FAEAEA !important;
            border: 1px solid #E8B5B5 !important;
            border-radius: 6px !important;
            padding: 10px 12px !important;
            font-size: 12px !important;
        }

        .success-message {
            color: #1B6B47 !important;
            background: #E6F2EC !important;
            border: 1px solid #B8D9C6 !important;
            border-radius: 6px !important;
            padding: 10px 12px !important;
            font-size: 12px !important;
        }
        
        </style>
        """, unsafe_allow_html=True)