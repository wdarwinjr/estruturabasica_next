# PROTO - Suite do Contencioso

Autor: Centro de Excelência em Inteligência Artificial - CEIA

Equipe: Jorge Eduardo de Schoucair Jambeiro Filho
        Patrick Moreira Nogali
        Tiago Monteiro Cardoso
        Willian Darwin Junior

Processo de Trabalho: Julgar impugnações e manifestação de inconformidade.

Descrição do Projeto: Plataforma para integração de processos de trabalho do contencioso da RFB preparada para uso de aplicações inteligentes (IA).

Elementos do Projeto:
1.	Containers Docker
2.	Autenticação (inicialmente Keycloak, em definitivo Azure)
3.	Proxy reverso (NGINX, depois Traefik)
4. 	Backend com FastAPI, Python, MotorAsyncIO
5. 	Frontend com Javascript, Vue.js, Vue.Router, Axios
6. 	Banco de Dados MongoDB (com transição a partir do MariaDB)
7. 	Jupyter Notebook para testes e execuções pontuais
8.  IDE VSCode para desenvolvimento

Funcionalidades do Protótipo: 
1.	Rotulação de acórdãos do CARF
2.	Prospecção de uso de inteligência artificial no processo de trabalho do contencioso da RFB, incluindo tratamento de Linguagem Natural (PLN).

Requisitos Essenciais:
1.	Implementação de solução de segurança (autenticação e trilha de auditoria) pela área de tecnologia;
2.	Disponibilização institucional dos dados que serão usados como insumo para o projeto.

Justificativa:
O objetivo estruturante e abrangente é iniciar a formação de cultura, a capacitação de equipe e a preparação de ambiente e infraestrutura para os próximos projetos de racionalização dos processos do Contencioso da RFB com uso de abordagens não-determinísticas e da tecnologia de Inteligência Artificial (IA).
Futuramente, mas não integra a primeira parte do projeto, a plataforma irá receber as aplicações que implementarem processos de trabalho do Contencioso dentro da abordagem por ela proposta, tais como ferramentas de apoio ao julgamento (migração e implementação de julgamentos de baixa complexidade - JAP), às atividades associadas (por exemplo, triagem) e à gestão dos processos de trabalho.

