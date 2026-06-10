import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import DynamicPage

html_content = """<div style="max-width:920px;margin:0 auto;">
  <p style="color:#556070;line-height:1.65;margin:0 0 1.2rem;">
    Teve uma ideia, encontrou algum problema ou quer sugerir melhoria? Preencha o formulário abaixo.
  </p>

  <div style="background:#fff;border:1px solid #eee;border-radius:14px;padding:18px;box-shadow:0 10px 25px rgba(0,0,0,0.06);">
    <iframe
      src="https://docs.google.com/forms/d/e/1FAIpQLSd4g42SeAyyuWq-s4jX0OKKmsZOC7T-jsw_NNCyjPTBYaL9ww/viewform?embedded=true"
      width="100%"
      height="980"
      frameborder="0"
      marginheight="0"
      marginwidth="0"
      style="border:0;border-radius:12px;background:#fff;">
      Carregando…
    </iframe>

    <div style="margin-top:14px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSd4g42SeAyyuWq-s4jX0OKKmsZOC7T-jsw_NNCyjPTBYaL9ww/viewform?usp=header"
         target="_blank" rel="noopener"
         style="background:linear-gradient(90deg,#0056b3,#00d4ff);color:#fff;text-decoration:none;
                padding:12px 16px;border-radius:10px;font-weight:800;display:inline-block;">
        Abrir formulário em nova aba
      </a>

      <span style="color:#64748b;font-size:.95rem;">
        Se o formulário não aparecer aqui, use o botão ao lado.
      </span>
    </div>
  </div>
</div>"""

page, created = DynamicPage.objects.update_or_create(
    slug='sugestoes',
    defaults={
        'title': 'Sugestões & Melhorias',
        'icon': 'fas fa-lightbulb',
        'content': html_content,
        'is_active': True
    }
)

if created:
    print("Página de Sugestões criada com sucesso!")
else:
    print("Página de Sugestões atualizada com sucesso!")
