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
           LOGIN
        ============================== */

        .login-title {
            font-family: Georgia, serif;
            font-style: italic;
            font-size: 34px;
            text-align: center;
            margin-bottom: 5px;
        }

        .login-subtitle {
            text-align: center;
            color: #8A8780;
            font-size: 11px;
            margin-bottom: 25px;
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
        }

        .stTextInput > div > div > input::placeholder,
        .stTextArea textarea::placeholder {
            color: #ADA99F !important;
        }

        /* Tabs (Sign in / Create account) */

        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
        }

        .stTabs [data-baseweb="tab"] {
            color: #8A8780;
            font-size: 13px;
        }

        .stTabs [aria-selected="true"] {
            color: #1B6B47 !important;
        }

        .stTabs [data-baseweb="tab-highlight"] {
            background-color: #1B6B47 !important;
        }

        /* File uploader dropzone */

        [data-testid="stFileUploaderDropzone"] {
            background: #FFFFFF !important;
            border: 1px dashed #D2CEC7 !important;
        }

        [data-testid="stFileUploaderDropzone"] * {
            color: #6B6860 !important;
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