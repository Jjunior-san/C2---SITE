import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """<p>🔄 <strong>Atualizações — C2 Sistemas | SHP (Hotelaria e Pousadas): </strong>Ajustes operacionais, melhorias na usabilidade, maior controle das reservas e atendimentos.</p>

<ul style="text-align: left;">
  <li style="list-style: none;">
    <span onclick="toggleChangelog(this, 'shp-patch')" style="cursor:pointer; display:inline-block; font-weight:bold; color:#0056b3;">
      ▶ Patch Notes
    </span>

    <div id="shp-patch" style="display:none; margin-top:10px; padding:12px 16px; background:#f4f7fa; border-left:4px solid #0056b3; border-radius:8px;">
      <ul style="margin:0; padding-left:18px; text-align:left;">
        <li>Ajustes operacionais</li>
        <li>Melhorias na usabilidade</li>
        <li>Maior controle das reservas</li>
        <li>Melhor organização dos atendimentos</li>
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
    slug='updates-shp',
    defaults={
        'title': 'Updates - SHP (Hotelaria e Pousada)',
        'icon': 'fas fa-hotel',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Updates SHP criada com sucesso!")
else:
    print("Página de Updates SHP atualizada com sucesso!")
