# 🌱 Git & GitHub – Récapitulatif de base

Git est un système de gestion de versions distribué. GitHub permet d’héberger des dépôts Git à distance.

---

## 🔧 Initialisation d’un dépôt

```bash
git init                     # Initialise un dépôt Git local
git clone <url>             # Clone un dépôt distant
```

---

## 👤 Configuration utilisateur (à faire une fois)

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
```

---

## 📁 Étapes de base (workflow)

```bash
git status                  # Voir l’état du dépôt
git add <fichier>           # Ajouter un fichier au suivi
git commit -m "Message"     # Sauvegarder l’état (commit)
```

Ajout rapide de tout :

```bash
git add .
git commit -m "Initial commit"
```

---

## 🔀 Connexion à GitHub

```bash
git remote add origin git@github.com:utilisateur/repo.git
git push -u origin main       # Push initial (avec tracking)
git push                      # Push suivant
git pull                      # Récupérer les changements distants
```

---

## 🧪 Autres commandes utiles

```bash
git log                     # Historique des commits
git diff                    # Voir les différences non committées
git branch                  # Voir les branches
git checkout -b feature-x  # Créer et basculer sur une nouvelle branche
```

---

## 💡 Conseils

- Faire des **commits fréquents**
- Utiliser des **messages clairs**
- Travailler avec des **branches** pour tester ou ajouter des fonctionnalités
- Pousser régulièrement sur GitHub (`git push`)

---

## 🔒 Astuce : tester sa connexion SSH à GitHub

```bash
ssh -T git@github.com
```
