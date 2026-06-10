import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """Seguimos evoluindo nossas soluções para entregar mais performance, integração e eficiência no dia a dia dos nossos clientes.&nbsp;<div><br /></div><div>&nbsp;💻 Sistemas atualizados:<br><br>STA (Sistema de Triagem e Atendimento): melhorias no painel, organização da triagem, otimização de guichês e novos relatórios gerenciais.</div><div><br /></div><div>SGEO (Georreferenciamento): evolução nas funcionalidades de mapeamento, precisão de dados e desempenho nas consultas.</div><div><br /></div><div>SHP (Hotelaria e Pousadas): ajustes operacionais, melhorias na usabilidade e maior controle das reservas e atendimentos.</div><div><br /></div><div>SGESTAO (Gestão Empresarial): avanços na integração entre departamentos, garantindo mais controle, agilidade e tomada de decisão.</div><div><br /></div><div>🌐 Sites e performance:<br><br>Otimizações em velocidade e responsividade<br>Melhorias em SEO e estrutura para conversão<br>Ajustes de layout focados em experiência do usuário<br><br>🔗 Integrações e tecnologia:<br><br>Atualizações nas integrações com WhatsApp, e-mail e APIs<br>Melhorias na comunicação com bancos de dados (SQL e NoSQL)<br>Maior estabilidade e segurança nas conexões&nbsp;</div><div><br /></div><div>&nbsp;⚙️ Infraestrutura:<br><br>Aprimoramento em hospedagem e desempenho<br>Manutenção evolutiva contínua dos sistemas e sites&nbsp;</div><div>Monitoramento e correções preventivas<br><br>📈&nbsp;</div><div><br /></div><div>Nosso foco é simples: sistemas mais rápidos, inteligentes e preparados para crescer junto com o seu negócio.<br><br>Acompanhe nossas atualizações e evoluções constantes 🚀</div>"""

page, created = DynamicPage.objects.update_or_create(
    slug='updates',
    defaults={
        'title': '🔄 Atualizações — Software & Sites | C2 Sistemas',
        'icon': 'fas fa-sync-alt',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Updates criada com sucesso!")
else:
    print("Página de Updates atualizada com sucesso!")
