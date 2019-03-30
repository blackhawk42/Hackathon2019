# BiSecurity

En México (y en el mundo) el robo de bicicletas es uno de los delitos más fácil de cometer. Una de las razones es que no hay una manera sencilla de rastrear una bicicleta después de ser robada.

Nuestro proyecto, abarcando el dominio de la seguridad, desea atacar este problema usando métodos modernos de rastreo, combinándolos con estrategias de administración de bases de datos y comunicaciones distribuidas.

## ¿Qué consiste?

El proyecto consiste en implementar un ID único a cada bicicleta que se compre (ID no es obligatorio para circular). Este ID de la bicicleta estará registrado, para los propósitos de este proyecto, mediante un chip RFID. Mediante una plataforma, el usuario ciclista podrá mantener un registro de su bicicleta y, en caso de hurto, extravío o similar, reportarla como tal.

Cada estado (o municipio, según convenga) mantendrá su propio registro de bicicletas, con mínima dependencia del nivel nacional. La información de que bicicletas han sido robadas puede ser fácilmente distribuida a nivel nacional. Todo esto divulgando pocos datos personales de los ciclistas.

Los gobiernos locales que se registren al sistema mantendrán una red de sensores en lugares concurridos por bicicletas (intersecciones, ciclovías, etc.). Cuando una bicicleta que ha sido reportada como robada sea detectada por un sensor, esto detonará una alerta. Un aviso automatizado puede ser enviado al dueño y a las autoridades correspondientes, y los datos de los sensores pueden ser usados para potencialmente dar con el criminal.