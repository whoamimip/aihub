import streamlit as st


def apply_glassmorphic_shell(page_title: str, subtitle: str, show_header: bool = True) -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg-deep: #04243d;
                --bg-mid: #0a4a73;
                --bg-soft: #4fb5e6;
                --glass: rgba(223, 244, 255, 0.16);
                --glass-strong: rgba(223, 244, 255, 0.24);
                --border: rgba(198, 232, 252, 0.42);
                --text-main: #edf8ff;
                --text-soft: #cfeaf9;
                --accent: #72d1ff;
            }
            .stApp {
                background:
                    radial-gradient(circle at 8% 12%, rgba(114, 209, 255, 0.35), transparent 34%),
                    radial-gradient(circle at 90% 14%, rgba(79, 181, 230, 0.26), transparent 40%),
                    linear-gradient(135deg, var(--bg-deep) 0%, var(--bg-mid) 52%, var(--bg-soft) 100%);
                color: var(--text-main);
            }
            header[data-testid="stHeader"] {
                display: none;
            }
            div[data-testid="stToolbar"] {
                display: none;
            }
            div[data-testid="stDecoration"] {
                display: none;
            }
            .stMainBlockContainer {
                padding-top: 1.25rem;
            }
            div[data-testid="stSidebar"] {
                background: linear-gradient(180deg, rgba(4, 36, 61, 0.9) 0%, rgba(10, 74, 115, 0.88) 100%);
                backdrop-filter: blur(12px);
            }
            div[data-testid="stBottom"] {
                background: transparent !important;
            }
            div[data-testid="stBottom"] > div {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                backdrop-filter: none !important;
            }
            .shell {
                background: var(--glass-strong);
                border: 1px solid var(--border);
                border-radius: 22px;
                padding: 1rem;
                backdrop-filter: blur(15px);
                box-shadow: 0 22px 38px rgba(8, 17, 28, 0.28), inset 0 1px 1px rgba(255, 255, 255, 0.22);
                margin-bottom: 0.8rem;
            }
            .shell-title {
                color: var(--text-main);
                font-size: 1.4rem;
                font-weight: 800;
                letter-spacing: 0.01em;
                margin-bottom: 0.25rem;
            }
            .shell-subtitle {
                color: var(--text-soft);
                font-size: 0.95rem;
                margin-bottom: 0;
            }
            .glass-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 0.9rem;
                backdrop-filter: blur(12px);
                box-shadow: 0 10px 20px rgba(4, 36, 61, 0.18);
                margin-bottom: 0.7rem;
            }
            div[data-testid="stMetric"] {
                background: rgba(223, 244, 255, 0.12);
                border: 1px solid rgba(198, 232, 252, 0.28);
                border-radius: 14px;
                padding: 0.45rem 0.55rem;
            }
            .shell-title,
            .shell-subtitle,
            .glass-card,
            .glass-card p,
            .glass-card li,
            .glass-card h3,
            .glass-card h4 {
                color: var(--text-main);
            }
            div[data-testid="stChatMessage"] {
                border-radius: 12px;
                padding: 0.05rem 0.1rem;
                margin-bottom: 0.38rem;
                border: none;
                background: transparent;
                box-shadow: none;
            }
            div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {
                line-height: 1.55;
            }
            div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
                background: rgba(223, 244, 255, 0.08);
            }
            div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
                background: transparent;
            }
            div[data-testid="stChatInput"] {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
            }
            div[data-testid="stChatInput"] > div {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }
            div[data-testid="stChatInput"] [data-baseweb="textarea"] {
                background: rgba(223, 244, 255, 0.08) !important;
                border: 1px solid rgba(198, 232, 252, 0.24) !important;
                border-radius: 14px !important;
                box-shadow: none !important;
                padding: 0.4rem 0.6rem !important;
            }
            div[data-testid="stChatInput"] [data-baseweb="base-input"] {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
            }
            div[data-testid="stChatInput"] textarea {
                background: transparent !important;
                border-radius: 12px;
                border: none !important;
                box-shadow: none !important;
                padding: 0.3rem 0.05rem !important;
                color: var(--text-main);
            }
            div[data-testid="stChatInput"] textarea::placeholder {
                color: #d9f0fd;
            }
            button[data-testid="stChatInputSubmitButton"] {
                background: transparent !important;
                border: none !important;
                color: var(--text-soft) !important;
                box-shadow: none !important;
            }
            button[data-testid="stChatInputSubmitButton"]:hover {
                color: var(--text-main) !important;
            }
            div[data-testid="stDataFrame"] {
                border: 1px solid rgba(198, 232, 252, 0.23);
                border-radius: 14px;
                overflow: hidden;
            }
            @media (max-width: 900px) {
                .shell {
                    border-radius: 18px;
                }
                .glass-card {
                    border-radius: 14px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if show_header:
        st.markdown(
            (
                "<div class='shell'>"
                f"<div class='shell-title'>{page_title}</div>"
                f"<p class='shell-subtitle'>{subtitle}</p>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )


def apply_home_page_styles() -> None:
    st.markdown(
        """
        <style>
            .home-left-shell {
                background: rgba(223, 244, 255, 0.14);
                border: 1px solid rgba(198, 232, 252, 0.32);
                border-radius: 18px;
                padding: 0.72rem;
                backdrop-filter: blur(12px);
                box-shadow: 0 10px 20px rgba(4, 36, 61, 0.18), inset 0 1px 1px rgba(233, 248, 255, 0.16);
            }
            .home-left-sticky {
                position: sticky;
                top: 0.8rem;
                max-height: calc(100vh - 2.1rem);
                overflow: hidden;
                display: flex;
                flex-direction: column;
            }
            .genie-panel-head {
                padding: 0.1rem 0.12rem 0.45rem 0.12rem;
                border-bottom: 1px solid rgba(198, 232, 252, 0.2);
                margin-bottom: 0.5rem;
            }
            .genie-panel-title {
                font-weight: 700;
                color: var(--text-main);
                margin-bottom: 0.2rem;
                font-size: 0.92rem;
                letter-spacing: 0.02em;
            }
            .genie-panel-caption {
                color: var(--text-soft);
                font-size: 0.72rem;
                line-height: 1.3;
            }
            .genie-panel-body {
                overflow-y: auto;
                padding-right: 0.16rem;
            }
            .genie-card {
                background: rgba(223, 244, 255, 0.09);
                border: 1px solid rgba(198, 232, 252, 0.22);
                border-left: 3px solid rgba(198, 232, 252, 0.45);
                border-radius: 12px;
                padding: 0.55rem 0.5rem;
                margin-bottom: 0.42rem;
                box-shadow: 0 6px 12px rgba(4, 36, 61, 0.12);
                transition: all 0.25s ease;
            }
            .genie-card.active {
                border-left-color: var(--accent);
                background: linear-gradient(160deg, rgba(114, 209, 255, 0.2) 0%, rgba(79, 181, 230, 0.12) 100%);
                box-shadow: 0 0 0 1px rgba(114, 209, 255, 0.5), 0 6px 12px rgba(79, 181, 230, 0.14);
            }
            .genie-title {
                color: var(--text-main);
                font-weight: 700;
                font-size: 0.76rem;
                line-height: 1.2;
                margin-bottom: 0.16rem;
            }
            .genie-status {
                font-size: 0.58rem;
                letter-spacing: 0.05em;
                font-weight: 700;
                margin-bottom: 0.18rem;
                color: var(--text-soft);
            }
            .genie-card.active .genie-status {
                color: #ebf8ff;
            }
            .genie-description {
                font-size: 0.63rem;
                color: var(--text-soft);
                line-height: 1.25;
            }
            .home-chat-head {
                background: rgba(223, 244, 255, 0.07);
                border: 1px solid rgba(198, 232, 252, 0.2);
                border-radius: 14px;
                padding: 0.7rem 0.85rem;
                margin-bottom: 0.5rem;
                backdrop-filter: blur(8px);
                box-shadow: 0 6px 14px rgba(4, 36, 61, 0.16);
            }
            .chat-header {
                color: var(--text-main);
                font-weight: 700;
                margin-bottom: 0.2rem;
                font-size: 1.04rem;
            }
            .chat-subtitle {
                color: var(--text-soft);
                margin-bottom: 0;
                font-size: 0.88rem;
            }
            @media (max-width: 900px) {
                .genie-description {
                    font-size: 0.72rem;
                }
                .home-chat-head,
                .home-left-shell {
                    border-radius: 18px;
                }
                .home-left-sticky {
                    position: static;
                    max-height: none;
                }
                .genie-panel-body {
                    overflow: visible;
                    padding-right: 0;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def open_glass_card() -> None:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)


def close_glass_card() -> None:
    st.markdown("</div>", unsafe_allow_html=True)
