from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.sql import func
import datetime
from typing import List

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    desafios: Mapped[int] = mapped_column(default=0, nullable=False)
    nivel: Mapped[int] = mapped_column(default=0, nullable=False)
    xp_total: Mapped[int] = mapped_column(default=0, nullable=False)

    conquistas: Mapped[List["UsuarioConquista"]] = relationship("UsuarioConquista", back_populates="usuario")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="usuario")
    rankings: Mapped[List["Ranking"]] = relationship("Ranking", back_populates="usuario")

class Curso(db.Model):
    __tablename__ = 'cursos'

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(3000), nullable=False)
    dificuldade: Mapped[str] = mapped_column(String(10), nullable=False)
    xp_total: Mapped[int] = mapped_column(nullable=False)

    modulos: Mapped[List["Modulo"]] = relationship("Modulo", back_populates="curso")

class Modulo(db.Model):
    __tablename__ = 'modulos'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    curso: Mapped["Curso"] = relationship("Curso", back_populates="modulos")
    aulas: Mapped[List["Aula"]] = relationship("Aula", back_populates="modulo")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="modulo")

class Aula(db.Model):
    __tablename__ = 'aulas'

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(60), nullable=False)
    conteudo: Mapped[str] = mapped_column(String(10000), nullable=False)
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    xp: Mapped[int] = mapped_column(nullable=False)

    modulo: Mapped["Modulo"] = relationship("Modulo", back_populates="aulas")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="aula")

class Progresso(db.Model):
    __tablename__ = 'progresso'

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    data_conclusao: Mapped[str] = mapped_column(String(10), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    aula_id: Mapped[int] = mapped_column(ForeignKey("aulas.id"))

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="progresso")
    modulo: Mapped["Modulo"] = relationship("Modulo", back_populates="progresso")
    aula: Mapped["Aula"] = relationship("Aula", back_populates="progresso")

class Conquista(db.Model):
    __tablename__ = 'conquistas'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    criterios: Mapped[str] = mapped_column(String(3000), nullable=False)

    usuarios_conquista: Mapped[List["UsuarioConquista"]] = relationship("UsuarioConquista", back_populates="conquista")

class UsuarioConquista(db.Model):
    __tablename__ = 'usuarios_conquistas'

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    conquista_id: Mapped[int] = mapped_column(ForeignKey("conquistas.id"))
    data_criacao: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="conquistas")
    conquista: Mapped["Conquista"] = relationship("Conquista", back_populates="usuarios_conquista")

class Desafio(db.Model):
    __tablename__ = 'desafios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao: Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    resultado: Mapped[str] = mapped_column(String(300), nullable=False)
    xp: Mapped[int] = mapped_column(nullable=False)

class Ranking(db.Model):
    __tablename__ = 'ranking'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    privilegios: Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    data_criacao: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="rankings")
