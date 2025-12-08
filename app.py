from fastapi import FastAPI, HTTPException, Request


# Árbol Binario de Búsqueda
class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)
    
    def _insertar_recursivo(self, nodo, producto):
        if producto["id"] < nodo.producto["id"]:
            if nodo.hijo_izquierdo is None:
                nodo.hijo_izquierdo = Nodo(producto)
            else:
                self._insertar_recursivo(nodo.hijo_izquierdo, producto)
        else:
            if nodo.hijo_derecho is None:
                nodo.hijo_derecho = Nodo(producto)
            else:
                self._insertar_recursivo(nodo.hijo_derecho, producto)
    
    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)
    
    def _buscar_recursivo(self, nodo, id):
        if nodo is None:
            return None
        
        if id == nodo.producto["id"]:
            return nodo.producto
        elif id < nodo.producto["id"]:
            return self._buscar_recursivo(nodo.hijo_izquierdo, id)
        else:
            return self._buscar_recursivo(nodo.hijo_derecho, id)
    
    def recorrer_inorder(self):
        productos = []
        self._recorrer_inorder_recursivo(self.raiz, productos)
        return productos
    
    def _recorrer_inorder_recursivo(self, nodo, productos):
        if nodo is not None:
            self._recorrer_inorder_recursivo(nodo.hijo_izquierdo, productos)
            productos.append(nodo.producto)
            self._recorrer_inorder_recursivo(nodo.hijo_derecho, productos)


# Instancia global del árbol
arbol_productos = ArbolBinario()


app = FastAPI(title="Productos y Pedidos API", version="1.0.0")


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/productos", status_code=201)
def crear_producto(request: Request):
    data = request.json()
    
    # Validar que el ID esté presente
    if "id" not in data or data["id"] is None:
        raise HTTPException(status_code=400, detail="El campo 'id' es obligatorio")
    
    producto_id = data["id"]
    
    # Validar que el ID no exista
    if arbol_productos.buscar(producto_id) is not None:
        raise HTTPException(status_code=400, detail=f"Ya existe un producto con ID {producto_id}")
    
    producto = {
        "id": producto_id,
        "nombre": data.get("nombre"),
        "valor": data.get("valor"),
        "peso": data.get("peso"),
        "descripcion": data.get("descripcion")
    }
    
    arbol_productos.insertar(producto)
    return producto


@app.get("/productos")
def listar_productos():
    return arbol_productos.recorrer_inorder()


@app.get("/productos/{id}")
def obtener_producto(id: int):
    producto = arbol_productos.buscar(id)
    if producto is None:
        raise HTTPException(status_code=404, detail=f"Producto con ID {id} no encontrado")
    return producto

