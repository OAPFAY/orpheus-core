# Marker-PDF Evaluation & Recommendation

- **Status**: NOT INSTALLED (Resource Protected).
- **Reason**: Marker-pdf requires heavy PyTorch / OCR weights that risk crashing the low-RAM environment (7.74 GB total, ~0.27 GB available) and destabilizing Hermes python venv.
- **Lightweight Alternative**: Use standard PyMuPDF (`fitz`) or python-based text extraction already present in Hermes stdlib ecosystem for fast, zero-overhead PDF reading.
