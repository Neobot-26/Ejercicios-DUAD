# Fundamentos de Internet 
## 1. Del Cliente al Servidor

**Enunciado:** Explique paso a paso qué ocurre cuando usted escribe
`www.youtube.com` en el navegador hasta que el video aparece en pantalla.

**Debe incluir:**
- Qué hace el cliente (navegador).
- Qué papel cumple el DNS.
- Qué ocurre con la dirección IP.
- Qué hace el servidor.
- Cómo entra en juego el protocolo HTTP/HTTPS.

---

## Paso a paso

### 1.1. El navegador (cliente)
Cuando escribes `www.youtube.com` y das **Enter**, el navegador:
- Identifica que `www.youtube.com` es un **dominio en la red**.
- Necesita saber la **dirección IP** de ese dominio para poder hablar con él.

### 1.2. El DNS
El navegador le pregunta a un **servidor DNS** (el de tu proveedor de Internet o
uno público como 8.8.8.8): «¿cuál es la IP de www.youtube.com?».
- Primero se revisa la caché del propio navegador y del sistema.
- Si no está, se consulta al DNS (a través del protocolo **UDP, puerto 53**).
- El DNS puede consultar a varios servidores (raíz, TLD, autoritativo de
  YouTube) hasta resolverlo.

### 1.3. La dirección IP
El DNS responde con algo como `142.250.x.x`. A partir de ahí:
- El navegador **no usa más el dominio** para la conexión real, usa esa IP.
- Los **routers** envían los paquetes por Internet por esa ruta.

### 1.4. Conexión con el servidor (HTTP/HTTPS)
- El cliente abre **TCP** en el **puerto 443** (HTTPS) del servidor de YouTube.
- Se negocia **TLS** (el candado 🔒): se acuerda una clave para cifrar el tráfico.
- Dentro de ese canal cifrado viaja una petición **HTTPS**, por ejemplo:

  ```
  GET /watch?v=XXXX HTTP/2
  Host: www.youtube.com
  ```

### 1.5. El servidor
YouTube recibe la petición, identifica el video por su ID y **responde** con:
- Un archivo **HTML** (la página),
- **CSS** (estilos),
- **JavaScript** (player, navegación),
- Datos del video (JSON con metadatos y enlaces).

### 1.6. De vuelta al navegador
- El navegador convierte el HTML en la página que ves.
- El **reproductor** pide el video por **CDN** (servidores cercanos a ti) con HTTPS.
- El video suele llegar **por trozos** (protocolos DASH/HLS), no entero, por eso
  empieza a reproducirse casi al instante.

---

## 1.7. Diagrama en ASCII

```
imagen.jpg
```
---
## 2. Frontend y Backend en acción 

**Supuesto:** construir una app web para agendar citas médicas.

### 2.1. Frontend
- Es lo que el paciente **ve y usa**: la página donde selecciona especialidad,
  fecha, hora, médico y confirma la cita.
- **Tres tecnologías posibles:**
  - **React** (con Vite) o **Vue.js** para construir la interfaz.
  - **HTML + CSS + JavaScript** (o Tailwind CSS) directamente.
  - **Next.js** (ya que genera tanto páginas como componentes UI con React).

### 2.2. Backend
- Es el **cerebro invisible**: guarda las citas, valida que el médico esté
  disponible, maneja usuarios y evita dobles reservas.
- **Tres tecnologías posibles:**
  - **Node.js** con **Express**.
  - **Python** con **Django** (o Flask).
  - **Java** con **Spring Boot** (o **Laravel** en PHP).

### 2.3. Cómo se comunican
1. El **frontend** hace una **petición HTTP** (por ejemplo `POST /api/citas` con
   datos JSON del paciente y la fecha elegida).
2. Esa llamada viaja a la **API** del backend (un conjunto de URL llamadas
   «endpoints»: `/api/citas`, `/api/medicos`, `/api/horarios`...).
3. El **backend** procesa la petición (guarda en la base de datos, valida) y
   responde con una **respuesta HTTP**: código de estado (200 OK, 201 Created,
   400 Bad Request...) y un cuerpo JSON.
4. El **frontend** recibe el JSON y **actualiza la pantalla** (muestra «Cita
   agendada correctamente» o un error).

