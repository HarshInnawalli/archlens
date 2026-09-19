from typing import Any, Optional

import streamlit as st

from app.graph.workflow import build_graph


st.set_page_config(
    page_title="ArchLens",
    page_icon=":material/account_tree:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --ink: #fff7ed;
    --ink-strong: #fffdf8;
    --muted: #ecd9dd;
    --burgundy-darkest: #14060f;
    --burgundy: #3a0d20;
    --burgundy-light: #57132e;

    --gold: #e7b866;
    --gold-light: #f4d49a;

    --ok: #7fe0a6;
    --warn: #ffcf7a;
    --bad: #ff9c9c;

    --line: rgba(244, 212, 154, 0.22);
    --surface: rgba(28, 8, 18, 0.82);
    --surface-2: rgba(46, 11, 27, 0.88);
}

/* --------------------------------------------------
   ICON FONTS — must never be overridden by DM Sans,
   or Material ligatures render as literal words
   ("search", "download") stacked over the label.
   -------------------------------------------------- */

[data-testid="stIconMaterial"],
[data-testid^="stIcon"],
span.material-symbols-rounded,
span.material-symbols-outlined,
span.material-icons,
i.material-icons,
[class*="material-symbols"],
[class*="material-icons"] {
    font-family: 'Material Symbols Rounded', 'Material Symbols Outlined',
                 'Material Icons' !important;
    font-weight: normal !important;
    font-style: normal !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    line-height: 1 !important;
    font-feature-settings: 'liga';
    -webkit-font-feature-settings: 'liga';
    -webkit-font-smoothing: antialiased;
    flex: 0 0 auto;
}

/* --------------------------------------------------
   REMOVE SIDEBAR
   -------------------------------------------------- */

[data-testid="stSidebar"],
[data-testid="stSidebarNav"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: none !important;
    width: 0 !important;
}

/* --------------------------------------------------
   BACKGROUND
   -------------------------------------------------- */

