import argparse

class Deploy:

    def __init__(self, args):
        pass
        # args.[command] <- vérification existence de méthode
        # args.[command} <- appel dynamique de methode





if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Deploy est un outil de deploiment en ligne de commande'
    )

    parser.add_argument(
        'command',
        type=str,
        metavar='Commande',
        help=""
    )

    parser.add_argument(
        'remote',
        metavar='Remote',
        help=""
    )

    args = parser.parse_args()
    deploy = Deploy(args)