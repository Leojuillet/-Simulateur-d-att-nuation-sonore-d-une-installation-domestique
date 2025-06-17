import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Titre de l'application
st.title("🏠 Simulateur d'atténuation sonore d'une installation domestique")
st.markdown("Simulez comment le bruit d'un appareil extérieur diminue avec la distance et les dispositifs anti-bruits.")

# Message d'aide pour mobile
st.info("ℹ️ Conseil : Faites défiler vers le haut pour ajuster les paramètres dans la section '🔧 Paramètres de simulation'.")

# Paramètres utilisateur dans le corps principal avec expander
options_attenuation = {
    "Aucun": 0,
    "Caisson insonorisé : -10dB": 10,
    "Écran acoustique : -20dB": 20,
    "Mur béton : -25dB": 25,
    "Végétation dense (haie) : -10dB": 10,
}

with st.expander("🔧 Paramètres de simulation", expanded=True):
    # Niveau sonore initial
    initial_dB = st.slider(
        "Niveau sonore initial (dB) : niveau sonore en dB (SPL) de votre installation",
        min_value=35, max_value=100, value=60
    )

    # Distance
    distance_max = st.slider(
        "Distance jusqu'au voisin (mètres)",
        min_value=1.0, max_value=20.0, value=10.0, step=0.5
    )

    # Obstacles
    st.markdown("#### Choisissez vos dispositifs anti-bruit")
    selected_obstacles = []
    for key in options_attenuation:
        if st.checkbox(key):
            selected_obstacles.append(key)

# Calculs pour le graphique
distances = np.arange(0.1, 20.1, 0.1)  # de 0.1 à 20.0 mètres
attenuation_distance = 20 * np.log10(distances)
total_attenuation_obstacles = sum(options_attenuation[obstacle] for obstacle in selected_obstacles)

# Calcul du niveau sonore final
final_dB_by_distance = np.clip(
    initial_dB - (attenuation_distance + total_attenuation_obstacles),
    0, None
)

# Récupérer le niveau sonore à la distance choisie
index = int(distance_max * 10) - 1  # car on a un pas de 0.1 m
final_dB_at_distance = final_dB_by_distance[index]

# Affichage résultats
st.header("📊 Résultats de la simulation")

# Afficher les métriques sous forme verticale (meilleure compatibilité mobile)
st.metric(label="Niveau sonore initial", value=f"{initial_dB} dB")
st.metric(label="Atténuation totale", value=f"{round(attenuation_distance[index] + total_attenuation_obstacles, 1)} dB")
st.metric(label="Niveau sonore à {:.1f} m".format(distance_max), value=f"{round(final_dB_at_distance, 1)} dB")

# Plafond réglementaire
plafond = 30
audible = 20
if final_dB_at_distance < audible:
    st.success(f"🔇✅ Le niveau sonore final ({round(final_dB_at_distance, 1)} dB) est inférieur au niveau audible de {audible} dB.")
elif final_dB_at_distance <= plafond:
    st.success(f"🔊✅ Le niveau sonore final ({round(final_dB_at_distance, 1)} dB) est supérieur au niveau audible mais conforme au plafond réglementaire.")
else:
    st.error(f"📢❌ Le niveau sonore final ({round(final_dB_at_distance, 1)} dB) dépasse le plafond réglementaire de {plafond} dB.")

# Graphique Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=distances,
    y=final_dB_by_distance,
    mode='lines',
    name='Niveau sonore (dB)',
    line=dict(color='blue')
))

fig.add_hline(y=plafond, line_dash="dot", line_color="red", annotation_text="Plafond réglementaire (30 dB)")
fig.add_hline(y=audible, line_dash="dot", line_color="green", annotation_text="Niveau audible (20 dB)")

fig.update_layout(
    title="Atténuation du niveau sonore en fonction de la distance",
    xaxis_title="Distance (m)",
    yaxis_title="Niveau sonore (dB)",
    yaxis_range=[0, initial_dB + 5],
    template="plotly_white"
)

# Afficher le graphique
st.plotly_chart(fig, use_container_width=True)

# Explication finale
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