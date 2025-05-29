-- 1. Crear el keyspace
CREATE KEYSPACE facturacion WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- 2. Usar el keyspace
USE facturacion;

-- 3. Crear tabla de Clientes
CREATE TABLE clientes (
    id_cliente UUID PRIMARY KEY,
    nombre TEXT,
    correo TEXT
);

-- 4. Crear tabla de Productos
CREATE TABLE productos (
    id_producto UUID PRIMARY KEY,
    nombre TEXT,
    precio DECIMAL
);

-- 5. Crear tabla de Facturas
CREATE TABLE facturas (
    id_factura UUID PRIMARY KEY,
    id_cliente UUID,
    fecha TIMESTAMP,
    total DECIMAL
);

-- 6. Crear tabla de Detalle de Factura (sin normalizar joins)
CREATE TABLE detalle_factura (
    id_factura UUID,
    id_producto UUID,
    cantidad INT,
    subtotal DECIMAL,
    PRIMARY KEY (id_factura, id_producto)
);

-- 7. Insertar datos de ejemplo

-- Clientes
INSERT INTO clientes (id_cliente, nombre, correo) VALUES (uuid(), 'Juan Pérez', 'juan@mail.com');
INSERT INTO clientes (id_cliente, nombre, correo) VALUES (uuid(), 'Ana Torres', 'ana@mail.com');

-- Productos
INSERT INTO productos (id_producto, nombre, precio) VALUES (uuid(), 'Laptop', 1200.00);
INSERT INTO productos (id_producto, nombre, precio) VALUES (uuid(), 'Mouse', 25.50);

-- Factura (usamos un ID fijo para facilitar el ejemplo)
INSERT INTO facturas (id_factura, id_cliente, fecha, total)
VALUES (uuid(), '79042753-6f94-4260-9b79-7bb0cb90c9b0', toTimestamp(now()), 1250.50);

-- Detalle de Factura
INSERT INTO detalle_factura (id_factura, id_producto, cantidad, subtotal)
VALUES (db307113-6157-43a7-9f39-1fbf5faf8d5f, ea175841-a303-4b70-9501-1b8a4177ba41, 1, 1200.00);

INSERT INTO detalle_factura (id_factura, id_producto, cantidad, subtotal)
VALUES (db307113-6157-43a7-9f39-1fbf5faf8d5f, 7bd32b7d-1657-4900-bf89-527c6335866c, 2, 50.50);

-- 8. Consultas básicas

-- Mostrar todos los clientes
SELECT * FROM clientes;

-- Mostrar todas las facturas
SELECT * FROM facturas;

-- Ver detalle de una factura específica
SELECT * FROM detalle_factura WHERE id_factura = db307113-6157-43a7-9f39-1fbf5faf8d5f;

-- Ver productos registrados
SELECT * FROM productos;
