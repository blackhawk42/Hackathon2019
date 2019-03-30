# Notación
Un byte será representado en formato hexadecimal: 0xBYTE. Por ejemplo,
4 = 0x04.

Varios bytes entre corchetes ('[]') son o un arreglo de bytes o un tipo de dato
con representación similar a dicho arreglo. Por ejmplo, un unsigned int representando
el número 2040 puede ser representado como [0x00 0x00 0x07 0xf8].

# Sobre información binaria
A menos que se indique lo contrario o el formato usado requiera algo específico
(e.g., UTF-8 indica su propio orden), todo dato será representado en orden big-endian.

Toda cadena de texto será codificada en formato UTF-8.

Cada sistema es libre de convertir y representar datos como más le convenga, pero al momento de comunicarse
se esperará que los flujos de bytes sean estandarizados.

# IDs

Este sistema depende de 4 tipos de IDs:

1. ID de Estado
2. ID de Municipio
3. ID de Ciclista
4. ID de Bicicleta

A menos que se indique lo contrario, cada formato de ID puede ser representado
internamente como más convenga a cada sistema.

## ID de Estado

Cada entidad federativa de los Estados Unidos Mexicanos tendrá asignada un número
en el rango 1-32 que identificará cada estado de manera única a nivel nacional.

## ID de Municipio

A nivel estatal, cada municipio será identificado de manera única con un número en el rango
1-_n_, donde _n_ es el número de municipios en el estado.

## ID de ciclista

A nivel estatal, cada ciclista será con identificado con un número único en
el rango de 0-4,294,967,295.

El número será representado internamente como un sólo número representable en 4 bytes de
tamaño (unsigned int). Por facilidad de uso, cada byte puede ser mostrado como
un número en el rango 0-255 al usuario humano. Por ejemplo, la ID de ciclista
2040 ([0x00 0x00 0x07 0xf8]) puede ser representado como "0-0-7-248".

## ID de bicicleta

A nivel estatal, cada bicicleta individual será identificada con un número único
en el rango de 0-4,294,967,295.

Reglas y sugerencias de representación del ID de ciclista aplican similarmente a
la ID de bicicleta.

# Token

Cada bicicleta será fisicamente y por el medio que más convenga (RFID, código QR,
etc.) asignada un token.

Este es un token de 13 bytes, formado por el ID del estado en el que se registró
la bicicleta, la ID de su municipio, la ID de su ciclista, y la ID de la bicicleta
en sí.

```
[ID de estado | ID de municipio | ID de ciclista | ID de bicicleta]
```

* ID de estado: 1 byte (unsigned char)
* ID de municipio: 4 bytes (unsigned int)
* ID de ciclista: 4 bytes (unsigned int)
* ID de bicicleta: 4 bytes (unsigned int)

Sintaxis para struct en Python:

```
struct.pack('>BIII', estado_id, municipio_id, ciclista_id, bicicleta_id)
```

Modificación de prueba