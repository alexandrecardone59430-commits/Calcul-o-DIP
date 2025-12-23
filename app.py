import streamlit as st
import pandas as pd

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Calculateur Fonderie Pro", layout="centered")

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

# --- ENTÊTE ---
st.title("🔩 Calculateur Fonderie")
st.caption("Développé par CARDONE Alexandre")

# --- PARAMÈTRES GÉNÉRAUX ---
col_cfg1, col_cfg2, col_cfg3 = st.columns([2,1,2])
with col_cfg1:
    nuance = st.selectbox("NUANCE", sorted(DATA.keys()))
with col_cfg2:
    circuit = st.selectbox("CIRCUIT", [4, 5])
with col_cfg3:
    poids = st.number_input("POIDS (T)", value=0.0, step=1.0, format="%g")

st.divider()

# --- SAISIE DES DONNÉES ---
results_list = []
apport_c_via_mn = 0.0

# 1. DÉSULFURATION
with st.expander("📉 DÉSULFURATION"):
    c1, c2 = st.columns(2)
    s_init = c1.number_input("S Initial", value=0.0, step=0.0001, format="%g")
    s_fin = c2.number_input("S Final", value=0.0, step=0.0001, format="%g")
    if s_init > 0:
        tx = ((s_init - s_fin) / s_init) * 100
        st.info(f"Taux de désulfuration : {tx:g} %")

# 2. MANGANÈSE (POUR CALCUL C)
with st.expander("✨ MANGANÈSE"):
    rend_mn = DATA[nuance]["manganèse"].get(circuit, (100, 0))[0]
    
    # Mn Carb
    st.write("**Manganèse Carburé (78%)**")
    mc1, mc2 = st.columns(2)
    mnc_ana = mc1.number_input("Analyse Mn Carb", value=0.0, format="%g", key="mnc_a")
    mnc_vis = mc2.number_input("Visée Mn Carb", value=0.0, format="%g", key="mnc_v")
    aj_mnc = 0.0
    if mnc_vis > mnc_ana and poids > 0:
        aj_mnc = ((mnc_vis - mnc_ana) / 100 * (poids * 1000)) / (0.78 * rend_mn / 100)
        apport_c_via_mn = (aj_mnc * 0.067) / (poids * 1000) * 100
    results_list.append({"Élément": "Mn Carb (78%)", "Analyse": mnc_ana, "Visée": mnc_vis, "Ajout (kg)": round(aj_mnc, 2)})

    # Mn Affiné
    st.write("**Manganèse Affiné (82%)**")
    ma1, ma2 = st.columns(2)
    mna_ana = ma1.number_input("Analyse Mn Affi", value=0.0, format="%g", key="mna_a")
    mna_vis = ma2.number_input("Visée Mn Affi", value=0.0, format="%g", key="mna_v")
    aj_mna = 0.0
    if mna_vis > mna_ana and poids > 0:
        aj_mna = ((mna_vis - mna_ana) / 100 * (poids * 1000)) / (0.82 * rend_mn / 100)
    results_list.append({"Élément": "Mn Affi (82%)", "Analyse": mna_ana, "Visée": mna_vis, "Ajout (kg)": round(aj_mna, 2)})

# 3. AUTRES ÉLÉMENTS
for elem, config in DATA[nuance].items():
    if elem == "manganèse": continue
    
    with st.expander(f"💎 {elem.upper()}"):
        c1, c2 = st.columns(2)
        ana = c1.number_input(f"Analyse {elem}", value=0.0, format="%g", key=f"{elem}_a")
        vis = c2.number_input(f"Visée {elem}", value=0.0, format="%g", key=f"{elem}_v")
        
        rend, teneur = config.get(circuit, (100, 100))
        ajout = 0.0
        
        if elem == "carbone":
            ana_reel = ana + apport_c_via_mn
            if apport_c_via_mn > 0:
                st.warning(f"Note: Apport C via Mn = +{apport_c_via_mn:g}% (Ana réelle: {ana_reel:g}%)")
            if vis > ana_reel and poids > 0:
                ajout = ((vis - ana_reel) / 100 * (poids * 1000)) / (teneur / 100 * rend / 100)
        else:
            if vis > ana and poids > 0:
                ajout = ((vis - ana) / 100 * (poids * 1000)) / (teneur / 100 * rend / 100)
        
        results_list.append({"Élément": elem.capitalize(), "Analyse": ana, "Visée": vis, "Ajout (kg)": round(ajout, 2)})

# --- BOUTON CALCULER ET TABLEAU FINAL ---
st.divider()
if st.button("📊 CALCULER TOUT", use_container_width=True, type="primary"):
    df = pd.DataFrame(results_list)
    
    # On ne garde que les lignes où il y a un ajout à faire ou une saisie
    df_filtered = df[df["Ajout (kg)"] >= 0]
    
    st.subheader("📋 Récapitulatif des ajouts")
    st.table(df_filtered)
    
    # Affichage des totaux ou alertes
    total_ajouts = df["Ajout (kg)"].sum()
    st.success(f"**Total des ajouts à prévoir : {total_ajouts:g} kg**")

if st.button("🔄 RAZ"):
    st.rerun()
