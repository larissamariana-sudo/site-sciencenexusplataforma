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
    /* Fundo geral da página mais limpo e profissional */
    .stApp {
        background-color: #f8f9fa;
    }
    .element-container {
        color: #333333;
    }
    /* Estilo para a caixa de citação acadêmica no rodapé */
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

# --- FUNÇÕES DE ESTILO (Imagem menor, centralizada e aplicada em todas as abas) ---
def mostrar_cabecalho(foto="capa0.jpg"):
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

# --- MENU ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Eventos e Inscrições", 
    "✍️ Trabalhos Científicos", 
    "📺 Transmissão ao Vivo",
    "🎓 Validação de Certificados", 
    "💳 Taxa de DOI Individual/Pessoal", 
    "💳 Taxa de ISBN Coletivo",
    "📚 Anais Publicados",
    "📂 Eventos Anteriores",
    "📞 Contato"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("Bem-vindo à Science Nexus Plataforma Científica")
    st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação e publicação de anais.")
    st.markdown("""
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Registros:** Anais com **ISBN** e **DOI** opcional.
    * **Avaliação:** Acompanhe em tempo real se seu trabalho está em análise, aprovado ou pendente de correções.
    """)

# --- 2. EVENTOS E INSCRIÇÕES ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho("eventos.png")
    st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes, consultar a programação e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia",
        "2. Acolhimento dos Monitores Caeme/Prograd", 
        "3. Mostra Extensionista da Graduação em Fisioterapia", 
        "4. Encontro Formativo PET Saúde Clima",
        "5. Minicurso Prático: Reabilitação e Terapia Manual", 
        "6. Workshop: Inovação e Tecnologias em Saúde",
        "7. Simpósio de Saúde Coletiva e Políticas Públicas",
        "8. Encontro Científico Psico História e as Leis da Robótica"
    ])
    
    st.markdown("---")
    
    # Exibição organizada por evento com espaço para Imagem e Logo
    if "Jornada Científica" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("logo_jornada.png.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação Institucional") # Substitua pelo arquivo de logo se houver
            
        st.markdown("### 🩺 Jornada Científica do Curso de Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes, docentes, profissionais e pesquisadores.
        * **Investimento:** 
          * Estudantes, Docentes e Banca da PUC Goiás: **Gratuito**.
          * Participantes Externos: **R$ 10,00** (Standby mediante comprovante na chave `eventoscientificosc@gmail.com`).
        * **Destaque:** Permite submissão de Resumos Simples, Expandidos e Artigos Completos com ISBN.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Fisioterapia Musculo Esquelética, Neurológica, Cardiorrespiratória, Terapia Intensiva, Geriatria e Gerontologia, Saúde da Mulher, Saúde Coletiva, Tecnologias e Inteligência Artificial na Saúde e Outras Áreas.**")
        st.warning("⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby** até a validação do comprovante.")
        
        st.markdown("---")
        st.markdown("#### 📅 Programação do Evento")
        st.write("Consulte os horários, apresentações de Projeto de Pesquisa e Trabalhos de Conclusão de Curso:")
        st.link_button("📅 Ver / Baixar Programação da Jornada EM BREVE", "COLE_LINK_PROGRAMACAO_JORNADA")
        
        opcoes_inscricao = [
            "Participante/Ouvinte", 
            "Orientador", 
            "Apresentador de Trabalho", 
            "Membro da Banca", 
            "Cadastro de Trabalho para Certificação (Orientador)"
        ]

    elif "Acolhimento dos Monitores" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("monitores.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("caeme.jpg", width=250, caption="Logo de Divulgação Caeme/Prograd")
            
        st.markdown("### 🤲 Acolhimento dos Monitores Caeme/Prograd")
        st.write("Data: 11/09 Matutino 9h às 10h30 Campus II Auditório Bloco S e Noturno 18h às 19h30 Área II Auditório II. Público: Monitores selecionados em 2026/2.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Acolhimento EM BREVE", "COLE_LINK_PROGRAMACAO_MINICURSO")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        
    elif "Mostra Extensionista da Graduação em Fisioterapia" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("extensao.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_extensao.png", width=250, caption="Logo de Divulgação")
            
        st.markdown("### 🩺 Mostra Extensionista da Graduação em Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes e docentes do curso de Fisioterapia.
        * **Investimento:** 
          * Estudantes e Docentes: **Gratuito**.
        * **Destaque:** Permite submissão de Resumos Simples e Resumos Expandidos com ISBN.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Disciplinas extensionistas do curso de Fisioterapia.**")
        st.warning("⚠️ **Sugestão: os modelos de banner devem ser adaptados para: Resumo Expandido**.")
        
        st.markdown("---")
        st.markdown("#### 📅 Programação do Evento")
        st.write("Consulte os horários de apresentações da Mostra Extensionista da Graduação da PUC Goiás:")
        st.link_button("📅 Ver / Baixar Programação da Mostra EM BREVE", "COLE_LINK_PROGRAMACAO_JORNADA")        
        
        opcoes_inscricao = [
            "Participante/Ouvinte", 
            "Orientador", 
            "Apresentador de Trabalho", 
            "Membro da Banca", 
            "Cadastro de Trabalho para Certificação (Orientador)"
        ]

    elif "PET Saúde Clima" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("capa0.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação PET Saúde Clima")
            
        st.markdown("### 🌱 Encontro Formativo PET Saúde Clima")
        st.write("""
        * **Foco:** Discussões integradas sobre saúde, meio ambiente e sustentabilidade climática.
        * **Modalidade de Certificação:** Certificado de Ouvinte / Participante.
        * **Público-alvo:** Membros do programa, acadêmicos, docentes e comunidade interessada.
        """)
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Encontro Formatível EM BREVE", "COLE_LINK_PROGRAMACAO_PET")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
    
    elif "Minicurso Prático" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("capa0.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação")
            
        st.markdown("### 🤲 Minicurso Prático: Reabilitação e Terapia Manual")
        st.write("Detalhes e práticas avançadas em terapia manual para acadêmicos e profissionais.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Minicurso EM BREVE", "COLE_LINK_PROGRAMACAO_MINICURSO")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        
    elif "Workshop" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("capa0.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação")
            
        st.markdown("### 💡 Workshop: Inovação e Tecnologias em Saúde")
        st.write("Discussão sobre novas tecnologias e o futuro da reabilitação e saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Workshop EM BREVE", "COLE_LINK_PROGRAMACAO_WORKSHOP")
        
        opcoes_inscricao = ["Participante/Ouvinte"]
        
    elif "Simpósio de Saúde Coletiva" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("capa0.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação")
            
        st.markdown("### 📊 Simpósio de Saúde Coletiva e Políticas Públicas")
        st.write("Debates e mesas-redondas sobre o impacto das políticas públicas na saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Simpósio EM BREVE", "COLE_LINK_PROGRAMACAO_SIMPOSIO")
        
        opcoes_inscricao = ["Participante/Ouvinte", "Apresentador de Trabalho"]
        
    elif "Encontro Científico" in evento_selecionado:
        col_img, col_logo = st.columns(2)
        with col_img:
            st.image("capa0.jpg", width=350, caption="Banner do Evento")
        with col_logo:
            st.image("logo_puc.png", width=250, caption="Logo de Divulgação")
            
        st.markdown("### 🎓 Encontro Científico Psico História e as Leis da Robótica")
        st.write("""
        * **Foco:** Integração científica dos acadêmicos da graduação.
        * **Investimento:** Gratuito para a comunidade acadêmica da FST.
        """)
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Encontro EM BREVE", "COLE_LINK_PROGRAMACAO_ENCONTRO")
        
        opcoes_inscricao = ["Participante/Ouvinte", "Apresentador de Trabalho"]
    
    st.markdown("---")
    cat = st.radio("Selecione a opção desejada para inscrição:", opcoes_inscricao)
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", "https://forms.gle/3q9LWnYiv3AdwiiM6")
    elif cat == "Orientador":
        st.link_button("🔗 Inscrever-se como Orientador", "https://forms.gle/3q9LWnYiv3AdwiiM6")
    elif cat == "Apresentador de Trabalho":
        st.link_button("🔗 Inscrever-se como Apresentador", "https://forms.gle/3q9LWnYiv3AdwiiM6")
    elif cat == "Membro da Banca":
        st.link_button("🔗 Inscrever-se como Banca", "https://forms.gle/3q9LWnYiv3AdwiiM6")
    else:
        st.info("⚠️ **Exclusivo para Orientadores:** Utilize este formulário para cadastrar o trabalho, estudante e banca para o certificado.")
        st.link_button("📝 Cadastrar Informações do Trabalho", "https://forms.gle/bTGR48dU3rrgBgr17")

# --- 3. TRABALHOS (SUBMISSÃO + STATUS) ---
elif menu == "✍️ Trabalhos Científicos":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("✍️ Central de Trabalhos Científicos")
    st.write("Consulte abaixo as normas e utilize o link do formulário exclusivo para enviar o seu arquivo Word (.doc/.docx).")
    
    tab_principal1, tab_principal2 = st.tabs(["📥 Submissão e Normas", "🔍 Consultar Status"])
    
    with tab_principal1:
        tab_simples, tab_expandido, tab_completo = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo"])
        
        with tab_simples:
            st.markdown("### Normas para Submissão de Resumo Simples")
            st.markdown("""
            * **Estrutura Obrigatória:** Introdução, Objetivos, Metodologia, Resultados e Discussão, e Considerações Finais.
            * **Formatação:** Mínimo de 250 palavras e Máximo de 350 palavras (excluindo título e referências). Fonte Times New Roman, tamanho 12, espaçamento 1,0.
            * **Palavras-chave:** De 3 a 5 palavras-chave separadas por ponto e vírgula.
            * **Autores:** Permitido até 3 autores por trabalho (incluindo o orientador).
            
            **INFORMAÇÕES PARA A SUBMISSÃO**
            * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
            * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
            * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
            * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
            """)
            st.info("💡 Ideal para resumos de trabalhos que exigem ineditismo, relatos de experiência, pesquisas em andamento ou revisões bibliográficas preliminares.")
            
            try:
                with open("regras_resumo_simples.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Resumo Simples)", pdf_file, file_name="Regras_Resumo_Simples.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *O PDF com as regras detalhadas estará disponível em breve.*")
        
        with tab_expandido:
            st.markdown("### Normas para Submissão de Resumo Expandido")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 4 páginas e no máximo 7 páginas completas.
            * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
            """)
            st.info("💡 Indicado para artigos científicos e pesquisas finalizadas que necessitam de detalhamento metodológico.")
            
            try:
                with open("regras_resumo_expandido.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Resumo Expandido)", pdf_file, file_name="Regras_Resumo_Expandido.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *O PDF com as regras detalhadas estará disponível em breve.*")
                    
        with tab_completo:
            st.markdown("### Normas para Submissão de Artigo Completo")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
            """)
            
            try:
                with open("regras_artigo_completo.pdf", "rb") as pdf_file:
                    st.download_button("📥 Baixar Regras Completas (PDF - Artigo Completo)", pdf_file, file_name="Regras_Artigo_Completo.pdf", mime="application/pdf")
            except Exception:
                st.caption("ℹ️ *O PDF com as regras detalhadas estará disponível em breve.*")

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
                                    if status_val.lower() == 'nan' or status_val == "":
                                        status_final = "Recebido"
                                    else:
                                        status_final = status_val
                                    
                                    if "aprovado" in status_final.lower():
                                        st.success(f"🎉 **Status:** {status_final}")
                                    elif "correção" in status_final.lower():
                                        st.error(f"⚠️ **Status:** {status_final} - Verifique seu e-mail.")
                                    else:
                                        st.info(f"⏳ **Status:** {status_final}")
                                else:
                                    st.error("Coluna 'Status' não encontrada na planilha.")
                            else:
                                st.warning("E-mail não encontrado na Coluna C.")
                        else:
                            st.error("Erro ao ler planilha.")
                    except Exception as e:
                        st.error(f"Erro ao ler planilha: {e}")
                else:
                    st.error("Por favor, digite um e-mail.")

# --- 4. TRANSMISSÃO AO VIVO ---
elif menu == "📺 Transmissão ao Vivo":
    mostrar_cabecalho("capa0.jpg")
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
    st.info("🔴 **Status:** Transmissão agendada.")
    st.link_button(f"🔗 Entrar na {sala_escolhida}", "COLE_LINK_DA_SALA_AQUI")

# --- 5. VALIDAÇÃO DE CERTIFICADOS ---
elif menu == "🎓 Validação de Certificados":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("🛡️ Validação de Autenticidade por Código")
    st.write("Insira o **Código de Autenticidade** exclusivo impresso no rodapé do certificado para comprovar sua validade:")
    
    with st.form("form_validacao_cert"):
        codigo_digitado = st.text_input("Código de Autenticidade:", placeholder="Ex: PUCGO-2026-XXXX").strip()
        validar_btn = st.form_submit_button("Verificar Autenticidade")
        
        if validar_btn:
            if codigo_digitado:
                try:
                    link_planilha_cert = "https://docs.google.com/spreadsheets/d/15D_Vay3AQDUrbmaHjgwTeg0irLHX5q2pw6sw_wtiDl0/edit?usp=sharing"
                    df_c = carregar_dados_planilha(link_planilha_cert)
                    
                    if df_c is not None:
                        col_cod = next((c for c in df_c.columns if 'codigo' in c or 'chave' in c or 'autenticidade' in c), None)
                        
                        if col_cod:
                            df_c[col_cod] = df_c[col_cod].astype(str).str.strip().str.lower()
                            res_c = df_c[df_c[col_cod] == codigo_digitado.lower()]
                            
                            if not res_c.empty:
                                nome_p = res_c.iloc[0].get('nome', 'Participante')
                                st.success("✅ **CERTIFICADO VÁLIDO E AUTÊNTICO!**")
                                st.write(f"Este certificado pertence oficialmente a: **{nome_p}** — Science Nexus (PUC Goiás).")
                            else:
                                st.error("❌ **Certificado Inválido ou Falso:** O código informado não consta na base de dados oficial da comissão organizadora.")
                        else:
                            st.warning("A planilha precisa ter uma coluna nomeada como 'Codigo' ou 'Chave'.")
                    else:
                        st.info("Configure o link da planilha de certificados no código para ativar a consulta automática.")
                except Exception as e:
                    st.error(f"Erro ao consultar base de certificados: {e}")
            else:
                st.error("Por favor, digite o código de autenticidade.")

# --- 6. DOI/ISBN ---
elif menu == "💳 Taxa de DOI Individual/Pessoal":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("O DOI individual é opcional (R$ 20,00).")
    st.info("ℹ️ **Chave PIX:** eventoscientificosc@gmail.com")
    st.link_button("🔗 Link para Solicitação DOI", "https://forms.gle/J1FArsU2fYT7nHU26")

elif menu == "💳 Taxa de ISBN Coletivo":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("💳 Solicitação e Pagamento de ISBN Coletivo")
    st.write("Taxa única ISBN, para o documento que conterá todos os resumos dos Anais (R$ 35,00).")
    st.info("ℹ️ **Chave PIX:** eventoscientificosc@gmail.com")
    st.link_button("🔗 Link para Solicitação ISBN", "https://forms.gle/2bN1yFrR5phvTcAu5")

# --- 7. ANAIS ---
elif menu == "📚 Anais Publicados":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📚 Repositório Oficial de Anais")
    st.link_button("📥 Baixar Anais Jornada Científica 2026/2", "COLE_LINK_PDF_ANAIS_AQUI")
    st.link_button("📥 Baixar Anais Mostra Extensionista 2026", "COLE_LINK_PDF_ANAIS_AQUI") 

# --- 8. EVENTOS ANTERIORES ---
elif menu == "📂 Eventos Anteriores":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📂 Repositório de Eventos Anteriores")
    st.write("Acesse abaixo os acervos, anais e emissão de certificados de edições passadas do nosso portal de eventos.")
    
    tab_ant1, tab_ant2 = st.tabs(["📚 Anais de Anos Anteriores", "📜 Certificados de Anos Anteriores"])
    
    with tab_ant1:
        st.markdown("### 📚 Anais Publicados em Edições Passadas")
        st.markdown("""
        * **Jornada Científica EM BREVE** — [📥 Baixar Anais EM BREVE](COLE_LINK_ANAIS_2026)
        * **Mostra Extensionista EM BREVE** — [📥 Baixar Anais EM BREVE](COLE_LINK_ANAIS_2026)
        """)
        st.link_button("📥 Baixar Apresentação; Expediente dos Anais da Jornada Científica 2026", "COLE_LINK_PDF_ANAIS_AQUI")
        st.link_button("📥 Baixar Apresentação; Expediente dos Anais da Mostra Extensionista 2026", "COLE_LINK_PDF_ANAIS_AQUI") 
        st.link_button("📥 Acessar Pasta Geral de Anais Anteriores no Drive", "COLE_LINK_PASTA_ANAIS_ANTERIORES")
        
    with tab_ant2:
        st.markdown("### 📜 Consulta de Certificados Anteriores")
        st.write("Se você participou de edições passadas e precisa recuperar seu certificado, selecione o ano correspondente:")
        ano_anterior = st.selectbox("Selecione o Ano do Evento:", ["20XX", "20XX"])
        
        with st.form("form_cert_antigos"):
            email_antigo = st.text_input("Digite seu e-mail cadastrado no evento anterior:")
            buscar_antigo = st.form_submit_button("Consultar Certificado Antigo")
            
            if buscar_antigo:
                if email_antigo:
                    st.info(f"Buscando histórico para o e-mail: {email_antigo} ({ano_anterior})")
                    st.link_button("🔗 Abrir Link de Emissão do Ano Selecionado", "COLE_LINK_CERTIFICADOS_ANTERIORES")
                else:
                    st.error("Por favor, informe o e-mail.")

# --- 9. CONTATO ---
elif menu == "📞 Contato":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📞 Fale Conosco")
    st.write("Entre em contato com a comissão organizadora para dúvidas sobre submissões, inscrições ou certificados.")
    st.markdown("---")
    st.info("📧 **E-mail oficial de suporte:** eventoscientificosc@gmail.com")
    st.write("Nossa equipe responderá sua mensagem em até 48 horas úteis.")

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
