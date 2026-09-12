import streamlit as st
import pandas as pd
from datetime import datetime

# Obter o ano atual dinamicamente para o copyright
ano_atual = datetime.now().year

st.set_page_config(
    page_title="Science Nexus Plataforma | Saúde • Sociedade • Tecnologias • Humanidades",
    page_icon="🩺",
    layout="wide"
)

# --- FUNÇÃO DE CACHE PARA CARREGAR PLANILHAS RAPIDAMENTE ---
@st.cache_data(ttl=600)
def carregar_dados_planilha(link_planilha):
    """Carrega os dados da planilha e guarda em cache por 10 minutos para evitar lentidão."""
    try:
        if "docs.google.com" in link_planilha:
            id_plan = link_planilha.split("/d/")[1].split("/")[0]
            # Usa export?format=csv para ler automaticamente a primeira aba da planilha do Google Sheets
            url_csv = f"https://docs.google.com/spreadsheets/d/{id_plan}/export?format=csv"
            df = pd.read_csv(url_csv)
            df.columns = df.columns.str.strip().str.lower()
            return df
    except Exception:
        return None
    return None
    
# --- ESTILIZAÇÃO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .element-container {
        color: #333333;
    }
    .footer-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 8px;
        font-size: 13px;
        color: #555555;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE ESTILO (Segura contra ausência de imagens) ---
