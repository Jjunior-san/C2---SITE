import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """<p>&nbsp;🔄 <strong>Atualizações — C² - Sistemas | SIG: </strong>Avanços na integração entre departamentos, garantindo mais controle, agilidade e tomadas de decisões.</p>

<ul style="text-align: left;">
  <li style="list-style: none;">
    <span onclick="toggleChangelog(this, 'sgestao-patch')" style="cursor:pointer; display:inline-block; font-weight:bold; color:#0056b3;">
      ▶ Patch Notes
    </span>

    <div id="sgestao-patch" style="display:none; margin-top:10px; padding:12px 16px; background:#f4f7fa; border-left:4px solid #0056b3; border-radius:8px;">
      <ul style="margin:0; padding-left:18px; text-align:left;">
        <li>Avanços na integração entre departamentos</li>
        <li>Mais controle operacional</li>
        <li>Mais agilidade nos processos</li>
        <li>Melhor apoio à tomada de decisões</li>
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
    slug='updates-sig',
    defaults={
        'title': 'Updates - SIG (Sistema de Integração de Gestão)',
        'icon': 'fas fa-project-diagram',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Updates SIG criada com sucesso!")
else:
    print("Página de Updates SIG atualizada com sucesso!")
