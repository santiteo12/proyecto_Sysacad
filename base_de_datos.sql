CREATE TABLE TipoDocumento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Alumno (
    id SERIAL PRIMARY KEY,
    apellido VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    id_tipo_documento INT NOT NULL,
    nro_documento VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    CONSTRAINT fk_tipo_documento FOREIGN KEY (id_tipo_documento)
        REFERENCES TipoDocumento (id)
);

CREATE TABLE Grado (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Departamento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Universidad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Autoridad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cargo VARCHAR(100)
);

CREATE TABLE TipoEspecialidad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel INT NOT NULL
);

CREATE TABLE Especialidad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_tipo_especialidad INT NOT NULL,
    CONSTRAINT fk_tipo_especialidad FOREIGN KEY (id_tipo_especialidad)
        REFERENCES TipoEspecialidad (id)
);

CREATE TABLE Area (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Grupo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_area INT NOT NULL,
    CONSTRAINT fk_area FOREIGN KEY (id_area)
        REFERENCES Area (id)
);

CREATE TABLE Facultad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_universidad INT NOT NULL,
    id_departamento INT,
    id_grupo INT,
    CONSTRAINT fk_universidad FOREIGN KEY (id_universidad)
        REFERENCES Universidad (id),
    CONSTRAINT fk_departamento FOREIGN KEY (id_departamento)
        REFERENCES Departamento (id),
    CONSTRAINT fk_grupo FOREIGN KEY (id_grupo)
        REFERENCES Grupo (id)
);

CREATE TABLE Plan (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_facultad INT NOT NULL,
    id_especialidad INT,
    observaciones TEXT,
    CONSTRAINT fk_facultad FOREIGN KEY (id_facultad)
        REFERENCES Facultad (id),
    CONSTRAINT fk_especialidad FOREIGN KEY (id_especialidad)
        REFERENCES Especialidad (id)
);

CREATE TABLE Materia (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_plan INT NOT NULL,
    observaciones TEXT,
    CONSTRAINT fk_plan FOREIGN KEY (id_plan)
        REFERENCES Plan (id)
);

CREATE TABLE Orientacion (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_facultad INT NOT NULL,
    CONSTRAINT fk_facultad_orientacion FOREIGN KEY (id_facultad)
        REFERENCES Facultad (id)
);

CREATE TABLE CategoriaCargo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE TipoDedicacion (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    observaciones TEXT
);

CREATE TABLE Cargo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puntos INT NOT NULL,
    id_categoria INT NOT NULL,
    id_tipo_dedicacion INT NOT NULL,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria)
        REFERENCES CategoriaCargo (id),
    CONSTRAINT fk_tipo_dedicacion FOREIGN KEY (id_tipo_dedicacion)
        REFERENCES TipoDedicacion (id)
);
