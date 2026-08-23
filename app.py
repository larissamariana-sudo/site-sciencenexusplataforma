import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Science Nexus Plataforma | Saúde • Sociedade • Tecnologias • Humanidades",
    page_icon="🩺",
    layout="wide"
)

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
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE ESTILO (Imagem menor, centralizada e aplicada em todas as abas) ---
def mostrar_cabecalho(foto="capa0.jpg"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(foto, width=600)
    
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
    "🎓 Certificados e Validação", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados",
    "📂 Eventos Anteriores",
    "📞 Contato"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("Bem-vindo à Science Nexus Plataforma | Saúde • Sociedade • Tecnologias • Humanidades")
    st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação e publicação de anais.")
    st.markdown("""
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Avaliação:** Acompanhe em tempo real se seu trabalho está em análise, aprovado ou pendente de correções.
    """)

# --- 2. EVENTOS E INSCRIÇÕES ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho("PORTAL0.jpg")
    st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes, consultar a programação e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia", 
        "2. Minicurso Prático: Reabilitação e Terapia Manual", 
        "3. Workshop: Inovação e Tecnologias em Saúde",
        "4. Simpósio de Saúde Coletiva e Políticas Públicas",
        "5. Encontro Científico Docente"
    ])
    
    st.markdown("---")
    
    if "Jornada Científica" in evento_selecionado:
        st.image("logo_jornada.png.jpg", width=400)
        st.markdown("### 🩺 Jornada Científica do Curso de Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes, docentes, profissionais e pesquisadores.
        * **Investimento:** 
          * Estudantes, Docentes e Banca da PUC Goiás: **Gratuito**.
          * Participantes Externos: **R$ 10,00** (Standby mediante comprovante na chave `eventoscientificosc@gmail.com`).
        * **Destaque:** Permite submissão de Resumos Simples, Expandidos e Artigos Completos com ISBN gratuito.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Fisioterapia Musculo Esquelética, Neurológica, Cardiorrespiratória, Terapia Intensiva, Geriatria e Gerontologia, Saúde da Mulher, Saúde Coletiva, Tecnologias e Inteligência Artificial na Saúde e Outras Áreas.**")
        st.warning("⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby** até a validação do comprovante.")
        
        st.markdown("---")
        st.markdown("#### 📅 Programação do Evento")
        st.write("Consulte os horários, apresentações de Projeto de Pesquisa e Trabalhos de Conclusão de Curso:")
        st.link_button("📅 Ver / Baixar Programação da Jornada EM BREVE", "COLE_LINK_PROGRAMACAO_JORNADA")
        
    elif "Minicurso Prático" in evento_selecionado:
        st.markdown("### 🤲 Minicurso Prático: As leis da robótica de Azimov aplicadas à IA")
        st.write("Detalhes e práticas avançadas em terapia manual para acadêmicos e profissionais.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Minicurso EM BREVE", "COLE_LINK_PROGRAMACAO_MINICURSO")
        
    elif "Workshop" in evento_selecionado:
        st.markdown("### 💡 Workshop: Inovação e Tecnologias em Saúde")
        st.write("Discussão sobre novas tecnologias e o futuro da reabilitação e saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Workshop EM BREVE", "COLE_LINK_PROGRAMACAO_WORKSHOP")
        
    elif "Simpósio de Saúde Coletiva" in evento_selecionado:
        st.markdown("### 📊 Simpósio de Saúde Coletiva e Políticas Públicas")
        st.write("Debates e mesas-redondas sobre o impacto das políticas públicas na saúde.")
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Simpósio EM BREVE", "COLE_LINK_PROGRAMACAO_SIMPOSIO")
        
    elif "Encontro Científico" in evento_selecionado:
        st.markdown("### 🎓 Encontro Científico PsicoHistória")
        st.write("""
        * **Foco:** Integração científica dos acadêmicos da graduação.
        * **Investimento:** Gratuito para a comunidade acadêmica da FST.
        """)
        st.markdown("#### 📅 Programação do Evento")
        st.link_button("📅 Ver / Baixar Programação do Encontro EM BREVE", "COLE_LINK_PROGRAMACAO_ENCONTRO")
    
    st.markdown("---")
    cat = st.radio("Selecione a opção desejada para inscrição:", [
        "Participante/Ouvinte", "Apresentador de Trabalho", "Membro da Banca", "Cadastro de Trabalho para Certificação (Orientador)"
    ])
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", "https://forms.gle/3q9LWnYiv3AdwiiM6")
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
            
            **INSTRUÇÕES DE FORMATAÇÃO OBRIGATÓRIAS**
            * **Espaçamento:** Entre os tópicos/seções do seu trabalho, inserir uma linha em branco. 
            * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
            * **Alinhamento:** Justificado.
            * **Título:** Alinhado à esquerda, em caixa alta e negrito.
            * **Autores:** Primeiro nome (acadêmico); segundo nome (orientador). Escritos de forma corrida, separados por ponto e vírgula, em caixa alta. Ex.: Maria de Oliveira1; Antônio da Silva2.
            * **Instituição:** 1;2 Nome da Universidade ou Instituição de Vínculo.
            """)
            st.info("💡 Ideal para resumos de trabalhos que exigem ineditismo, relatos de experiência, pesquisas em andamento ou revisões bibliográficas preliminares.")
        
        with tab_expandido:
            st.markdown("### Normas para Submissão de Resumo Expandido")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 4 páginas e no máximo 7 páginas completas.
            * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
            * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
            * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
            * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
            * **Título:** Alinhado à esquerda, em caixa alta e negrito.
            * **Autores:** Primeiro nome (acadêmico); segundo nome (orientador). Escritos de forma corrida, separados por ponto e vírgula, em caixa alta. Ex.: Maria de Oliveira1; Antônio da Silva2.
            * **Instituição:** 1;2 Nome da Universidade ou Instituição de Vínculo.
            
            **INFORMAÇÕES PARA A SUBMISSÃO**
            * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
            * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
            * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
            * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
            """)
            st.info("💡 Indicado para artigos científicos e pesquisas finalizadas que necessitam de um detalhamento metodológico maior.")
                   
        with tab_completo:
            st.markdown("### Normas para Submissão de Artigo Completo")
            st.markdown("""
            * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
            * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
            * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
            * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
            * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
            * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
            * **Título:** Alinhado à esquerda, em caixa alta e negrito.
            * **Autores:** Primeiro nome (acadêmico); segundo nome (orientador). Escritos de forma corrida, separados por ponto e vírgula, em caixa alta. Ex.: Maria de Oliveira1; Antônio da Silva2.
            * **Instituição:** 1;2 Nome da Universidade ou Instituição de Vínculo.
            
            **INFORMAÇÕES PARA A SUBMISSÃO**
            * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
            * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
            * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
            * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
            """)

        st.markdown("---")
        st.info("📌 **Importante:** Para que os arquivos sejam salvos diretamente na nuvem da comissão científica, a submissão é feita por formulário dedicado.")
        st.link_button("📥 Clique aqui para acessar o Formulário de Submissão de Trabalhos", "https://forms.gle/UUmLAAEdCwY9JRrY6")
    
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
                        id_planilha = link_planilha.split("/d/")[1].split("/")[0]
                        url_csv = f"https://docs.google.com/spreadsheets/d/{id_planilha}/export?format=csv"
                        
                        df = pd.read_csv(url_csv)
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
                    except Exception as e:
                        st.error(f"Erro ao ler planilha: {e}")
                else:
                    st.error("Por favor, digite um e-mail.")

