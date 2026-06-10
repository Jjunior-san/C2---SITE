import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import UpdateNote

html_content = """<p>Seguimos evoluindo nossas soluções para entregar mais performance, integração e eficiência no dia a dia dos nossos clientes.&nbsp;</p>
<div><br /></div>
<div>&nbsp;💻 <strong>Sistemas atualizados:</strong><br><br>
<b>STA (Sistema de Triagem e Atendimento):</b> melhorias no painel, organização da triagem, otimização de guichês e novos relatórios gerenciais.</div>
<div><br /></div>
<div><b>SGEO (Georreferenciamento):</b> evolução nas funcionalidades de mapeamento, precisão de dados e desempenho nas consultas.</div>
<div><br /></div>
<div><b>SHP (Hotelaria e Pousadas):</b> ajustes operacionais, melhorias na usabilidade e maior controle das reservas e atendimentos.</div>
<div><br /></div>
<div><b>SGESTAO (Gestão Empresarial):</b> avanços na integração entre departamentos, garantindo mais controle, agilidade e tomada de decisão.</div>
<div><br /></div>
<div>🌐 <strong>Sites e performance:</strong><br>
<ul>
<li>Otimizações em velocidade e responsividade</li>
<li>Melhorias em SEO e estrutura para conversão</li>
<li>Ajustes de layout focados em experiência do usuário</li>
</ul>
</div>
<div><br /></div>
<div>🔗 <strong>Integrações e tecnologia:</strong><br>
<ul>
<li>Atualizações nas integrações com WhatsApp, e-mail e APIs</li>
<li>Melhorias na comunicação com bancos de dados (SQL e NoSQL)</li>
<li>Maior estabilidade e segurança nas conexões&nbsp;</li>
</ul>
</div>
<div><br /></div>
<div>&nbsp;⚙️ <strong>Infraestrutura:</strong><br>
<ul>
<li>Aprimoramento em hospedagem e desempenho</li>
<li>Manutenção evolutiva contínua dos sistemas e sites&nbsp;</li>
<li>Monitoramento e correções preventivas</li>
</ul>
</div>
<div><br /></div>
<div>📈&nbsp;<br>Nosso foco é simples: sistemas mais rápidos, inteligentes e preparados para crescer junto com o seu negócio.<br><br>
Acompanhe nossas atualizações e evoluções constantes 🚀</div>"""

# Limpar notas antigas e inserir a nova
UpdateNote.objects.all().delete()

UpdateNote.objects.create(
    version="1.0.0",
    date=date.today(),
    title="🔄 Atualizações — Software & Sites | C2 Sistemas",
    description=html_content
)

print("Nota de atualização criada com sucesso!")
