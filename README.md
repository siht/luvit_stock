# Backend Challenge: #

### Objetivo ###
El objetivo del challenge es crear un API utilizando python 3+ con django que pueda recibir un array de objetos de tipo “Product” y basicamente el servicio debe validar distintos puntos en el producto y regresar un resultado como respuesta con un 200 en el caso de que todos los productos sean validos, en el caso contrario debe regresar un 422 indicando un listado de los errores que encontro  ya sea porque no pudo parsear algunos productos o porque algun producto no paso las validaciones.

### Especificaciones del API: ###
**El objeto producto debe tener la siguiente estructura:**
```
Product {
	id: String
	name: String
	value: Float
	discount_value: Float?
	stock: Int
}
```

**El endpoint debe debe ser el siguiente:**  
POST api/products/bulk_validate

**Parametros del endpoint:**  
Los parametros que recibira el endpoint son:
```
{
	"products": [
		{
			Product (Con los fields como se definieron anteriormente.)
		},…
	]
}
```

**Resultado del endpoint:**
En caso de que todos los productos esten bien y sean validos:  
**HTTP Code 200**  
```
{
	"status": "OK"
}
```

En caso de que uno o mas productos no pasen la validación o si alguno de los productos no se pudieron parsear:  
**HTTP Code 422**  
```
{
	"status": "ERROR",
	"products_report": [
		{
			“product_id”: string,
			“errors”: [string] <- Un array de strings con las validaciones que no paso.
		},...
	],
	"number_of_products_unable_to_parse": Int (Este campo es en el caso de recibir un json con algun producto que no se pueda parsear se debe acumular la cantidad de productos que no se pudieron siquiera parsear en este campo, si no hubo niguno solo colocar un 0.)
}
```

**Las validaciones que se deben de tomar en cuenta son:**  
*Validation Type: name*  
>Validation:  El producto debe tener un name con un string de longitud minima de 3 caracteres y maxima 55.  
>Message in case of failure: "Invalid product name"  
	
*Validation Type: value*  
>Validation: El producto debe tener un valor mayor a 0 y menor a 99999.9  
>Message in case of failure: "Invalid value"  
	
*Validation Type: discount_value*  
>Validation: El producto en caso de tener un discount value, debe ser menor al precio normal.  
>Message in case of failure: "Invalid discount value"  
	
*Validation Type: stock*  
>Validation: El producto debe tener un stock mayor a -1.  
>Message in case of failure: "Invalid stock value"  

### Puntos que vamos a evaluar:  ###
* Creacion del API/endpoint.   
* Modelado y arquitectura de los objetos.  
* Testing de los modelos y el endpoint.  
* Deployment a AWS.  
* Claridad en los commits.  
* Tiempo destinado  

### Instrucciones adicionales: ###
* Se debe ocupar un elastic beanstalk de AWS (utilizar el free tier y aceptar la base que viene con elastic, la base debe ser postgreSQL).  
* El codigo debe subirse a github en un repositorio publico.  
* En el repositorio el README file debe tener un ejemplo de como consumir el endpoint utilizando un curl.  
* No invertir mas de 5 horas en el transcurso de 2 dias.  
* Hacer varios commits, no un solo commit, ya que es un elemento a evaluar.  
* Al finalizar se debe enviar el repo a los siguientes correos:  
>kevin@plataforma.io  
>ro@plataforma.io  
>juan@plataforma.io  