<h1 align="center"; style="text-align:center;">Laboratorio 2: Cinemática Directa - Phantom X - ROS</h1>
<p align="center";style="font-size:50px; background-color:pink; color:red; text-align:center;line-height : 60px; margin : 0; padding : 0;">
Robótica</p1>
<p align="center";style="font-size:50px; text-align:center; line-height : 40px;  margin-top : 0; margin-bottom : 0; "> <br> Giovanni Andrés Páez Ujueta</p>
<p align="center";style="font-size:50px; text-align:center; line-height : 20px; margin-top : 0; "> email: gpaezu@unal.edu.co</p>
<p align="center"; style="font-size:50px; text-align:center; line-height : 40px;  margin-top : 0; margin-bottom : 0; "> <br> Daniel Esteban Bohórquez Cifuentes</p>
<p align="center"; style="font-size:50px; text-align:center; line-height : 20px; margin-top : 0; "> email: dbohorquezc@unal.edu.co</p>
<p align="center"; style="font-size:50px; text-align:center; line-height : 30px;  margin-top : 0; margin-bottom : 0; "> <br><br>INGENIERÍA MECATRÓNICA</p>
<p align="center"; style="font-size:50px; text-align:center; line-height : 30px; margin-top : 0; "> Facultad de Ingeniería</p>
<p align="center"; style="font-size:50px; text-align:center; line-height : 30px; margin-top : 0; "> Universidad Nacional de Colombia Sede Bogotá</p>
<br>
<p align="center">
  <img align="center"; width="100" height="100" src="Fig/Escudo_UN.png">
</p>

<p align="center"; style="font-size:50px; text-align:center; line-height : 30px; margin-top : 0; "> <br>13 de mayo de 2022</p>

## Metodología

### Mediciones
Por medio de un calibrador se obtienes la medidas con las cuales se realiza un diagrama para tener una idea basica de las juntas que presenta el robot (Imagen de la izquierda). Con este avance se procede a realizar el análisis de DHstd por medio de la ubicación de los marcos de referencia en el diagrama (Diagrama de la derecha) y su respectiva tabla.
<p align="center">
  <img align="center"; width="200" height="300" src="Fig/Diagram.jpg">
  <img align="center"; width="200" height="300" src="Fig/Marcos.jpg">
</p>

### Análisis
Obteniendo asi la siguiente tabla mostrada en el software de Matlab, el cual por medio de la librería de Peter Corke se representa un modelo del robot que permita evidenciar la orientación de cada articulación y sus respectivos eslabones. 
<p align="center">
  <img align="center"; width="500" height="300" src="Fig/TablaDH.png">
</p>
<p align="center">
  <img align="center"; width="500" height="300" src="Fig/Robot.jpg">
</p>

### ROS
### Toolbox
Como se mostro en el análsis la tabla obtenida se obtuvo por medio de la función SerialLink generando así el siguiente código.

```
q_deg=[0 0 0 0];
q_rad=q_deg*(pi/180);
l=[4.4,10.5,10.5 9];
L(1) = Link('revolute','alpha',pi/2,'a',0,'d',l(1),'offset',0);
L(2) = Link('revolute','alpha',0,'a',l(2),'d',0,'offset',pi/2);
L(3) = Link('revolute','alpha',0,'a',l(3),'d',0,'offset',0);
L(4) = Link('revolute','alpha',0,'a',0,'d',0,'offset',0);

PhantomX=SerialLink(L,'name','PX');
PhantomX.tool=[0 0 1 l(4);-1 0 0 0;0 -1 0 0;0 0 0 1];
figure
PhantomX.plot(q_deg,'notiles','noname','floorlevel',-1);
``` 
En primer lugar se crea dos variables que contengan un arreglo, en este caso la primera es la posición objetivo en radianes que para iniciar se pone en HOME y la segunda contiene los valores de las articulaciones mostradas al inicio. Con esto realizado añaden los parametros de DH hallados previamente y con esto se crea el robot teniendo en cuenta que se configura una herramienta por medio del método .tool y su respectiva MTH. Por último como método de comprobación se grafica el robot en diferentes posiciones:
<p align="center">
  <img align="center"; width="250" height="300" src="Fig/Robot.jpg">
  <img align="center"; width="250" height="300" src="Fig/Pos1.jpg">
  <img align="center"; width="250" height="300" src="Fig/Pos2.jpg">
  <img align="center"; width="250" height="300" src="Fig/Pos3.jpg">
  <img align="center"; width="250" height="300" src="Fig/Pos4.jpg">
  <img align="center"; width="250" height="300" src="Fig/Pos5.jpg">
</p>

### Conexión con Matlab

Para esta sección se tiene como objetivo realizar un código que permita publicar en los tópicos del controldor de la junta, pero para esto se realiza un análisis de los límites de la articulación, primero se sabe que este tipo de robot tiene motores con una resolución de 1024 bits por lo tanto lo que resta es conocer los ángulos limite, para lo cual se utilizó el programa de Dynamixel Wizard el cual al realizar la conexión el robot permite evidenciar información de cada uno de los motores incluyendo el ángulo requerido, que para este tipo de motores es 300 grados distribuidos de -150° a 150° por lo tanto lo que faltaria realizar un mapeo que permita recibir los ángulos en grados y transformarlos en bits, por lo tanto se hizó uso de la siguinete función:
```
round(mapfun(q_deg(),-150,150,0,1023))
```
