# 🧰 Python – Module `os`

Le module `os` permet d’interagir avec le système d’exploitation, en particulier le système de fichiers.

---

## 🔹 Accès aux fichiers et répertoires

| Fonction                   | Description                                   |
|----------------------------|-----------------------------------------------|
| `os.listdir(path)`         | Liste les fichiers/dossiers d’un répertoire  |
| `os.walk(path)`            | Parcourt récursivement les fichiers           |
| `os.path.join(a, b, ...)`  | Concatène proprement des chemins              |
| `os.getcwd()`              | Renvoie le répertoire courant                 |
| `os.chdir(path)`           | Change le répertoire courant                  |

---

## 🔹 Vérifications

| Fonction                   | Description                        |
|----------------------------|------------------------------------|
| `os.path.exists(path)`     | Vérifie si un chemin existe        |
| `os.path.isfile(path)`     | Vérifie si c’est un fichier        |
| `os.path.isdir(path)`      | Vérifie si c’est un dossier        |

---

## 🔹 Infos sur fichiers

| Fonction                         | Description                        |
|----------------------------------|------------------------------------|
| `os.path.getsize(path)`          | Taille du fichier (en octets)      |
| `os.path.getmtime(path)`         | Timestamp de dernière modification |
| `os.remove(path)`                | Supprime un fichier                |
| `os.rmdir(path)`                 | Supprime un dossier vide           |

---

## 🧠 Exemple pratique

```python
import os
import time

for root, dirs, files in os.walk("."):
    for f in files:
        path = os.path.join(root, f)
        if os.path.getsize(path) > 1000:
            print(f"{path} ({os.path.getsize(path)} octets)")
```
