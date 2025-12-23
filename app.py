import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Calculateur Fonderie - Option B", layout="centered")

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

st.title("📟 Calculateur Fonderie - Option B")

# --- PARAMÈTRES GÉNÉRAUX ---
col1, col2, col3 = st.columns(3)
with col1:
    nuance = st.selectbox("SÉLECTION NUANCE :", sorted(DATA.keys()))
with col2:
    circuit = st.selectbox("CIRCUIT :", [4, 5])
with col3:
    poids_t = st.number_input("POIDS POCHE (t) :", value=0.0, step=1.0, format="%.2f")
    poids_kg = poids_t * 1000

st.divider()

# --- GÉNÉRATION DES LIGNES ---
saisies = {}
elements = DATA[nuance]
ordre = []

if "manganèse" in elements:
    ordre.append(("Mn Carb (78%)", "mn_carb", 78, elements["manganèse"]))
    ordre.append(("Mn Affi (82%)", "mn_affi", 82, elements["manganèse"]))

for k, v in elements.items():
    if k != "manganèse":
        ordre.append((k.capitalize(), k, None, v))

h1, h2, h3 = st.columns([2, 1, 1])
h1.write("**ÉLÉMENT**")
h2.write("**ANA (%)**")
h3.write("**VISÉE (%)**")

for label, key_id, teneur_fixe, circuits in ordre:
    r1, r2, r3 = st.columns([2, 1, 1])
    with r1:
        st.write(f"**{label}**")
    with r2:
        ana = st.number_input("", key=f"a_{key_id}", step=0.001, format="%.4f", label_visibility="collapsed")
    with r3:
        vis = st.number_input("", key=f"v_{key_id}", step=0.001, format="%.4f", label_visibility="collapsed")
    
    saisies[key_id] = {
        "label": label,
        "ana": ana,
        "vis": vis,
        "teneur_fixe": teneur_fixe,
        "circuits": circuits
    }

st.divider()

# --- CALCULS ---
if st.button("CALCULER", type="primary", use_container_width=True):
    if poids_t <= 0:
        st.error("Veuillez saisir un poids de poche.")
    else:
        carb_induit = 0.0
        resultats_final = []

        # 1. ÉTAPE Mn Carb
        if "mn_carb" in saisies:
            d = saisies["mn_carb"]
            rend = d["circuits"].get(circuit, (0, 0))[0]
            if d["vis"] > d["ana"] and rend > 0:
                ajout_mn = ((d["vis"] - d["ana"]) / 100 * poids_kg) / (0.78 * rend / 100)
                ajout_mn = max(0, ajout_mn)
                carb_induit = (ajout_mn * 0.067) / poids_kg * 100
                # Virgule décalée de 3 rangs (/1000)
                resultats_final.append({"Métal": d["label"], "Résultat (décalé)": f"{ajout_mn/1000:.3f}"})
            else:
                resultats_final.append({"Métal": d["label"], "Résultat (décalé)": "0.000"})

        # 2. ÉTAPE Autres éléments
        for key_id, d in saisies.items():
            if key_id == "mn_carb": continue
            
            ana_finale = d["ana"]
            if key_id == "carbone":
                ana_finale += carb_induit
            
            rend_tab, ten_tab = d["circuits"].get(circuit, (0,0))
            teneur = d["teneur_fixe"] if d["teneur_fixe"] else ten_tab
            rendement = rend_tab

            if d["vis"] > ana_finale and rendement > 0:
                aj = ((d["vis"] - ana_finale) / 100 * poids_kg) / (teneur / 100 * rendement / 100)
                # Virgule décalée de 3 rangs (/1000)
                resultats_final.append({"Métal": d["label"], "Résultat (décalé)": f"{max(0, aj)/1000:.3f}"})
            else:
                resultats_final.append({"Métal": d["label"], "Résultat (décalé)": "0.000"})

        # Affichage
        st.subheader("📋 RÉSULTATS (Valeurs / 1000)")
        st.table(pd.DataFrame(resultats_final))
        if carb_induit > 0:
            st.warning(f"💡 Apport Mn -> Carbone : +{carb_induit:.3f}%")

if st.button("RAZ (Réinitialiser)"):
    st.rerun()