.stApp {
    position: relative;
    overflow-x: hidden;
    background:
        radial-gradient(circle at 15% 15%, rgba(116, 31, 65, 0.55), transparent 30rem),
        radial-gradient(circle at 85% 80%, rgba(91, 20, 52, 0.45), transparent 28rem),
        linear-gradient(135deg, #180713 0%, #300b1d 42%, #4a1028 68%, #1d0714 100%);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.stApp::before,
.stApp::after {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
}

.stApp::before {
    opacity: 0.7;
    background-image:
        radial-gradient(circle, rgba(255, 247, 237, 0.85) 1px, transparent 1.5px),
        radial-gradient(circle, rgba(244, 212, 154, 0.65) 1px, transparent 1.5px),
        radial-gradient(circle, rgba(255, 255, 255, 0.45) 1px, transparent 1.5px);
    background-size: 110px 110px, 170px 170px, 230px 230px;
    background-position: 10px 20px, 60px 90px, 130px 40px;
    animation: star-drift 28s linear infinite;
}

.stApp::after {
    opacity: 0.22;
    background-image:
        radial-gradient(circle, rgba(244, 212, 154, 0.9) 1.2px, transparent 2px);
    background-size: 280px 280px;
    animation: star-drift-slow 45s linear infinite;
}

@keyframes star-drift {
    from { transform: translate3d(0, 0, 0); }
    to   { transform: translate3d(-80px, 100px, 0); }
}

@keyframes star-drift-slow {
    from { transform: translate3d(0, 0, 0); }
    to   { transform: translate3d(100px, -70px, 0); }
}

[data-testid="stAppViewContainer"] { position: relative; z-index: 1; }
[data-testid="stHeader"] { background: transparent; }

/* --------------------------------------------------
   TYPOGRAPHY  (font-family applied to text nodes only,
   never to generic span/div, so icons keep their font)
   -------------------------------------------------- */

h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: 0 !important;
    color: var(--ink-strong) !important;
}

.stApp p,
.stApp li,
.stApp label,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p,
.stApp small {
    color: var(--muted) !important;
}

.stApp a,
[data-testid="stMarkdownContainer"] a {
    color: var(--gold-light) !important;
    text-decoration: underline;
}

.stApp hr { border-color: var(--line) !important; }

.stApp code,
.stApp kbd {
    background: rgba(255, 247, 237, 0.10) !important;
    color: var(--gold-light) !important;
    border: 1px solid var(--line);
    border-radius: 5px;
    padding: 0.05rem 0.35rem;
}

.stApp pre,
[data-testid="stCode"] pre,
[data-testid="stCodeBlock"] pre {
    background: var(--burgundy-darkest) !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px;
}

.stApp pre code,
[data-testid="stCode"] code,
[data-testid="stCodeBlock"] code {
    background: transparent !important;
    color: #ffe9c9 !important;
    border: none !important;
}

.stApp blockquote {
    border-left: 3px solid var(--gold) !important;
    background: rgba(255, 247, 237, 0.06);
    color: var(--ink) !important;
    padding: 0.5rem 1rem;
    border-radius: 0 8px 8px 0;
}

.stApp table,
[data-testid="stTable"] table {
    background: var(--surface) !important;
    color: var(--ink) !important;
}

.stApp th {
    background: rgba(255, 247, 237, 0.10) !important;
    color: var(--gold-light) !important;
    border-color: var(--line) !important;
}

.stApp td {
    color: var(--ink) !important;
    border-color: var(--line) !important;
}

/* --------------------------------------------------
   HERO
   -------------------------------------------------- */

.hero {
    position: relative;
    overflow: hidden;
    padding: 2.5rem 2.7rem 2.7rem;
    margin: 0 0 1.8rem;
    border: 1px solid rgba(244, 212, 154, 0.30);
    border-radius: 20px;
    background:
        radial-gradient(circle at 90% 10%, rgba(244, 212, 154, 0.20), transparent 15rem),
        linear-gradient(120deg, #3a0d20 0%, #59132e 52%, #7a2842 100%);
    box-shadow:
        0 20px 55px rgba(0, 0, 0, 0.32),
        inset 0 1px 0 rgba(255, 255, 255, 0.08);
    animation: rise-in 650ms ease-out both;
}

.hero::after {
    content: '';
    position: absolute;
    width: 19rem;
    height: 19rem;
    right: -5rem;
    top: -8rem;
    border: 1px solid rgba(244, 212, 154, 0.35);
    border-radius: 50%;
    box-shadow:
        0 0 0 2rem rgba(244, 212, 154, 0.06),
        0 0 0 4rem rgba(244, 212, 154, 0.035);
    animation: drift 9s ease-in-out infinite;
}

.hero-kicker {
    position: relative;
    z-index: 1;
    margin: 0 0 0.5rem;
    color: var(--gold-light) !important;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.hero h1 {
    position: relative;
    z-index: 1;
    margin: 0;
    color: #fffaf2 !important;
    font-size: clamp(2.2rem, 5vw, 4.4rem);
    line-height: 1.02;
}

.hero-copy {
    position: relative;
    z-index: 1;
    max-width: 38rem;
    margin: 1rem 0 0;
    color: #f7e7e9 !important;
    font-size: 1.04rem;
    line-height: 1.55;
}

/* --------------------------------------------------
   FORM / INPUT
   -------------------------------------------------- */

[data-testid="stForm"] {
    border: 1px solid rgba(244, 212, 154, 0.20);
    border-radius: 16px;
    background: rgba(34, 8, 20, 0.72);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.22);
    backdrop-filter: blur(14px);
}

[data-testid="stWidgetLabel"] p {
    color: var(--gold-light) !important;
    font-weight: 600;
}

[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input {
    border: 1px solid rgba(244, 212, 154, 0.28);
    border-radius: 12px;
    background: rgba(18, 5, 12, 0.72) !important;
    color: #fff7ed !important;
    -webkit-text-fill-color: #fff7ed;
    font-size: 1rem;
    line-height: 1.55;
}

[data-testid="stTextArea"] textarea::placeholder,
[data-testid="stTextInput"] input::placeholder {
    color: rgba(255, 247, 237, 0.55) !important;
    -webkit-text-fill-color: rgba(255, 247, 237, 0.55);
}

[data-testid="stTextArea"] textarea:focus,
[data-testid="stTextInput"] input:focus {
    border-color: var(--gold);
    box-shadow: 0 0 0 1px rgba(231, 184, 102, 0.35);
}

/* --------------------------------------------------
   BUTTONS — flex layout so icon and label sit side by
   side with real spacing instead of stacking/overlapping
   -------------------------------------------------- */

.stButton > button,
.stFormSubmitButton > button,
[data-testid="stDownloadButton"] > button,
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-secondary"] {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.55rem !important;
    flex-wrap: nowrap !important;
    white-space: nowrap !important;
    overflow: hidden;
    text-overflow: ellipsis;

    min-height: 2.75rem;
    padding: 0.55rem 1.25rem !important;
    line-height: 1.35 !important;

    border: none;
    border-radius: 10px;
    background: linear-gradient(135deg, #d9a441, #f0c875);
    color: #26090f !important;
    font-weight: 700;
    box-shadow: 0 8px 25px rgba(217, 164, 65, 0.22);
    transition: box-shadow 180ms ease, filter 180ms ease;
}

.stButton > button p,
.stFormSubmitButton > button p,
[data-testid="stDownloadButton"] > button p,
.stButton > button div,
.stFormSubmitButton > button div,
[data-testid="stDownloadButton"] > button div {
    margin: 0 !important;
    padding: 0 !important;
    line-height: 1.35 !important;
    color: #26090f !important;
    white-space: nowrap;
}

.stButton > button [data-testid="stIconMaterial"],
.stFormSubmitButton > button [data-testid="stIconMaterial"],
[data-testid="stDownloadButton"] > button [data-testid="stIconMaterial"] {
    color: #26090f !important;
    font-size: 1.15rem !important;
    margin: 0 !important;
    position: static !important;
}

/* hover moves nothing — translateY was causing label smear on repaint */
.stButton > button:hover,
.stFormSubmitButton > button:hover,
[data-testid="stDownloadButton"] > button:hover {
    filter: brightness(1.06);
    box-shadow: 0 12px 30px rgba(217, 164, 65, 0.34);
}

.stButton > button:focus,
.stFormSubmitButton > button:focus,
[data-testid="stDownloadButton"] > button:focus {
    outline: 2px solid var(--gold-light);
    outline-offset: 2px;
    color: #26090f !important;
}

/* --------------------------------------------------
   CONTAINERS / EXPANDERS / STATUS
   -------------------------------------------------- */

[data-testid="stExpander"] {
    border: 1px solid rgba(244, 212, 154, 0.18) !important;
    border-radius: 12px;
    background: var(--surface) !important;
    overflow: hidden;
}

/* flex header: spinner/check icon + label never overlap */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] details > summary {
    display: flex !important;
    align-items: center !important;
    gap: 0.6rem !important;
    padding: 0.65rem 0.9rem !important;
    background: rgba(87, 19, 46, 0.65) !important;
    color: var(--ink-strong) !important;
    line-height: 1.4 !important;
}

[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: var(--ink-strong) !important;
    font-weight: 600;
    margin: 0 !important;
    line-height: 1.4 !important;
}

[data-testid="stExpander"] summary svg {
    fill: var(--gold-light) !important;
    flex: 0 0 auto;
}

[data-testid="stExpanderDetails"] {
    background: transparent !important;
    color: var(--ink) !important;
    padding-top: 0.6rem;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--line) !important;
    border-radius: 12px;
    background: var(--surface) !important;
}

[data-testid="stStatusWidget"],
div[data-testid="stStatus"] {
    background: var(--surface-2) !important;
    border: 1px solid var(--line) !important;
    color: var(--ink) !important;
}

/* status header row: icon, label, chevron in a row */
div[data-testid="stStatus"] > summary,
[data-testid="stStatusWidget"] summary {
    display: flex !important;
    align-items: center !important;
    gap: 0.6rem !important;
    white-space: normal !important;
}

div[data-testid="stStatus"] summary label,
div[data-testid="stStatus"] summary p {
    margin: 0 !important;
    line-height: 1.4 !important;
    color: var(--ink-strong) !important;
}

/* --------------------------------------------------
   ALERTS
   -------------------------------------------------- */

[data-testid="stAlert"],
[data-baseweb="notification"] {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    border-radius: 12px !important;
    border-left: 4px solid var(--gold) !important;
    background: rgba(30, 9, 19, 0.92) !important;
    color: var(--ink) !important;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.25);
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] li {
    color: var(--ink) !important;
    margin: 0 !important;
    line-height: 1.5 !important;
}

