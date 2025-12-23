import streamlit as st

st.set_page_config(layout="wide")

# CSS pour forcer l'affichage sur un seul écran et réduire les polices
st.markdown("""
    <style>
    .block-container {padding: 0.5rem 1rem;}
    .stTextInput input {height: 25px; padding: 2px !important; font-size: 14px !important;}
    div[data-testid="stVerticalBlock"] {gap: 0.1rem !important;}
    p {margin-bottom: 0px !important; font-weight: bold; font-size: 13px;}
    </style>
    """, unsafe_allow_html=True)

# --- LIGNE 1 : CONFIG (Très compacte) ---
c1, c2, c3, c4, c5 = st.columns([1.5, 1, 1, 1.5, 1])
with c1: nuance = st.selectbox("Nuance", ["7778", "7777", "6129", "6718", "6729"]) # simplifé pour l'exemple
with c2: circuit = st.selectbox("Ckt", [4, 5])
with c3: poids = st.text_input("Poids(t)", "0.0")
pk = float(poids.replace(',','.'))*1000 if poids else 0

# --- LIGNE 1 SUITE : DESULF ---
with c4: 
    s1 = st.text_input("S-Init", "0")
    s2 = st.text_input("S-Fin", "0")
with c5:
    st.write("Taux")
    if s1 and s2 and float(s1) > 0:
        tx = (float(s1)-float(s2))/float(s1)*100
        st.code(f"{tx:.1f}%")

st.write("---")

# --- GRILLE DES MÉTAUX (Affichage en 3 colonnes) ---
# On simule ici 9 métaux pour montrer que ça tient
metaux = ["Aluminium", "Carbone", "Calcium", "Bore", "Manganèse", "Nobium", "Silicium", "Titane", "Chrome"]
saisies = {}

cols = st.columns(3) # On crée 3 colonnes principales
for i, m in enumerate(metaux):
    target_col = cols[i % 3] # On répartit les métaux
    with target_col:
        # Pour chaque métal, on crée une sous-ligne compacte
        r1, r2, r3, r4 = st.columns([1.5, 1, 1, 1.2])
        with r1: st.write(f"{m[:6]}.")
        with r2: a = st.text_input("A", key=f"a{i}", label_visibility="collapsed", placeholder="Ana")
        with r3: v = st.text_input("V", key=f"v{i}", label_visibility="collapsed", placeholder="Vis")
        with r4: 
            # CALCUL EN DIRECT SANS BOUTON (Optionnel)
            if a and v and pk > 0:
                res = (float(v)-float(a)) * 10 # Calcul simplifié pour l'exemple
                st.markdown(f"**{res/1000:.2f}**")
            else: st.write("0.00")

st.write("---")
st.caption("Designed by Alexandre Cardone")
