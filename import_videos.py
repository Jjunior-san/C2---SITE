import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c2_sistemas.settings')
django.setup()

from website.models import VideoTutorial

source_dir = r"D:\C2 - Projetos\Site c2\Takeout\Blogger\Blogs\C² - Sistemas"

mapping = {
    "video01": "01 - C² Apresentação de Modulos.mp4",
    "agendamento": "02 - C² Agendamento.mp4",
    "cidadaos": "03 - C²  Cidadãos.mp4",
    "triagem": "04 - C² Triagem.mp4",
    "atendimento": "05 - C² Atendimento.mp4"
}

for slug, filename in mapping.items():
    filepath = os.path.join(source_dir, filename)
    if os.path.exists(filepath):
        try:
            video = VideoTutorial.objects.get(slug=slug)
            with open(filepath, 'rb') as f:
                video.video_file.save(filename, File(f), save=True)
            print(f"Vídeo {filename} anexado com sucesso!")
        except VideoTutorial.DoesNotExist:
            print(f"Página com slug '{slug}' não encontrada.")
    else:
        print(f"Arquivo não encontrado: {filepath}")