[data-testid="stAlert"] svg,
[data-testid="stAlert"] [data-testid="stIconMaterial"] {
    fill: var(--gold-light) !important;
    color: var(--gold-light) !important;
    flex: 0 0 auto;
}

[data-testid="stAlertContentSuccess"] { border-left-color: var(--ok) !important; }
[data-testid="stAlertContentWarning"] { border-left-color: var(--warn) !important; }
[data-testid="stAlertContentError"],
[data-testid="stAlertContentException"] { border-left-color: var(--bad) !important; }

[data-testid="stException"],
[data-testid="stExceptionMessage"] {
    background: var(--burgundy-darkest) !important;
    color: #ffdede !important;
    border: 1px solid rgba(255, 156, 156, 0.35) !important;
    border-radius: 10px;
}

/* --------------------------------------------------
   JSON VIEWER
   -------------------------------------------------- */

[data-testid="stJson"] {
    background: var(--burgundy-darkest) !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px;
    padding: 0.6rem 0.8rem;
}

[data-testid="stJson"] * { background: transparent !important; }
[data-testid="stJson"] span { color: #ffe9c9 !important; }

/* --------------------------------------------------
   METRICS
   -------------------------------------------------- */

[data-testid="stMetric"] {
    border-left: 3px solid var(--gold);
    padding: 0.8rem 1rem;
    border-radius: 8px;
    background: rgba(255, 247, 237, 0.08);
    overflow: hidden;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: var(--muted) !important;
    font-weight: 600;
    line-height: 1.4 !important;
}

[data-testid="stMetricValue"] {
    color: var(--gold-light) !important;
    line-height: 1.25 !important;
}

/* --------------------------------------------------
   TABS / PROGRESS / TOOLTIPS
   -------------------------------------------------- */

[data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--line);
    gap: 0.35rem;
}