def mostrar_cabecalho(foto="capaS.jpg"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image(foto, width=600)
        except Exception:
            pass
    
    st.markdown("""
        <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h1 style='margin:0; font-size: 26px;'>Saúde • Sociedade • Tecnologias • Humanidades</h1>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

# --- MENU (Nome da aba sincronizado perfeitamente) ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Eventos e Inscrições", 
    "✍️ Trabalhos Científicos", 
    "🎓 Validação de Certificados", 
    "💳 Taxa de DOI Individual/Pessoal", 
    "💳 Taxa de ISBN Coletivo",
    "📚 Anais Publicados",
    "📺 Transmissão ao Vivo",
    "📂 Eventos Anteriores",
    "📞 Contato"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("Bem-vindo à Science Nexus Plataforma Científica")
    st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação e publicação de anais.")
    st.markdown("""
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Registros:** Anais com **ISBN** e **DOI** opcional.
    * **Avaliação:** Acompanhe em tempo real se seu trabalho está em análise, aprovado ou pendente de correções.
    """)

# --- 2. EVENTOS E INSCRIÇÕES (Com Links Independentes por Evento) ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes, consultar a programação e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia",
        "2. Encontro Formativo PET Saúde Clima",
        "3. Acolhimento dos Monitores Caeme/Prograd", 
        "4. Atividades de Extensão e Vínculo com a Comunidade", 
        "5. Minicurso Prático: Reabilitação e Terapia Manual", 
        "6. Workshop: Inovação e Tecnologias em Saúde",
        "7. Simpósio de Saúde Coletiva e Políticas Públicas",
        "8. Encontro Científico Psico História e as Leis da Robótica"
    ])
    
    st.markdown("---")
    
    if "Jornada Científica" in evento_selecionado:
        try:
            st.image("logo_jornada.png.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo institucional da Jornada não encontrada no repositório]*")
            
        st.markdown("### 🩺 Jornada Científica do Curso de Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes, docentes, profissionais e pesquisadores.
        * **Investimento:** 
          * Estudantes, Docentes e Banca da PUC Goiás: **Gratuito**.
          * Participantes Externos: **R$ 10,00** (Standby mediante comprovante na chave `eventos@sciencenexus.com.br`).
        * **Destaque:** Permite submissão de Resumos Simples, Expandidos e Artigos Completos com ISBN.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Fisioterapia Musculo Esquelética, Neurológica, Cardiorrespiratória, Terapia Intensiva, Geriatria e Gerontologia, Saúde da Mulher, Saúde Coletiva, Tecnologias e Inteligência Artificial na Saúde e Outras Áreas.**")
        st.warning("⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby** até a validação do comprovante.")
        
        st.markdown("---")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação da Jornada EM BREVE", "COLE_LINK_PROGRAMACAO_JORNADA")
        
        opcoes_inscricao = ["Participante/Ouvinte", "Orientador", "Apresentador de Trabalho", "Membro da Banca", "Cadastro de Trabalho para Certificação (Orientador)"]
        
        link_ouv = "https://forms.gle/tVKQtkEpQHG9Bo3K7"
        link_ori = "https://forms.gle/tVKQtkEpQHG9Bo3K7"
        link_apr = "https://forms.gle/tVKQtkEpQHG9Bo3K7"
        link_ban = "https://forms.gle/tVKQtkEpQHG9Bo3K7"
        link_cad = "https://forms.gle/GM55UFo18d7EqPgL8"

    elif "Encontro Formativo PET Saúde Clima" in evento_selecionado:
        try:
            st.image("pet clima.png", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo de divulgação do PET Saúde Clima não encontrada no repositório]*")
            
        st.markdown("### 🌱 Encontro Formativo PET Saúde Clima")
        st.write("""
        * **Público-alvo:** Integrantes do programa, estudantes e comunidade acadêmica.
        * **Modalidade de Certificação:** Certificado de Ouvinte Participante.
        * **Investimento:** Gratuito.
        """)
        st.markdown("---")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação PET Saúde Clima", "COLE_LINK_PROGRAMACAO_PET")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        link_ouv = "https://forms.gle/u8nseAtgNAN5aMJDA"

    elif "Acolhimento dos Monitores" in evento_selecionado or "Monitores" in evento_selecionado:
        try:
            st.image("monitores.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo/Imagem do evento não encontrada]*")
            
        st.markdown("### 🤲 Acolhimento dos Monitores Caeme/Prograd")
        st.write("Data: 11/09 Matutino 9h às 10h30 Campus II Auditório Bloco G e Noturno 18h às 19h30 Área II Auditório II. Público: Monitores selecionados em 2026/2.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação", "COLE_LINK_PROGRAMACAO_MONITORES")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        link_ouv = "https://forms.gle/wtTcSXZt6PnwzjEL7"
        
    elif "Atividades de Extensão" in evento_selecionado:
        try:
            st.image("extensao.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo/Imagem da Mostra não encontrada]*")
            
        st.markdown("### 🩺 Atividades de Extensão e Vínculo com a Comunidade")
        st.write("""
        * **Público-alvo:** Estudantes e docentes do curso de Fisioterapia.
        * **Investimento:** Gratuito para Estudantes e Docentes.
        * **Destaque:** Permite submissão de Relatos de Experiência e Resumos Expandidos com ISBN.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Disciplinas extensionistas; Atividades de Extensão nos Estágios e Atividades Externas às Disciplinas do curso de Fisioterapia.**")
        st.write("**Submissões em regime de fluxo contínuo durante o ano. A publicação dos anais eletrônicos é realizada em volume único ao final de cada ciclo.**")
        st.warning("⚠️ **Sugestão:** os modelos de atividades devem ser adaptados para **Relato de Experiência** ou **Resumo Expandido**.")
        
        st.markdown("---")
        st.markdown("#### 📅 Submissões em regime de fluxo contínuo")
        try:
        with open("regras_relato_experiencia.pdf", "rb") as pdf_file:
        st.download_button("📥 Baixar Regras Completas (PDF - Relato de Experiência)", pdf_file, file_name="Regras_Relato_Experiencia.pdf", mime="application/pdf")
        try:
        with open("regras_resumo_expandido.pdf", "rb") as pdf_file:
        st.download_button("📥 Baixar Regras Completas (PDF - Resumo Expandido)", pdf_file, file_name="Regras_Resumo_Expandido.pdf", mime="application/pdf")
        st.link_button("📅 Instruções / Relato de Experiência ou Resumo Expandido", "https://forms.gle/j5ESvsXoYoahGpJB9")        
        
        opcoes_inscricao = ["Orientador/Professor", "Apresentador de Trabalho", "Cadastro de Trabalho para Certificação (Orientador)"]
        
        link_ori = "https://forms.gle/j5ESvsXoYoahGpJB9"
        link_apr = "https://forms.gle/j5ESvsXoYoahGpJB9"
        link_cad = "https://forms.gle/j5ESvsXoYoahGpJB9"
    
    elif "Minicurso Prático" in evento_selecionado:
        try:
            st.image("minicurso.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo do Minicurso não encontrada]*")
            
        st.markdown("### 🤲 Minicurso Prático: Reabilitação e Terapia Manual")
        st.write("Detalhes e práticas avançadas em terapia manual para acadêmicos e profissionais.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Minicurso", "COLE_LINK_PROGRAMACAO_MINICURSO")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        link_ouv = "https://forms.gle/LINK_MINICURSO_OUVINTE"
        
    elif "Workshop" in evento_selecionado:
        try:
            st.image("workshop.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo do Workshop não encontrada]*")
            
        st.markdown("### 💡 Workshop: Inovação e Tecnologias em Saúde")
        st.write("Discussão sobre novas tecnologias e o futuro da reabilitação e saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Workshop", "COLE_LINK_PROGRAMACAO_WORKSHOP")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        link_ouv = "https://forms.gle/LINK_WORKSHOP_OUVINTE"
        
    elif "Simpósio de Saúde Coletiva" in evento_selecionado:
        try:
            st.image("simposio.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo do Simpósio não encontrada]*")
            
        st.markdown("### 📊 Simpósio de Saúde Coletiva e Políticas Públicas")
        st.write("Debates e mesas-redondas sobre o impacto das políticas públicas na saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Simpósio", "COLE_LINK_PROGRAMACAO_SIMPOSIO")
        
        opcoes_inscricao = ["Participante/Ouvinte", "Apresentador de Trabalho"]
        link_ouv = "https://forms.gle/LINK_SIMPOSIO_OUVINTE"
        link_apr = "https://forms.gle/LINK_SIMPOSIO_APRESENTADOR"
        
    elif "Encontro Científico" in evento_selecionado:
        try:
            st.image("encontro.jpg", width=400)
        except Exception:
            st.caption("ℹ️ *[Logo do Encontro não encontrada]*")
            
        st.markdown("### 🎓 Encontro Científico Psico História e as Leis da Robótica")
        st.write("""
        * **Foco:** Integração científica dos acadêmicos da graduação.
        * **Investimento:** Gratuito para a comunidade acadêmica da FST.
        """)
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Encontro", "COLE_LINK_PROGRAMACAO_ENCONTRO")
        
        opcoes_inscricao = ["Participante/Ouvinte", "Apresentador de Trabalho"]
        link_ouv = "https://forms.gle/LINK_ENCONTRO_OUVINTE"
        link_apr = "https://forms.gle/LINK_ENCONTRO_APRESENTADOR"
    
    st.markdown("---")
    cat = st.radio("Selecione a opção desejada para inscrição:", opcoes_inscricao)
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", link_ouv)
    elif cat == "Orientador" or cat == "Orientador/Professor":
        st.link_button("🔗 Inscrever-se como Orientador", link_ori)
    elif cat == "Apresentador de Trabalho":
        st.link_button("🔗 Inscrever-se como Apresentador", link_apr)
    elif cat == "Membro da Banca":
        st.link_button("🔗 Inscrever-se como Banca", link_ban)
    else:
        st.info("⚠️ **Exclusivo para Orientadores:** Utilize este formulário para cadastrar o trabalho, estudante e banca para o certificado.")
        st.link_button("📝 Cadastrar Informações do Trabalho", link_cad)

# --- 3. TRABALHOS (SUBMISSÃO + STATUS COM RELATO DE EXPERIÊNCIA) ---
elif menu == "✍️ Trabalhos Científicos":
    mostrar_cabecalho("eventos.png")
    st.subheader("✍️ Central de Trabalhos Científicos")
    st.write("Consulte abaixo as normas e utilize o link do formulário exclusivo para enviar o seu arquivo Word (.doc/.docx).")
    
    tab_principal1, tab_principal2 = st.tabs(["📥 Submissão e Normas", "🔍 Consultar Status"])
    
    with tab_principal1:
        tab_simples, tab_expandido, tab_completo, tab_relato = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo", "📝 Relato de Experiência"])
        
        with tab_simples:
            st.markdown("### Normas para Submissão de Resumo Simples")
            st.markdown("""
            * **Estrutura Obrigatória:** Introdução, Objetivos, Materiais e Métodos, Resultados e Discussão, e Considerações Finais.
            * **Formatação:** Mínimo de 250 palavras e Máximo de 350 palavras (excluindo título e referências). Fonte Times New Roman, tamanho 12, espaçamento 1,0.
            * **Palavras-chave:** De 3 a 5 palavras-chave separadas por ponto e vírgula.
            * **Autores:** Permitido até 3 autores por trabalho (incluindo o orientador).
            
            **INFORMAÇÕES PARA A SUBMISSÃO**
            * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
            * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
            * **ISBN:** Registro ISBN - necessário para a publicação dos anais do evento. Pode ser adquirido pelo organizador do evento ou solicitado nessa plataforma.
            * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
            """)
            
            try:
                with open("regras_resumo_simples.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Resumo Simples)", pdf_file, file_name="Regras_Resumo_Simples.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *[PDF com regras detalhadas de Resumo Simples em breve]*")
        
        with tab_expandido:
            st.markdown("### Normas para Submissão de Resumo Expandido")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 4 páginas e no máximo 8 páginas completas.
            * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
            """)
            
            try:
                with open("regras_resumo_expandido.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Resumo Expandido)", pdf_file, file_name="Regras_Resumo_Expandido.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *[PDF com regras detalhadas de Resumo Expandido em breve]*")
                    
        with tab_completo:
            st.markdown("### Normas para Submissão de Artigo Completo")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
            """)
            
            try:
                with open("regras_resumo_artigo.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Artigo Completo)", pdf_file, file_name="Regras_Artigo_Completo.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *[PDF com regras detalhadas de Artigo Completo em breve]*")

        with tab_relato:
            st.markdown("### Normas para Submissão de Relato de Experiência")
            st.markdown("""
            * **Estrutura Obrigatória:** Introdução/Fundamentação Teórica, Descrição da Experiência (Vivência, Local, Público Envolvido), Reflexão Crítica/Resultados Alcançados, e Considerações Finais.
            * **Extensão:** De 4 a 8 páginas completas.
            * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
            * **Palavras-chave:** De 3 a 5 palavras-chave separadas por ponto e vírgula.
            
            **INFORMAÇÕES PARA A SUBMISSÃO**
            * **Formato:** O arquivo deve ser submetido em formato WORD (.doc/.docx).
            * **Prazo:** Respeitar o cronograma oficial do evento.
            * **Publicação:** Inserido nos anais oficiais com ISBN da plataforma.
            """)
            
            try:
                with open("regras_relato_experiencia.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Relato de Experiência)", pdf_file, file_name="Regras_Relato_Experiencia.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *[PDF com regras detalhadas de Relato de Experiência em breve]*")

        st.markdown("---")
        st.info("📌 **Importante:** Para que os arquivos sejam salvos diretamente na nuvem da comissão científica, a submissão é feita por formulário dedicado.")
        st.link_button("📥 Jornada Científica / Clique aqui para acessar o Formulário de Submissão de Trabalhos", "https://forms.gle/UUmLAAEdCwY9JRrY6")
        st.link_button("📥 Mostra Extensionista / Clique aqui para acessar o Formulário de Submissão de Trabalhos", "https://forms.gle/7JXdM3jRKzqJyqdR9")
    
    with tab_principal2:
        st.write("Digite o seu e-mail cadastrado na submissão para verificar o parecer atual da comissão científica.")
        with st.form("form_status"):
            email_busca = st.text_input("Digite o seu E-mail cadastrado:").strip().lower()
            consultar = st.form_submit_button("Consultar Status")
            
            if consultar:
                if email_busca:
                    st.markdown("---")
                    st.info(f"🔎 Buscando parecer para: **{email_busca}**")
                    
                    try:
                        link_planilha = "https://docs.google.com/spreadsheets/d/1X7XoT0ohgtc5DZOw-ezcu0HjPPSaBF-nSrGWOFSVsUY/edit?usp=sharing"
                        df = carregar_dados_planilha(link_planilha)
                        
                        if df is not None:
                            df.columns.values[2] = 'email_col'
                            coluna_email = 'email_col'
                            coluna_status = next((col for col in df.columns if 'status' in col.lower()), None)
                            
                            df[coluna_email] = df[coluna_email].astype(str).str.strip().str.lower()
                            resultado = df[df[coluna_email] == email_busca]
                            
                            if not resultado.empty:
                                if coluna_status:
                                    status_val = str(resultado.iloc[0][coluna_status]).strip()
                                    status_final = "Recebido" if (status_val.lower() == 'nan' or status_val == "") else status_val
                                    
                                    if "aprovado" in status_final.lower():
                                        st.success(f"🎉 **Status:** {status_final}")
                                    elif "correção" in status_final.lower():
                                        st.error(f"⚠️ **Status:** {status_final} - Verifique seu e-mail.")
                                    else:
                                        st.info(f"⏳ **Status:** {status_final}")
                                else:
                                    st.error("Coluna 'Status' não encontrada na planilha.")
                            else:
                                st.warning("E-mail não encontrado na base de dados.")
                        else:
                            st.error("Erro ao ler planilha.")
                    except Exception as e:
                        st.error(f"Erro ao ler planilha: {e}")
                else:
                    st.error("Por favor, digite um e-mail.")

# --- 4. VALIDAÇÃO DE CERTIFICADOS ---
elif menu == "🎓 Validação de Certificados":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("🎓 Validação de Autenticidade de Certificados")
    st.write("Insira o **Código de Autenticidade** exclusivo impresso no rodapé do certificado para comprovar sua validade:")
    
    with st.form("form_validacao_cert"):
        codigo_digitado = st.text_input("Código de Autenticidade:", placeholder="Ex: PUCGO-2026-XXXX").strip()
        validar_btn = st.form_submit_button("Verificar Autenticidade")
        
        if validar_btn:
            if codigo_digitado:
                try:
                    # Lista contendo os links das planilhas de certificados cadastradas (lendo a 1ª aba)
                    links_planilhas = [
                        "https://docs.google.com/spreadsheets/d/15D_Vay3AQDUrbmaHjgwTeg0irLHX5q2pw6sw_wtiDl0/edit?usp=sharing",  # Planilha 1
                        "https://docs.google.com/spreadsheets/d/1ymnfGiFmC_PZLUIra7mWyZMjD_hc9Uu6jXvLohUjBeE/edit?usp=sharing",  # Planilha 2
                        "https://docs.google.com/spreadsheets/d/1eEQeDcwCQ9gkpy9MAI9It7gk1fx1QwZRXBnhRhvkg6o/edit?usp=sharing",  # Planilha 3
                        "https://docs.google.com/spreadsheets/d/1uQnTs-ijo0d4fiTFoIKC0ANuJ5A2SfRQO3jOA65OruI/edit?usp=sharing",  # Planilha 4
                        "https://docs.google.com/spreadsheets/d/1ym70HWRIJPhzFbcYhmf4bcQLmzW4rbF5GkkycDyEC_0/edit?usp=sharing",  # Planilha 5
                        # Adicione links de planilhas de novos eventos abaixo:
                        # "COLE_LINK_NOVA_PLANILHA_AQUI",
                    ]
                    
                    encontrado = False
                    nome_p = "Participante"
                    erros_diagnostico = []
                    
                    for i, link in enumerate(links_planilhas):
                        if "docs.google.com" in link:
                            df_c = carregar_dados_planilha(link)
                            if df_c is not None and not df_c.empty:
                                df_c.columns = df_c.columns.str.strip().str.lower()
                                
                                col_cod = next((c for c in df_c.columns if any(termo in c for termo in ['codigo', 'chave', 'autenticidade', 'código'])), None)
                                
                                if col_cod:
                                    df_c[col_cod] = df_c[col_cod].astype(str).str.strip().str.lower()
                                    res_c = df_c[df_c[col_cod] == codigo_digitado.lower()]
                                    
                                    if not res_c.empty:
                                        colunas_possiveis = ['nome', 'nome completo', 'nome_completo', 'nome_orientador', 'nome_aluno', 'participante', 'autor', 'aluno', 'orientador']
                                        col_nome_encontrada = next((c for c in df_c.columns if any(p in c for p in colunas_possiveis)), None)
                                        
                                        if col_nome_encontrada:
                                            nome_p = str(res_c.iloc[0].get(col_nome_encontrada, 'Participante')).title()
                                        else:
                                            nome_p = "Participante Registrado"
                                            
                                        encontrado = True
                                        break
                                else:
                                    erros_diagnostico.append(f"Planilha {i+1}: Coluna de código não encontrada (Colunas lidas: {list(df_c.columns)})")
                            else:
                                erros_diagnostico.append(f"Planilha {i+1}: Dados vazios ou sem permissão pública de leitura na 1ª aba.")
                    
                    if encontrado:
                        st.success("✅ **CERTIFICADO VÁLIDO E AUTÊNTICO!**")
                        st.write(f"Este certificado pertence oficialmente a: **{nome_p}** — Science Nexus / PUC Goiás.")
                    else:
                        st.error("❌ **Certificado Inválido ou Não Encontrado:** O código informado não consta em nenhuma das bases de dados oficiais.")
                        with st.expander("🔍 Detalhes técnicos da varredura"):
                            for err in erros_diagnostico:
                                st.write(err)
                        
                except Exception as e:
                    st.error(f"Erro técnico ao consultar a base de dados: {e}")
            else:
                st.error("Por favor, digite o código de autenticidade.")

# --- 5. DOI/ISBN ---
elif menu == "💳 Taxa de DOI Individual/Pessoal":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("O DOI individual é opcional (R$ 20,00). **O DOI individual é por trabalho/título**")
    st.info("ℹ️ **Chave PIX:** eventos@sciencenexus.com.br")
    st.link_button("🔗 Link para Solicitação DOI", "https://forms.gle/J1FArsU2fYT7nHU26")

elif menu == "💳 Taxa de ISBN Coletivo":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("💳 Solicitação e Pagamento de ISBN Coletivo")
    st.write("Taxa única ISBN por evento, para o documento que conterá todos resumos/relatos/artigos dos Anais (R$ 35,00). Caso você queira registrar de forma independente o ISBN do seu evento, solicite o PDF dos Anais, sem ISBN, faça o registro e nos encaminhe o número ISBN para que seja anexado ao documento/Anais e publicizado na plataforma")
    st.info("ℹ️ **Chave PIX:** eventos@sciencenexus.com.br")
    st.link_button("🔗 Link para Solicitação ISBN", "https://forms.gle/2bN1yFrR5phvTcAu5")

# --- 6. ANAIS ---
elif menu == "📚 Anais Publicados":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("📚 Repositório Oficial de Anais")
    st.link_button("📥 Baixar Anais Jornada Científica 2026/2", "COLE_LINK_PDF_ANAIS_AQUI")
    st.link_button("📥 Baixar Anais Mostra de Extensão 2026", "COLE_LINK_PDF_ANAIS_AQUI") 

# --- 7. TRANSMISSÃO AO VIVO ---
elif menu == "📺 Transmissão ao Vivo":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("📺 Central de Transmissões ao Vivo e Eventos Online")
    st.write("Acompanhe abaixo as palestras, sessões de apresentação de trabalhos e mesas-redondas em tempo real.")
    
    st.markdown("---")
    link_transmissao = st.text_input("🔗 Cole aqui o link da transmissão (YouTube Live):", "https://www.youtube.com/watch?v=EXEMPLO_LIVE")
    
    if link_transmissao:
        try:
            st.video(link_transmissao)
        except Exception:
            st.warning("Insira um link válido do YouTube para exibir o player de transmissão.")
            
    st.markdown("---")
    st.markdown("### 📋 Programação das Salas Online")
    sala_escolhida = st.selectbox("Escolha a Sala:", [
        "Sala 1: Abertura e Conferências Principais",
        "Sala 2: Apresentação de Trabalhos - Fisioterapia Musculoesquelética",
        "Sala 3: Apresentação de Trabalhos - Saúde Coletiva e Extensão",
        "Sala 4: Mesas-redondas e Encerramento"
    ])
    st.info("🔴 **Status:** Transmissão agendada. O link será ativado no horário oficial do evento.")
    st.link_button(f"🔗 Entrar na {sala_escolhida}", "COLE_LINK_DA_SALA")

# --- 8. EVENTOS ANTERIORES ---
elif menu == "📂 Eventos Anteriores":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("📂 Repositório de Eventos Anteriores")
    st.write("Acesse abaixo os acervos, anais e certificados de edições passadas do nosso portal.")
    
    tab_ant1, tab_ant2 = st.tabs(["📚 Anais de Anos Anteriores", "📜 Certificados de Anos Anteriores"])
    
    with tab_ant1:
        st.markdown("### 📚 Anais Publicados em Edições Passadas")
        st.link_button("📥 Baixar Apresentação; Expediente dos Anais da Jornada Científica", "COLE_LINK_PDF_ANAIS_AQUI")
        st.link_button("📥 Baixar Apresentação; Expediente dos Anais da Mostra de Extensão", "COLE_LINK_PDF_ANAIS_AQUI") 
        st.link_button("📥 Acessar Pasta Geral de Anais Anteriores no Drive", "COLE_LINK_PASTA_ANAIS_ANTERIORES")
        
    with tab_ant2:
        st.markdown("### 📜 Consulta de Certificados Anteriores")
        ano_anterior = st.selectbox("Selecione o Ano do Evento:", ["2025", "2024"])
        with st.form("form_cert_antigos"):
            email_antigo = st.text_input("Digite seu e-mail cadastrado no evento anterior:")
            buscar_antigo = st.form_submit_button("Consultar Certificado Antigo")
            if buscar_antigo and email_antigo:
                st.link_button("🔗 Abrir Link de Emissão do Ano Selecionado", "COLE_LINK_CERTIFICADOS_ANTERIORES")

# --- 9. CONTATO (Com seção para Solicitação de Cadastro de Evento) ---
elif menu == "📞 Contato":
    mostrar_cabecalho("capaS.jpg")
    st.subheader("📞 Fale Conosco")
    st.write("Entre em contato com a comissão organizadora para dúvidas sobre submissões, inscrições ou certificados.")
    st.markdown("---")
    
    # Seção para solicitação de cadastro de evento
    st.markdown("### 🏛️ Está organizando um Evento? Solicite o Cadastro pelo link")
    st.write("Deseja hospedar e gerenciar as inscrições, submissões e certificações do seu evento acadêmico em nossa plataforma? Acesse o formulário dedicado abaixo:")
    st.link_button("📝 Solicitar Cadastro de Novo Evento", "COLE_LINK_FORMULARIO_CADASTRO_EVENTO_AQUI")
    
    st.markdown("---")
    st.info("📧 **E-mail oficial de suporte:** eventos@sciencenexus.com.br")
    st.write("Nossa equipe responderá sua mensagem em até 24 horas úteis.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray; font-size: 14px;'>© {ano_atual} OLIVEIRA, L.M.V. Todos os direitos reservados.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 13px;'>O conteúdo deste website (textos, imagens e dados) está protegido pela Lei de Direitos Autorais (Lei nº 9.610/1998).</p>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 13px;'>
    Esta obra está licenciada sob uma Licença <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt-br" target="_blank">Creative Commons Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional</a>.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class='footer-box'>
    <strong>Como citar este site:</strong><br>
    OLIVEIRA, L.M.V. <em>Science Nexus Plataforma</em>. Disponível em: &lt;www.sciencenexus.com.br&gt;. Acesso em: [Data de Acesso].
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray; font-size: 13px;'>Science Nexus Plataforma | Saúde • Sociedade • Tecnologias • Humanidades</p>", unsafe_allow_html=True)
