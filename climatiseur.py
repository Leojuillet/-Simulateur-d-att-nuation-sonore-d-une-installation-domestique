import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Titre de l'application
st.title("Simulateur d'atténuation sonore d'une installation domestique extérieure")
st.markdown("Simulez comment le bruit d'un appareil extérieur diminue avec la distance et les protections.")

# Paramètres utilisateur
st.sidebar.header("Paramètres")

# Niveau sonore initial
initial_dB = st.sidebar.slider("Niveau sonore initial (dB)", min_value=35, max_value=100, value=60)

# Distance
distance_max = st.sidebar.slider("Distance jusqu'au voisin (mètres)", min_value=1.0, max_value=20.0, value=10.0, step=0.5)

# Obstacles
st.sidebar.subheader("Choisissez les dispositifs d'atténuation")
options_attenuation = {
    "Aucun": 0,
    "Caisson insonorisé : -10dB": 10,
    "Écran acoustique : -20dB": 20,
    "Mur béton (10cm d'épaiseur) : -45dB": 45,
    "Végétation dense (haie) : -10dB": 10,
}

selected_obstacles = []
for key in options_attenuation:
    if st.sidebar.checkbox(key):
        selected_obstacles.append(key)

# Calculs
distances = np.arange(0.1, 20.1, 0.1)
attenuation_distance = 20 * np.log10(distances)
total_attenuation_obstacles = sum(options_attenuation[obstacle] for obstacle in selected_obstacles)
final_dB_by_distance = initial_dB - (attenuation_distance + total_attenuation_obstacles)

# Récupérer le niveau sonore à la distance choisie
final_dB_at_distance = final_dB_by_distance[int(distance_max * 10) - 1]

# Affichage résultats
st.header("Résultats de la simulation")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Niveau sonore initial", value=f"{initial_dB} dB")
    st.metric(label="Atténuation totale", value=f"{round(total_attenuation_obstacles + 20 * np.log10(distance_max), 1)} dB")

with col2:
    st.metric(label="Niveau sonore à {:.1f} m".format(distance_max), value=f"{round(final_dB_at_distance, 1)} dB")

# Plafond réglementaire
plafond = 30
if final_dB_at_distance <= plafond:
    st.success(f"✅ Le niveau sonore final ({round(final_dB_at_distance, 1)} dB) est inférieur ou égal au plafond réglementaire de {plafond} dB.")
else:
    st.error(f"❌ Le niveau sonore final ({round(final_dB_at_distance, 1)} dB) dépasse le plafond réglementaire de {plafond} dB.")

# Graphique Plotly
fig = go.Figure()

# Courbe principale
fig.add_trace(go.Scatter(
    x=distances,
    y=final_dB_by_distance,
    mode='lines',
    name='Niveau sonore (dB)',
    line=dict(color='blue')
))

# Seuil réglementaire
fig.add_hline(y=plafond, line_dash="dot", line_color="red", annotation_text="Plafond réglementaire (30 dB)")

# Personnalisation
fig.update_layout(
    title="Atténuation du niveau sonore en fonction de la distance",
    xaxis_title="Distance (m)",
    yaxis_title="Niveau sonore (dB)",
    yaxis_range=[0, initial_dB + 5],
    template="plotly_white"
)

# Afficher le graphique
st.plotly_chart(fig)

# Explication
st.markdown("""
### 💡 Notes importantes :
- L'atténuation due à la distance suit la loi du carré inverse : $20 \cdot \log_{10}(d)$.
- Les valeurs d'atténuation des obstacles sont des estimations typiques.
- En réalité, la géométrie, le vent, les réflexions, et la fréquence influencent aussi le niveau perçu.
""")

# Option : Afficher les détails techniques
with st.expander("🔍 Détails techniques"):
    st.write(f"- Atténuation des obstacles sélectionnés : {total_attenuation_obstacles} dB")
    st.write(f"- Dispositifs sélectionnés : {', '.join(selected_obstacles) if selected_obstacles else 'Aucun'}")
