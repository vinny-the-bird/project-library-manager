Welcome to "Library Manager App Online" project

This project aim to test our skills in project organization, problem study and solution plannification.

Author: Vincent Vogel
School: IBM Academy 2024


## Setup:

rename ".env-sample" file as ".env" and input your own variables.


## Basic SQL samples


CREATE DATABASE library_manager_app_online;

USE library_manager_app_online;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INT
);

INSERT INTO books (title, author, publication_year)
VALUES
    ('Dune', 'Frank Herbert', 1965),
    ('Neuromancien', 'William Gibson', 1984),
    ('Fondation', 'Isaac Asimov', 1951),
    ('La Main gauche de la nuit', 'Ursula K. Le Guin', 1969),
    ('Fahrenheit 451', 'Ray Bradbury', 1953),
    ('Le Meilleur des mondes', 'Aldous Huxley', 1932),
    ('1984', 'George Orwell', 1949),
    ('Chroniques martiennes', 'Ray Bradbury', 1950),
    ('Les androïdes rêvent-ils de moutons électriques ?', 'Philip K. Dick', 1968),
    ('La Guerre des mondes', 'H.G. Wells', 1898),
    ('La Machine à explorer le temps', 'H.G. Wells', 1895),
    ('Hypérion', 'Dan Simmons', 1989),
    ('En terre étrangère', 'Robert A. Heinlein', 1961),
    ('Les Étoiles, destination', 'Alfred Bester', 1956),
    ('Un cantique pour Leibowitz', 'Walter M. Miller Jr.', 1960),
    ('La Fin de l’enfance', 'Arthur C. Clarke', 1953),
    ('Rendez-vous avec Rama', 'Arthur C. Clarke', 1973),
    ('Abattoir 5', 'Kurt Vonnegut', 1969),
    ('Histoire du futur : Révolte sur la Lune', 'Robert A. Heinlein', 1966),
    ('Le Samouraï virtuel', 'Neal Stephenson', 1992);

