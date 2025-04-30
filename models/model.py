from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Table
from sqlalchemy.sql import func
from datetime import datetime
from typing import List
from config.Database import db

# Tabelas de associação para relacionamentos muitos-para-muitos

table_role_permission = Table(
    'role_permission',
    db.metadata,
    db.Column('role_id', ForeignKey('roles.id'), primary_key=True),
    db.Column('permission_id', ForeignKey('permissions.id'), primary_key=True)
)
"""
Tabela de associação entre 'Role' e 'Permission' para um relacionamento muitos-para-muitos.
"""

table_curso_modulo = Table(
    'curso_modulo',
    db.metadata,
    db.Column('curso_id', ForeignKey('cursos.id'), primary_key=True),
    db.Column('modulo_id', ForeignKey('modulos.id'), primary_key=True)
)
"""
Tabela de associação entre 'Curso' e 'Modulo' para um relacionamento muitos-para-muitos.
"""

# Modelos principais

class Role(db.Model):
    """
    Representa os papéis (roles) no sistema, como Admin, Usuário, etc.
    Um papel pode ter várias permissões e ser atribuído a vários usuários.
    """
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    permissions: Mapped[List["Permission"]] = relationship("Permission", secondary=table_role_permission, back_populates="roles")
    users: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="role")

class Permission(db.Model):
    """
    Representa as permissões no sistema, como 'criar', 'editar', 'deletar', etc.
    Uma permissão pode ser associada a vários papéis (roles).
    """
    __tablename__ = 'permissions'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    roles: Mapped[List["Role"]] = relationship("Role", secondary=table_role_permission, back_populates="permissions")

class Ranking(db.Model):
    """
    Representa um ranking no sistema, que define privilégios e requisitos para os usuários.
    Os usuários podem ser atribuídos a um ranking específico.
    """
    __tablename__ = 'ranking'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    privilegios: Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuarios: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="ranking")

class Usuario(db.Model):
    """
    Representa um usuário no sistema, que possui dados pessoais, progresso, conquistas, e um ranking.
    O usuário também pode ter vários papéis e cursos.
    """
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
    """
    Representa uma conquista desbloqueada por um usuário.
    Cada conquista é associada a um usuário e a um conjunto de critérios.
    """
    __tablename__ = 'usuarios_conquistas'
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    conquista_id: Mapped[int] = mapped_column(ForeignKey("conquistas.id"))
    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped[Usuario] = relationship("Usuario", back_populates="conquistas")
    conquista: Mapped["Conquista"] = relationship("Conquista", back_populates="usuarios_conquista")

class Conquista(db.Model):
    """
    Define as conquistas no sistema, que os usuários podem alcançar ao atender certos critérios.
    """
    __tablename__ = 'conquistas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    criterios: Mapped[str] = mapped_column(String(3000), nullable=False)

    usuarios_conquista: Mapped[List[UsuarioConquista]] = relationship("UsuarioConquista", back_populates="conquista")

class Modulo(db.Model):
    """
    Representa um módulo dentro de um curso. Cada módulo contém várias aulas.
    """
    __tablename__ = 'modulos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)

    cursos: Mapped[List["Curso"]] = relationship("Curso", secondary=table_curso_modulo, back_populates="modulos")
    aulas: Mapped[List["Aula"]] = relationship("Aula", back_populates="modulo")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="modulo")

class Curso(db.Model):
    """
    Representa um curso no sistema, com título, descrição e XP total. 
    Cada curso pode ter múltiplos módulos e ser acessado por vários usuários.
    """
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
    """
    Representa uma aula dentro de um módulo, com título, conteúdo e XP atribuído.
    """
    __tablename__ = 'aulas'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(60), nullable=False)
    conteudo: Mapped[str] = mapped_column(String(10000), nullable=False)
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    xp: Mapped[int] = mapped_column(nullable=False)

    modulo: Mapped[Modulo] = relationship("Modulo", back_populates="aulas")
    progresso: Mapped[List["Progresso"]] = relationship("Progresso", back_populates="aula")

class Progresso(db.Model):
    """
    Rastreia o progresso de um usuário em relação a uma aula ou módulo específico.
    """
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
    """
    Representa um desafio que os usuários podem participar, com descrição, requisitos e recompensa de XP.
    """
    __tablename__ = 'desafios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao: Mapped[str] = mapped_column(String(3000), nullable=False)
    requisitos: Mapped[str] = mapped_column(String(500), nullable=False)
    resultado: Mapped[str] = mapped_column