# --- 4. CERTIFICADOS E VALIDAÇÃO ---
elif menu == "🎓 Certificados e Validação":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("🎓 Central de Certificados e Validação")
    tab1, tab2 = st.tabs(["📜 Emitir Certificado", "🛡️ Validar Autenticidade por Código"])
    
    with tab1:
        st.write("Selecione a categoria do seu certificado:")
        
        cat_cert = st.selectbox("Categoria de Emissão:", [
            "Participante / Ouvinte", 
            "Apresentador de Trabalho", 
            "Membro da Banca Examinadora"
        ])
        
        # Definição dos links das planilhas conforme solicitado
        if "Ouvinte" in cat_cert:
            link_planilha_cert = "https://docs.google.com/spreadsheets/d/15D_Vay3AQDUrbmaHjgwTeg0irLHX5q2pw6sw_wtiDl0/edit?usp=sharing"
            st.info("ℹ️ Emissão baseada na planilha de frequência de ouvintes.")
        else:
            link_planilha_cert = "https://docs.google.com/spreadsheets/d/1eEQeDcwCQ9gkpy9MAI9It7gk1fx1QwZRXBnhRhvkg6o/edit?usp=sharing"
            st.info("ℹ️ Emissão baseada na planilha de apresentadores e membros da banca.")
        
        termo_busca = st.text_input("Digite o seu Nome Completo ou E-mail cadastrado:").strip().lower()
        
        if st.button("Gerar e Baixar Certificado em PDF"):
            if termo_busca:
                try:
                    if "COLE_LINK" in link_planilha_cert:
                        st.error("⚠️ O link da planilha correspondente ainda não foi configurado no sistema. Por favor, insira o link correto.")
                    else:
                        id_c = link_planilha_cert.split("/d/")[1].split("/")[0]
                        url_c_csv = f"https://docs.google.com/spreadsheets/d/{id_c}/export?format=csv"
                        
                        df_emit = pd.read_csv(url_c_csv)
                        df_emit.columns = df_emit.columns.str.strip().str.lower()
                        
                        col_email_emit = next((c for c in df_emit.columns if 'email' in c.replace('-', '').lower()), None)
                        col_nome_emit = next((c for c in df_emit.columns if 'nome' in c.lower() or 'participante' in c.lower()), None)
                        col_cod_emit = next((c for c in df_emit.columns if 'codigo' in c.lower() or 'chave' in c.lower() or 'autenticidade' in c.lower()), None)
                        
                        if col_email_emit and col_nome_emit:
                            df_emit[col_email_emit] = df_emit[col_email_emit].astype(str).str.strip().str.lower()
                            df_emit[col_nome_emit] = df_emit[col_nome_emit].astype(str).str.strip().str.lower()
                            
                            # Busca por e-mail ou por nome
                            res_emit = df_emit[(df_emit[col_email_emit] == termo_busca) | (df_emit[col_nome_emit].str.contains(termo_busca, na=False))]
                            
                            if not res_emit.empty:
                                pessoa_logada = str(res_emit.iloc[0][col_nome_emit]).title()
                                codigo_auth = str(res_emit.iloc[0][col_cod_emit]) if col_cod_emit else "PUCGO-2026-OFICIAL"
                                
                                Título = str(res_emit.iloc[0].get('titulo', 'Título do Trabalho não informado')).strip()
                                Nome_Orientador = str(res_emit.iloc[0].get('orientador', 'Orientador')).strip().title()
                                Nome_Aluno = str(res_emit.iloc[0].get('nome_aluno', 'Nome')).strip().title()
                                Nome_Banca1 = str(res_emit.iloc[0].get('banca1', 'Avaliador 1')).strip().title()
                                Nome_Banca2 = str(res_emit.iloc[0].get('banca2', 'Avaliador 2')).strip().title()
                                Data_Evento = "20 a 22 de outubro de 2026"
                                CargaHoraria = "20"
                                Evento = "Jornada Científica do Curso de Fisioterapia da PUC Goiás (2026/2)"
                                
                                st.success(f"✅ Participante encontrado: **{pessoa_logada}**")
                                
                                # --- GERAÇÃO DO PDF COM REPORTLAB ---
                                import io
                                from reportlab.lib.pagesizes import letter, landscape
                                from reportlab.pdfgen import canvas
                                from reportlab.lib import colors
                                from reportlab.platypus import Paragraph
                                from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                                
                                buffer = io.BytesIO()
                                c = canvas.Canvas(buffer, pagesize=landscape(letter))
                                largura, altura = landscape(letter)
                                
                                try:
                                    c.drawImage("fundo_certificado.jpg", 0, 0, width=largura, height=altura, preserveAspectRatio=False)
                                except:
                                    c.setFillColor(colors.white)
                                    c.rect(0, 0, largura, altura, fill=1, stroke=0)
                                    
                                    c.setStrokeColor(colors.HexColor("#004225"))
                                    c.setLineWidth(6)
                                    c.rect(25, 25, largura - 50, altura - 50)
                                    c.setLineWidth(1)
                                    c.rect(32, 32, largura - 64, altura - 64)

                                c.setFont("Helvetica-Bold", 16)
                                c.setFillColor(colors.HexColor("#004225"))
                                c.drawCentredString(largura / 2, altura - 75, "PONTIFÍCIA UNIVERSIDADE CATÓLICA DE GOIÁS")
                                
                                c.setFont("Helvetica", 11)
                                c.setFillColor(colors.HexColor("#555555"))
                                c.drawCentredString(largura / 2, altura - 95, "Escola de Ciências Sociais e da Saúde • Curso de Fisioterapia")
                                
                                c.setFont("Helvetica-Bold", 26)
                                c.setFillColor(colors.HexColor("#004225"))
                                c.drawCentredString(largura / 2, altura - 150, "CERTIFICADO DE PARTICIPAÇÃO")
                                
                                c.setFont("Helvetica", 13)
                                c.setFillColor(colors.HexColor("#333333"))
                                c.drawCentredString(largura / 2, altura - 195, "Certificamos, para os devidos fins, que")
                                
                                c.setFont("Helvetica-Bold", 22)
                                c.setFillColor(colors.HexColor("#000000"))
                                c.drawCentredString(largura / 2, altura - 230, pessoa_logada)
                                
                                styles = getSampleStyleSheet()
                                estilo_texto = ParagraphStyle(
                                    'EstiloCertificado',
                                    parent=styles['Normal'],
                                    fontName='Helvetica',
                                    fontSize=11,
                                    leading=16,
                                    alignment=1,
                                    textColor=colors.HexColor("#333333")
                                )
                                
                                if "Ouvinte" in cat_cert:
                                    texto_conteudo = f"participou do evento científico {Evento}, realizado na modalidade presencial, no período de {Data_Evento}, com carga horária total de {CargaHoraria} horas, na qualidade de Ouvinte."
                                elif "Apresentador" in cat_cert:
                                    texto_conteudo = f"apresentou como autor o trabalho intitulado <b>\"{Título}\"</b>, orientado por <b>{Nome_Orientador}</b>, tendo como banca examinadora <b>{Nome_Banca1}</b> e <b>{Nome_Banca2}</b>, apresentado em sessão pública na {Evento} nos dias {Data_Evento}."
                                else:
                                    texto_conteudo = f"participou como Membro da Banca Examinadora do trabalho intitulado <b>\"{Título}\"</b>, orientado por <b>{Nome_Orientador}</b> e apresentado em sessão pública na {Evento} nos dias {Data_Evento}."
                                
                                p = Paragraph(texto_conteudo, estilo_texto)
                                p.wrap(largura - 160, 100)
                                p.drawOn(c, 80, altura - 330)
                                
                                try:
                                    c.drawImage("signsf.png", largura - 250, 95, width=160, height=50, mask='auto')
                                except:
                                    pass 
                                
                                c.setStrokeColor(colors.HexColor("#333333"))
                                c.setLineWidth(0.8)
                                c.line(largura - 270, 90, largura - 70, 90)
                                
                                c.setFont("Helvetica-Bold", 9)
                                c.setFillColor(colors.HexColor("#333333"))
                                c.drawCentredString(largura - 170, 75, "Comissão Organizadora / Coordenação do Curso de Fisioterapia / Prof. Larissa Mariana V de Oliveira")

                                c.setStrokeColor(colors.HexColor("#CCCCCC"))
                                c.line(60, 60, largura - 60, 60)
                                
                                c.setFont("Helvetica-Bold", 8)
                                c.setFillColor(colors.HexColor("#444444"))
                                c.drawString(60, 45, f"Código de Autenticidade: {codigo_auth}")
                                c.drawRightString(largura - 60, 45, "Verificado oficialmente via Science Nexus (PUC Goiás)")
                                
                                c.showPage()
                                c.save()
                                
                                buffer.seek(0)
                                
                                st.download_button(
                                    label="📥 Baixar Certificado Oficial em PDF",
                                    data=buffer,
                                    file_name=f"Certificado_{pessoa_logada.replace(' ', '_')}.pdf",
                                    mime="application/pdf"
                                )
                            else:
                                st.error("Nenhum registro encontrado com este nome ou e-mail na base de dados de certificados. Verifique se digitou corretamente.")
                        else:
                            st.error("A planilha precisa conter colunas de 'Email' e 'Nome'.")
                except Exception as e:
                    st.error(f"Erro ao processar a emissão do certificado: {e}")
            else:
                st.error("Por favor, digite o nome ou o e-mail cadastrado.")
                
    with tab2:
        st.subheader("🛡️ Validação de Autenticidade por Código")
        st.write("Insira o **Código de Autenticidade** impresso no rodapé do certificado para verificar sua veracidade:")
        with st.form("form_validacao_cert"):
            codigo_digitado = st.text_input("Código de Autenticidade:", placeholder="Ex: PUCGO-2026-XXXX").strip()
            validar_btn = st.form_submit_button("Verificar Autenticidade")
            
            if validar_btn:
                if codigo_digitado:
                    try:
                        link_planilha_cert_val = "https://docs.google.com/spreadsheets/d/1eEQeDcwCQ9gkpy9MAI9It7gk1fx1QwZRXBnhRhvkg6o/edit?usp=sharing"
                        
                        id_c = link_planilha_cert_val.split("/d/")[1].split("/")[0]
                        url_c_csv = f"https://docs.google.com/spreadsheets/d/{id_c}/export?format=csv"
                        
                        df_c = pd.read_csv(url_c_csv)
                        df_c.columns = df_c.columns.str.strip().str.lower()
                        
                        col_cod = next((c for c in df_c.columns if 'codigo' in c or 'chave' in c or 'autenticidade' in c), None)
                        
                        if col_cod:
                            df_c[col_cod] = df_c[col_cod].astype(str).str.strip().str.lower()
                            res_c = df_c[df_c[col_cod] == codigo_digitado.lower()]
                            
                            if not res_c.empty:
                                nome_p = res_c.iloc[0].get('nome', 'Participante')
                                st.success("✅ **CERTIFICADO VÁLIDO E AUTÊNTICO!**")
                                st.write(f"Este certificado pertence oficialmente a: **{nome_p}** — Jornada Científica de Fisioterapia 2026/2 (PUC Goiás).")
                            else:
                                st.error("❌ **Certificado Inválido ou Falso:** O código informado não consta na base de dados oficial.")
                        else:
                            st.warning("A planilha precisa ter uma coluna nomeada como 'Codigo' ou 'Chave'.")
                    except Exception as e:
                        st.error(f"Erro ao consultar base de certificados: {e}")
                else:
                    st.error("Por favor, digite o código de autenticidade.")

