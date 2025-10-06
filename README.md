# Patika.dev — Python Temel / Proje Çözümü

Bu proje, **Patika.dev Python Temel** dersi kapsamında verilen iki fonksiyonu içerir:

---

## 🧩 1. `flatten()` Fonksiyonu  
İç içe geçmiş (nested) listeleri düzleştirir.  
Yani, bir listenin içindeki alt listeleri açarak tek katmanlı hale getirir.

**Örnek:**
```python
flatten([[1, 'a', ['cat'], 2], [[3]], 'dog', 4, 5])
# Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
