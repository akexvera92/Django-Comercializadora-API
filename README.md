# Django-Comercializadora-API
# Joan Alexander Vera Beltrán 
# correo :akexvera92@gmail.com
# SENA mosquera
# Jorge Orlando Castro Nova - instructor



Este proyecto consiste en realizar y utilizar apis como lo son :


-CafeteriaApiView:Esta API nos trae en una lista los datos que dijitamos en la base de datos sql lite


-CafeteriaDetailApiView:Esta API nos trae el metodo get el cual nos trae las motos,metodo put el cual nos dejar crear una nueva moto o editar,metodo delete el cual nos deja eliminar una moto

-CafeteriaClasificacionApiView:Esta api es la que nos permite ver los productos por clasificacion



Para iniciar el proyecto debes
tener instalado python,django,visual studio code
luego entrar a la carpeta app_comercializadora y poner CMD en la url luego deber poner la siguiente linea ..\scripts\activate para activar el ambiente luego instalaras los requerimientos o librerias con la siguiente linea pip install -r requirements.txt el paso siguiente debes dar python manage.py runserver en el CMD te dara un link y tendras la siguiente vista
![image](https://user-images.githubusercontent.com/101748327/208256850-49b344fa-1b23-4a2b-9133-cf7d01005c4f.png)
lo siguiente que haremos sera poner el url /api/ 
![image](https://user-images.githubusercontent.com/101748327/208257329-40547459-0b55-4fb0-ac3b-43492b010e47.png)
como ustedes no tienen ninguna producto para agregar una nueva moto sera asi daremos click al boton post
![image](https://user-images.githubusercontent.com/101748327/208257360-3f0aca50-5e2c-4b19-9c3c-bbfccb767ceb.png)
tendremos la siguiente vista asi sabremos que se agrego correctamente
![image](https://user-images.githubusercontent.com/101748327/208257370-01fe648d-9d39-44c8-8853-7931d0e267ff.png)
si la queremos editar haremos los siguiente: copearemos la informacion y la pegaremos abajo y daremos click al boton post
![image](https://user-images.githubusercontent.com/101748327/208257423-fb99c764-6df1-4a03-a730-25d7312633c8.png)
podremos ver que el dato se actualizo
!![image](https://user-images.githubusercontent.com/101748327/208257440-ee694c4a-2184-4a5f-9694-f743ee3f931c.png)

si la queremos eliminar pondremos el id en la url 
![image](https://user-images.githubusercontent.com/101748327/208257478-d165d38a-29bc-4d24-8085-8c1e4db081ad.png)
daremos click en delete y nos saldra una confirmacion
!![image](https://user-images.githubusercontent.com/101748327/208257560-60249fe4-26b8-4f2a-86df-02cb0eb4272e.png)
volveremos a dar click en delete y nos saldra lo siguiente
![image](https://user-images.githubusercontent.com/101748327/208257600-270b7af3-e4dd-4d75-9c52-f15c2f612202.png)
lo cual es que se elimino exitosamente


si queremos ver los productos por clasificacion en la url pondremos que clasificacion queremos ver
![image](https://user-images.githubusercontent.com/101748327/208257850-c150f265-ff6a-4b0e-ac4c-916b0e457aa7.png)
