<a name="readme-top"></a>
<div align="center">
  <h3 align="center">Ecosystème</h3>

  <p align="center">
    Voici tout ce que vous devez savoir sur le projet de l'Ecosystème.
    <br/>
  </p>
</div>

<details>
  <summary>Tables des matières</summary>
  <ol>
    <li>
      <a href="#a-propos-du-projet">A propos du projet</a>
    </li>
    <li><a href="#règles">Règles</a></li>
    <li><a href="#Comment marche le jeu ?">Comment marche le jeu ?</a></li>
    <li><a href="#Choix">Choix</a></li>
    <li><a href="#Conclusion">Conclusion</a></li>
  </ol>
</details>

## A propos du projet

Vous avez la un projet d'Ecosysteme. Ce programme, à pour but de simuler une prairie découper en caréer d'herbe. Ou se deplace des moutons, qui broute et de déplace librement dans la prairie. Quand il rencontre un amis mouton, un petit mouton apprait pour vivre une vie. Mais les loups eux aussi sont de la partie, ils se deplace à fin de trouver de quoi se nourir, les moutons on qua bien se tenir. 

Le but de ce devoirs était de s'experimenter sur la programmatioon en Python avec des Classes et differentes entites (moutons et loups). Mais aussi d'integrer plusieur petites fonctionnalité, tel que la croissance de l'herbe ou la gestion de la nourriture des animaux. 

## Comment marche le jeu ? 

Vous allez pouvoir lancer le code et changer les paramètres suivants de la simulation, si vous le voulez sinon la simulation se lance à avec des paramètres choisis à l'avance :

 * Durée de repouse de l'herbe 
 * Hauteur maximale de l'herbe
 * Taille de la prairie (LxL)
 * Le nombre de moutons
 * Le nombre de loups
 * Et leurs stats

Après avoir remplie vos paramètre custom, la prairie va être générée avec l'herbe et les moutons et les loups. Chaque tour la prairie va être mise à jour, l'herbe pousse d'un le mouton pourront se déplacer librement dans la prairie pour brouter l'herbe 
si elle est assez grande, se reproduire si deux moutons sont sur la même case. Et les loups pourront chasser les moutons a faim de manger de se reproduire. S'il ne mange pas assez ils peuvent mourir de faim.

Tout se deroule dans l'interpreteur, dans la console. 

## Affichage

Légende :
Vous pouvez remarquer que la prairie est constitué de carrer d'herbe avec un nombre et une couleur, elle indique la taille de l'herbe et si elle consumable par les moutons.
Les moutons sont représenté par des "M" et les loups par des "L".
Vous pouvez voir l'état de la population de mouton et de loup de la prairie.

![img.png](img.png)

## Choix

J'ai choisi de découper le projet en plusieurs classes, pour une meilleur lisibilité du code. J'ai donc crée une classe Prairie, qui contient les moutons et les loups. J'ai aussi crée une classe Animal, qui contient les moutons et les loups. J'ai aussi crée une classe Herbe, qui contient les moutons et les loups.
Chaque classe à ses propres méthodes et attributs, pour une meilleur gestion des entités. Le code est donc plus lisible et plus facile à comprendre. 
Les programmes sont divisés en plusieurs fichiers, pour une meilleur gestion des classes et des fonctions, que j'ai rangé dans des folders pour une meilleur organisation.

## Fonctionnalité

Le programme gére la croissance de l'herbe, la reproduction des moutons et des loups, la chasse des loups, la mort des loups et des moutons, la faim des loups, la gestion de la nourriture des moutons et des loups, la gestion de la prairie, la gestion des déplacements des moutons et des loups, la gestion de la population des moutons et des loups, la gestion de la taille de la prairie, la gestion des paramètres de la simulation, la gestion de l'affichage de la prairie, la gestion de l'affichage des moutons et des loups, la gestion de l'affichage des statistiques de la simulation, la gestion de l'affichage des légendes de la simulation, la gestion de l'affichage des messages de la simulation, la gestion de l'affichage des erreurs de la simulation, la gestion de l'affichage des logs de la simulation, la gestion de l'affichage des warnings de la simulation, la gestion de l'affichage des informations de la simulation, la gestion de l'affichage des paramètres de la simulation, la gestion de l'affichage des options de la simulation, la gestion de l'affichage des choix de la simulation, la gestion de l'affichage des actions
Chaque tour commence, l'herbe pousse, les moutons et les loups se déplacent, les moutons et les loups se reproduisent, les loups chassent les moutons, les loups meurent de faim, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons et les loups meurent, les moutons et les loups se reproduisent, les moutons et les loups se déplacent, les moutons et les loups mangent, les moutons

L'ensemble des programmes est codé en Python 3.9.6. J'ai utilisé les bibliothéque suivante : random, time, os, sys. 

## Conclusion

Ce projet m'a permis de m'experimenter sur la programmation en Python avec des Classes et differentes entites (moutons et loups). Mais aussi d'integrer plusieur petites fonctionnalité, tel que la croissance de l'herbe ou la gestion de la nourriture des animaux. J'ai pu améliorer mes compétences en programmation et en algorithmique. J'ai pu apprendre à gérer des entités, des classes, des fonctions, des méthodes, des attributs, des paramètres, des arguments, des boucles, des conditions, des exceptions, des erreurs, des logs, des warnings, des informations, des options, des choix, des actions, des messages, des légendes, des statistiques, des paramètres, des options, des choix, des actions, des déplacements, des reproductions, des chasses, des morts, des faims, des nourritures, des prairies, des moutons, des loups, des herbes

