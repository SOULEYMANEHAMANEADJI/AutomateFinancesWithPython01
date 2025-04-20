# Tableau de Bord Financier Simple (V1)

Une application Streamlit interactive pour analyser vos transactions financières à partir d'un fichier CSV, offrant des fonctionnalités de catégorisation automatique et de visualisation des dépenses.

## Fonctionnalités Clés

- **Importation CSV Facile :** Téléchargez rapidement votre historique de transactions au format CSV via une interface utilisateur intuitive.
- **Catégorisation Automatique des Dépenses :** Les transactions identifiées comme "Débit" sont automatiquement classées en catégories basées sur des mots-clés présents dans la colonne "Détails".
- **Gestion Intelligente des Catégories :**
    - **Création Dynamique :** Ajoutez de nouvelles catégories de dépenses directement depuis l'application.
    - **Apprentissage Automatique :** Le système mémorise les mots-clés associés à chaque catégorie lorsque vous modifiez manuellement une transaction, améliorant la précision de la catégorisation future.
- **Tableau Interactif des Dépenses :** Explorez vos dépenses dans un tableau éditable, vous permettant de modifier la catégorie de chaque transaction en temps réel. Les changements sont persistants pour les sessions suivantes.
- **Visualisation Claire des Dépenses :** Obtenez une vue d'ensemble de vos habitudes de dépenses grâce à un tableau récapitulatif et un graphique en secteurs interactif, affichant le total des dépenses par catégorie.
- **Aperçu des Paiements :** Consultez un récapitulatif simple de vos revenus (transactions "Crédit").

## Installation et Configuration Locale

Pour exécuter cette application sur votre machine locale, suivez ces étapes :

1. **Cloner le dépôt GitHub :**
   Récupérez le code source du projet en clonant le dépôt :
   ```bash
   git clone https://github.com/SOULEYMANEHAMANEADJI/AutomateFinancesWithPython01.git
   cd https://github.com/SOULEYMANEHAMANEADJI/AutomateFinancesWithPython01.git
2.  **Créer un environnement virtuel (Fortement Recommandé) :**
    L'utilisation d'un environnement virtuel isole les dépendances du projet.

      - **Sous macOS et Linux :**

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

      - **Sous Windows :**

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

    L'activation réussie affichera `(venv)` au début de votre invite de commande.

3.  **Installer les dépendances :**
    Installez les bibliothèques Python nécessaires à l'exécution de l'application :

    ```bash
    pip install streamlit pandas plotly
    ```

    (Si un fichier `requirements.txt` est inclus dans le dépôt, utilisez `pip install -r requirements.txt`.)

4.  **Exécuter l'application Streamlit :**
    Lancez l'application avec la commande Streamlit :

    ```bash
    streamlit run main.py
    ```
    L'application s'ouvrira automatiquement dans votre navigateur web.

## Utilisation

1.  **Téléchargement du Fichier CSV :** Sur la page d'accueil, utilisez le téléchargeur de fichiers pour sélectionner et importer votre fichier CSV de transactions.
2.  **Exploration des Dépenses :** Naviguez vers l'onglet "Dépenses (Débits)" pour visualiser vos transactions de débit dans un tableau interactif.
3.  **Gestion des Catégories :**
      - **Ajouter une Nouvelle Catégorie :** Entrez le nom de la nouvelle catégorie dans le champ prévu à cet effet et cliquez sur "Ajouter Catégorie".
      - **Modifier une Catégorie Existante :** Utilisez le menu déroulant dans la colonne "Catégorie" du tableau des dépenses pour réassigner une transaction à une autre catégorie. Cliquez sur "Appliquer les Changements" pour sauvegarder vos modifications et permettre au système d'apprendre de nouveaux mots-clés.
4.  **Analyse des Dépenses :** Consultez l'onglet "Résumé des Dépenses" pour voir une agrégation de vos dépenses par catégorie, présentée sous forme de tableau et de graphique en secteurs.
5.  **Aperçu des Paiements :** L'onglet "Paiements (Crédits)" affiche le montant total de vos transactions de crédit.

## Format du Fichier CSV

Assurez-vous que votre fichier CSV respecte le format suivant pour une analyse correcte :

| Colonne       | Description                                          | Format Exemple |
|---------------|------------------------------------------------------|----------------|
| Date          | Date de la transaction                               | JJ MMM AAAA    |
| Détails       | Description détaillée de la transaction              | Achat en ligne  |
| Débit/Crédit  | Type de transaction (dépense ou revenu)              | Débit / Credit |
| Montant       | Montant de la transaction                             | 150.50         |

**Note :** Les virgules dans la colonne "Montant" sont automatiquement gérées.

## Gestion des Catégories

L'application utilise un fichier nommé `categories.json` pour stocker les associations entre les catégories de dépenses et les mots-clés pertinents extraits des descriptions de transactions. Ce fichier est géré automatiquement par l'application au fur et à mesure de votre utilisation et de vos modifications. Vous n'avez pas besoin d'interagir directement avec ce fichier.

## Améliorations Possibles

Ce projet est une version initiale et plusieurs améliorations pourraient être apportées :

  - **Logique de Catégorisation Avancée :** Implémenter des techniques de correspondance de texte plus sophistiquées (par exemple, correspondance partielle, similarité de chaînes, expressions régulières) pour une catégorisation plus précise et flexible.
  - **Filtrage Temporel :** Ajouter la possibilité de filtrer les transactions par différentes périodes (par exemple, mois, année, plage de dates personnalisée).
  - **Analyse Détaillée des Revenus :** Fournir une analyse plus approfondie des transactions de crédit, potentiellement en les catégorisant également.
  - **Persistance des Données Utilisateur :** Explorer des options pour sauvegarder et charger les données catégorisées spécifiques à chaque utilisateur.
  - **Interface Utilisateur/Expérience Utilisateur (UI/UX) :** Améliorer l'aspect visuel et la convivialité de l'application.
  - **Gestion des Erreurs Robuste :** Ajouter une meilleure gestion des erreurs pour les fichiers CSV mal formatés ou les données inattendues.
  - **Fonctionnalités d'Exportation :** Permettre l'exportation des données catégorisées dans différents formats (par exemple, CSV, Excel).

## Contribution

Les contributions à ce projet sont les bienvenues. Si vous avez des idées d'amélioration, des corrections de bugs ou de nouvelles fonctionnalités, n'hésitez pas à ouvrir une issue ou à soumettre une pull request. Veuillez suivre les directives de contribution si elles sont définies.
