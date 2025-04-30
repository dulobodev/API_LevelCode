from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Table
from sqlalchemy.sql import func
from datetime import datetime
from typing import List
from config.Database import db


table_role_permission = Table(
    'role_permission',
    db.metadata,
    db.Column('role_id', ForeignKey('roles.id'), primary_key=True),
    db.Column('permission_id', ForeignKey('permissions.id'), primary_key=True)
)

table_curso_modulo = Table(
    'curso_modulo',
    db.metadata,
    db.Column('curso_id', ForeignKey('cursos.id'), primary_key=True),
    db.Column('modulo_id', ForeignKey('modulos.id'), primary_key=True)
)


class Role(db.Model):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    permissions: Mapped[List["Permission"]] = relationship("Permission", secondary=table_role_permission, back_populates="roles")
    users: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="role")

class Permission(db.Model):
    __tablename__ = 'permissions'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    roles: Mapped[List["Role"]] = relationship("Role", secondary=table_role_permission, back_populates="permissions")

class Ranking(db.Model):
    __tablename__ = 'ranking'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    privilegios: Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuarios: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="ranking")

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False)
    senha: Mapped[str] = mapped_column(String(64), nullable=False)
    desafios: Mapped[int] = mapped_column(default=0, nullable=False)
    nivel: Mapped[int] = mapped_column(default=0, nullable=False)
    xp_total: Mapped[int] = mapped_column(default=0, nullable=False)
    roles_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    ranking_id: Mapped[int] = mapped_column(ForeignKey("ranking.id"))

    cursos_inscritos: Mapped[List["UsuarioCurso"]] = relationship("UsuarioCurso", back_populates="usuario")
    ranking: Mapped[Ranking] = relationship("Ranking", back_populates="usuarios")
    conquistas: Mapped[List["UsuarioConquista"]] = relationship("UsuarioConquista", back_populates="usuario")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="usuario")
    role: Mapped[Role] = relationship("Role", back_populates="users")

class UsuarioConquista(db.Model):
    __tablename__ = 'usuarios_conquistas'
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    conquista_id: Mapped[int] = mapped_column(ForeignKey("conquistas.id"))
    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped[Usuario] = relationship("Usuario", back_populates="conquistas")
    conquista: Mapped["Conquista"] = relationship("Conquista", back_populates="usuarios_conquista")

class Conquista(db.Model):
    __tablename__ = 'conquistas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    criterios: Mapped[str] = mapped_column(String(3000), nullable=False)

    usuarios_conquista: Mapped[List[UsuarioConquista]] = relationship("UsuarioConquista", back_populates="conquista")

class Modulo(db.Model):
    __tablename__ = 'modulos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)

    cursos: Mapped[List["Curso"]] = relationship("Curso", secondary=table_curso_modulo, back_populates="modulos")
    aulas: Mapped[List["Aula"]] = relationship("Aula", back_populates="modulo")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="modulo")

class Curso(db.Model):
    __tablename__ = 'cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(3000), nullable=False)
    dificuldade: Mapped[str] = mapped_column(String(10), nullable=False)
    xp_total: Mapped[int] = mapped_column(nullable=False)
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"), nullable=True)

    inscritos: Mapped[List["UsuarioCurso"]] = relationship("UsuarioCurso", back_populates="curso")
    modulos: Mapped[List[Modulo]] = relationship("Modulo", secondary=table_curso_modulo, back_populates="cursos")

class Aula(db.Model):
    __tablename__ = 'aulas'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(60), nullable=False)
    conteudo: Mapped[str] = mapped_column(String(10000), nullable=False)
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    xp: Mapped[int] = mapped_column(nullable=False)

    modulo: Mapped[Modulo] = relationship("Modulo", back_populates="aulas")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="aula")

class Progresso(db.Model):
    __tablename__ = 'progresso'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    data_conclusao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    aula_id: Mapped[int] = mapped_column(ForeignKey("aulas.id"))

    usuario: Mapped[Usuario] = relationship("Usuario", back_populates="progresso")
    modulo: Mapped[Modulo] = relationship("Modulo", back_populates="progresso")
    aula: Mapped[Aula] = relationship("Aula", back_populates="progresso")

class Desafio(db.Model):
    __tablename__ = 'desafios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao : Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    resultado: Mapped[str] = mapped_column(String(300), nullable=False)
    xp: Mapped[int] = mapped_column(nullable=False)

class UsuarioCurso(db.Model):
    __tablename__ = 'usuarios_cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    data_inicio: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    data_fim: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="em progresso", nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="cursos_inscritos")
    curso: Mapped["Curso"] = relationship("Curso", back_populates="inscritos")
