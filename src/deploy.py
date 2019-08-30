import argparse, inspect

class Deploy:

    def __init__(self, args):

        self.command = args.command
        # args.[command] <- vérification existence de méthode
        # args.[command} <- appel dynamique de methode


    def run_manager(self):
        command = 'action_' + self.command
        is_hasattr  = hasattr(self, command)

        if is_hasattr and inspect.ismethod(getattr(self, command)):
            getattr(self, command)()



    def action_on(self):
        print("appel de la methode on")

    def action_remote(self):
        print("appel de la methode remote")


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
    deploy.run_manager()