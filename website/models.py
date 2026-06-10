from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField(verbose_name="Conteúdo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"


class UpdateNote(models.Model):
    SYSTEM_CHOICES = [
        ('STA', 'STA'),
        ('SGEO', 'SGEO'),
        ('SHP', 'SHP'),
        ('SGESTAO', 'SGESTAO'),
    ]
    system = models.CharField(max_length=50, choices=SYSTEM_CHOICES, verbose_name="Sistema")
    version = models.CharField(max_length=20, verbose_name="Versão")
    date = models.DateField(verbose_name="Data de Atualização")
    details = models.TextField(verbose_name="Detalhes da Atualização (Use formato de lista)")
    
    def __str__(self):
        return f"{self.system} - {self.version}"

    class Meta:
        verbose_name = "Nota de Atualização"
        verbose_name_plural = "Notas de Atualização"


class VideoTutorial(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título Completo (ex: 01 — Apresentação)")
    short_title = models.CharField(max_length=50, verbose_name="Título Curto (para o botão)", help_text="Ex: Apresentação", default="Novo Vídeo")
    icon = models.CharField(max_length=10, verbose_name="Emoji do Botão", help_text="Ex: 🎬", blank=True)
    slug = models.SlugField(max_length=50, unique=True, help_text="Ex: apresentacao (usado para o link interno)", default="video")
    
    description = HTMLField(verbose_name="Texto Explicativo (Aceita formatação e listas)", blank=True)
    video_file = models.FileField(upload_to='videos/', verbose_name="Arquivo de Vídeo (.mp4)", help_text="Faça o upload do arquivo MP4 direto aqui.")
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name="Capa do Vídeo", blank=True, null=True)
    caption = models.TextField(verbose_name="Texto da Legenda (Abaixo do vídeo)", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vídeo Tutorial"
        verbose_name_plural = "Vídeos Tutoriais"

from tinymce.models import HTMLField

class DynamicPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título da Página")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="A URL da página. Ex: contato-corporativo")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Ícone FontAwesome", help_text="Ex: fas fa-file-alt (opcional)")
    content = HTMLField(verbose_name="Conteúdo da Página")
    is_active = models.BooleanField(default=True, verbose_name="Publicada?")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Página Dinâmica"
        verbose_name_plural = "Páginas Dinâmicas"

class HomePageContent(models.Model):
    # Hero Section
    hero_title_1 = models.CharField(max_length=100, default="Inovação e Tecnologia para o", verbose_name="Título Principal (Parte 1)")
    hero_title_highlight = models.CharField(max_length=100, default="Seu Negócio", verbose_name="Título em Destaque (Azul)")
    hero_subtitle = models.TextField(default="Oferecendo soluções de tecnologia para otimizar processos e garantir a segurança da sua empresa.", verbose_name="Subtítulo Principal")
    hero_btn_text = models.CharField(max_length=50, default="Ver Nossas Soluções", verbose_name="Texto do Botão Principal")
    hero_btn_link = models.CharField(max_length=100, default="#servicos", verbose_name="Link do Botão Principal")
    
    # Services Header
    services_title = models.CharField(max_length=100, default="Nossas Soluções", verbose_name="Título da Seção de Soluções")
    services_subtitle = models.TextField(default="Especialistas em transformar desafios em resultados digitais.", verbose_name="Subtítulo da Seção de Soluções")
    
    # Service Card 1
    service1_icon = models.CharField(max_length=50, default="fas fa-code", verbose_name="Ícone do Cartão 1")
    service1_title = models.CharField(max_length=100, default="Software", verbose_name="Título do Cartão 1")
    service1_desc = models.TextField(default="Sistemas personalizados focados na experiência do Cliente.", verbose_name="Descrição do Cartão 1")
    service1_link = models.CharField(max_length=100, default="/software/", verbose_name="Link do Cartão 1")
    
    # Service Card 2
    service2_icon = models.CharField(max_length=50, default="fas fa-server", verbose_name="Ícone do Cartão 2")
    service2_title = models.CharField(max_length=100, default="Infraestrutura & Cloud", verbose_name="Título do Cartão 2")
    service2_desc = models.TextField(default="Segurança e alta disponibilidade para sua rede e servidores.", verbose_name="Descrição do Cartão 2")
    service2_link = models.CharField(max_length=100, default="/infraestrutura/", verbose_name="Link do Cartão 2")
    
    # Service Card 3
    service3_icon = models.CharField(max_length=50, default="fas fa-bullhorn", verbose_name="Ícone do Cartão 3")
    service3_title = models.CharField(max_length=100, default="Marketing", verbose_name="Título do Cartão 3")
    service3_desc = models.TextField(default="Estratégias digitais e presença online para o seu negócio.", verbose_name="Descrição do Cartão 3")
    service3_link = models.CharField(max_length=100, default="/marketing/", verbose_name="Link do Cartão 3")

    class Meta:
        verbose_name = "Conteúdo da Home"
        verbose_name_plural = "Conteúdo da Home"

    def __str__(self):
        return "Conteúdo da Página Inicial"

