import typer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Crea la aplicación Typer
app = typer.Typer()

# Configura la conexión a la base de datos con SQLAlchemy
DATABASE_URL = "postgresql://postgres:@localhost:5433/db_salinas"
engine = create_engine(DATABASE_URL)

# Define un modelo utilizando SQLAlchemy
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Crea la tabla en la base de datos (solo una vez)
Base.metadata.create_all(bind=engine)

# Crea una función para obtener una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir comandos Typer para interactuar con la base de datos
@app.command()
def crear_item(nombre: str):
    """Crea un nuevo ítem en la base de datos."""
    db = SessionLocal()
    db_item = Item(name=nombre)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    typer.echo(f"Ítem '{nombre}' creado con ID {db_item.id}")

@app.command()
def listar_items():
    """Lista todos los ítems en la base de datos."""
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    typer.echo("Ítems en la base de datos:")
    for item in items:
        typer.echo(f"ID: {item.id}, Nombre: {item.name}")

if __name__ == "__main__":
    app()