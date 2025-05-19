# ⏱️ Python – Module `time`

Le module `time` permet de manipuler le temps à bas niveau (timestamps, pauses, conversions).

---

## 🔹 Fonctions principales

| Fonction             | Description                                       |
|----------------------|---------------------------------------------------|
| `time.time()`        | Timestamp actuel (secondes depuis 1970)           |
| `time.sleep(x)`      | Pause le programme pendant `x` secondes           |
| `time.ctime(ts)`     | Convertit un timestamp en chaîne lisible          |
| `time.localtime(ts)` | Convertit en structure `time.struct_time`         |
| `time.strftime(fmt)` | Formate un temps selon un modèle                  |

---

## 🧠 Exemple : pause et formatage

```python
import time

print("Début")
time.sleep(2)
print("Fin après 2 secondes")

maintenant = time.time()
print("Timestamp :", maintenant)
print("Lisible :", time.ctime(maintenant))
```

---

## 🔧 Formatage (strftime)

| Format | Signification    | Exemple     |
|--------|------------------|-------------|
| `%Y`   | Année            | `2024`      |
| `%m`   | Mois (01-12)     | `05`        |
| `%d`   | Jour (01-31)     | `19`        |
| `%H`   | Heure (00-23)    | `16`        |
| `%M`   | Minute           | `45`        |
| `%S`   | Seconde          | `08`        |

```python
from datetime import datetime

print(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
```
