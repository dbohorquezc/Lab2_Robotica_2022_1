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

Obteniendo asi la siguiente tabla mostrada en el software de Matlab, el cual por medio de la librería de Peter Corke se representa un modelo del robot que permita ecidecira la orientacion de cada articulacion y sus respectivos eslabones. 
<p align="center">
  <img align="center"; width="500" height="300" src="Fig/TablaDH.png">
</p>
<p align="center">
  <img align="center"; width="500" height="300" src="Fig/Robot.jpg">
</p>
