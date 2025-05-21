# SarmentOCR

OCR de alta precisão para exames médicos oftalmológicos (como Pentacam), com pré-processamento customizado e detecção robusta sem uso do EasyOCR.

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
