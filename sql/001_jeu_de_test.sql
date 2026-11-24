DROP TABLE IF EXISTS cours;
DROP TABLE IF EXISTS bilans;
DROP TABLE IF EXISTS societes;
-- les tables

CREATE TABLE societes (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    nom      VARCHAR(100) NOT NULL,
    symbole  VARCHAR(10)  NOT NULL UNIQUE,   
    secteur  VARCHAR(100) NOT NULL,
    pays     VARCHAR(100) NOT NULL
);

CREATE TABLE bilans (
    id                INT AUTO_INCREMENT PRIMARY KEY,
    societe_id        INT NOT NULL,
    annee             INT NOT NULL,
    chiffre_affaires  DECIMAL(15,2) NOT NULL,  
    resultat_net      DECIMAL(15,2) NOT NULL,   
    actifs_courants   DECIMAL(15,2) NOT NULL,
    passifs_courants  DECIMAL(15,2) NOT NULL,
    dettes_totales    DECIMAL(15,2) NOT NULL,
    capitaux_propres  DECIMAL(15,2) NOT NULL,
    total_actifs      DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (societe_id) REFERENCES societes(id),  
    UNIQUE (societe_id, annee)                         
);

CREATE TABLE cours (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    societe_id     INT NOT NULL,
    date_cours     DATE NOT NULL,              
    cours_cloture  DECIMAL(10,2) NOT NULL,
    volume         INT NOT NULL,
    FOREIGN KEY (societe_id) REFERENCES societes(id),
    UNIQUE (societe_id, date_cours)           
);
-- donnée de societés
INSERT INTO societes (nom, symbole, secteur, pays) VALUES
    ('SIMPLON', 'SIMP', 'Formations de ouf',  'France'), 
    ('Tasty Crousty',       'TSC', 'Riz et Poulet',  'France'),
    ('Sante Plus',     'SPL', 'Sante',        'Belgique'),
    ('Vertigo Retail', 'VRT', 'Distribution', 'Espagne');
-- societe_id , anne , chfire d'affaires , resultat net , actifs courants, passifs courants, detes , capitaux propres, total actifs
INSERT INTO bilans VALUES
    (NULL, 1, 2023, 500, 40, 120,   80, 250, 150, 400),
    (NULL, 1, 2024, 520, 45, 130, 85, 250, 170, 420),
    (NULL, 1, 2025, 540, 50, 140, 90, 260, 190, 450),

    (NULL, 2, 2023, 300, 30, 100, 50, 100, 200, 300),
    (NULL, 2, 2024, 350, 40, 120, 55, 110, 240, 350),
    (NULL, 2, 2025, 420, 55, 150, 60, 120, 300, 420),

    (NULL, 3, 2023, 200,  10, 60, 40, 120,  80, 200),
    (NULL, 3, 2024, 210, -15, 50, 55, 140,  60, 200),   
    (NULL, 3, 2025, 230,   8, 65, 50, 130,  90, 220),

    (NULL, 4, 2023, 800, 20, 200, 180, 400, 100, 500),
    (NULL, 4, 2024, 820, 25, 210, 185, 400, 125, 525),
    (NULL, 4, 2025, 860, 30, 220, 190, 410, 140, 550);

INSERT INTO cours (societe_id, date_cours, cours_cloture, volume) VALUES
    (1, '2026-01-05', 25.00, 1000), (1, '2026-01-06', 25.40, 1200),
    (1, '2026-01-07', 24.90,  900), (1, '2026-01-08', 25.10, 1100),
    (1, '2026-01-09', 25.60, 1500), (1, '2026-01-12', 25.30,  800),
    (1, '2026-01-13', 25.80, 1300), (1, '2026-01-14', 26.00, 1400),
    (1, '2026-01-15', 25.70, 1000), (1, '2026-01-16', 26.20, 1600),

    (2, '2026-01-05', 110.00, 500), (2, '2026-01-06', 111.50, 650),
    (2, '2026-01-07', 109.80, 700), (2, '2026-01-08', 112.00, 600),
    (2, '2026-01-09', 113.20, 550), (2, '2026-01-12', 112.40, 480),
    (2, '2026-01-13', 114.00, 720), (2, '2026-01-14', 115.30, 680),
    (2, '2026-01-15', 114.10, 520), (2, '2026-01-16', 116.00, 800),

    (3, '2026-01-05', 38.00, 300), (3, '2026-01-06', 37.60, 350),
    (3, '2026-01-07', 37.20, 400), (3, '2026-01-08', 37.90, 320),
    (3, '2026-01-09', 38.50, 380), (3, '2026-01-12', 38.10, 310),
    (3, '2026-01-13', 37.80, 360), (3, '2026-01-14', 38.40, 330),
    (3, '2026-01-15', 38.90, 420), (3, '2026-01-16', 39.10, 390),

    (4, '2026-01-05', 9.80, 3000), (4, '2026-01-06', 9.90, 2800),
    (4, '2026-01-07', 9.70, 3200), (4, '2026-01-08', 9.60, 3000),
    (4, '2026-01-09', 9.85, 2700), (4, '2026-01-12', 10.00, 2900),
    (4, '2026-01-13', 10.10, 3400), (4, '2026-01-14', 10.05, 2600),
    (4, '2026-01-15', 9.95, 2800), (4, '2026-01-16', 10.20, 3500);

