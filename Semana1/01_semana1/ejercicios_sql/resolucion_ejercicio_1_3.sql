#Calcular las ventas totales y las llamadas totales realizadas a los clientes de la profesion de ingenieria.
SELECT 
    SUM(t1.productsold) AS ventas_totales,
    COUNT(t1.callid) AS llamadas_totales
FROM
    calls t1
        LEFT JOIN
    customers t2 ON t1.customerid = t2.customerid
WHERE
    UPPER(t2.occupation) LIKE '%ENGINEER%';
#Mismas metricas pero sin filtro
SELECT 
    SUM(t1.productsold) AS ventas_totales,
    COUNT(t1.callid) AS llamadas_totales
FROM
    calls t1;
#Ver tasa de conversion de ingenieros.
SET @ventas_ingenieros = 760;
SET @llamadas_totales_ingenieros = 3619;
SET @conversion_ingenieros = @ventas_ingenieros/@llamadas_totales_ingenieros;
SET @ventas_totales = 2089;
SET @llamadas_totales = 9940;
SET @conversion_general = @ventas_totales/@llamadas_totales;
SET @porcentajeVentasIngenieros = @ventas_ingenieros/@ventas_totales;
SET @porcentajeLlamadasIngenieros = @llamadas_totales_ingenieros/@llamadas_totales;
SELECT @conversion_ingenieros, @conversion_general, @porcentajeVentasIngenieros, @porcentajeLlamadasIngenieros;

#La conversion general es muy parecida a la conversion de los ingenieros, dado que los ingenieros constituyen el 36% de las ventas totales y 36% de las llamadas.alter
SELECT 
    SUM(t1.productsold) AS ventas_totales,
    COUNT(t1.callid) AS llamadas_totales,
    SUM(t1.productsold)/COUNT(t1.callid) AS conversion
FROM
    calls t1
        LEFT JOIN
    customers t2 ON t1.customerid = t2.customerid
WHERE
    UPPER(t2.occupation) LIKE '%ENGINEER%' AND Age>30;
/*
#Por lo visto el nivel de conversion en ingenieros mayores 
de 30 años es menor al nivel de conversion de los ingenieros en general, 
con lo cual habria que revisar si esta diferencia es representativa y significativa. 
Si lo es, la estrategia deberia estar orientada a los de 30 o menos.
*/