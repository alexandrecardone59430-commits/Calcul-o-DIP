import streamlit as st
import pandas as pd

# Configuration pour mobile et ordinateur
st.set_page_config(page_title="Calculateur Option B", layout="centered")

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

st.title("📟 Calculateur Option B")

# --- RÉGLAGES ---
c1, c2, c3 = st.columns(3)
with c1: nuance = st.selectbox("NUANCE", sorted(DATA.keys()))
with c2: circuit = st.selectbox("CIRCUIT", [4, 5])
with c3:
    poids_t = st.number_input("POIDS (t)", value=200, step=1)
    poids_kg = poids_t * 1000

st.divider()

# --- FORMULAIRE ---
saisies = {}
elements = DATA[nuance]
ordre = []
if "manganèse" in elements:
    ordre.append(("Mn Carb (78%)", "mn_carb"))
    ordre.append(("Mn Affi (82%)", "mn_affi"))
for k in elements.keys():
    if k != "manganèse": ordre.append((k.capitalize(), k))

h1, h2, h3 = st.columns([2, 1, 1])
h1.write("**ÉLÉMENT**")
h2.write("**ANA (%)**")
h3.write("**VISÉE (%)**")

for label, key_id in ordre:
    r1, r2, r3 = st.columns([2, 1, 1])
    with r1: st.write(f"**{label}**")
    with r2: ana = st.number_input("", key=f"a_{key_id}", format="%.4f", step=0.001, label_visibility="collapsed")
    with r3: vis = st.number_input("", key=f"v_{key_id}", format="%.4f", step=0.001, label_visibility="collapsed")
    saisies[key_id] = {"ana": ana, "vis": vis, "label": label}

# --- CALCUL ET RÉSULTAT REGROUPÉ ---
if st.button("CALCULER LES AJOUTS", type="primary", use_container_width=True):
    carb_induit = 0.0
    final_data = []

    # 1. Mn Carb
    if "mn_carb" in saisies:
        d = saisies["mn_carb"]
        rend = elements["manganèse"].get(circuit, (0, 0))[0]
        if d["vis"] > d["ana"] and rend > 0:
            aj = ((d["vis"] - d["ana"]) / 100 * poids_kg) / (0.78 * rend / 100)
            carb_induit = (aj * 0.067) / poids_kg * 100
            # Division par 100 appliquée ici
            final_data.append({"Métal": d["label"], "Ajout (/100)": round(aj / 100, 2)})
        else:
            final_data.append({"Métal": d["label"], "Ajout (/100)": 0})

    # 2. Reste
    for key_id, d in saisies.items():
        if key_id == "mn_carb": continue
        rend, teneur = elements[key_id].get(circuit, (0, 0)) if key_id != "mn_affi" else (elements["manganèse"].get(circuit, (0, 0))[0], 82)
        
        ana_f = d["ana"] + (carb_induit if key_id == "carbone" else 0)
        
        if d["vis"] > ana_f and rend > 0:
            aj = ((d["vis"] - ana_f) / 100 * poids_kg) / (teneur / 100 * rend / 100)
            # Division par 100 appliquée ici
            final_data.append({"Métal": d["label"], "Ajout (/100)": round(aj / 100, 2)})
        else:
            final_data.append({"Métal": d["label"], "Ajout (/100)": 0})

    st.divider()
    st.subheader("📋 RÉSULTATS (Valeurs divisées par 100)")
    st.table(pd.DataFrame(final_data))
    if carb_induit > 0: st.info(f"💡 Carbone induit : +{carb_induit:.4f}%")
        
