# Fundamentos de GitHub para Ciencia de Datos

## 📦 Instalación de Git (si aún no lo tienen)

### Windows

Descargar e instalar desde: [https://git-scm.com/download/win](https://git-scm.com/download/win)

- Durante instalación, aceptar todas las opciones por defecto
- Después de instalar, abrir CMD o PowerShell y verificar:

  ```bash
  git --version
  ```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git -y
git --version
```

### Linux (Other distros)

- Fedora: `sudo dnf install git -y`
- Arch: `sudo pacman -S git`

### Verificación en cualquier sistema

```bash
git --version
```

---

## ⚙️ Logueo en la PC

### Configurar

```bash
git config --global user.nombre "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

### Verificar configuración

```bash
git config --global --list
```

---

## 👤 Proceso de creación de repositorio

### Perfil de GitHub

![git_profile.png](git_profile.png)

### Lista de repositorios

![git_repos_list.png](git_repos_list.png)

### Pantalla "New Repository"

![git_new_repo.png](git_new_repo.png)

### Repositorio creado

![git_created_repo.png](git_created_repo.png)

---

## 🌐 Interfaz Online en GitHub

1. Ir a: **github.com** e iniciar sesión
2. Clic en el botón **New** (verde)
3. **Nombre del repositorio**: `Clases_ICD`

- Sin espacios
- Sin caracteres especiales

1. Marcar la opción: **Add a README file**
2. Clic en **Create repository**
3. Subir un archivo:

- Arrastrar archivo al área o hacer clic en **Add file → Upload files**

1. Hacer commit:

- Escribir mensaje: "Subida inicial"
- Clic en botón verde **Commit changes**

---

## 💻 Consola - Comandos Esenciales

```bash
# 1. Primera vez: Clonar repositorio
git clone https://github.com/AriadnaVelazquez744/Clases_ICD.git

# 2. Entrar a la carpeta
cd Clases_ICD

# 3. Ver qué archivos hay (estado)
git status

# 4. Preparar los cambios
git add .

# 5. Confirmar con mensaje
git commit -m "Mi primera actualización"

# 6. Subir a GitHub
git push origin main
```

---

## 🔄 Parte 4: Ciclo de Trabajo Diario

Siempre que trabajen en un proyecto:

```
[Modificar archivo(s) localmente]
            ↓
git status            ← Ver cambios (en rojo)
            ↓
git add nombre-archivo.py    ← O: git add .
            ↓
git commit -m "descripción breve"  ← Confirmar
            ↓
git push               ← Subir a la nube
```

---
