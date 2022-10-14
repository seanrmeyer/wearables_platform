-- Database: wearables

DROP DATABASE IF EXISTS wearables;

CREATE DATABASE wearables
    WITH
    OWNER = wearables_admin
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE studies (
    study_id INTEGER NOT NULL,
    study_title VARCHAR(255) NOT NULL,
    study_url VARCHAR(255) NOT NULL,
    study_abstract TEXT,
    year_published INTEGER,
    date_added timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    subject_count INTEGER,
    enabled boolean DEFAULT TRUE,
    PRIMARY KEY (study_id)
);

INSERT INTO studies(id, study_title, study_url, year_published)
VALUES (1, 'Pre-symptomatic detection of COVID-19 from smartwatch data', 'https://www.nature.com/articles/s41551-020-00640-6', 2020);

CREATE TABLE subjects (
    study_id INTEGER NOT NULL,
    subject_id VARCHAR(100) NOT NULL,
    PRIMARY KEY (subject_id),
    FOREIGN KEY (study_id) REFERENCES studies(study_id) ON DELETE CASCADE,
);

-- STEPS

CREATE TABLE steps (
    id serial,
    subject_id VARCHAR(100) NOT NULL,
    study_id INTEGER NOT NULL,
    start_time timestamp,
    end_time timestamp,
	steps REAL,
    time_index INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (study_id) REFERENCES studies(study_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
);

COPY steps (subject_id, start_time, steps, study_id) FROM '<STORAGE_DIR>/covid_data/study1_steps.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8'

-- HEART RATE

CREATE TABLE heart_rate (
    id serial,
    subject_id VARCHAR(100) NOT NULL,
    study_id INTEGER NOT NULL,
    start_time timestamp,
    end_time timestamp,
	heart_rate REAL,
    time_index INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (study_id) REFERENCES studies(study_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
);

COPY public.heart_rate (subject_id, start_time, heart_rate, study_id) FROM '<STORAGE_DIR>/covid_data/study1_hr.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8'