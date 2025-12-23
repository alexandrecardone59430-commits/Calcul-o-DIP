import streamlit as st
import pandas as pd

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Calculateur Fonderie", layout="centered")

# --- BASE DE DONNÉES ---
DATA = {
    "6149": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 82)}, "nobium": {5: (92, 66)}, "silicium": {5: (100, 76)}, "titane": {5: (84, 69)}},
    "6748": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 82)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "titane": {5: (84, 69)}},
    "6868": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (89, 19)}, "manganèse": {5: (100, 82)}, "nobium": {5: (91, 66)}, "silicium": {5: (90, 76)}, "titane": {5: (83, 69)}},
    "6869": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (89, 19)}, "manganèse": {5: (100, 82)}, "nobium": {5: (91, 66)}, "silicium": {5: (90, 76)}, "titane": {5: (83, 69)}},
    "7787": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (17, 99), 5: (17, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 82), 5: (100, 82)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "titane": {4: (85, 69), 5: (83, 69)}},
    "7718": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (12, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (96, 82)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "titane": {4: (75, 69)}},
    "7778": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (12, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (96, 78)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "Titane": {4: (75, 69)}},
    "7777": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "6129": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6718": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6729": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (18, 99), 5: (18, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6758": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (20, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6759": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (18, 99), 5: (18, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (86, 69), 5: (82, 69)}},
    "6768": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6788": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (16, 99), 5: (16, 99)}, "bore": {4: (93, 19), 5: (93, 19)}, "manganèse": {4: (96, 78), 5: (96, 78)}, "nobium": {4: (90, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (84, 69), 5: (84, 69)}},
    "6828": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6838": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6858": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "7758": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7759": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7779": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7929": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (15, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (96, 78)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "Titane": {4: (75, 69)}},
    "7969": {"aluminium": {4: (100, 94)}, "carbone": {4: (100, 100)}, "calcium": {4: (13, 99)}, "bore": {4: (89, 19)}, "manganèse": {4: (100, 78)}, "nobium": {4: (94, 66)}, "silicium": {4: (90, 76)}, "Titane": {4: (82, 69)}},
    "7978": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (93, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "4647": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}}
}

# --- ÉTAT DE L'APPLICATION (RESET) ---
if 'reset' not in st.session_state:
    st.session_state.reset = False

def reset_fields():
    st.session_state.reset = True

# --- TITRE ET SIGNATURE ---
st.title("🚀 Calculateur Fonderie")
st.caption("Développé par CARDONE Alexandre")

# --- SECTION DÉSULFURATION ---
with st.expander("📉 DÉSULFURATION", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        s_init = st.number_input("S Init", value=0.0, format="%.4f")
    with col2:
        s_fin = st.number_input("S Fin", value=0.0, format="%.4f")
    with col3:
        if s_init > 0:
            taux = ((s_init - s_fin) / s_init) * 100
            st.metric("Taux %", f"{taux:.2f}%")
        else:
            st.metric("Taux %", "0.00%")

# --- CONFIGURATION ---
st.subheader("⚙️ Configuration")
c1, c2, c3 = st.columns([2, 1, 2])
with c1:
    nuance_selected = st.selectbox("NUANCE", sorted(list(DATA.keys())))
with c2:
    circuit_selected = st.selectbox("CIRCUIT", [4, 5])
with c3:
    poids_poche = st.number_input("POIDS (Tonnes)", value=0.0, step=0.1)

# --- CALCULS ---
st.divider()
st.subheader("🧪 Analyse et Visée")

elements_data = DATA[nuance_selected]
resultats = {}
apport_carb_mn = 0.0

# On crée d'abord les lignes pour le Manganèse pour calculer l'apport carbone
col_labels = st.columns([2, 2, 2, 2])
col_labels[0].write("**Élément**")
col_labels[1].write("**Analyse (%)**")
col_labels[2].write("**Visée (%)**")
col_labels[3].write("**Ajout (kg)**")

inputs = {}

for label, circuits in elements_data.items():
    if label == "manganèse":
        # Ligne Mn Carb
        c_mn1, c_mn2, c_mn3, c_mn4 = st.columns([2, 2, 2, 2])
        c_mn1.write("Mn Carb (78%)")
        ana_mnc = c_mn2.number_input("Ana MnC", label_visibility="collapsed", key="ana_mnc", format="%.3f")
        vis_mnc = c_mn3.number_input("Vis MnC", label_visibility="collapsed", key="vis_mnc", format="%.3f")
        
        rend_mn = circuits.get(circuit_selected, (100, 0))[0]
        if vis_mnc > ana_mnc and poids_poche > 0:
            ajout_mnc = ((vis_mnc - ana_mnc) / 100 * (poids_poche * 1000)) / (0.78 * rend_mn / 100)
            apport_carb_mn = (ajout_mnc * 0.067) / (poids_poche * 1000) * 100
            c_mn4.info(f"{ajout_mnc:.2f}")
        else:
            c_mn4.write("0.00")

        # Ligne Mn Affi
        c_mna1, c_mna2, c_mna3, c_mna4 = st.columns([2, 2, 2, 2])
        c_mna1.write("Mn Affi (82%)")
        ana_mna = c_mna2.number_input("Ana MnA", label_visibility="collapsed", key="ana_mna", format="%.3f")
        vis_mna = c_mna3.number_input("Vis MnA", label_visibility="collapsed", key="vis_mna", format="%.3f")
        
        if vis_mna > ana_mna and poids_poche > 0:
            ajout_mna = ((vis_mna - ana_mna) / 100 * (poids_poche * 1000)) / (0.82 * rend_mn / 100)
            c_mna4.info(f"{ajout_mna:.2f}")
        else:
            c_mna4.write("0.00")
            
    else:
        # Autres éléments
        ce1, ce2, ce3, ce4 = st.columns([2, 2, 2, 2])
        ce1.write(label.capitalize())
        ana = ce2.number_input(f"Ana {label}", label_visibility="collapsed", key=f"ana_{label}", format="%.4f")
        vis = ce3.number_input(f"Vis {label}", label_visibility="collapsed", key=f"vis_{label}", format="%.4f")
        
        rend, ten_base = circuits.get(circuit_selected, (100, 100))
        
        if label == "carbone":
            ana_corrige = ana + apport_carb_mn
            st.warning(f"C corrigé (Mn) : {ana_corrige:.3f}%")
            if vis > ana_corrige and poids_poche > 0:
                ajout = ((vis - ana_corrige) / 100 * (poids_poche * 1000)) / (ten_base / 100 * rend / 100)
                ce4.success(f"{ajout:.2f}")
            else:
                ce4.write("0.00")
        else:
            if vis > ana and poids_poche > 0:
                ajout = ((vis - ana) / 100 * (poids_poche * 1000)) / (ten_base / 100 * rend / 100)
                ce4.info(f"{ajout:.2f}")
            else:
                ce4.write("0.00")

# --- BOUTON RAZ ---
st.divider()
if st.button("🔄 REMISE À ZÉRO (RAZ)", on_click=reset_fields, use_container_width=True):
    st.rerun()

# --- STYLISATION CSS ---
st.markdown("""
    <style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #16a085;
    }
    </style>
    """, unsafe_allow_html=True)
