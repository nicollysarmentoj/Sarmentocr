# Sarmentocr
Biblioteca em OCR para extrair dados provenientes de exames oftalmológicos (Tomógrafos e Pentacam).

## Instalação

```bash
pip install sarmentocr
```

## Uso

```python
from sarmentocr import extract_ocr_data

dados = extract_ocr_data("exame.jpg")
for linha in dados:
    print(linha)
```
