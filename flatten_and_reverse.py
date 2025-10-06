# flatten_and_reverse.py
# Patika.dev - Python Temel / Proje
# 1) Düzleştirme (flatten) fonksiyonu
# 2) Listedeki elemanları (ve iç içe listeleri) tersine çeviren fonksiyon

from typing import Any, List, Union

def flatten(items: Union[List[Any], Any]) -> List[Any]:
    """
    Verilen iç içe geçmiş listeleri (veya demetleri) düzleştirir.
    String'leri karakterlerine ayırmaz, tek eleman olarak tutar.
    Örnek:
        flatten([[1,'a',['cat'],2],[[3]],'dog',4,5])
        -> [1,'a','cat',2,3,'dog',4,5]
    """
    result: List[Any] = []

    def _walk(x: Any) -> None:
        if isinstance(x, (list, tuple)):
            for y in x:
                _walk(y)
        else:
            result.append(x)

    _walk(items)
    return result


def reverse_deep(items: Any) -> Any:
    """
    Verilen listeyi tersine çevirir; eğer alt elemanlar da listeyse onları da (derinlemesine) tersine çevirir.
    Örnek:
        reverse_deep([[1,2],[3,4],[5,6,7]])
        -> [[7,6,5],[4,3],[2,1]]
    """
    if isinstance(items, list):
        return [reverse_deep(x) for x in reversed(items)]
    else:
        return items


if __name__ == "__main__":
    # ---- 1) Flatten testi
    input1 = [[1,'a',['cat'],2],[[3]],'dog',4,5]
    output1 = flatten(input1)
    print("Flatten input :", input1)
    print("Flatten output:", output1)   # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

    # ---- 2) Deep reverse testi
    input2 = [[1,2], [3,4], [5,6,7]]
    output2 = reverse_deep(input2)
    print("\nReverse input :", input2)
    print("Reverse output:", output2)   # [[7, 6, 5], [4, 3], [2, 1]]

    # Basit doğrulama testleri
    assert output1 == [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
    assert output2 == [[7, 6, 5], [4, 3], [2, 1]]
    print("\nTüm testler geçti ✅")
