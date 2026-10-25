from maya import cmds

#planches verticales
def creer_cloture(nb_poteaux=6, espacement=2.0, hauteur=2, nb_planches=2):
    for i in range(nb_poteaux):
        poteau = cmds.polyCube(name="poteau_", width =0.5, height = hauteur, depth=0.2)[0]
        cmds.move(i*espacement, hauteur/2, 0, poteau)

    #planches horizontales
    for y in range(nb_planches):
        longueur = nb_poteaux*espacement
        planche = cmds.polyCube(name="planche_", width =longueur, height = .15, depth=0.15)[0]
        cmds.move(longueur /2, y+.5, 0, planche)
    return

creer_cloture()