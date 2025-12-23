import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Calculateur DIP OB", layout="centered")

# --- BASE DE DONNÉES ---
DATA = {
    "7778": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (12, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (90, 78)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "Titane": {4: (75, 69)}},
    "7777": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "6129": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (18, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6718": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6729": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (18, 99), 5: (18, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6758": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (20, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6759": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (18, 99), 5: (18, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (86, 69), 5: (82, 69)}},
    "6768": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6788": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (16, 99), 5: (16, 99)}, "bore": {4: (93, 19), 5: (93, 19)}, "manganèse": {4: (96, 78), 5: (96, 78)}, "nobium": {4: (90, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (84, 69), 5: (84, 69)}},
    "6828": {"aluminium": {5: (100, 94)}, "carbone": {5: (100, 100)}, "calcium": {5: (16, 99)}, "bore": {5: (93, 19)}, "manganèse": {5: (96, 78)}, "nobium": {5: (90, 66)}, "silicium": {5: (100, 76)}, "Titane": {5: (84, 69)}},
    "6838": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "6858": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (16, 99)}, "bore": {4: (89, 19), 5: (93, 19)}, "manganèse": {4: (100, 78), 5: (96, 78)}, "nobium": {4: (93, 66), 5: (90, 66)}, "silicium": {4: (100, 76), 5: (100, 76)}, "Titane": {4: (88, 69), 5: (84, 69)}},
    "7758": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (102, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7759": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (15, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (10, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7779": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (15, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "7929": {"aluminium": {4: (67, 94)}, "carbone": {4: (70, 100)}, "calcium": {4: (15, 99)}, "bore": {4: (70, 19)}, "manganèse": {4: (96, 78)}, "nobium": {4: (90, 66)}, "silicium": {4: (85, 76)}, "Titane": {4: (75, 69)}},
    "7969": {"aluminium": {4: (100, 94)}, "carbone": {4: (100, 100)}, "calcium": {4: (13, 99)}, "bore": {4: (89, 19)}, "manganèse": {4: (100, 78)}, "nobium": {4: (94, 66)}, "silicium": {4: (90, 76)}, "Titane": {4: (82, 69)}},
    "7978": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (93, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}},
    "4647": {"aluminium": {4: (100, 94), 5: (100, 94)}, "carbone": {4: (100, 100), 5: (100, 100)}, "calcium": {4: (13, 99), 5: (11, 99)}, "bore": {4: (89, 19), 5: (89, 19)}, "manganèse": {4: (100, 78), 5: (100, 78)}, "nobium": {4: (89, 66), 5: (91, 66)}, "silicium": {4: (90, 76), 5: (90, 76)}, "Titane": {4: (85, 69), 5: (83, 69)}}
}

st.title("📟 Calculateur DIP OB")

# --- PARAMÈTRES GÉNÉRAUX ---
col1, col2, col3 = st.columns(3)
with col1:
    nuance = st.selectbox("SÉLECTION NUANCE :", sorted(DATA.keys()))
with col2:
    circuit = st.selectbox("CIRCUIT :", [4, 5])
with col3:
    poids_t_str = st.text_input("POIDS POCHE (t) :", value="")
    poids_kg = float(poids_t_str.replace(',', '.')) * 1000 if poids_t_str else 0.0

st.divider()

# --- GÉNÉRATION DES LIGNES ---
saisies = {}
elements = DATA[nuance]
ordre = []

if "manganèse" in elements:
    ordre.append(("Mn Carb ", "mn_carb", 78, elements["manganèse"]))
    ordre.append(("Mn Affi ", "mn_affi", 82, elements["manganèse"]))

for k, v in elements.items():
    if k != "manganèse":
        ordre.append((k.capitalize(), k, None, v))

# Entête de section
st.write("### 🧪 Saisie des Analyses")

for label, key_id, teneur_fixe, circuits in ordre:
    st.write(f"{label}")
    r1, r2 = st.columns(2)
    with r1:
        ana_val = st.text_input("ANA", key=f"a_{key_id}")
    with r2:
        vis_val = st.text_input("VISÉE", key=f"v_{key_id}")
    
    saisies[key_id] = {
        "label": label,
        "ana": float(ana_val.replace(',', '.')) if ana_val else 0.0,
        "vis": float(vis_val.replace(',', '.')) if vis_val else 0.0,
        "ana_str": ana_val if ana_val else "0",
        "vis_str": vis_val if vis_val else "0",
        "teneur_fixe": teneur_fixe,
        "circuits": circuits
    }
    st.write("---")

# --- CALCULS ---
if st.button("CALCULER", type="primary", use_container_width=True):
    if poids_kg <= 0:
        st.error("Veuillez saisir un poids de poche.")
    else:
        carb_induit = 0.0
        resultats_final = []

        # 1. Mn Carb (pour le Carbone Induit)
        d_mn = saisies.get("mn_carb")
        if d_mn and d_mn["vis"] > d_mn["ana"]:
            rend = d_mn["circuits"].get(circuit, (0, 0))[0]
            if rend > 0:
                ajout_mn = ((d_mn["vis"] - d_mn["ana"]) / 100 * poids_kg) / (0.78 * rend / 100)
                ajout_mn = max(0, ajout_mn)
                carb_induit = (ajout_mn * 0.067) / poids_kg * 100

        # 2. Boucle de calcul
        for key_id, d in saisies.items():
            ana_effective = d["ana"]
            note_carbone = ""
            if key_id == "carbone":
                ana_effective += carb_induit
                if carb_induit > 0:
                    note_carbone = f" (+{carb_induit:.3f} induit)"
            
            rend_tab, ten_tab = d["circuits"].get(circuit, (0,0))
            teneur = d["teneur_fixe"] if d["teneur_fixe"] else ten_tab
            
            ajout_final = 0.0
            if d["vis"] > ana_effective and rend_tab > 0:
                aj_kg = ((d["vis"] - ana_effective) / 100 * poids_kg) / (teneur / 100 * rend_tab / 100)
                ajout_final = max(0, aj_kg)
            
            resultats_final.append({
                "Métal": d["label"],
                "Analyse (%)": d["ana_str"] + note_carbone,
                "Visée (%)": d["vis_str"],
                "Résultat": f"{ajout_final/1000:.3f}"
            })

        st.subheader("📋 RÉCAPITULATIF DES CALCULS")
        st.dataframe(pd.DataFrame(resultats_final), use_container_width=True, hide_index=True)
        
        if carb_induit > 0:
            st.info(f"💡 Info : L'apport de carbone provenant du Mn Carb est de +{carb_induit:.4f}%")

if st.button("RAZ (Réinitialiser)"):
    st.rerun()
    
