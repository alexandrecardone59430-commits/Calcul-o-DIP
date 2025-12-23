import streamlit as st
import pandas as pd

# Configuration pour maximiser l'espace
st.set_page_config(page_title="Calculateur", layout="wide")

# Style CSS pour supprimer les marges inutiles en haut et réduire l'espacement des blocs
st.markdown("""
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    div.stButton > button {width: 100%; border-radius: 5px; height: 3em;}
    hr {margin: 0.5em 0px;}
    .stTextInput>div>div>input {padding: 5px;}
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DONNÉES --- (Simplifiée pour le code, garde ta version complète)
DATA = {
    "7778": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (12, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (90, 78)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "Titane": {4: (75, 69)}},
    "7777": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    # ... (Ajoute tes autres nuances ici)
}

# --- EN-TÊTE COMPACT ---
c1, c2, c3 = st.columns([1.5, 1, 1.2])
with c1:
    nuance = st.selectbox("Nuance", sorted(DATA.keys()))
with c2:
    circuit = st.selectbox("Ckt", [4, 5])
with c3:
    poids_t = st.text_input("Poids(t)", placeholder="0.0")
    poids_kg = float(poids_t.replace(',', '.')) * 1000 if poids_t else 0.0

st.divider()

# --- BLOC DÉSULFURATION ---
col_s1, col_s2, col_s3 = st.columns([1, 1, 1.5])
with col_s1:
    s_init = st.text_input("S Init", key="si")
with col_s2:
    s_final = st.text_input("S Fin", key="sf")
with col_s3:
    st.write(" ") # Alignement
    if st.button("CALC S"):
        if s_init and s_final:
            v_i = float(s_init.replace(',','.'))
            v_f = float(s_final.replace(',','.'))
            st.info(f"Retrait: {((v_i-v_f)/v_i)*100:.1f}%")

st.divider()

# --- GRILLE D'ANALYSES (3 éléments par ligne pour éviter de défiler) ---
elements = DATA[nuance]
ordre = []
if "manganèse" in elements:
    ordre.append(("Mn Carb", "mn_carb", 78, elements["manganèse"]))
    ordre.append(("Mn Affi", "mn_affi", 82, elements["manganèse"]))
for k, v in elements.items():
    if k != "manganèse":
        ordre.append((k.capitalize()[:5], k, None, v))

saisies = {}
# On crée des lignes de 3 colonnes pour tout condenser
for i in range(0, len(ordre), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(ordre):
            label, key_id, ten_f, circs = ordre[i+j]
            with cols[j]:
                # On met ANA et VIS sur la même ligne pour chaque élément
                st.write(f"**{label}**")
                a = st.text_input("A", key=f"a_{key_id}", label_visibility="collapsed", placeholder="Ana")
                v = st.text_input("V", key=f"v_{key_id}", label_visibility="collapsed", placeholder="Vis")
                saisies[key_id] = {"ana": float(a.replace(',','.')) if a else 0.0, "vis": float(v.replace(',','.')) if v else 0.0, 
                                   "label": label, "teneur_fixe": ten_f, "circuits": circs, "ana_str": a or "0", "vis_str": v or "0"}

# --- BOUTONS FINAUX ---
st.write(" ")
cb1, cb2 = st.columns(2)
with cb1:
    btn_calc = st.button("CALCULER", type="primary")
with cb2:
    if st.button("RAZ"): st.rerun()

# --- RÉSULTATS (Tableau petit format) ---
if btn_calc and poids_kg > 0:
    res = []
    carb_induit = 0.0
    # Calcul Mn Carb pour le carbone induit
    d_mn = saisies.get("mn_carb")
    if d_mn and d_mn["vis"] > d_mn["ana"]:
        r, _ = d_mn["circuits"].get(circuit, (0,0))
        if r > 0:
            carb_induit = (((d_mn["vis"]-d_mn["ana"])/100*poids_kg)/(0.78*r/100)) * 0.067 / poids_kg * 100

    for kid, d in saisies.items():
        ana_eff = d["ana"] + (carb_induit if kid == "carbone" else 0)
        rend, ten_t = d["circuits"].get(circuit, (0,0))
        ten = d["teneur_fixe"] or ten_t
        ajout = 0.0
        if d["vis"] > ana_eff and rend > 0:
            ajout = ((d["vis"]-ana_eff)/100*poids_kg)/(ten/100*rend/100)
        res.append({"M": d["label"], "Ajout(kg)": round(ajout, 1)})
    
    st.table(pd.DataFrame(res))
    if carb_induit > 0: st.caption(f"Carbone induit: +{carb_induit:.3f}")

st.caption("Designed by Alexandre Cardone")
