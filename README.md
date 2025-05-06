# YouTube Downloader (MP3/MP4)

Este é um projeto em Python que permite baixar vídeos do YouTube a partir de uma URL fornecida pelo usuário. Você pode escolher entre baixar apenas o áudio (formato `.mp3`) ou o vídeo completo (formato `.mp4`).

## 📦 Funcionalidades

- 🔗 Baixe qualquer vídeo público do YouTube com uma URL
- 🎵 Escolha entre baixar apenas o áudio (mp3) ou o vídeo completo (mp4)
- 📁 Os arquivos são salvos em pastas separadas: `./audios` e `./videos`

## 🧰 Tecnologias usadas

- Python 3.8+
- [pytubefix](https://pypi.org/project/pytubefix/)

## ⚙️ Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```
   pip install pytubefix
   ```

## 🚀 Como usar

Execute o script principal:


```python main.py```


1. Cole a URL do vídeo do YouTube.
2. Confirme o título exibido.
3. Escolha o formato de saída: `mp3` ou `mp4`.
4. O vídeo ou áudio será baixado na pasta correspondente.

## 🗂 Estrutura de diretórios

```
.
├── main.py
├── audios/
└── videos/
```

## ❗ Aviso legal

Este projeto é apenas para fins educacionais. Baixar conteúdo protegido por direitos autorais pode violar os Termos de Serviço do YouTube. Use por sua conta e risco.

```
