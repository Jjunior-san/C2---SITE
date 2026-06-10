import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """<p>🔄 <b>Atualizações — C2 Sistemas | STA (Sistema de Triagem e Atendimento): </b>Melhorias no painel, organização da triagem, otimização de guichês e novos relatórios gerenciais.</p>

<ul style="text-align: left; list-style: none; padding-left: 0;">
  <li style="margin-bottom: 10px;">
    <span onclick="toggleChangelogArrow(this, 'sta-2213')" style="cursor: pointer; font-weight: bold; color: #0056b3;">
      ▶ Patch Notes 01/03/2026 - Versão 2.2.13
    </span>
    <div id="sta-2213" style="display: none; margin-top: 10px; padding: 12px 16px; background: #f4f7fa; border-left: 4px solid #0056b3; border-radius: 8px;">
      <p><b>IMPROVED</b></p>
      <ul>
        <li>Melhorias no painel</li>
        <li>Otimização de guichês</li>
        <li>Novo sistema de relatórios</li>
      </ul>
    </div>
  </li>

  <li style="margin-bottom: 10px;">
    <span onclick="toggleChangelogArrow(this, 'sta-2212')" style="cursor: pointer; font-weight: bold; color: #0056b3;">
      ▶ Patch Notes 20/02/2026 - Versão 2.2.12
    </span>
    <div id="sta-2212" style="display: none; margin-top: 10px; padding: 12px 16px; background: #f4f7fa; border-left: 4px solid #0056b3; border-radius: 8px;">
      <p><b>FIXED</b></p>
      <ul>
        <li>Correções de estabilidade</li>
        <li>Ajustes na triagem</li>
      </ul>
    </div>
  </li>
</ul>

<script>
  function toggleChangelogArrow(element, id) {
    var el = document.getElementById(id);
    if (el.style.display === "none" || el.style.display === "") {
      el.style.display = "block";
      element.innerHTML = element.innerHTML.replace("▶", "▼");
    } else {
      el.style.display = "none";
      element.innerHTML = element.innerHTML.replace("▼", "▶");
    }
  }
</script>"""

page, created = DynamicPage.objects.update_or_create(
    slug='updates-sta',
    defaults={
        'title': 'Updates - STA',
        'icon': 'fas fa-sync-alt',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Updates STA criada com sucesso!")
else:
    print("Página de Updates STA atualizada com sucesso!")
