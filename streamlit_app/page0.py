
import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
   layout="wide",
   page_title= "Analyse des données de notre API MovieLenz",
   page_icon= "🎞️"
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
        "profil_Isabelle.jpg",  # Remplacez par le chemin de votre image
        width=80,     # Ajustez la taille si nécessaire
        use_container_width=False,
    )

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Exploration des Données de l'API MovieLens</h1>
        """,
        unsafe_allow_html=True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/isabelle-lacmago/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>Isabelle LACMAGO </strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python & Architecte API**")
# Afficher l'image séparément
st.image("architecture_phase1.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/ISABELLE-LAC/Moovie_backend_I" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Cliquer pour voir le Code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration et Visualisation**")
# Afficher l'image séparément
st.image("architecturephase.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/ISABELLE-LAC/Movie_analytic" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Cliquer pour voir le Code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )