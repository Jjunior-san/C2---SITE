import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage, HomePageContent

# Seed Home Page
home, created = HomePageContent.objects.get_or_create(id=1)
if created:
    print("Conteúdo da Home Page criado com valores padrão.")
else:
    print("Conteúdo da Home Page já existe.")

# Seed Software
software_html = """<p>Criamos soluções sob medida para empresas e órgãos públicos: <b>STA, SGEO, SHP, SIG</b>, além do <b>desenvolvimento de sites</b> rápidos, responsivos e prontos para converter visitantes em clientes.</p>

<ul style="color: #555555; margin-left: 1.5rem; margin-top: 1rem;">
  <li><b>STA - Sistema de Triagem e Atendimento</b> (painel, triagem, guichês e relatórios) <i><a href="/p/updates-sta/">versões</a></i></li>
  <li><b>SGEO - Sistema de Georreferenciamento&nbsp;</b><i><a href="/p/updates-sgeo/">versões</a></i></li>
  <li><b>SHP- Sistema de Hotelaria e Pousada&nbsp;</b><i style="font-weight: 400;"><a href="/p/updates-shp/">versões</a></i></li>
  <li><b>SIG - Sistema de Integração de Gestão&nbsp;</b><i><a href="/p/updates-sig/">versões</a></i></li>
  <li><b>Sites institucionais</b> e landing pages (responsivos e otimizados)</li>
  <li><b>Integrações</b> com WhatsApp, e-mail, APIs e banco de dados (SQL/NoSQL)</li>
  <li><b>Hospedagem, domínio</b> e manutenção evolutiva do sistema/site</li>
</ul>

<div style="margin-top: 2rem;">
  <a class="btn-cta" href="/contato/">Solicitar Orçamento</a>
</div>"""

DynamicPage.objects.update_or_create(
    slug='software',
    defaults={
        'title': 'Software & Sites',
        'icon': 'fas fa-code',
        'content': software_html,
        'is_active': True
    }
)

# Seed Infraestrutura
infra_html = """<p>Planejamento e execução de <b>infraestrutura lógica</b> (diagramação, roteamento e configuração geral de equipamentos), com ambientes modernos em <b>cluster</b>, <b>VMs</b> e <b>nuvem</b> — garantindo desempenho, segurança e alta disponibilidade.</p>

<ul style="color: #555555; margin-left: 1.5rem; margin-top: 1rem;">
  <li><b>Diagrama lógico</b> (rede, VLANs, sub-redes, ACLs e serviços)</li>
  <li><b>Roteamento lógico</b> (estático/dinâmico, segmentação e regras)</li>
  <li><b>Configuração de equipamentos</b> (switches, roteadores, mikrotik, firewall, Wi-Fi)</li>
  <li><b>Virtualização</b>: cluster, VMs, snapshots e políticas de backup</li>
  <li><b>Linux</b> e <b>Windows Server</b> (AD, DNS, DHCP, arquivos e permissões)</li>
</ul>

<div style="margin-top: 2rem;">
  <a class="btn-cta" href="/contato/">Analisar Minha Rede</a>
</div>"""

DynamicPage.objects.update_or_create(
    slug='infraestrutura',
    defaults={
        'title': 'Infraestrutura Lógica & Cloud',
        'icon': 'fas fa-server',
        'content': infra_html,
        'is_active': True
    }
)

# Seed Marketing
mkt_html = """<p>Estratégias digitais para fortalecer sua marca, atrair clientes e aumentar vendas com presença online profissional, tráfego qualificado e campanhas bem segmentadas.</p>

<ul style="margin-left: 1.5rem; margin-top: 1rem; color: #555;">
  <li>Gestão de redes sociais (conteúdo, calendário e design)</li>
  <li>Tráfego pago (Google Ads e Meta Ads) com otimização contínua</li>
  <li>Criação de landing pages e campanhas para captação de leads</li>
  <li>SEO (posicionamento no Google) e melhoria de performance do site</li>
  <li>Relatórios e métricas (alcance, leads, CAC, conversão)</li>
</ul>

<div style="margin-top: 2rem;">
  <a href="/contato/" class="btn-cta">Impulsionar Meu Negócio</a>
</div>"""

DynamicPage.objects.update_or_create(
    slug='marketing',
    defaults={
        'title': 'Marketing',
        'icon': 'fas fa-bullhorn',
        'content': mkt_html,
        'is_active': True
    }
)

# Seed Contato
contato_html = """<p>Estamos prontos para ouvir você. Utilize os canais abaixo para solicitar orçamentos, suporte técnico ou esclarecer dúvidas.</p>
<br>
<ul>
    <li><strong>WhatsApp:</strong> (75) 98314-5691</li>
    <li><strong>E-mail:</strong> contato@c2sistemas.com</li>
</ul>
<br>
<a class='btn-cta' href='https://wa.me/75983145691?text=Ol%C3%A1%2C%20quero%20falar%20com%20a%20C%C2%B2%20Sistemas.' rel='noopener' target='_blank'>
    Abrir Atendimento no WhatsApp
</a>"""

DynamicPage.objects.update_or_create(
    slug='contato',
    defaults={
        'title': 'Fale Conosco',
        'icon': 'fas fa-envelope',
        'content': contato_html,
        'is_active': True
    }
)

print("Todas as páginas dinâmicas foram migradas/populadas com sucesso!")
