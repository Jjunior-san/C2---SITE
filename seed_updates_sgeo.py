import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """<p class="isSelectedEnd">🔄 <strong>Atualizações — C2 Sistemas | SGEO (Georreferenciamento): </strong>Evolução nas funcionalidades de mapeamento, precisão de dados e desempenho nas consultas.</p>

<ul data-spread="false" style="text-align: left;">
  <li style="list-style: none;">
    <span onclick="toggleChangelog(this, 'sgeo-102')" style="cursor:pointer; display:inline-block; font-weight:bold; color:#0056b3;">
      ▶ Patch Notes 01/03/2026 - Versão 1.0.2
    </span>

    <div id="sgeo-102" style="display:none; margin-top:10px; padding:12px 16px; background:#f4f7fa; border-left:4px solid #0056b3; border-radius:8px;">
      <ul style="margin:0; padding-left:18px; text-align:left;">
        <li>Evolução nas funcionalidades de mapeamento</li>
        <li>Maior precisão de dados</li>
        <li>Melhoria no desempenho das consultas</li>
      </ul>
    </div>
  </li>
</ul>

<script>
  function toggleChangelog(el, id) {
    var box = document.getElementById(id);
    if (box.style.display === "none" || box.style.display === "") {
      box.style.display = "block";
      el.innerHTML = el.innerHTML.replace("▶", "▼");
    } else {
      box.style.display = "none";
      el.innerHTML = el.innerHTML.replace("▼", "▶");
    }
  }
</script>"""

page, created = DynamicPage.objects.update_or_create(
    slug='updates-sgeo',
    defaults={
        'title': 'Updates - SGEO (Georreferenciamento)',
        'icon': 'fas fa-map-marked-alt',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Updates SGEO criada com sucesso!")
else:
    print("Página de Updates SGEO atualizada com sucesso!")