Todo este ciclo se llama **request/response**:

```
Frontend  ──request (HTTP + JSON)──►  API del Backend
Frontend  ◄──response (HTTP + JSON)──  API del Backend
```
---
## 3. REST vs SOAP vs GraphQL 

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|-----------------------|------------------------------|----------------------------------|
| **REST**    | JSON (también XML)     | **Media/Alta**: el cliente pide un recurso concreto; el servidor define la estructura. | **Baja**: simple, HTTP estándar, abundantes herramientas. | **Alta**: estándar de facto en APIs web modernas. |
| **SOAP**    | XML (obligatorio)      | **Baja**: contratos fijos vía WSDL, el servidor controla todo el intercambio. | **Alta**: más configuraciones, difícil depurar, contratos obligatorios. | **Baja** en proyectos nuevos; sigue presente en banca/enterprise. |
| **GraphQL** | JSON                   | **Muy alta**: el cliente pide exactamente los campos que necesita; el servidor solo responde. | **Media-Alta**: requiere esquema + resolvers; curva de aprendizaje. | **Media** (creciente, popular en frontend moderno). |

### 3.1. ¿Cuál conviene a una startup moderna con un sistema de reservas en línea?

**REST**.

**¿Por qué?**
1. **Simplicidad y rapidez**: para flujos típicos de reservas (listar disponibilidad,
   crear reserva, cancelar) basta con endpoints como `GET /reservas`, `POST /reservas`.
2. **Ecosistema maduro**: muchísimas librerías, hosting serverless y soporte estándar
   en cualquier framework (Express, Django REST, Spring).
3. **Mejor curva para el equipo**: un equipo nuevo empieza a producir resultados
   rápidos con REST antes que con GraphQL o SOAP.
4. **Facilita el despliegue**: las respuestas JSON ligeras rinden bien, lo que importa
   en un producto nuevo con tráfico aún moderado.

---
## 4. Explorando APIs con Postman 

### 4.1: Selección de la API 

