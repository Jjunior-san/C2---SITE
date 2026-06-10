import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import VideoTutorial

# Clear existing to prevent duplicates if run multiple times
VideoTutorial.objects.all().delete()

videos = [
    {
        "title": "01 — C² Apresentação de Módulos",
        "short_title": "Apresentação",
        "icon": "🎬",
        "slug": "video01",
        "description": "<p>Visão geral do sistema e onde encontrar cada funcionalidade. Ideal para começar.</p>",
        "caption": "Tutorial — 01 (Apresentação). Mostra os módulos principais (Agendamento, Cidadãos, Triagem, Atendimento e Monitor), e como acessar os tutoriais para resolver dúvidas rapidamente."
    },
    {
        "title": "02 — Agendamento",
        "short_title": "Agendamento",
        "icon": "📅",
        "slug": "agendamento",
        "description": "<p>Como criar, consultar e organizar agendamentos, evitando filas e melhorando o fluxo de atendimento.</p><ul><li>Criar um novo agendamento</li><li>Pesquisar e confirmar horários</li><li>Reagendar/cancelar quando necessário</li></ul>",
        "caption": "Tutorial — 02 (Agendamento). Explica o fluxo completo de criação e gestão de agendamentos no C²."
    },
    {
        "title": "03 — Cidadãos",
        "short_title": "Cidadãos",
        "icon": "👤",
        "slug": "cidadaos",
        "description": "<p>Cadastro e gerenciamento de cidadãos/clientes, com busca rápida e organização do histórico.</p><ul><li>Cadastrar e editar dados</li><li>Pesquisar por nome/telefone/documento</li><li>Evitar duplicidades e manter cadastro limpo</li></ul>",
        "caption": "Tutorial — 03 (Cidadãos). Mostra como cadastrar, buscar e manter os dados organizados."
    },
    {
        "title": "04 — Triagem",
        "short_title": "Triagem",
        "icon": "🧾",
        "slug": "triagem",
        "description": "<p>Triagem e direcionamento do atendimento: emissão/organização de senhas, prioridades e encaminhamento correto.</p><ul><li>Gerar/emitir senha por serviço</li><li>Prioridades e organização da fila</li><li>Encaminhar para o setor/guichê</li></ul>",
        "caption": "Tutorial — 04 (Triagem). Explica como organizar a fila, emitir senhas e encaminhar o cidadão corretamente."
    },
    {
        "title": "05 — Atendimento",
        "short_title": "Atendimento",
        "icon": "🧑‍💼",
        "slug": "atendimento",
        "description": "<p>Fluxo do atendente: iniciar atendimento, registrar informações e finalizar com segurança.</p><ul><li>Chamar próxima senha</li><li>Registrar observações e status</li><li>Finalizar/encerrar atendimento</li></ul>",
        "caption": "Tutorial — 05 (Atendimento). Mostra como conduzir o atendimento do início ao fim no C²."
    },
    {
        "title": "Monitor (Painel)",
        "short_title": "Monitor",
        "icon": "🖥️",
        "slug": "monitor",
        "description": "<p>O módulo Monitor exibe as chamadas de senha e informações em telas/TVs para o público.</p>",
        "caption": "Em breve: Adicione o vídeo aqui pelo painel."
    }
]

for v in videos:
    VideoTutorial.objects.create(**v)

print("Vídeos inseridos no banco de dados com sucesso!")
