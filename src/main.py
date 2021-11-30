from controllers.controller import Controller


class Main:
    @staticmethod
    def run() -> None:
        controller = Controller()
        controller.start_application()


if __name__ == "__main__":
    Main.run()
