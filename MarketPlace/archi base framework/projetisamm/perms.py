from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('projetisamm.Etudiant', AuthorPermissionLogic()),
    ('projetisamm.Etudiant', CollaboratorsPermissionLogic()),
)