button[data-baseweb="tab"] {
    background: transparent !important;
    white-space: nowrap;
}

button[data-baseweb="tab"] p {
    color: var(--muted) !important;
    font-weight: 600;
    margin: 0 !important;
}

button[data-baseweb="tab"][aria-selected="true"] p {
    color: var(--gold-light) !important;
}

[data-baseweb="tab-highlight"] { background: var(--gold) !important; }
[data-baseweb="tab-panel"] { background: transparent !important; color: var(--ink) !important; }

[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #d9a441, #f4d49a) !important;
}

[data-testid="stProgress"] > div > div > div {
    background: rgba(255, 247, 237, 0.14) !important;
}

[data-baseweb="tooltip"],
[data-baseweb="popover"] div {
    background: var(--burgundy-darkest) !important;
    color: var(--ink) !important;
}

@keyframes rise-in {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes drift {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    50%      { transform: translate(-14px, 10px) rotate(8deg); }
}

</style>
""",
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------
# PROCESS STEP DEFINITIONS
# ----------------------------------------------------------------------

# node -> (step number, title, message, scope)
PROCESS_STEPS: dict[str, tuple[str, str, str, str]] = {
    "extract_claims": (
        "01",
        "Mapping the architecture",
        "Understanding the proposed components, constraints, and assumptions.",
        "global",
    ),
    "generate_support_query": (
        "02",
        "Identifying what to verify",
        "Formulating a focused search for evidence that supports this claim.",
        "claim",
    ),
    "generate_challenge_query": (
        "03",
        "Testing the assumption",
        "Formulating a second search for limitations, trade-offs, and failure conditions.",
        "claim",
    ),
    "retrieve_support_evidence": (
        "04",
        "Looking for supporting evidence",
        "Searching the technical corpus for evidence consistent with this claim.",
        "claim",
    ),
    "retrieve_challenge_evidence": (
        "05",
        "Looking for counter-evidence",
        "Searching the corpus for limitations, caveats, and contradicting findings.",
        "claim",
    ),
    "check_evidence_sufficiency": (
        "06",
        "Checking evidence coverage",
        "Determining whether the retrieved evidence is sufficient for a meaningful assessment.",
        "claim",
    ),
    "refine_queries": (
        "07",
        "Refining the investigation",
        "Expanding the search where important aspects of this claim remain unsupported.",
        "claim",
    ),
    "assess_claim": (
        "08",
        "Assessing the claim",
        "Comparing this claim against the available supporting and challenging evidence.",
        "claim",
    ),
    "move_to_next_claim": (
        "09",
        "Closing out this claim",
        "Review of this claim is complete.",
        "claim",
    ),
    "generate_final_report": (
        "10",
        "Building the evidence trail",
        "Assembling the findings, evidence, and unresolved questions into the final review.",
        "global",
    ),
}

CLAIM_STEP_ORDER = [node for node, meta in PROCESS_STEPS.items() if meta[3] == "claim"]

REFINEMENT_NODE = "refine_queries"
ASSESS_NODE = "assess_claim"
ADVANCE_NODE = "move_to_next_claim"


@st.cache_resource
def get_graph():
    return build_graph()


# ----------------------------------------------------------------------
# LIVE PROCESS TRACKER  (native Streamlit widgets only — no HTML)
# ----------------------------------------------------------------------

class ProcessTracker:
    """
    Renders the live run scoped to the claim currently under review.

    - One row per node, so a node revisited during refinement updates its row
      with a pass counter rather than appending a duplicate.
    - The panel is rebuilt whenever the claim changes, so the previous claim's
      steps disappear as the review moves on.
    - Step 08 states whether step 07 ran or was skipped for this claim.
    """

    def __init__(self, panel: Any, progress: Any) -> None:
        self.panel = panel
        self.progress = progress

        self.scope_key: Optional[str] = None
        self.steps: dict[str, dict[str, Any]] = {}
        self.order: list[str] = []
        self.refined = False
        self.pending_reset = False

        self.claim_number: Optional[int] = None
        self.total_claims: Optional[int] = None
        self.claim_text = ""
        self.completed_claims = 0
        self.event_count = 0

    # -- state reading ------------------------------------------------

    @staticmethod
    def _claim_index(state: dict[str, Any]) -> Optional[int]:
        for key in (
            "current_claim_index",
            "claim_index",
            "current_claim_idx",
            "claim_pointer",
        ):
            value = state.get(key)
            if isinstance(value, int):
                return value
        return None

    @staticmethod
    def _total_claims(state: dict[str, Any]) -> Optional[int]:
        claims = state.get("claims")
        if isinstance(claims, list) and claims:
            return len(claims)
        return None

    @staticmethod
    def _claim_text(state: dict[str, Any], index: Optional[int]) -> str:
        claims = state.get("claims")
        if not isinstance(claims, list) or index is None:
            return ""
        if 0 <= index < len(claims):
            claim = claims[index]
            if isinstance(claim, dict):
                return str(claim.get("claim", "")).strip()
            return str(claim).strip()
        return ""

    # -- event handling -----------------------------------------------

    def handle(self, node_name: str, state: dict[str, Any]) -> None:
        self.event_count += 1

        step_no, title, message, scope = PROCESS_STEPS.get(
            node_name,
            ("··", "Reviewing architecture", "Processing the architecture review.", "claim"),
        )

        index = self._claim_index(state)
        self.total_claims = self._total_claims(state) or self.total_claims
        claim_text = self._claim_text(state, index)

        if scope == "global":
            scope_key = f"global:{node_name}"
            self.claim_number = None
        else:
            self.claim_number = (index + 1) if index is not None else self.claim_number
            scope_key = f"claim:{index if index is not None else 'current'}"

        # a new claim (or a new global phase) clears the previous steps
        if self.pending_reset or scope_key != self.scope_key:
            self.scope_key = scope_key
            self.steps = {}
            self.order = []
            self.refined = False
            self.claim_text = claim_text

        self.pending_reset = node_name == ADVANCE_NODE
        if node_name == ADVANCE_NODE:
            self.completed_claims += 1

        if node_name == REFINEMENT_NODE:
            self.refined = True

        if claim_text:
            self.claim_text = claim_text

        if node_name in self.steps:
            self.steps[node_name]["passes"] += 1
        else:
            self.steps[node_name] = {
                "no": step_no,
                "title": title,
                "message": message,
                "passes": 1,
                "note": None,
            }
            self.order.append(node_name)

        if node_name == ASSESS_NODE:
            self.steps[node_name]["note"] = (
                "Step 07 refinement: ran before this assessment"
                if self.refined
                else "Step 07 refinement: skipped — evidence was already sufficient"
            )

        for key in self.steps:
            self.steps[key]["active"] = key == node_name

        self._render()
        self._advance_progress(scope, step_no)

    # -- rendering ----------------------------------------------------

    def _scope_line(self) -> str:
        if self.claim_number is None:
            return "Architecture review"
        if self.total_claims:
            return f"Claim {self.claim_number} of {self.total_claims}"
        return f"Claim {self.claim_number}"

    def _render(self) -> None:
        with self.panel.container(border=True):
            st.markdown(f"**{self._scope_line()}**")

            if self.claim_text:
                detail = (
                    self.claim_text
                    if len(self.claim_text) <= 160
                    else self.claim_text[:157].rstrip() + "…"
                )
                st.caption(detail)

            for node_name in self.order:
                step = self.steps[node_name]
                active = step.get("active", False)

                marker = "▶" if active else "✓"
                passes = f"  ·  pass {step['passes']}" if step["passes"] > 1 else ""
                st.markdown(f"{marker}  **{step['no']} · {step['title']}**{passes}")

                if active:
                    st.caption(step["message"])

                if step["note"]:
                    st.caption(step["note"])

    def _advance_progress(self, scope: str, step_no: str) -> None:
        if scope == "global":
            fraction = 0.04 if step_no == "01" else 0.97
        elif self.total_claims and self.claim_number:
            try:
                active_node = next(k for k in self.steps if self.steps[k].get("active"))
                inner = CLAIM_STEP_ORDER.index(active_node) / max(
                    len(CLAIM_STEP_ORDER) - 1, 1
                )
            except (StopIteration, ValueError):
                inner = 0.5
            done = (self.claim_number - 1 + inner) / self.total_claims
            fraction = 0.05 + 0.9 * min(done, 1.0)
        else:
            fraction = min(self.event_count / 40, 0.9)

        self.progress.progress(min(max(fraction, 0.02), 0.97))

    def finish(self) -> None:
        self.progress.progress(1.0)
        with self.panel.container(border=True):
            st.markdown("**Review complete**")
            st.caption(
                "Findings, evidence, and unresolved questions are ready below."
            )


# ----------------------------------------------------------------------
# RESULT RENDERING
# ----------------------------------------------------------------------

def verdict_marker(verdict: str) -> str:
    key = str(verdict or "").strip().lower()
    if "insufficient" in key or "unsupported" in key:
        return "◐"
    if "challeng" in key or "contradict" in key or "refut" in key:
        return "✕"
    if "support" in key:
        return "✓"
    return "•"


def render_evidence(evidence: list[dict[str, Any]]) -> None:
    if not evidence:
        st.info("No evidence was selected.")
        return

    for index, item in enumerate(evidence, start=1):
        score = item.get("rerank_score", item.get("score", 0)) or 0
        title = f"{index}. {item.get('source') or 'Unknown source'}  ·  score {float(score):.3f}"

        with st.expander(title):
            st.markdown(item.get("text", ""))

            metadata = {
                "Document ID": item.get("document_id"),
                "Chunk ID": item.get("chunk_id"),
                "Technology": item.get("technology"),
                "Topic": item.get("topic"),
                "Document type": item.get("document_type"),
                "Section": item.get("section"),
                "File": item.get("file_path"),
                "URL": item.get("url"),
            }

            st.json({k: v for k, v in metadata.items() if v is not None})


def render_assessment(index: int, assessment: dict[str, Any]) -> None:
    verdict = assessment.get("verdict", "Unknown")
    claim = assessment.get("claim", "Unnamed claim")
    short_claim = claim if len(claim) <= 90 else claim[:87].rstrip() + "…"

    header = f"{verdict_marker(verdict)}  Claim {index} · {verdict} — {short_claim}"

    with st.expander(header, expanded=index == 1):
        st.markdown(f"**Claim {index}**")
        st.write(claim)

        col1, col2, col3 = st.columns(3)
        col1.metric("Verdict", verdict)
        col2.metric("Importance", assessment.get("importance", "Unknown"))

        iterations = assessment.get("refinement_iterations", 0) or 0
        col3.metric("Refinement iterations", iterations)

        st.markdown("**Refinement**")
        if iterations:
            st.caption(f"Step 07 refinement ran {iterations}× for this claim.")
        else:
            st.caption(
                "Step 07 refinement was skipped — the evidence was already sufficient."
            )

        st.markdown("**Reasoning**")
        st.write(assessment.get("reasoning", ""))

        st.markdown("**Evidence sufficiency**")
        st.write(
            assessment.get(
                "evidence_sufficiency_reasoning",
                "No sufficiency reasoning available.",
            )
        )

        missing_aspects = assessment.get("missing_evidence_aspects", [])
        if missing_aspects:
            st.markdown("**Missing evidence aspects**")
            for aspect in missing_aspects:
                st.markdown(f"- {aspect}")

        missing_information = assessment.get("missing_information", [])
        if missing_information:
            st.markdown("**Missing information**")
            for item in missing_information:
                st.markdown(f"- {item}")

        supporting = assessment.get("supporting_evidence", [])
        challenging = assessment.get("challenging_evidence", [])

        if supporting:
            st.markdown("**Supporting evidence**")
            render_evidence(supporting)

        if challenging:
            st.markdown("**Challenging evidence**")
            render_evidence(challenging)


def render_results(result: dict[str, Any]) -> None:
    claims = result.get("claims", [])
    requirements = result.get("requirements", [])
    assessments = result.get("claim_assessments", [])
    final_report = result.get("final_report", "No final report was generated.")

    st.download_button(
        label="Download report",
        data=final_report,
        file_name="archlens-report.md",
        mime="text/markdown",
    )

    report_tab, claims_tab, requirements_tab, evidence_tab = st.tabs(
        ["Final report", "Claims", "Requirements", "Evidence"]
    )

    with report_tab:
        st.markdown(final_report)

    with claims_tab:
        if not claims:
            st.info("No architecture claims were extracted.")
        else:
            for index, claim in enumerate(claims, start=1):
                with st.container(border=True):
                    st.markdown(f"### Claim {index}")
                    st.write(claim.get("claim", ""))

                    col1, col2 = st.columns(2)
                    col1.caption(f"Category: {claim.get('category', 'Unknown')}")
                    col2.caption(f"Importance: {claim.get('importance', 'Unknown')}")

            st.divider()
            st.subheader("Claim assessments")

            for index, assessment in enumerate(assessments, start=1):
                render_assessment(index, assessment)

    with requirements_tab:
        if not requirements:
            st.info("No explicit requirements were extracted.")
        else:
            for index, requirement in enumerate(requirements, start=1):
                with st.container(border=True):
                    st.markdown(f"### Requirement {index}")
                    st.write(requirement.get("requirement", ""))

                    col1, col2 = st.columns(2)
                    col1.caption(f"Category: {requirement.get('category', 'Unknown')}")
                    col2.caption(f"Importance: {requirement.get('importance', 'Unknown')}")

    with evidence_tab:
        if not assessments:
            st.info("No evidence is available.")
        else:
            for index, assessment in enumerate(assessments, start=1):
                st.markdown(f"### Claim {index}: {assessment.get('claim', '')}")

                support_col, challenge_col = st.columns(2)

                with support_col:
                    st.markdown("**Supporting**")
                    render_evidence(assessment.get("supporting_evidence", []))

                with challenge_col:
                    st.markdown("**Challenging**")
                    render_evidence(assessment.get("challenging_evidence", []))


# ----------------------------------------------------------------------
# PAGE
# ----------------------------------------------------------------------

st.markdown(
    """
<section class="hero">
    <h1>ArchLens</h1>
    <p class="hero-copy">
        Turn an architecture description into a grounded review of its claims,
        constraints, trade-offs, and supporting evidence.
    </p>
</section>
""",
    unsafe_allow_html=True,
)

default_architecture = """I am building an event-driven order processing system.

Clients communicate with an HTTP API gateway.
The API publishes order events to Apache Kafka.
Several backend services consume Kafka topics asynchronously.
PostgreSQL stores transactional order data.
The system must process 50,000 orders per second.
Losing an order event is unacceptable.
"""

with st.form("architecture_review"):
    architecture = st.text_area(
        "Architecture description",
        value=default_architecture,
        height=300,
        placeholder="Describe the architecture, workloads, constraints, and priorities.",
    )

    submitted = st.form_submit_button(
        "Analyze architecture",
        type="primary",
        use_container_width=True,
    )

if submitted:
    if not architecture.strip():
        st.error("Enter an architecture description first.")
        st.stop()

    try:
        with st.status("Reviewing your architecture", expanded=True) as status:
            panel = st.empty()
            progress = st.progress(0.0)

            tracker = ProcessTracker(panel, progress)
            streamed_state: dict[str, Any] = {"architecture": architecture.strip()}

            for event in get_graph().stream(
                {"architecture": architecture.strip()},
                stream_mode="updates",
            ):
                for node_name, update in event.items():
                    if isinstance(update, dict):
                        streamed_state.update(update)

                    tracker.handle(node_name, streamed_state)

            tracker.finish()
            status.update(
                label="Architecture review complete",
                state="complete",
                expanded=False,
            )

        st.session_state["review_result"] = streamed_state

    except Exception as error:
        st.error("The architecture review failed.")
        st.exception(error)

result = st.session_state.get("review_result")

if result:
    render_results(result)
else:
    st.info("Enter an architecture description and start a review.")