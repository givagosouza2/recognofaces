import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="RecognoFaces",
    page_icon="😃",
    layout="wide"
)

s1, s2 = st.columns([0.2, 1])

with s1:
    st.image('icon.png')
with s2:
    # Cabeçalho customizado com HTML
    st.markdown("""
        <div style="background-color:#f0f2f6;padding:10px;border-radius:10px;margin-bottom:20px">
            <h1 style="color:#262730;">Análise de Reconhecimento de Expressões Faciais</h1>
            <p style="color:#404040;font-size:16px">
                Esta página é dedicada a analisar o desempenho em tarefas de reconhecimento de expressões faciais usando o aplicativo <strong>RecognoFaces</strong>,
                desenvolvido no Laboratório de Neurologia Tropical do Núcleo de Medicina Tropical da Universidade Federal do Pará.
                Aqui você pode importar o arquivo exportado pelo aplicativo e acessar os principais parâmetros de desempenho.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Upload do arquivo
st.header("1. Faça upload da planilha com os resultados do teste:")
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("1. Pré-visualização dos dados importados:")
        st.dataframe(df)

        # Conta quantos VP, VN, FP e FN existem na coluna 'Categoria'
        categorias = df['Categoria'].value_counts()
        vp = categorias.get("VP", 0)
        vn = categorias.get("VN", 0)
        fp = categorias.get("FP", 0)
        fn = categorias.get("FN", 0)

    with c2:
        st.subheader("2. Totais extraídos da coluna 'Categoria'")
        st.write(f"- Verdadeiros Positivos (VP): {vp}")
        st.write(f"- Verdadeiros Negativos (VN): {vn}")
        st.write(f"- Falsos Positivos (FP): {fp}")
        st.write(f"- Falsos Negativos (FN): {fn}")

    with c3:
        # Cálculo das métricas
        total = vp + vn + fp + fn
        acuracia = (vp + vn) / total if total > 0 else 0.0
        precisao = vp / (vp + fp) if (vp + fp) > 0 else 0.0
        recall = vp / (vp + fn) if (vp + fn) > 0 else 0.0
        f1 = 2 * (precisao * recall) / (precisao +
                                        recall) if (precisao + recall) > 0 else 0.0

        # Exibir resultados
        st.subheader("3. Resultados das métricas:")
        st.markdown(f"**Acurácia**: `{acuracia:.3f}`")
        st.markdown(f"**Precisão**: `{precisao:.3f}`")
        st.markdown(f"**Recall (Sensibilidade)**: `{recall:.3f}`")
        st.markdown(f"**F1-score**: `{f1:.3f}`")

    st.subheader("**Conceitos importantes**")
    c1, c2 = st.columns(2)
    with c1:
        st.success(
            "**Acurácia: Indica a proporção de classificações corretas em relação ao total de casos.**")
        st.text('')
    with c2:
        st.image('acuracia.png', width=160)
    with c1:
        st.success(
            "**Precisão: Proporção de positivos preditos que realmente são positivos.**")
        st.text('')
    with c2:
        st.image('precisao.png', width=150)
    with c1:
        st.success(
            "**Recall: Proporção de positivos reais que foram corretamente identificados.**")
        st.text('')
    with c2:
        st.image('recall.png', width=150)
    with c1:
        st.success("**F1-score: Média harmônica entre Precisão e Recall.**")
        st.text('')
    with c2:
        st.image('f1score.png', width=150)
    st.info(
        'Sugestões e informações sobre o aplicativo e sua análise, enviar email para givagosouza@ufpa.br')

else:
    st.info("Aguardando upload do arquivo.")