# --- 5. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("A publicação nos Anais oficiais com ISBN é gratuita. O DOI individual é opcional (R$ 20,00).")
    st.info("ℹ️ **Chave PIX:** eventoscientificosc@gmail.com")
    st.link_button("🔗 Link para Solicitação DOI", "https://forms.gle/ZjKAcp7LuK8zFFub8")

# --- 6. ANAIS ---
elif menu == "📚 Anais Publicados":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📚 Repositório Oficial de Anais")
    st.link_button("📥 Baixar Anais", "COLE_LINK_PDF_ANAIS_AQUI")

# --- 7. EVENTOS ANTERIORES ---
elif menu == "📂 Eventos Anteriores":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📂 Repositório de Eventos Anteriores")
    st.write("Acesse abaixo os acervos, anais e emissão de certificados de edições passadas do nosso portal de eventos.")
    
    tab_ant1, tab_ant2 = st.tabs(["📚 Anais de Anos Anteriores", "📜 Certificados de Anos Anteriores"])
    
    with tab_ant1:
        st.markdown("### 📚 Anais Publicados em Edições Passadas")
        st.write("Consulte os cadernos de resumos e anais oficiais dos anos anteriores:")
        st.markdown("""
        * **Jornada Científica EM BREVE** — [📥 Baixar Anais EM BREVE](COLE_LINK_ANAIS_2026)
        * **Jornada Científica EM BREVE** — [📥 Baixar Anais EM BREVE](COLE_LINK_ANAIS_2027)
        """)
        st.link_button("📥 Acessar Pasta Geral de Anais Anteriores no Drive EM CONSTRUÇÃO", "COLE_LINK_PASTA_ANAIS_ANTERIORES")
        
    with tab_ant2:
        st.markdown("### 📜 Consulta de Certificados Anteriores EM CONTRUÇÃO")
        st.write("Se você participou de edições passadas e precisa recuperar seu certificado, selecione o ano correspondente:")
        ano_anterior = st.selectbox("Selecione o Ano do Evento:", ["20XX", "20XX"])
        
        with st.form("form_cert_antigos"):
            email_antigo = st.text_input("Digite seu e-mail cadastrado no evento anterior:")
            buscar_antigo = st.form_submit_button("Consultar e Baixar Certificado Antigo")
            
            if buscar_antigo:
                if email_antigo:
                    st.info(f"Buscando histórico para o e-mail: {email_antigo} ({ano_anterior})")
                    st.link_button("🔗 Abrir Link de Emissão do Ano Selecionado", "COLE_LINK_CERTIFICADOS_ANTERIORES")
                else:
                    st.error("Por favor, informe o e-mail.")

# --- 8. CONTATO ---
elif menu == "📧 Contato":
    mostrar_cabecalho("capa0.jpg")
    st.subheader("📧📞 Fale Conosco")
    st.write("Entre em contato com a comissão organizadora para dúvidas sobre submissões, inscrições ou certificados.")
    st.markdown("---")
    st.info("📧 **E-mail oficial de suporte:** eventoscientificosc@gmail.com")
    st.write("Nossa equipe responderá sua mensagem em até 48 horas úteis.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Science Nexus Plataforma | Saúde • Sociedade • Tecnologias • Humanidades</p>", unsafe_allow_html=True)