**Nombre de la API:** PokéAPI (https://pokeapi.co)

**Breve descripción de lo que ofrece:**
PokéAPI es una API pública y gratuita que expone datos de la franquicia
Pokémon: información de Pokémon, tipos, habilidades, movimientos, generaciones,
objetos, ubicaciones de cada juego, etc. No requiere autenticación y devuelve
las respuestas en JSON, por lo que es ideal para practicar peticiones HTTP
usando Postman.

**Endpoint de ejemplo elegido para la práctica:**

```
GET https://pokeapi.co/api/v2/pokemon/pikachu
```

Este endpoint devuelve en JSON los datos completos del Pokémon Pikachu (altura,
peso, tipos, habilidades y estadísticas base).
### Parte 2: Configuración en Postman

**1. Crear la colección**
- En Postman → botón **+ New** → **Collection**.
- Nombre: **PokéAPI**.

**2. Variables de entorno** (para no repetir URLs):
- Click en **Environments** → **+** y llama al entorno **local**.
- Agrega:

  | Variable | Valor inicial |
  |----------|---------------|
  | `baseUrl` | `https://pokeapi.co/api/v2` |
  | `pokemon` | `pikachu` |
  | `id` | `25` |

- Luego selecciona ese entorno (desplegable arriba a la derecha) en cada petición
  escribe la URL con los símbolos `{{ }}`:

```
{{baseUrl}}/pokemon/{{pokemon}}
{{baseUrl}}/pokemon/{{id}}
```

**3. Solicitudes configuradas (3 tipos):**

- **GET** — obtener información de un Pokémon:
  ```
  GET {{baseUrl}}/pokemon/{{pokemon}}
  ```
  → Respuesta esperada: 200 OK con JSON de datos (altura, peso, etc.)

- **GET** — lista paginada de Pokémons:
  ```
  GET {{baseUrl}}/pokemon?limit=10&offset=0
  ```

- **POST** — PokéAPI es **de solo lectura**; para simular operaciones de
  escritura usaremos la API de pruebas JSONPlaceholder (también gratuita y sin
  token):
  ```
  POST https://jsonplaceholder.typicode.com/posts
  Headers:
    Content-Type: application/json
  Body (JSON):
    { "title": "Nuevo post", "body": "Contenido...", "userId": 1 }
  ```
  → Respuesta: código 201 Created con el objeto creado y su `id`.

- **PUT ** — en JSONPlaceholder también se simulan:
  ```
  PUT https://jsonplaceholder.typicode.com/posts/{id}
  DELETE https://jsonplaceholder.typicode.com/posts/1
  ```
  → Respuesta: 200 OK con el recurso actualizado.

**4. Environment variables en Postman:**
- Pestaña **Environment** del entorno `local`: `baseUrl`, `pokemon`, `id`.
- Al ejecutar una petición, Postman reemplaza `{{baseUrl}}` automáticamente.

### Parte 3: Ejecución de solicitudes
- Ver Archivos adicionales.

### Parte 4: Ejecución de solicitudes
**4.1 Descripción general de las API elegidas**
Se usaron dos API públicas para practicar distintos tipos de solicitudes HTTP:
- PokéAPI permite consultar información de Pokémon. Es una API de solo lectura, así que se utiliza para solicitudes GET.
- JSONPlaceholder es una API de prueba que simula operaciones sobre publicaciones, como crear, actualizar y eliminar. No requiere token.
**4.2. Explicación de cada solicitud**
Solicitud	Método y endpoint	Parámetros o cuerpo	Respuesta esperada
Obtener un Pokémon	GET {{baseUrl}}/pokemon/{{pokemon}}	pokemon es el nombre o número del Pokémon.	200 OK con datos como altura, peso, tipos y habilidades.
Listar Pokémon	GET {{baseUrl}}/pokemon?limit=10&offset=0	limit=10 solicita hasta 10 resultados; offset=0 indica que se empieza desde el primero.	200 OK con una lista paginada de Pokémon.
Crear una publicación	POST https://jsonplaceholder.typicode.com/posts	Header Content-Type: application/json. Cuerpo: {"title":"Nuevo post","body":"Contenido...","userId":1}.	201 Created con los datos enviados y un id asignado.
Actualizar una publicación	PUT https://jsonplaceholder.typicode.com/posts/{id}	{id} identifica la publicación. Se envía un cuerpo JSON con los datos actualizados.	200 OK con la representación de la publicación actualizada.
Eliminar una publicación	DELETE https://jsonplaceholder.typicode.com/posts/1	El identificador 1 indica qué publicación eliminar. No requiere cuerpo.	Confirma la operación; en JSONPlaceholder suele responder con un objeto vacío.

**4.3. Ejemplos de respuestas JSON**
Una respuesta de PokéAPI para un Pokémon puede tener esta forma:
{
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "types": [
    {
      "type": {
        "name": "electric"
      }
    }
  ]
}
Una respuesta simulada de JSONPlaceholder al crear una publicación puede ser:
{
  "title": "Nuevo post",
  "body": "Contenido...",
  "userId": 1,
  "id": 101
}
Los valores exactos pueden variar según la solicitud. JSONPlaceholder simula las operaciones: las respuestas sirven para practicar, pero los cambios no se guardan de forma permanente.

**4.4. Qué aprendí del proceso**
Aprendí que el método HTTP depende de la acción que se quiere realizar: GET consulta información, POST crea un recurso, PUT lo actualiza y DELETE lo elimina. También practiqué cómo construir endpoints con parámetros, cómo enviar un cuerpo JSON y cómo interpretar códigos de estado como 200 OK y 201 Created. Finalmente, entendí que algunas API son de solo lectura, por lo que se pueden combinar con una API de pruebas para practicar operaciones de escritura.

---
### Parte 5: Reflexion Final
**5.1 ¿Qué aprendiste sobre el funcionamiento de las APIs?**  
Aprendí que las APIs permiten que un cliente solicite o envíe información a un servidor mediante métodos HTTP como GET, POST, PUT y DELETE. Cada solicitud incluye un endpoint y, según la operación, parámetros o un cuerpo JSON; el servidor responde con datos y un código de estado que indica el resultado.
**5.2 ¿Cómo te ayudó Postman a entender la comunicación entre cliente y servidor?** 
Postman me ayudó a probar esas solicitudes sin tener que crear un programa, y a observar directamente qué se envía al servidor y qué devuelve. Así pude entender mejor cómo se comunican cliente y servidor y cómo cambian las respuestas según el método y los datos de la solicitud.

